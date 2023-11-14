from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import PeopleSerializer
from .models import People


class PeopleAPIView(APIView):
    def get(self, request):
        w = People.objects.all()
        return Response({'posts': PeopleSerializer(w, many=True).data})

    def post(self, request):
        serializer = PeopleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = People.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            cat_id=request.data["cat_id"]
        )

        return Response({'post': PeopleSerializer(post_new).data})


# class PeopleAPIView(generics.ListAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer
