from django.db import models
from django.contrib.auth.models import User

class NoteType(models.Model):
	note_type = models.CharField(max_length=255)

	def __str__(self):
		return self.note_type

class Note(models.Model):
	note = models.TextField()
	note_type = models.ForeignKey('NoteType', on_delete=models.CASCADE)
	uid = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.note[:50]