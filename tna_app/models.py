from django.db import models
import uuid

# Create your models here.
class Record(models.Model):
    # Noticed some of the records on database have string id and not all are uuid
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.CharField(max_length=50, primary_key=True, editable=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    scopeContent_description = models.CharField(max_length=1000, blank=True, null=True)
    citableReference = models.CharField(max_length=1000, blank=True, null=True)
    message_to_user = models.CharField(max_length=50, blank=True, null=True)
