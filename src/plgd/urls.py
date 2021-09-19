from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from graph import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', views.index, name='homepage'),
    url('predict_graph', views.predict_graph, name='predict_graph'),
    url('find_model', views.find_model, name='find_model'),
    url('models', views.models, name='models'),
    url('about', views.about, name='about'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)