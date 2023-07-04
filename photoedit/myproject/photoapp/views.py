from django.shortcuts import render

# Create your views here.


from rembg import remove
from PIL import Image

input_path = 'ear.jpg' # input image path
output_path = 'ear_.png' # output image path

input = Image.open(input_path) # load image
output = remove(input) # remove background
output.save(output_path) # save image