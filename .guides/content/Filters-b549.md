The last option we are going to cover in our lab is to create a function that creates a filter of a given image. Let's start by adding our print statement at the top of our `main` function. 
```python
print("4. Add a filter to your image")
```
{Try it!|terminal}(python3 main.py 13)
Then we are going to create an extra option after option 3. Let's call it option 4. 
```python
elif option=="4":
          image_path = input("Enter the path of the image you want to add a filter to: ")
          # run filter function
          filters(image_path)
```

Now we are ready to add our extra function that adds filters using PIL. Our function should ask the user to pick which filter they want to apply. The options are :
1. `contour`: The contour filter traces the edges of objects in the image, creating a high-contrast, black-and-white image that highlights the shapes in the scene.
1. `EDGE_ENHANCE`: The edge enhance filter highlights the edges of objects in the image, making them more distinct and pronounced. This filter can be used to create a more stylized or artistic effect.
1. `FIND_EDGES`: The find edges filter detects the edges of objects in the image and creates a high-contrast, black-and-white image that highlights these edges.


First, our function should open an image file. Then we prompt the user to choose one of the three provided filters to apply to the image. If the user's input is not among the three options (1, 2, or 3), we default to the Contour filter. After applying the chosen filter, we save the result to `filtered_image.jpg` in the current directory.

```python 
def filters(image_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Ask the user to choose a filter
        print("Choose a filter to apply on the image:")
        print("1. Contour")
        print("2. Edge Enhance")
        print("3. Find Edges")
        option = input("Enter your option: ")

        if option == "1":
            filtered_img = img.filter(ImageFilter.CONTOUR)
        elif option == "2":
            filtered_img = img.filter(ImageFilter.EDGE_ENHANCE)
        elif option == "3":
            filtered_img = img.filter(ImageFilter.FIND_EDGES)
        else:
            print("Invalid option. Applying Contour filter by default.")
            filtered_img = img.filter(ImageFilter.CONTOUR)
        
        # Save the filtered image
        filtered_img.save('filtered_image.png')
        print("Filter applied successfully, 'filtered_image.png' created.")

```
{Try it!|terminal}(python3 main.py 14)
[Click here to refresh your filtered image](close_file filtered_image.png panel=1; open_file filtered_image.png panel=1) 


{Check It!|assessment}(fill-in-the-blanks-3496964524)
