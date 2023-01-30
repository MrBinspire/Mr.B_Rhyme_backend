from django.contrib import admin
from .models import *


class RhymesAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "word", "Word_of_the_day")


class WordOfTheDayAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "Word_of_the_day")

class AcceptedAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "word", "Word_of_the_day","count")

class RejectedAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "word", "Word_of_the_day","count")

admin.site.register(Rhymes, RhymesAdmin)
admin.site.register(WordOfTheDay, WordOfTheDayAdmin)
admin.site.register(Accepted, AcceptedAdmin)
admin.site.register(Rejected, RejectedAdmin)

