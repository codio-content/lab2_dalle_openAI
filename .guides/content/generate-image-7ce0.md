Now we are going to write the first piece of our program which is the program to generate our image. All the code on this page should go under the comment `# call DALL-E API here`

```python-hide-clipboard
def generate_image(prompt1):
    # Generate the image with DALL-E
    print(f"Generating an image for the prompt: {prompt1}")
     # Call DALL-E API here

```

We are going to fill our function. You can create an image using DALL-E by providing a textual prompt, the number of images you want, and the desired size of the image. We are going to make our generic function create 1 image, with the size 256x256. 
```python 
response = openai.Image.create(
  prompt=prompt1,
  n=1,
  size="256x256"
)
```
Test out that everything runs without error before moving to the next steps.
{Try it!|terminal}(python3 main.py 3)

DALL-E generates the image and returns a response that includes a URL where the image can be accessed. You can extract this URL from the response. We already know what the URL looks like, let's extract it to a variable we can use.

```python
image_url = response['data'][0]['url']
```
{Try it!|terminal}(python3 main.py 4)

Now that you have the URL of the image, you can download it using the requests library. After sending a `GET` request to the image URL and receiving the image data, you can write this data to a file to save the image locally. For our program we will save the file generated as `image_created.png`.
```python
img_data = requests.get(image_url).content
with open('image_created.png', 'wb') as handler:
    handler.write(img_data)
```
{Try it!|terminal}(python3 main.py 5)

As an indication that our function got done running we will add a print message at the end of our code. 
```print
print("Your image was generated under the `image_created.png` file name.")
```
{Try it!|terminal}(python3 main.py 6)

The following link will open the `image_created.png` on the bottom left panel.

[Click here to refresh your image](close_file image_created.png panel=1; open_file image_created.png panel=1) 

By following these steps, you can generate a variety of images from textual prompts using DALL-E, illustrating the power of AI in creative tasks like image generation. Just like that we have our first option ready.

{Check It!|assessment}(multiple-choice-3126019534)
