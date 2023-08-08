|||
**Goals:**
This lab will have learners generate images using prompts given to DALL-E, and then manipulate those images with PIL. They will need to understand how to interact with DALL-E and the PIL library. We will write code to generate images, and then write code to modify those images.
|||

There will be **Try It!** buttons that will call our function in our terminal (bottom-left panel).
The first step is to have all the libraries and API keys:
```python
#import our libraries
import os
import openai
from PIL import Image,ImageOps,ImageFilter
from io import BytesIO
import requests


# Set API key and prompt
openai.api_key = os.getenv('OPENAI_KEY')
``` 
{Try it!|terminal}(python3 main.py)



Let's create a main function that acts as a control center for the program. Here's a simple example to give you an idea.
```python
def main():
    while True:
        print("\n1. Generate an image with DALL-E")
        print("2. Create variations of an image")
        print("0. Exit")
        
        option = input("Choose an option: ")

        if option == "1":
            prompt = input("Enter the prompt for DALL-E: ")
            # Generate the image with DALL-E
            generate_image(prompt)
        elif option == "2":
            image_path = input("Enter the path of the image: ")
            # Open the image file
            create_variations(image_path)
        elif option == "0":
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please enter a valid number.")
```
{Try it!|terminal}(python3 main.py 2)
In this program, the main function is running a continuous loop that prompts the user to choose an option. If the user chooses option "1", they're asked for a prompt which is then passed to the `generate_image` function (where DALL-E would be used to generate an image). If the user chooses option "2", they're asked for an image path, and the image at that path is opened and passed to the `create_variations` function. Lastly, an option "0" is given to exit our program.

Next we are going to put placeholder code for the function code
```python
def generate_image(prompt1):
    # Generate the image with DALL-E
    print(f"Generating an image for the prompt: {prompt1}")
    # Call DALL-E API here

def create_variations(img):
    # Create variations of an image using PIL
    print("Creating variations of the image...")
     # Call DALL-E API here

if __name__ == "__main__":
    main()
```
{Try it!|terminal}(python3 main.py 3)

The `generate_image` and `create_variations` functions are placeholders for you to implement the actual logic of interacting with DALL-E. 

{Check It!|assessment}(multiple-choice-2565980586)
