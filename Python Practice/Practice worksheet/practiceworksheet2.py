# Install an external module and use it to perform an operation of your interest. 
# i am using qr code generator which will generate qr
import qrcode

# 1. Define the data you want in the QR code
data = "https://www.google.com"

# 2. Configure the QR code appearance
qr = qrcode.QRCode(
    version=1,           # Controls the size (1 is smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L, # Error tolerance
    box_size=10,         # Size of each individual box in pixels
    border=4,            # Thickness of the white border
)

# 3. Add data and generate the image
qr.add_data(data)
qr.make(fit=True)

# 4. Create an image from the QR Code instance
# You can customize colors here!
img = qr.make_image(fill_color="black", back_color="white")

# 5. Save it to your directory
img.save("my_first_qrcode.png")

print("QR code generated and saved as 'my_first_qrcode.png'!")