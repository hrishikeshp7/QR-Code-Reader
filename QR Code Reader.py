from PIL import Image
from pyzbar import pyzbar

print("Enter the file path of the QR Code you want to decode - ")
filepath = input()
img = Image.open(filepath)
output = pyzbar.decode(img)
print(output)

print("Press Any Key To Exit")
resexit = input()