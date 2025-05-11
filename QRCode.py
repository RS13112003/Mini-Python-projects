import qrcode
# Taking upi id as input
upi = input("Enter your UPI ID: ")
# upi://pay?pa=upi&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# Define the payment URL based i the UPI ID and the payment app
# You can modify these URL's based on the payment apps you want to support

phonepe_url = f"upi://pay?pa={upi}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi}&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi}&pn=Recipient%20Name&mc=1234"
# Create  QR code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save the QR code to the image files(optional)
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

# Display the QR codes (you may need to install PIL/Pillow Library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()