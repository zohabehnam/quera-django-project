from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User


from .serializers import UserSerializer


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(
            data={'message': f'Bye {request.user.username}!'},
            status=status.HTTP_204_NO_CONTENT
        )

class UserRegistration(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        user_serializer = UserSerializer(data= request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(data={'data':user_serializer.data}, status= status.HTTP_200_OK)
        return Response({'message':user_serializer.errors}, status= status.HTTP_400_BAD_REQUEST)
