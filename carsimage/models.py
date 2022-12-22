from django.db import models

# Create your models here.
class AutoGenFeaturedImageWhitelist(models.Model):
    default_image = models.CharField(max_length=255,unique=True)
    whitelist_urls = models.TextField()

    def __str__(self) -> str:
        return self.default_image

    def clean(self) -> None:
        if self.default_image.startswith("http"):
            self.default_image = "-".join(self.default_image.strip("/").split("/")[3:])
        if not self.default_image.endswith(".webp"):
            self.default_image += ".webp"
        whitelist_urls = ""
        for url in self.whitelist_urls.split():
            if url and url.startswith("http"):
                url = "-".join(url.strip("/").split("/")[3:])
            whitelist_urls += f"{url}\n"
        self.whitelist_urls = whitelist_urls
        return super().clean()