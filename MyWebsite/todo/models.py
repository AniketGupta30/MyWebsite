from django.db import models

# Create your models here.
class todo(models.Model):
    content = models.CharField(max_length=200)
    complete  = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content
