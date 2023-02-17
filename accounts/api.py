from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import Group
from .helpers import *
from rest_framework import status
import pymongo
from rest_framework import status

client = pymongo.MongoClient("localhost", 27017)
db = client["NanditaDb"]
col1 = db["auth_user"]


class RegisterApi(APIView):
    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            # if not serializer.is_valid():
            #     print(serializer.errors)
            #     return Response({"status": 403, "message": "Something went wrong"},status=status.HTTP_403_FORBIDDEN)
            if serializer.is_valid():
                user_info = col1.find()
                values = list(user_info)
                flag = False
                for i in values:
                    if request.data["email"] == i["email"]:
                        flag = True

                if flag == True:
                    return Response(
                        {"Status": "Fail", "Message": "Email already used"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )
                else:
                    serializer.save()
                    user = User.objects.get(username=serializer.data["username"])
                    group = Group.objects.get(name="Users")
                    user.groups.add(group)
                    return Response(
                        {
                            "status": "Pass",
                            "payload": serializer.data,
                            "message": "Registration successful!!",
                        },
                        status=status.HTTP_200_OK,
                    )
            else:
                print(serializer.errors)
                return Response(
                    {"status": 403, "message": "Something went wrong"},
                    status=status.HTTP_403_FORBIDDEN,
                )
        except Exception as e:
            content = {
                "text": "Username already exists!",
                "error": str(e),
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserApi(APIView):
    def get(self, request):
        user_info = User.objects.all()
        req_data = []
        for i in user_info:
            serializer = UserSerializer(i, many=False)
            req_data.append(serializer.data["is_staff"])
        print(req_data)
        return Response(req_data)

    # def get(self, request):
    #     user_info = User.objects.all()
    #     req_data = []
    #     for i in user_info:
    #         serializer = MyTokenObtainPairSerializer(i, many=False)
    #         req_data.append(serializer.data)
    #         print(req_data)
    #         return Response(req_data)


# class LoginApi(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def post(self,request):
#         serializer = UserSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response({'status':403,'message':'something went wrong'})
#         print(list(serializer.data))
#         username = User.objects.get(username = serializer.data['username'])
#         password = User.objects.get(password = serializer.data['password'])

#         user = serializer.validated_data(username=username , password=password)
#         login(request,user)
#         return Response({'status':200,"payload":serializer.data,"message":"login successful!!"})
