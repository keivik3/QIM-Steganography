import os
import math
import numpy as np
from PIL import Image


def to_numeric(message):
    return [ord(c) for c in message.lower() if ord(c) <= 255]


def to_text(numbers):
    return ''.join(chr(num) for num in numbers)


def calculate_psnr(original_image, modified_image):
    mse = np.mean((original_image - modified_image) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 10 * math.log10((max_pixel ** 2) / mse)
    return psnr

def qim_embed(image_path, message):
    image = np.array(image_path)
    height, width, _ = image.shape

    if height * width < len(message) * 8:
        print("Not enough pixels to embed the message.")
        return

    max_symbols = (width * height) // 8
    message = message[:max_symbols]

    q = int(input("Enter the quantization step (q): "))

    message_nums = to_numeric(message)
    message_bits = ''.join([bin(num)[2:].rjust(8, '0') for num in message_nums])
    embedded_image = image.copy()

    for i in range(len(message_bits)):
        row = i // width
        col = i % width
        pixel = embedded_image[row][col][0]
        new_pixel = q * np.floor(pixel / q) + (q / 2) * int(message_bits[i])
        embedded_image[row][col][0] = new_pixel
    for i in range(100):
        Image.fromarray(embedded_image).save(os.path.join(os.getcwd(), 'res_' + str(i) +'.png'))

    psnr = calculate_psnr(image, embedded_image)
    print("PSNR after embedding message:", psnr)


def qim_extract(image_path):
    image = np.array(image_path)

    q = int(input("Enter the quantization step (q): "))
    extracted_message = ''
    for i in range(image.shape[0] * image.shape[1]):
        row = i // image.shape[1]
        col = i % image.shape[0]
        pixel = image[row][col][0]

        bit0 = q * np.floor(pixel / q)
        bit1 = q * np.floor(pixel / q) + q / 2

        if pixel % q == 0:
            extracted_message += '0'
        else:
            extracted_message += '1'
    message_nums = [int(extracted_message[i:i + 8], 2) for i in range(0, len(extracted_message), 8)]
    extracted_text = to_text(message_nums)
    print("Extracted message:\n", extracted_text)


image_path = Image.open("image.png")
print("Введите сообщение (два раза Enter для окончания ввода): ")
message = ''
new_string = input()
while len(new_string):
    message += new_string + '\n'
    new_string = input()
qim_embed(image_path, message)

image_path = Image.open('result.png')
qim_extract(image_path)

