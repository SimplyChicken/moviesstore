from django.db import models

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=100, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_display_name(self):
        return self.name if self.name else 'Anonymous'

    def __str__(self):
        return f"{self.get_display_name()}: {self.comment[:30]}"
