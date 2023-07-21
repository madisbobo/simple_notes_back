from rest_framework.serializers import ModelSerializer
from .models import Note, Category


# Model serializer
class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'description', 'last_updated', 'bg_color', 'category']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


# Try the simple "no-model" serializer again and make a summary somewhere


