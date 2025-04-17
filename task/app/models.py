from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class QueryLog(models.Model):
    query=models.TextField()
    tone=models.CharField(max_length=1000)
    intent=models.CharField(max_length=1000)
    actions = models.JSONField()
    timestamp=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"({self.tone}, {self.intent})"

