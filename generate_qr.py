import qrcode

# URL that the QR code will link to (your Flask form URL)
url = 'http://172.26.125.205:5002/form'  # change port if your Flask app runs on a different port

# Create QR code object
qr = qrcode.QRCode(
    version=1,  # size of the QR code (1 = 21x21)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # size of each box in pixels
    border=4,     # thickness of border (boxes)
)

# Add URL data to the QR code
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image file
img.save("attendance_form_qr.png")

print("QR code generated and saved as attendance_form_qr.png")
