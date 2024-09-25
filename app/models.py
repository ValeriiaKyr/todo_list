from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("app:tag-list", kwargs={"pk": self.pk})


class Task(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name='tasks')

    class Meta:
        ordering = ["done", '-created_at']