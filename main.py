def encrypt_message(input_text_file, output_text_file, secret_message):
    with open(input_text_file, 'rb') as file:
        data = file.read()
    
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message) + '00000000'  
    
    if len(binary_message) > len(data) - 54:  
        print("Error: Message too long for the file.")
        return
    
    modified_data = bytearray(data[:54])  
    for i in range(len(binary_message)):
        modified_data.append(data[54 + i] & 0b11111110 | int(binary_message[i]))
    modified_data.extend(data[54 + len(binary_message):])
    
    with open(output_text_file, 'wb') as file:
        file.write(modified_data)
    print("Message hidden successfully!")

def decrypt_message(text_file):
    with open(text_file, 'rb') as file:
        data = file.read()
    
    binary_message = ''
    for i in range(54, len(data)):
        binary_message += str(data[i] & 1)
    
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '00000000':
            break
        message += chr(int(byte, 2))
    
    return message

input_file = input("enter your file path:")
output_file = input("enter your file name:")
message_secret = input("enter your secret message here:")
encrypt_message(input_file, output_file, message_secret)
print("Hidden Message:", decrypt_message(output_file))

