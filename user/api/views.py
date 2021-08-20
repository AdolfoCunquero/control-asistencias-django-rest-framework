from rest_framework.generics import ListAPIView
from user.models import User, Rol
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerialier, RolSerializer
from rest_framework.permissions import IsAuthenticated

class RolView(ListAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated]    
     
     

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(status = status.HTTP_400_BAD_REQUEST, data = serializer.errors)

class UserView(APIView):
    permission_classes =[IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


    def put(self, request):
        user = User.objects.get(pk=request.user.id)
        serializer = UserUpdateSerialier(user, request.data) 

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    



        