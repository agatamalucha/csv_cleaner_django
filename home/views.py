from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import datetime


def home(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        dataset_vaccination = pd.read_csv(csv_file, encoding="utf-8-sig")
        country_dict = {"BG": "Bulgaria", "CY": "Cyprus", "CZ": "Czech Republic", "DE": "Germany",
                        "EE": "Estonia", "EL": "Greece", "FI": "Finland", "FR": "France",
                        "HR": "Croatia", "HU": "Hungary", "IE": "Ireland", "IT": "Italy",
                        "LT": "Lithuania", "LU": "Luxembourg", "LV": "Latvia", "MT": "Malta",
                        "NL": "Netherlands", "NO": "Norway", "PL": "Poland", "PT": "Portugal",
                        "SE": "Sweden", "SI": "Slovenia", "SK": "Slovakia", "AT": "Austria",
                        "BE": "Belgium", "DK": "Denmark", "ES": "Spain", "IS": "Iceland",
                        "RO": "Romania", "LI": "Lichtenstein"}


        dataset_vaccination = dataset_vaccination.rename(
            columns={"YearWeekISO": "year week", "FirstDose": "first dose", 'TargetGroup': "group",
                     "Vaccine": "vaccine", "SecondDose": "second dose", "ReportingCountry": "country"})

        def country_name(string):
            return country_dict[string]

        dataset_vaccination['country'] = dataset_vaccination["country"].apply(lambda x: country_name(x))
        dataset_vaccination = dataset_vaccination.loc[:,
                              ["year week", "first dose", "second dose", "group", "country", "vaccine"]]

        # filters all rows where in column "group" is string "ALL"
        dataset_all = dataset_vaccination["group"].isin(["ALL"])

        # Saving dataset with filtered data
        dataset_vaccination = dataset_vaccination[dataset_all]

        # Grouping by two columns (country and year week and sum number of "first dose" received)
        dataset_vaccination = dataset_vaccination.groupby(["country", "year week"])["first dose"].agg([sum])

        # Creating new column that containd indexes data
        dataset_vaccination.reset_index(inplace=True)

        # Renaming column
        dataset_vaccination = dataset_vaccination.rename(columns={"year week": "date"})

        dataset_vaccination['date'] = dataset_vaccination['date'].str.replace("W", "")
        dataset_vaccination["date"] = dataset_vaccination["date"].apply(lambda x: datetime.datetime.strptime(x + '-1', "%Y-%W-%w"))
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=download.csv'
        dataset_vaccination.to_csv(path_or_buf=response, float_format='%.2f', index=False,)

        return response

    return render(request, "home.html", )


def dashboard(request):
    return render(request, "dashboard.html", )


def my_page(request):
    return render(request, "my_page.html", )