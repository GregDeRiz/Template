from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def story(request):
    return render(request, "story.html")

def contact(request):
    return render(request, "contact.html")

