from django.db import models

# Create your models here.
class employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    designation = models.CharField(max_length=255)

    def __str__(self):
        return self.name
 