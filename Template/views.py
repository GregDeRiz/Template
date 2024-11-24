from django.shortcuts import render


def story(request):
    return render(request, "story.html")

def contact(request):
    return render(request, "contact.html")
