from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Note
from django.contrib.auth.models import User
from .forms import NoteForm

def list_notes(request):
	if not request.user.is_authenticated:
		return redirect('login')

	notes = Note.objects.all().filter(uid=request.user.id)
	return render(request, 'notes/notes.html', {'notes': notes})

def create_note(request):
	if not request.user.is_authenticated:
		return redirect('login')

	form = NoteForm(request.POST or None)

	if form.is_valid():
		data = form.save(commit=False)
		data.uid = User.objects.get(pk=request.user.id)
		data.save()
		return redirect('list_notes')

	return render(request, 'notes/notes-form.html', {'form': form})

def update_note(request, id):
	if not request.user.is_authenticated:
		return redirect('login')

	note = Note.objects.get(pk=id)

	if note.uid != request.user:
		return redirect('list_notes')

	form = NoteForm(request.POST or None, instance=note)

	if form.is_valid():
		form.save()
		return redirect('list_notes')

	return render(request, 'notes/notes-form.html', {'form': form, 'note': note})

def delete_note(request, id):
	if not request.user.is_authenticated:
		return redirect('login')

	note = Note.objects.get(id=id)

	if request.method == 'POST':
		note.delete();
		return redirect('list_notes')

	return render(request, 'notes/note-delete-confirm.html', {'note': note})