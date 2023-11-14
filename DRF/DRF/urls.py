from django.contrib import admin
from django.urls import path, include

from people.views import PeopleAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/peoplelist/', PeopleAPIView.as_view())
]
