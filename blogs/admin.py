from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import (
    CustomUser,
    BlogModel
)

# CUSTOM USER ADMIN

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (

        (
            "Additional Information",
            {
                "fields": (
                    "full_name",
                )
            }
        ),
    )


    add_fieldsets = UserAdmin.add_fieldsets + (

        (
            "Additional Information",
            {
                "fields": (
                    "full_name",
                    "email"
                )
            }
        ),
    )


    list_display = (

        "username",

        "full_name",

        "email",

        "is_staff",

        "is_active",
    )

# BLOG ADMIN

@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):

    list_display = (

        "title",

        "author_name",

        "category",

        "publish_date",
    )


    list_filter = (

        "category",

        "publish_date",
    )


    search_fields = (

        "title",

        "author_name",

        "content",
    )

