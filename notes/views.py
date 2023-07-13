from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Note
from .serializers import NoteSerializer

# Create your views here.
# Do it in all 3 common ways to set a good example


# Class based views
class NoteListView(APIView):
    def get(self, request):
        queryset = Note.objects.all()
        serializer = NoteSerializer(queryset, many=True) # many=True if you are serializing a collection of objects, as it informs the serializer that the input is not a single object.
        return Response(serializer.data)


