# Generated by Django 4.1.3 on 2023-01-11 07:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_alter_rhymes_date"),
    ]

    operations = [
        migrations.DeleteModel(
            name="WordOfTheDay",
        ),
        migrations.AddField(
            model_name="rhymes",
            name="word_of_the_day",
            field=models.CharField(default="", max_length=250),
        ),
        migrations.AlterField(
            model_name="rhymes",
            name="date",
            field=models.CharField(default=datetime.date(2023, 1, 11), max_length=250),
        ),
    ]
