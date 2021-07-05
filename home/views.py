from django.shortcuts import render
import pandas as pd



def home(request):
    if request.method == "POST":
        csv_file=request.FILES["csv_file"]
        dataset = pd.read_csv(csv_file, encoding="utf-8-sig")
        new_message = str(dataset.columns)
        return render(request, "home.html", {"new_message": new_message},)
    return render(request, "home.html", )

def dashboard(request):
    return render(request, "dashboard.html", )
