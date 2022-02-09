from urllib.parse import urlparse
from django.urls import path
from rest_framework import routers
from .views import *
from . import views
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register('files', FilesViewSet)


urlpatterns = router.urls


# urlpatterns = [
#    url(r'^', include(router.urls)),
#    path('upload/', FilesViewSet.upload, name="upload")
# ]
