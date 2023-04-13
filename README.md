Steganography Tool
This is a Python tool that can hide messages or files inside images and retrieve them later. This tool uses a technique called steganography, which is the practice of hiding information in plain sight.

Usage
To use this tool, you need to save the steganography.py file to your computer. You can then import the hideMessage and retrieveMessage functions from the steganography module in your own Python script and use them to hide and retrieve messages from images.

Hiding a Message in an Image
To hide a message in an image, use the hideMessage function. The function takes two arguments:

image_path: the path to the image file you want to hide the message in
message: the message you want to hide in the image
Here's an example of how to use the hideMessage function:

from steganography import hideMessage
# the path to the image you want to hide the message in
image_path = 'my_image.png'
# the message you want to hide in the image
message = 'This is a secret message!'
# hide the message in the image
hideMessage(image_path, message)
This will create a new image file with the name my_image_hidden.png that contains the hidden message.

Retrieving a Message from an Image
To retrieve a message from an image, use the retrieveMessage function. The function takes one argument:

image_path: the path to the image file that contains the hidden message
Here's an example of how to use the retrieveMessage function:

from steganography import retrieveMessage
# the path to the image file that contains the hidden message
image_path = 'my_image_hidden.png'
# retrieve the hidden message from the image
message = retrieveMessage(image_path)
print(message)
This will print the hidden message that was stored in the image.
