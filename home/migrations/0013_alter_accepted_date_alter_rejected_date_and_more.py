# Generated by Django 4.1.4 on 2023-02-27 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0012_rename_word_of_the_day_rhymes_word_of_the_day_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accepted",
            name="date",
            field=models.CharField(default=datetime.date(2023, 2, 27), max_length=250),
        ),
        migrations.AlterField(
            model_name="rejected",
            name="date",
            field=models.CharField(default=datetime.date(2023, 2, 27), max_length=250),
        ),
        migrations.AlterField(
            model_name="rhymes",
            name="date",
            field=models.CharField(default=datetime.date(2023, 2, 27), max_length=250),
        ),
    ]
