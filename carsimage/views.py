from django.shortcuts import render, redirect
from carsimage.task import getMetaImg
import glob
import os
from pathlib import Path
import shutil
from os.path import exists

# file_exists = exists(path_to_file)


# Create your views here.
from PIL import Image, ImageFont, ImageDraw 

def images(request,title=None):
    # title = title.strip()
    title = '-'.join(title.strip().split())
    print("########################################")
    print(request.build_absolute_uri())
    return redirect("image", title=title) 

# def images(request):

#     my_image = Image.open("static/google.png")
#     title_font = ImageFont.truetype('carsimage/Roboto/Roboto-Black.ttf', 20)
#     title_text = "Evcarshub tesla"
#     image_editable = ImageDraw.Draw(my_image)
#     image_editable.text((340,345), title_text, (18, 17, 17), font=title_font)
#     imagePath = f"media/cars_images/{title_text.replace(' ','_')}.jpg"

#     my_image.save(imagePath)
#     context = {
#        "url":imagePath,
#        "title": title_text,
#        "Des":f"{title_text} is one of the best electric vechile in the world.",
#        "imgDes":f"{title_text}",
#     }
#     return render(request,"images.html",context)

# def home(request):
#     print("I am home function")
#      # Auto gen img
#     default_image = "I am home"
#     meta_img_content = f"I am content"
#     meta_img_url = getMetaImg(request.build_absolute_uri(),default_image,meta_img_content)

#     context = {
#            "meta_img_url":meta_img_url,
#             "meta_img_content":meta_img_content

#         }
#     return render(request,'home.html', context)

# <img class="image" src="{{meta_img_url}}" alt="{{meta_img_content}}">

def timages(request, title=None):
    if " " in title:
        return redirect(images, title)
    file_name = title

    

    title = title.replace('-',' ')
    # print(exists(f"media/cars_images/{file_name}.jpg"))
    if exists(f"media/cars_images/{file_name}.jpg"):
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        context = {
       "url":f"media/cars_images/{file_name}.jpg",
       "title": title,
       "Des":f"{title} is one of the best electric vechile in the world.",
       "imgDes":f"{title}",
        }
        return render(request,"images.html",context)
    # title = str(title)
    # car_list = ["evcarshub tesla","evcarshub Nano","evcarshub Nexon","evcarshub ford",]
    # for i in car_list:
    #     if i.casefold() == title.casefold():
    #         return 

    my_image = Image.open("static/google.png")
    title_font = ImageFont.truetype('carsimage/Roboto/Roboto-Black.ttf', 20)
    # title = title
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((340,345), title, (18, 17, 17), font=title_font)
    imagePath = f"media/cars_images/{file_name}.jpg"

    my_image.save(imagePath)
    context = {
       "url":imagePath,
       "title": title,
       "Des":f"{title} is one of the best electric vechile in the world.",
       "imgDes":f"{title}",
    }
    print("=================================================================")
    return render(request,"images.html",context)



def g(request,title=None):
    # title = title.strip()
    title = '-'.join(title.strip().split())
    print("########################################")
    print(request.build_absolute_uri())
    return redirect("gif", title=title)  
    


def gif(request,title=None):
    if " " in title:
        return redirect(g, title)
    my_image = Image.open("static/google.png")
    title_font = ImageFont.truetype('carsimage/Roboto/Roboto-Black.ttf', 20)
    file_name = title
    title = title.replace('-',' ')

    if exists(f"media/gif/{file_name}.gif"):
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        context = {
       "url":f"media/gif/{file_name}.gif",
       "title": title,
       "Des":f"{title} is one of the best electric vechile in the world.",
       "imgDes":f"{title}",
        }
        return render(request,"images.html",context)


    # image_editable = ImageDraw.Draw(my_image)
    BASE_DIR = Path(__file__).resolve().parent.parent 
    directory = "gif-images"
    path = os.path.join(BASE_DIR, directory)
    os.makedirs(path)
    # print(path)
    for i in range(len(title)):
        image_editable = ImageDraw.Draw(my_image)

        image_editable.text((340,345), title[:i+1], (18, 17, 17), font=title_font)
        n = title[:i+1]
        print("**************************")
        print(n)
        imagePath = f"gif-images/{n}.jpg"

        my_image.save(imagePath)



        
    # image_editable.text((340,345), title, (18, 17, 17), font=title_font)
    # imagePath = f"media/cars_images/{title.replace(' ','_')}.jpg"

    # my_image.save(imagePath)

    frames = [Image.open(image) for image in glob.glob(f"gif-images/*.jpg")]
    print("**************************")
    # print(frames)
    # BASE_DIR = Path(__file__).resolve().parent.parent 
    # directory = "gif-images"
    # path = os.path.join(BASE_DIR, directory)

    # print(path)
    # os.makedirs(path)

    # shutil.rmtree(path)
    
    frame_one = frames[0]
    frame_one.save(f"media/gif/{file_name}.gif", format="GIF", append_images=frames,
               save_all=True, duration=500, loop=0)
    # frame_one.save("static/my_awesome.gif", format="GIF", append_images=frames,
    #            save_all=True, duration=500, loop=0)
    shutil.rmtree(path)
    context = {
       "url":f"media/gif/{file_name}.gif",
    #    "title": title,
    #    "Des":f"{title} is one of the best electric vechile in the world.",
    #    "imgDes":f"{title}",
    }
    return render(request,"images.html",context)
    
# if __name__ == "__main__":
#     gif("/path/to/images")