from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from .models import Record
from django.shortcuts import get_object_or_404


# API url
url = "http://discovery.nationalarchives.gov.uk/API/records/v1/details/"


# initial view where user can type in the recordID
def get_id(request):

    id = request.POST.get("record_text", "")
    # build API url to get record
    url = "http://discovery.nationalarchives.gov.uk/API/records/v1/details/%s" % id

    # GET
    response = requests.get(url)
    # GET successfuly received status 200, record is there
    if response.status_code == 200:
        data = response.json()
        title = data["title"]
        scopeContent_description = data["scopeContent"]["description"]
        citableReference = data["citableReference"]
        print(title)
        print(scopeContent_description)
        print(citableReference)
        # create  Record object from Models
        newrecord = Record(
            id=id,
            title=title,
            scopeContent_description=scopeContent_description,
            citableReference=citableReference,
        )
        # Save record to Model database
        newrecord, created = Record.objects.get_or_create(
            id=id,
            title=title,
            scopeContent_description=scopeContent_description,
            citableReference=citableReference,
        )
        # Redirect to display record details
        record_detail(request, id)
        return redirect("record_detail", id=id)
    # if recordID is not found/ invalid record ID
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
    # get record from the database
    record = get_object_or_404(Record, pk=id)
    # apply logic for what fields of the record to display to user and save fields to display
    #  into a new Record object
    display_record = record_display_logic(record)
    # render this new object showing only the appropriate fields as per instructions
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
