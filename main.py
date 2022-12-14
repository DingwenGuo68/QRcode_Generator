import qrcodeGeneratoroptimize as Q

# path of the input file to be read
path = 'qrcode.txt'
# 槽口数量
number = 8
c = Q.QR_Generator(path, number)
print(c.read_file())
c.qr_generate()
b = Q.QR2pdf
b.img2pdf()
