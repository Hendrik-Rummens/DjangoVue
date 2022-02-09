from django.http import JsonResponse
from .models import File
from rest_framework.viewsets import ModelViewSet
from .serializers import FileSerializer
# Create your views here.


class FilesViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer


def upload(request):
    return None