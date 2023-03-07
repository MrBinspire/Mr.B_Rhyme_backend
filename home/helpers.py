from .models import *
from datetime import date
from django.contrib.auth.models import User


def check_duplicates_rhymes(data):
    input_word = data['word']

    obj = Rhymes.objects.all()
    available_words = []
    for i in obj:
        available_words.append(i.word)
    print(available_words)
    if input_word in available_words or input_word == "":
        return True
    else:
        return False


def check_duplicates_accepted(data):
    input_word = data['word']

    obj = Accepted.objects.all()
    available_words = []
    for i in obj:
        available_words.append(i.word)
    print(available_words)
    if input_word in available_words or input_word == "":
        return True
    else:
        return False


def check_duplicate_date():
    req_date = str(date.today())
    obj = WordOfTheDay.objects.all()
    available_dates = []
    for i in obj:
        available_dates.append(i.date)
    # print(available_dates)
    if req_date in available_dates:
        return False
    else:
        return True


def get_user_info(username):
    try:
        obj = User.objects.get(username=username)
        return obj
    except Exception as e:
        print(e)
        return None
