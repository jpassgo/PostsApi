from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'^$', views.home)
router.register(r'^create_post/$', views.create_post)
router.register(r'^delete_post/$', views.delete_post)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
]