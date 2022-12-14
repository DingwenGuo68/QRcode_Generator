# -*- ecoding: utf-8 -*-
# @Function:
# @Author: Dingwen
# @Time: 2022/12/14 14:00
import qrcode
from PIL import Image
import os
import img2pdf
from PIL import ImageDraw
from PIL import ImageFont


class QR_Generator(object):

    def __init__(self, path, number):
        self.path = path
        self.number = number

    def read_file(self):
        file = open(self.path, 'r')
        read = file.read().upper()
        if len(read) == 0:
            raise ValueError("file content shouldn't be empty")
        txt = read.split()
        return txt

    def qr_generate(self):
        capi_txt = self.read_file()
        my_font = ImageFont.truetype("arial.ttf", 20)
        for i in range(self.number):
            for txt in capi_txt:
                # create a qrcode according to the input text
                qr_text = txt + str(i + 1)
                qr_code = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,
                    border=4,
                )
                qr_code.add_data(qr_text)
                qr_code.make(fit=True)
                qr_img_format = qr_code.make_image(fill_color="black", back_color="white").convert('RGB')
                qr_name = qr_text + '.png'
                # add name of the qr in the background
                qr_img_text = ImageDraw.Draw(qr_img_format)
                qr_img_text.text((10, 10), qr_text, font=my_font, fill=(0, 0, 0))
                qr_img_format.save(qr_name)
        return 0


class QR2pdf(object):
    @staticmethod
    def img2pdf():
        imagelist = [i for i in os.listdir() if i.endswith('png')]
        if len(imagelist) == 0:
            raise ValueError("There is no pictures with format of .png")
        print(imagelist)
        image_new_list = []
        size = 290, 290
        for image in imagelist:
            im = Image.open(image)
            im.thumbnail(size, Image.Resampling.LANCZOS)
            im.save(image, quality=100)
            image_new_list.append(im)

        file = open('qrcode1.pdf', "wb")
        file.write(img2pdf.convert(imagelist))
        file.close()


if __name__ == '__main__':
    # path of the input file to be read
    path = 'qrcode.txt'
    # 槽口数量
    number = 8
    c = QR_Generator(path, number)
    print(c.read_file())
    c.qr_generate()
    b= QR2pdf()
    b.img2pdf()
