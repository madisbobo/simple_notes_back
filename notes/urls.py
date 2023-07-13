from django.urls import path
from .views import NoteListView

urlpatterns = [
    path('all-notes/', NoteListView.as_view()) # as_view() converts it into a regular function_based view
]