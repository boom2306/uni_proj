def hide_message(image, message):

    with open(image, "r,b") as f:
        image_data = bytearray(f.read())