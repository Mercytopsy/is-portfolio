from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,"index.html")


def about (request):
    return render (request, "about.html")

def experience (request):
    return render (request, "experience.html")

def education (request):
    return render (request, "education.html")

def publications (request):
    return render (request, "publications.html")

def skills (request):
    return render (request, "skills.html")

def projects (request):
    return render (request, "projects.html")

def awards (request):
    return render (request, "awards.html")
