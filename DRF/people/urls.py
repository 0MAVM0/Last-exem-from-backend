from django.urls import path

from .views import *


urlpatterns = [
    path('api/v1/peoplelist/', PeopleAPIList.as_view(), name=""),
    path('api/v1/peoplelist/<int:pk>/', PeopleAPIUpdate.as_view(), name=""),
    path('api/v1/peopledetail/<int:pk>/', PeopleAPIDetailView.as_view(), name=""),
]
