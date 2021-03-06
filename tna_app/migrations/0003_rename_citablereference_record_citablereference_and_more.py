# Generated by Django 4.0.4 on 2022-05-27 21:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tna_app', '0002_record_citablereference_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='citablereference',
            new_name='citableReference',
        ),
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
