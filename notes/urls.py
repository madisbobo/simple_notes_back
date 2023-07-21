from django.urls import path
from .views import NoteList, NoteDetail, CategoryList

urlpatterns = [
    path('notes/', NoteList.as_view()), # as_view() converts it into a regular function_based view
    path('notes/<int:id>', NoteDetail.as_view()),
    path('categories/', CategoryList.as_view())
]