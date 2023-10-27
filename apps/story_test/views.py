from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Story, User
from .serializers import StorySerializer, UserRegistrationSerializer
from django.http import HttpResponse


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class StoryViewSet(ReadOnlyModelViewSet):

    serializer_class = StorySerializer

    def get_queryset(self):
        return Story.objects.all()


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            nickname = serializer.validated_data['nickname']
            password = serializer.validated_data['password']
            email = serializer.validated_data['email']
            user = User.objects.create_user(username=nickname, password=password, email=email)
            return Response({'message': 'Inscription réussie'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



