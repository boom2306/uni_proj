def hide_message(image, message):

    with open(image, "r,b") as f:
        image_data = bytearray(f.read())

    pixel = 3
    message_bits = ''.join(format(ord(char), '08b') for char in message)
    index = 54