from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from .models import Record
from django.shortcuts import get_object_or_404


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

        newrecord, created = Record.objects.get_or_create(
            id=id,
            title=title,
            scopeContent_description=scopeContent_description,
            citableReference=citableReference,
        )

        record_detail(request, id)
        return redirect("record_detail", id=id)

    elif response.status_code == 204:
        return render(request, "notfound.html")

    return render(
        request,
        "id.html",
        {
            "record_text": request.POST.get("record_text", ""),
        },
    )


def record_detail(request, id):

    record = get_object_or_404(Record, pk=id)
    display_record = record_display_logic(record)

    return render(request, "record_detail.html", context={"record": display_record})


# choose which fields to display based on if they are Null or not
def record_display_logic(record):
    if record.title is not None:
        newrecord = Record(id=record.id, title=record.title)

    if record.title is None:
        if record.scopeContent_description is not None:
            newrecord = Record(
                id=record.id, scopeContent_description=record.scopeContent_description
            )

    if record.title is None:
        if record.scopeContent_description is None:
            if record.citablereference is not None:
                newrecord = Record(
                    id=record.id, citablereference=record.citablereference
                )
    if record.title is None:
        if record.scopeContent_description is None:
            if record.citablereference is None:
                newrecord = Record(
                    id=record.id, message_to_user="not sufficient information"
                )

    return newrecord
