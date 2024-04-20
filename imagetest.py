import ollama

# Open the image file in binary mode
with open('C:\\Users\\shach\\.ollama\\ShreeRam.jpg', 'rb') as file:
    
    # Read the image file content
    image_content = file.read()
    
    # Close the file after reading
    file.close()

    # Chat with the llava model using ollama
    response = ollama.chat(
        model='llava',
        messages=[
            {
                'role': 'user',
                'content': 'What is in this image?',
                'images': [image_content],
            }
        ]
    )
    
    # Print the response content
    print(response['message']['content'])
