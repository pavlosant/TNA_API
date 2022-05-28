from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_id, name="home"),
    path("records/<uuid:id>/", views.record_detail, name="record_detail"),
]
