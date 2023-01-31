# Generated by Django 4.1.3 on 2023-01-23 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_rhymes_word_of_the_day"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rhymes",
            name="is_accepted",
        ),
        migrations.AlterField(
            model_name="rhymes",
            name="date",
            field=models.CharField(default=datetime.date(2023, 1, 23), max_length=250),
        ),
    ]