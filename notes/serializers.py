from rest_framework.serializers import ModelSerializer
from .models import Note


# Model serializer
class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'description']