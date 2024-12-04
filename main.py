def hide_message(image, message):

    with open(image, "r,b") as f:
        image_data = bytearray(f.read())

    pixel = 3
    message_bits = ''.join(format(ord(char), '08b') for char in message)
    index = 54

    for bit in message_bits:
        for color_channel in range(pixel):
            image_data[index + color_channel] &= 254
            image_data[index + color_channel] |= int(bit)
        index += pixel

    with open("secret_image.bmp", "wb") as f:
        f.write(image_data)

image_path = "image.bmp"
message = "secret"

hide_message(image_path, message)