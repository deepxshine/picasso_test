from rest_framework.serializers import ModelSerializer

from .models import File


class FileSerializer(ModelSerializer):

    class Meta:
        model = File
        fields = ('file', 'id', 'uploaded_at', 'processed')
        read_only_fileds = ('id', 'uploaded_at', 'processed')