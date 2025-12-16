import qrcode

url = input("enter URL: ").strip()
print(url)
file_path = "qrcode_results\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("qr generated!")