from django.shortcuts import render
from django.shortcuts import HttpResponse


data = {
    "blogs": [
        {
            "id": 1,
            "title": "Complete Web Programming",
            "image": "1.webp",
            "is_active": True,
            "is_home": False,
            "description": "Very well"
        },
        {
            "id": 2,
            "title": "Python Course",
            "image": "2.webp",
            "is_active": True,
            "is_home": True,
            "description": "Very well"
        },
        {
            "id": 3,
            "title": "Django Course",
            "image": "3.webp",
            "is_active": False,
            "is_home": False,
            "description": "Very well"
        }
    ]
}

def index(request):
    context = {
        "blogs": data["blogs"]
    }

    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": data["blogs"]
    }

    return render(request, "blog/blogs.html", context)


def blog_details(request, id):
    blogs = data["blogs"]
    selectedBlog = [blog for blog in blogs if blog["id"] == id][0]

    return render(request, "blog/blog-details.html", {
        "blog": selectedBlog
    })