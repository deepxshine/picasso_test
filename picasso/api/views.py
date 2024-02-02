from pathlib import Path

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FileSerializer
from .tasks import handling


filetypes = {
    '.png': 'Image',
    '.jpeg': 'Image',
    '.doc': "Document",
    '.pdf': "Document",
    '.docx': "Document",
    '.txt': 'Text',
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.mp4': 'Video',
    '.mov': 'Video',
    '.py': 'Python',
    '.html': 'HTML',
}


class FileAPIView(APIView):
    def post(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            pk = serializer.data['id']
            handling.apply_async(args=[pk])

            file = serializer.data['file']
            file_type = filetypes.get(Path(file).suffix)

            data = {'file_type': file_type, **serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
