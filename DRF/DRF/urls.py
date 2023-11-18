from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from people.views import *

router = routers.SimpleRouter()
router.register(r'people', PeopleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
]
