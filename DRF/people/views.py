from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import generics

from .serializer import PeopleSerializer
from .permissions import *
from .models import People, Category


class PeopleAPIList(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PeopleAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PeopleAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsAdminOrReadOnly,)
