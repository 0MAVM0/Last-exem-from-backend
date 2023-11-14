from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import PeopleSerializer
from .models import People


class PeopleAPIView(APIView):
    def get(self, request):
        lst = People.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = People.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            cat_id=request.data["cat_id"]
        )

        return Response({'post': model_to_dict(post_new)})


# class PeopleAPIView(generics.ListAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer
