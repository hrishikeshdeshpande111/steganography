from steganography import hideMessage, retrieveMessage

# the path to the image you want to hide the message in
image_path = 'D:/HTML-CSS/steganography/image.jpg'

# get the message from the user
message = input("Enter the message you want to hide: ")

# hide the message in the image
hideMessage(image_path, message)

# the path to the modified image that contains the hidden message
modified_image_path = 'D:/HTML-CSS/steganography/image_hidden.png'

# retrieve the hidden message from the image
retrieved_message = retrieveMessage(modified_image_path)

# print the hidden message
print("The hidden message is:", retrieved_message)
