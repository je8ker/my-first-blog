# Generated by Django 4.1 on 2023-03-30 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_fileupload"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fileupload",
            name="content",
        ),
    ]
