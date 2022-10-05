from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        for show in Show.objects.all():
            if show.title == postData['title']:
                errors["title"] = "A show's title should be Unique"
        if len(postData['title']) < 2:
            errors["name"] = "A show's title should be at least two characters"
        if len(postData['network']) < 3:
            errors["network"] = "A show's network should be at least three characters"
        if postData['description'] :
            if len(postData['description']) < 10:
                errors["description"] = "A show's description should be at least ten characters"
        if datetime.strptime(postData['release_date'], '%Y-%m-%d') >= datetime.today():
            errors["release_date"] = "A show's release date should be in the past"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

