The transformative capability of OpenAI's DALL-E extends beyond generating images from scratch; it can also generate variations of existing images. This capacity enriches the creative process, providing novel perspectives and interpretations of a given subject, or assisting in creating different versions of the same concept. For our second option we are going to interact with the following function:

```python-hide-clipboard
def create_variations(img):
    # Create variations of an image using PIL
    print("Creating variations of the image...")
    # Call DALL-E API here
```
The Images API offers three methods of interaction with images, one of which is creating variations of an existing image. The API's image variation endpoint enables the generation of images similar to the input image. This feature is particularly useful when you have a base image and want to create variations without manually editing the image.

The code to generate a variation of an image is similar to that used for generating an image from scratch, with a few minor differences:


Instead of providing a textual prompt as we did while creating an image from scratch, we give DALL-E an existing image as a prompt. The image parameter in `openai.Image.create_variation` expects an open image file in read-binary mode ("rb"). Make sure the image is located locally, or will have to provide the whole path. 

```python
response = openai.Image.create_variation(
  image=open(img, "rb"),
  n=1,
  size="256x256"
)
```
{Try it!|terminal}(python3 main.py 7)

Just like in the image creation process, DALL-E returns a URL for the created variation image, which you can extract from the response.
```python
image_url = response['data'][0]['url']
```
{Try it!|terminal}(python3 main.py 8)

```python
img_data = requests.get(image_url).content
with open('image_var.png', 'wb') as handler:
    handler.write(img_data)
```
{Try it!|terminal}(python3 main.py 9)

Just to make everything more clear you can try adding a print statement at the end to indicate your function finished running.
```python
print("Your image was generated under the `image_var.png` file name.")
```
{Try it!|terminal}(python3 main.py 10)


[Click here to refresh your var image](close_file image_var.png panel=1; open_file image_var.png panel=1) 



By employing DALL-E's image variation capabilities, you can diversify your image portfolio, generate fresh ideas, or improve the original design.

{Check It!|assessment}(multiple-choice-3684191972)
