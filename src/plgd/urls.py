from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from graph import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', views.index, name='homepage'),
]
