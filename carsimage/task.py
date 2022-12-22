from django.template.loader import render_to_string
from django.conf import settings
from PIL import Image
import imgkit
import os
from .models import AutoGenFeaturedImageWhitelist
import re


FEATURED_OPTIONS = {
    "quiet": "",
    "format": "jpg",
    "width": 1200,
    "height": 630,
    # "load-error-handling": "ignore",
    # "load-media-error-handling": "ignore",
    # "enable-local-file-access": None,
}
FEATURED_OUTPUT_PATH = os.path.join(settings.MEDIA_ROOT, "featured_images")


def convertImgToWebp(image_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    image.save(image_path, 'webp')


def genImg(output_img_path, template_name, context):
    html_string = render_to_string(template_name, context)
    imgkit.from_string(html_string, output_img_path, options=FEATURED_OPTIONS)
    convertImgToWebp(output_img_path)


def getMetaImg(absolute_uri,default_image,meta_img_content=None):
    suburl = re.search("http[s]?://.*?/(.*?)/.*",absolute_uri).group(1)
    filename = f"{suburl}.webp"
    output_img_path = os.path.join(FEATURED_OUTPUT_PATH, filename)
    template_name = "task/autogen_featured_img_template.html"

    if not meta_img_content:
        meta_img_content = suburl.replace("-"," ").title()

    if not default_image.endswith(".webp"):
        default_image += ".webp"

    whitelist_obj = AutoGenFeaturedImageWhitelist.objects.filter(default_image=default_image)
    if whitelist_obj:
        whitelist_obj = whitelist_obj.first()
        whitelist_urls = whitelist_obj.whitelist_urls.split() + [default_image.replace(".webp","")]
        if suburl in whitelist_urls:
            if not os.path.exists(output_img_path):
                genImg(output_img_path, template_name, {"para_content":meta_img_content})
            return f"{settings.MEDIA_URL}featured_images/{filename}"

    filename = default_image
    default_image_path = os.path.join(FEATURED_OUTPUT_PATH, filename)
    if not os.path.exists(default_image_path):
        if suburl != default_image.replace(".webp",""):
            meta_img_content = default_image.replace(".webp","").replace("-"," ").title()
        genImg(default_image_path, template_name, {"para_content":meta_img_content})

    return f"{settings.MEDIA_URL}featured_images/{filename}"