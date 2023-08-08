Now let's try adding additional options to our program. We are going to add a function that can resize our images for us. You can resize images using the Python Imaging Library (PIL). First we are going to add a print statement after option 2.
```python
def main():
    while True:
        print("\n1. Generate an image with DALL-E")
        print("2. Create variations of an image")
        print("3. Resize an image")
        print("0. Exit")
```
We also need to add a resize option call. Place the following code after option 2.
```python
elif option=="3":
          image_path = input("Enter the path of the image you want resized: ")
          # run resize function
          re_size(image_path)
```
A Try It! button is not provided here since we have not written our resize function yet and because of that you would just get an error.

Let's write our `re_size` function. We know that for our Dall-E we need our images to be in the following 3 dimensions: 256x256, 512x512, or 1024x1024. We will ask for additional user input as to pick which one
```python
def re_size(image_path):
## Open an image file
    with Image.open(image_path) as img:
        # Ask the user to choose a dimension
        print("Choose a dimension for resizing the image:")
        print("1. 256x256")
        print("2. 512x512")
        print("3. 1024x1024")
        option = input("Enter your option: ")
        if option == "1":
            target_size = (256, 256)
        elif option == "2":
            target_size = (512, 512)
        elif option == "3":
            target_size = (1024, 1024)
        else:
            print("Invalid option. Using default size 256x256.")
            target_size = (256, 256)

        # Resize the image
        resized_img = img.resize(target_size)

        # Save the resized image
        resized_img.save('resized_image.png')
```
{Try it!|terminal}(python3 main.py 11)


We're asking the user to choose a dimension for resizing the image. If the user's choice is not among the three options (1, 2, or 3), we default to the size 256x256. After the user makes their choice, we resize the image to the selected dimension and save it as `'resized_image.png'` .

Let's add a little message saying the function ended.
```python
print("Your given image was resized and saved under `resized_image.png` ")
```
{Try it!|terminal}(python3 main.py 12)

[Click here to refresh your resized image](close_file resized_image.png panel=1; open_file resized_image.png panel=1) 

{Check It!|assessment}(multiple-choice-524912195)
