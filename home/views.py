from django.shortcuts import render
from django.contrib import messages


def home(request):
    if request.method == "POST":
        new_message = "Successful upload!"
        return render(request, "home.html", {"new_message": new_message},)
    return render(request, "home.html", )

