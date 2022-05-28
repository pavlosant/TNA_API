from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from .models import Record

# Create your views here.

url = "http://discovery.nationalarchives.gov.uk/API/records/v1/details/"


def home_page(request):
    return render(request, "home.html")


def get_id(request):

    id = request.POST.get("record_text", "")

    print(id)

    url = "http://discovery.nationalarchives.gov.uk/API/records/v1/details/%s" % id
    print(url)

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        title = data["title"]
        scopeContent_description = data["scopeContent"]["description"]
        citableReference = data["citableReference"]
        print(title)
        print(scopeContent_description)
        print(citableReference)
        newrecord = Record(
            id=id,
            title=title,
            scopeContent_description=scopeContent_description,
            citableReference=citableReference,
        )
        # newrecord.save()
        newrecord, created = Record.objects.get_or_create(
            id=id,
            title=title,
            scopeContent_description=scopeContent_description,
            citableReference=citableReference,
        )
        return render(request, "record_detail.html", {"record": newrecord})
        # record_detail(request, id)

    elif response.status_code == 204:
        print("INVALID")
        return render(request, "notfound.html")

    return render(
        request,
        "id.html",
        {
            "record_text": request.POST.get("record_text", ""),
        },
    )


def record_detail(request, id):
    print("villos")
    print(id)
    record = Record.objects.get(id=id)
    print(record)
    return render(request, "record_detail.html", {"record": record})
