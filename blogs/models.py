from django.contrib.auth.models import AbstractUser
from django.db import models

# CUSTOM USER MODEL

class CustomUser(AbstractUser):

    full_name = models.CharField(
        max_length=150
    )

    def __str__(self):

        return self.username

# BLOG MODEL

class BlogModel(models.Model):

    CATEGORY_CHOICES = [

        (
            "Educational",
            "Educational"
        ),

        (
            "Technologies",
            "Technologies"
        ),

        (
            "Sports",
            "Sports"
        ),
    ]


    title = models.CharField(
        max_length=200
    )


    author_name = models.CharField(
        max_length=150
    )


    content = models.TextField()


    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )


    blog_image = models.ImageField(
        upload_to="blog_images/",
        blank=True,
        null=True
    )


    publish_date = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:

        ordering = [
            "-publish_date"
        ]


    def __str__(self):

        return self.title
