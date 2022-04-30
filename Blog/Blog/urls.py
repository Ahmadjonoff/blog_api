from django.contrib import admin
from django.urls import path, include
from app1.views import MaqolaViewSet, TalksViewSet
from rest_framework.routers import DefaultRouter

r = DefaultRouter()
r.register('maqola', MaqolaViewSet)
r.register('talks', TalksViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(r.urls)),
]
