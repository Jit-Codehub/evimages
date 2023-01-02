from django.shortcuts import render, redirect
import glob
import os
from pathlib import Path
import shutil
from os.path import exists
from PIL import Image, ImageFont, ImageDraw 



# Create your views here.

def images(request,title=None):
    """adds hyphen in title and redirects it to image url"""
    title = '-'.join(title.strip().split())
    print(request.build_absolute_uri())
    return redirect("image", title=title) 



def timages(request, title=None):
    if " " in title:
        return redirect(images, title)
    file_name = title

    
    title = title.replace('-',' ')
    if exists(f"media/cars_images/{file_name}.jpg"):
        #runs if image already exists and returns it
        context = {
       "url":f"media/cars_images/{file_name}.jpg",
       "title": title,
       "Des":f"{title} is one of the best electric vehicle in the world.",
       "imgDes":f"{title}",
        }
        return render(request,"images.html",context)
   

    my_image = Image.open("static/google.png")
    title_font = ImageFont.truetype('carsimage/Roboto/Roboto-Regular.ttf', 18)
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((115,228), title, (18, 17, 17), font=title_font)
    imagePath = f"media/cars_images/{file_name}.jpg"

    my_image.save(imagePath)
    context = {
       "url":imagePath,
       "title": title,
       "Des":f"{title} is one of the best electric vehicle in the world.",
       "imgDes":f"{title}",
    }
    return render(request,"images.html",context)



def g(request,title=None):
    """adds hyphen in title and redirects it to gif url"""
    title = '-'.join(title.strip().split())
    print(request.build_absolute_uri())
    return redirect("gif", title=title)  
    


def gif(request,title=None):
    if " " in title:
        return redirect(g, title)
    my_image = Image.open("static/google.png")
    title_font = ImageFont.truetype('carsimage/Roboto/Roboto-Regular.ttf', 18)
    file_name = title
    title = title.replace('-',' ')

    if exists(f"media/gif/{file_name}.gif"):
        #runs if gif already exists and returns it
        context = {
       "url":f"media/gif/{file_name}.gif",
       "title": title,
       "Des":f"{title} is one of the best electric vehicle in the world.",
       "imgDes":f"{title}",
        }
        return render(request,"images.html",context)


    BASE_DIR = Path(__file__).resolve().parent.parent 
    directory = "gif-images"
    path = os.path.join(BASE_DIR, directory)
    os.makedirs(path) #creates a folder "gif-images"
    for i in range(len(title)):
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((115,228), title[:i+1], (18, 17, 17), font=title_font)
        n = title[:i+1]
        imagePath = f"gif-images/{n}.jpg"
        my_image.save(imagePath)

    frames = [Image.open(image) for image in glob.glob(f"gif-images/*.jpg")]
    frame_one = frames[0]
    frame_one.save(f"media/gif/{file_name}.gif", format="GIF", append_images=frames,
               save_all=True, duration=500, loop=0)
    
    shutil.rmtree(path) #deletes folder "gif-images" after GIF has been saved in "media/gif/"
    context = {
       "url":f"media/gif/{file_name}.gif",
       "title": title,
       "Des":f"{title} is one of the best electric vehicle in the world.",
       "imgDes":f"{title}",
    }
    return render(request,"images.html",context)
    
