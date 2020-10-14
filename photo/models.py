from django.db import models
# Create your models here.
class Photo(models.Model):

    photoName = models.CharField(max_length=128)
    userId = models.IntegerField(default=-1)
    photoDate = models.DateTimeField(auto_now_add=True)
    photoUrl = models.CharField(max_length=128)
    photoResult = models.FloatField()
    photoInfo = models.CharField(max_length=128)

    class Meta:
        db_table = "photo"

    def __str__(self):
        return self.photoName