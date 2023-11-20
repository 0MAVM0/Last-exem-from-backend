from django.contrib import admin
from django.urls import path, include

from people.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/people/", PeopleAPIList.as_view()),
    path("api/people/<int:pk>", PeopleAPIUpdate.as_view()),
    path("api/people_delete/<int:pk>", PeopleAPIDestroy.as_view()),
]
