from django.contrib import admin
from django.urls import path, include, re_path

# JTW
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )

from people.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drf-auth/', include('rest_framework.urls')),  
    path("api/people/", PeopleAPIList.as_view()),
    path("api/people/<int:pk>", PeopleAPIUpdate.as_view()),
    path("api/people_delete/<int:pk>", PeopleAPIDestroy.as_view()),

    # Djoser
    path('api/auth', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # JWT
    # path('api/token/create/', TokenObtainPairView.as_view(),
    #                                             name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), 
    #                                             name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), 
    #                                             name='token_verify'),
]
