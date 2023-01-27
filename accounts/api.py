from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterApi(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,"message":'Something went wrong'})

        serializer.save()
        print(serializer.data)
        user = User.objects.get(username = serializer.data['username'])
        return Response({'status':200,"payload":serializer.data,'message':'Registeration successfull!!'})


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

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

