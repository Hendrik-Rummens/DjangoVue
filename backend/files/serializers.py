from rest_framework.serializers import ModelSerializer
from .models import File

class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = [
            'id', 
            'name',
            'description',
            'date_added',
            'file_uploaded'
        ]

        