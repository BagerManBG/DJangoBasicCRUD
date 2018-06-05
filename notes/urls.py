from django.urls import path
from .views import list_notes, create_note, update_note, delete_note

urlpatterns = [
	path('', list_notes, name='list_notes'),
	path('new', create_note, name='create_note'),
	path('update/<int:id>', update_note, name='update_note'),
	path('delete/<int:id>', delete_note, name='delete_note'),
]