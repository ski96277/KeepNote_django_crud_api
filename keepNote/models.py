from django.db import models

class NoteModel(models.Model):
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=5000)
    