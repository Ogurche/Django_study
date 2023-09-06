from django.urls import path

from .views import * 

urlpatterns = [
    path('', index_page),
    path('sec/<int:add_arg>/',second_page),
    path('sec/',index_page)
]