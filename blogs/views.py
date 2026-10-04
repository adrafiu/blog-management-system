from django.contrib import messages

from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model
)

from django.contrib.auth.decorators import login_required

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import BlogModel


User = get_user_model()

# HOME


def home(request):

    return render(
        request,
        "home.html"
    )

# REGISTER


def register_view(request):

    # Already logged in
    if request.user.is_authenticated:

        return redirect("home")


    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()


        full_name = request.POST.get(
            "full_name",
            ""
        ).strip()


        email = request.POST.get(
            "email",
            ""
        ).strip()


        password = request.POST.get(
            "password",
            ""
        )


        confirm_password = request.POST.get(
            "confirm_password",
            ""
        )



        # VALIDATION
        

        if not username:

            messages.error(
                request,
                "Username is required."
            )

            return render(
                request,
                "register.html"
            )


        if not full_name:

            messages.error(
                request,
                "Full name is required."
            )

            return render(
                request,
                "register.html"
            )


        if not email:

            messages.error(
                request,
                "Email is required."
            )

            return render(
                request,
                "register.html"
            )


        if not password:

            messages.error(
                request,
                "Password is required."
            )

            return render(
                request,
                "register.html"
            )


        if len(password) < 8:

            messages.error(
                request,
                "Password must be at least 8 characters."
            )

            return render(
                request,
                "register.html"
            )


        if password != confirm_password:

            messages.error(
                request,
                "Passwords do not match."
            )

            return render(
                request,
                "register.html"
            )


        
        # USERNAME CHECK


        if User.objects.filter(
            username__iexact=username
        ).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return render(
                request,
                "register.html"
            )


        
        # EMAIL CHECK
        

        if User.objects.filter(
            email__iexact=email
        ).exists():

            messages.error(
                request,
                "Email already exists."
            )

            return render(
                request,
                "register.html"
            )


        
        # CREATE USER
        

        user = User.objects.create_user(

            username=username,

            email=email,

            password=password,

            full_name=full_name
        )


        
        # LOGIN AFTER REGISTRATION
        

        login(
            request,
            user
        )


        messages.success(
            request,
            f"Welcome {full_name}! Registration successful."
        )


        return redirect("home")


    return render(
        request,
        "register.html"
    )

# LOGIN

def login_view(request):

    if request.user.is_authenticated:

        return redirect("home")


    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()


        password = request.POST.get(
            "password",
            ""
        )


        if not username or not password:

            messages.error(
                request,
                "Username and password are required."
            )

            return render(
                request,
                "login.html"
            )


        # Authenticate user

        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(
                request,
                user
            )


            messages.success(
                request,
                "Login successful. Welcome back!"
            )


            return redirect(
                "home"
            )


        messages.error(
            request,
            "Invalid username or password."
        )


    return render(
        request,
        "login.html"
    )

# LOGOUT

def logout_view(request):

    logout(request)


    messages.success(
        request,
        "You have been logged out successfully."
    )


    return redirect(
        "home"
    )

# BLOG LIST

@login_required
def blog_list(request):

    blogs = BlogModel.objects.all()


    return render(
        request,
        "blog_list.html",
        {
            "blogs": blogs
        }
    )

# BLOG DETAIL

@login_required
def blog_detail(request, pk):

    blog = get_object_or_404(
        BlogModel,
        pk=pk
    )


    return render(
        request,
        "blog_detail.html",
        {
            "blog": blog
        }
    )

# ADD BLOG

@login_required
def blog_create(request):

    if request.method == "POST":

        title = request.POST.get(
            "title",
            ""
        ).strip()


        content = request.POST.get(
            "content",
            ""
        ).strip()


        category = request.POST.get(
            "category",
            ""
        )


        blog_image = request.FILES.get(
            "blog_image"
        )


        
        # VALIDATION
        

        if not title:

            messages.error(
                request,
                "Blog title is required."
            )

            return render(
                request,
                "blog_form.html",
                {
                    "page_title":
                    "Add New Blog Post"
                }
            )


        if not content:

            messages.error(
                request,
                "Blog content is required."
            )

            return render(
                request,
                "blog_form.html",
                {
                    "page_title":
                    "Add New Blog Post"
                }
            )


        if category not in [
            "Educational",
            "Technologies",
            "Sports"
        ]:

            messages.error(
                request,
                "Please select a valid category."
            )

            return render(
                request,
                "blog_form.html",
                {
                    "page_title":
                    "Add New Blog Post"
                }
            )


        
        # CREATE BLOG
        

        blog = BlogModel.objects.create(

            title=title,

            author_name=(
                request.user.full_name
                or request.user.username
            ),

            content=content,

            category=category,

            blog_image=blog_image
        )


        messages.success(
            request,
            "Blog post added successfully."
        )


        return redirect(
            "blog_detail",
            pk=blog.pk
        )


    return render(
        request,
        "blog_form.html",
        {
            "page_title":
            "Add New Blog Post"
        }
    )



# UPDATE BLOG


@login_required
def blog_update(request, pk):

    blog = get_object_or_404(
        BlogModel,
        pk=pk
    )


    if request.method == "POST":

        title = request.POST.get(
            "title",
            ""
        ).strip()


        content = request.POST.get(
            "content",
            ""
        ).strip()


        category = request.POST.get(
            "category",
            ""
        )


        blog_image = request.FILES.get(
            "blog_image"
        )


        
        # VALIDATION
        

        if not title:

            messages.error(
                request,
                "Blog title is required."
            )

            return render(
                request,
                "blog_form.html",
                {
                    "page_title":
                    "Update Blog Post",

                    "blog":
                    blog
                }
            )


        if not content:

            messages.error(
                request,
                "Blog content is required."
            )

            return render(
                request,
                "blog_form.html",
                {
                    "page_title":
                    "Update Blog Post",

                    "blog":
                    blog
                }
            )


        if category not in [
            "Educational",
            "Technologies",
            "Sports"
        ]:

            messages.error(
                request,
                "Please select a valid category."
            )

            return render(
                request,
                "blog_form.html",
                {
                    "page_title":
                    "Update Blog Post",

                    "blog":
                    blog
                }
            )


        
        # UPDATE BLOG
        

        blog.title = title

        blog.content = content

        blog.category = category

        blog.author_name = (
            request.user.full_name
            or request.user.username
        )


        if blog_image:

            blog.blog_image = blog_image


        blog.save()


        messages.success(
            request,
            "Blog post updated successfully."
        )


        return redirect(
            "blog_detail",
            pk=blog.pk
        )


    return render(
        request,
        "blog_form.html",
        {
            "page_title":
            "Update Blog Post",

            "blog":
            blog
        }
    )



# DELETE BLOG


@login_required
def blog_delete(request, pk):

    blog = get_object_or_404(
        BlogModel,
        pk=pk
    )


    if request.method == "POST":

        blog.delete()


        messages.success(
            request,
            "Blog post deleted successfully."
        )


        return redirect(
            "blog_list"
        )


    return render(
        request,
        "blog_confirm_delete.html",
        {
            "blog": blog
        }
    )
