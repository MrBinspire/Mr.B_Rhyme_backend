from django.shortcuts import render, redirect
import pymongo
from .models import *
from datetime import date
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .helpers import *
import logging
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
logger = logging.getLogger(__file__)

client = pymongo.MongoClient("localhost", 27017)
db = client["NanditaDb"]
collections = db["home_rhymes"]


def add_word(request):
    """User can add a word to the rhyme dictionary"""
    context = {}
    if request.method == "POST":
        word_added = request.POST.get("word")
        data = {"rhyme": word_added}

        input_list = collections.find(data, {"_id": 0})
        user_input_list = list(input_list)
        if user_input_list is not None:
            length = len(user_input_list)
        if length == 1:
            input_words = list(user_input_list[0].values())

            context = {"data": input_words}
        return context
    return context


def home_search(request):
    """Home search function for users"""
    context = add_word(request)
    return render(request, "home.html", context)


# to submit a word of the day and get the list of them----------------------------
class WordOfTheDayApi(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        user_info = WordOfTheDay.objects.all()
        req_data = []
        for i in user_info:
            serializer = WordOfTheDaySerializer(i, many=False)
            req_data.append(serializer.data)
        return Response(req_data)

    def post(self, request):
        context = {
            "date": str(date.today()),
            "Word_of_the_day": request.data["Word_of_the_day"],
        }
        serializer = WordOfTheDaySerializer(data=context)
        if serializer.is_valid():
            if check_duplicate_date():
                serializer.save()
                return Response(serializer.data)
        return Response({"Status": "Fail"})


# To input rhyming words , save them and to display them.----------------------------------------------
class HomeInputApi(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        user_info = Rhymes.objects.filter(user=self.request.user.username)
        req_data = []
        for i in user_info:
            serializer = RhymeSerializer(i, many=False)
            req_data.append(serializer.data)

        return Response(req_data)

    def post(self, request):
        try:
            # ----------------------------------------------------------
            col2 = db["home_wordoftheday"]
            wordOfTheDay = ""
            wordOfTheDay_list = list(
                col2.find({"date": str(date.today())}, {
                          "_id": 0, "date": 0, "id": 0})
            )
            wordOfTheDay_1 = wordOfTheDay_list[0]
            for i in wordOfTheDay_1.values():
                wordOfTheDay = i
            # ------------------------------------------------------------

            user_data = {
                "user": request.data["user"],
                "word": request.data["word"],
                "Word_of_the_day": wordOfTheDay,
            }
            serializer = RhymeSerializer(data=user_data)
            if serializer.is_valid():
                if check_duplicates_rhymes(request.data) or check_duplicates_accepted(request.data) is not True:
                    serializer.save()
                    print(serializer.data["word"])
                    return Response({"Status": "OK"})
            return Response({"Status": "Fail"})
        except Exception as e:
            print(e)


# To add more words after search.-------------------------------------------------------------------------
class AddAfterSearch(APIView):
    def post(self, request):
        req_data = {
            "user": request.data['user'],
            "word": request.data['word'],
            "Word_of_the_day": request.data['Word_of_the_day']
        }
        serializer = RhymeSerializer(data=req_data)
        if serializer.is_valid():
            if (check_duplicates_rhymes(request.data) or check_duplicates_accepted(request.data)) is not True:
                serializer.save()
                return Response({"Status": "OK"})
        return Response({"Status": "Fail"})


# To set the value of is_accepted to true or false.---------------------------------------------------------
class AcceptOrRejectApi(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        user_info = Rhymes.objects.all()
        req_data = []
        for i in user_info:
            serializer = RhymeSerializer(i, many=False)
            req_data.append(serializer.data)
        return Response(req_data)

    def post(self, request):
        colR = db["home_rejected"]
        colA = db["home_accepted"]
        try:
            for item in request.data:
                user_obj = Rhymes.objects.get(word=request.data[item]["word"])
                if user_obj is not None:
                    serializer = RhymeSerializer(user_obj, many=False)
                    user_obj.is_accepted = request.data[item]["is_accepted"]
                    user_obj.save()
                    if request.data[item]["is_accepted"] == True:
                        colA.insert_one(serializer.data)
                        collections.delete_one(serializer.data)
                    else:
                        colR.insert_one(serializer.data)
                        collections.delete_one(serializer.data)
            return Response({"Status": "Pass"})
        except Exception as e:
            return Response({"Status": "Fail"})


# To search for rhyming words.-----------------------------------------------------------------------------------
class SearchRhymingWordsApi(APIView):
    def get(self, request):
        logger.info("inside the Sarching API")
        logger.error("inside the Sarching API")
        logger.debug("inside the Sarching API")

        user_info = Accepted.objects.all()
        req_data = []
        for i in user_info:
            serializer = AcceptedSerializer(i, many=False)
            req_data.append(serializer.data)
        return Response(req_data)


# ADDING RHYMING WORDS WITHOUT WORD OF THE DAY---------------------------------------------------------------------
class AddRandomWords(APIView):
    def post(self, request):
        req_data = {
            "ref_id": request.data['ref_id'],
            "user": request.data['user'],
            "word": request.data['word']
        }
        serializer = RhymeSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status": "OK"})
        return Response({"Status": "Fail"})
