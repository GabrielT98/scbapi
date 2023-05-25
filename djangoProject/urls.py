from django.contrib import admin
from django.urls import path

import scbapi.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login',scbapi.views.LoginAPIView.as_view(), name='login'),
    path('api/user/<int:pk>',scbapi.views.LoginAPIView.as_view(), name='user'),
    path('api/user/create', scbapi.views.CreateUserAPIView.as_view(), name='create_user'),
    path('api/user/<int:pk>/barraginha',scbapi.views.BarraginhaAPIView.as_view(),name="user_barraginha"),
]
