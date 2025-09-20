from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Petition(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    upvotes = models.PositiveIntegerField(default=0)

    @classmethod
    def create_petition(cls, name, description, upvotes=0):
        petition = cls(name=name, description=description, upvotes=upvotes)
        petition.save()
        return petition

class PetitionLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'petition')
