
The **Gaussian blur** filter softens the image by reducing noise and details. This filter can be used to create a dreamy or ethereal effect, or to reduce noise in an image. We have interacted with it in our previous assignment.

To implement the Gaussian blur in PIL, we use the filter function with `ImageFilter.GaussianBlur`. As an example, here's a code snippet that applies a Gaussian blur filter to an image with a radius of 5:
```python
# Apply a Gaussian blur filter to the base image
blurred_image = img.filter(ImageFilter.GaussianBlur(radius=5))
```

For our coding exercise, you are going to add an extra option to your `filter` function. That function should apply Gaussian Blur to a given image, if the user selects option 4. As a bonus feel free to add a 5th option that shows your current directory's files.

{Try it!|terminal}(python3 main.py)
[Click here to refresh your filtered image](close_file filtered_image.png panel=1; open_file filtered_image.png panel=1) 

{Check It!|assessment}(code-output-compare-1706188383)