# Generated by Django 4.1 on 2022-08-07 05:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("reference", "0001_initial"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="referencerequest",
            name="requester",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="referencerequest",
            name="requester_company",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="user.company"),
        ),
        migrations.AddField(
            model_name="reference",
            name="reference_request",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="reference.referencerequest",
            ),
        ),
        migrations.AddField(
            model_name="reference",
            name="writer",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]