# Lecture 7 - Stenography

## Classwork

Below is a sample of python code that implements the hiding of a text message in an immage.

The code uses an inpout image file `img.png` and embeds the message `Hello, World!` into it. The output image file is saved as `output_image.png`.

Make sure that the initial image file is in the project root folder that is running this code.

```python
from PIL import Image

def embed_message(image_path, message, output_path):
    img = Image.open(image_path)
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Delimiter to mark end of message
    data_index = 0

    pixels = list(img.getdata())
    for i in range(len(pixels)):
        if data_index < len(binary_message):
            pixel = list(pixels[i])
            for j in range(3):  # Modify RGB values
                if data_index < len(binary_message):
                    pixel[j] = pixel[j] & ~1 | int(binary_message[data_index])
                    data_index += 1
            pixels[i] = tuple(pixel)
        else:
            break

    img.putdata(pixels)
    img.save(output_path)

def extract_message(image_path):
    img = Image.open(image_path)
    binary_message = ''
    pixels = list(img.getdata())

    for pixel in pixels:
        for value in pixel[:3]:  # Only consider RGB values
            binary_message += str(value & 1)

    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '11111110':  # End delimiter
            break
        message += chr(int(byte, 2))

    return message

# Example usage
embed_message('img.png', 'Hello, World!', 'output_image.png')
print(extract_message('output_image.png'))
```

* Work through this with your own text string and notice the increase in the file size of the file that contains the embedded message.

* Work through teh logic of the embedding process and understand how the message is hidden in the image.

The above code was genrated by Microsoft `Copilot` and is a simple example of how to hide a message in an image.



