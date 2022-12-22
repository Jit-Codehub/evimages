from django.shortcuts import render
from carsimage.task import getMetaImg

# Create your views here.
def home(request):
    print("I am home function")
     # Auto gen img
    default_image = "I am home"
    meta_img_content = f"I am content"
    meta_img_url = getMetaImg(request.build_absolute_uri(),default_image,meta_img_content)

    context = {
           "meta_img_url":meta_img_url,
            "meta_img_content":meta_img_content

        }
    return render(request,'home.html', context)

# <img class="image" src="{{meta_img_url}}" alt="{{meta_img_content}}">
