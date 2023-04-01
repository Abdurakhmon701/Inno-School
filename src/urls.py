from django.contrib import admin
from django.urls import path

from student.views import NewsViewUzRetrieveAPI, NewsViewRuRetrieveAPI, NewsViewEnRetrieveAPI, ListNewsUzAPI, ListNewsRuAPI, ListNewsEnAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/uz/<int:pk>/', NewsViewUzRetrieveAPI.as_view()),
    path('news/ru/<int:pk>/', NewsViewRuRetrieveAPI.as_view()),
    path('news/en/<int:pk>/', NewsViewEnRetrieveAPI.as_view()),
    path('news/uz/', ListNewsUzAPI.as_view()),
    path('news/ru/', ListNewsRuAPI.as_view()),
    path('news/en/', ListNewsEnAPI.as_view()),
]
