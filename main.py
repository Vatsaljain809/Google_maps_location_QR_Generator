import qrcode


def generate_google_maps_qr_code(google_maps_url):
    # Construct the Google Maps URL
    google_maps_url = f"Your Location"

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(google_maps_url)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save or display the image
    img.save("Location.png")
    img.show()


# Example usage:
location = "Your Location"
generate_google_maps_qr_code(location)
