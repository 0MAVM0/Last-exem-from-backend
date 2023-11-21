from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics

from .serializer import PeopleSerializer
from .permissions import *
from .models import People


class PeopleAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class PeopleAPIList(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PeopleAPIListPagination


class PeopleAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class PeopleAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsAdminOrReadOnly,)
