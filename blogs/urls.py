from django.urls import path

from .views import (
    home,
    register_view,
    login_view,
    logout_view,
    blog_list,
    blog_detail,
    blog_create,
    blog_update,
    blog_delete,
)


urlpatterns = [

    # Home
    path(
        "",
        home,
        name="home"
    ),


    # Register
    path(
        "register/",
        register_view,
        name="register"
    ),


    # Login
    path(
        "login/",
        login_view,
        name="login"
    ),


    # Logout
    path(
        "logout/",
        logout_view,
        name="logout"
    ),


    # Blog List
    path(
        "blogs/",
        blog_list,
        name="blog_list"
    ),


    # Add Blog
    path(
        "blogs/add/",
        blog_create,
        name="blog_create"
    ),


    # Blog Detail
    path(
        "blogs/<int:pk>/",
        blog_detail,
        name="blog_detail"
    ),


    # Update
    path(
        "blogs/<int:pk>/edit/",
        blog_update,
        name="blog_update"
    ),


    # Delete
    path(
        "blogs/<int:pk>/delete/",
        blog_delete,
        name="blog_delete"
    ),
]
