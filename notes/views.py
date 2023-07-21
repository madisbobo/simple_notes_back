from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Note, Category
from .serializers import NoteSerializer, CategorySerializer

# Create your views here.
# Do it in all 3 common ways to set a good example


# Class based views
class NoteList(APIView):
    def get(self, request):
        queryset = Note.objects.all()
        serializer = NoteSerializer(queryset, many=True) # many=True if you are serializing a collection of objects, as it informs the serializer that the input is not a single object.
        return Response(serializer.data)

    def post(self, request): 
        serializer = NoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NoteDetail(APIView):
    def get(self, request, id):
        note = get_object_or_404(Note, pk=id)
        serializer = NoteSerializer(note)
        return Response(serializer.data)
    
    def put(self, request, id):
        note = get_object_or_404(Note, pk=id)
        serializer = NoteSerializer(note, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        note = get_object_or_404(Note, pk=id)
        note.delete()
        return Response({'message': 'Note successfully deleted!'})
    

class CategoryList(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

# TODO: class based views for adding new notes, viewing individual notes, editing and deleting them
# TODO: Do the same in function based views, with mixins and modelviewsets. Make a summary somewhere.
# TODO: Every user has their own notes, so you need to login to see your notes

# Authentication and Authorization: Implement user authentication and authorization to restrict access to certain views or actions. This will ensure that only authorized users can create, view, update, or delete notes.

# Pagination: If the number of notes grows large, consider implementing pagination to limit the number of notes returned in a single request. This will improve performance and make it easier for users to navigate through a large number of notes.

# Search and Filtering: Add search functionality to allow users to search for specific notes based on keywords or other criteria. Implement filtering options to let users filter notes based on attributes such as date, category, or tags.

# Sorting: Allow users to sort notes based on different parameters such as date, title, or category. This can be useful when dealing with a large number of notes and helps users find the desired information quickly.

# Categories and Tags: Implement a feature to categorize notes and add tags to organize them. This will make it easier for users to find and group related notes.
