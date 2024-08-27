from django.db import models

# Create your models here.
class Task(models.Model):
    # The title of the to-do item
    title = models.CharField(max_length=200)
    
    # A boolean field to indicate whether the item is complete
    complete = models.BooleanField(default=False, blank=True,null=True)
    
    
    def __str__(self):
        return self.title