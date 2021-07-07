from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd


def home(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        dataset = pd.read_csv(csv_file, encoding="utf-8-sig")
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=download.csv'
        dataset.to_csv(path_or_buf=response, float_format='%.2f', index=False,)
        return response
        #new_message = str(dataset.columns)
        # return render(request, "home.html", {"new_message": new_message}, )
    return render(request, "home.html", )


def dashboard(request):
    return render(request, "dashboard.html", )
