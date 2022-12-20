from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import postDetailsSerializer
# Create your views here.
from .models import postDetails
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
class addPost(APIView):
    def post(self,request):
        serializer = postDetailsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)
class viewPost(APIView):
    def get(self,request):
        profileName = request.query_params["profileName"]
        listOfPosts = list(postDetails.objects.filter(profileName = profileName).values())
        qs = postDetails.objects.all()
        return JsonResponse(listOfPosts,safe = False)


class viewAll(APIView):
    def get(self,request):
        # profileName = request.query_params["profileName"]
        # listOfPosts = list(postDetails.objects.filter(profileName = profileName).values())
        qs = postDetails.objects.all()
        return JsonResponse(list(qs.values()),safe = False)

class viewPostById(APIView):
    def get(self,request):
        postId = request.query_params["id"]
        return JsonResponse(list(postDetails.objects.filter(id=postId).values()),safe = False)