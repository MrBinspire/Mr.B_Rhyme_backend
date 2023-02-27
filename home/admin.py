from django.contrib import admin
from .models import *


class RhymesAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "word", "Word_of_the_day")
    search_fields = ('word',)


class WordOfTheDayAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "Word_of_the_day")


class AcceptedAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "user", "word", "Word_of_the_day", "count")
    search_fields = ('word',)


class RejectedAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "user", "word", "Word_of_the_day", "count")
    search_fields = ('word',)


admin.site.register(Rhymes, RhymesAdmin)
admin.site.register(WordOfTheDay, WordOfTheDayAdmin)
admin.site.register(Accepted, AcceptedAdmin)
admin.site.register(Rejected, RejectedAdmin)
