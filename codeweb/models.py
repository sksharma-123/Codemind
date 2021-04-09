from django.db import models
import uuid
from datetime import date



class Submission(models.Model):
    username = models.CharField(max_length=40, default="")
    language = models.CharField(max_length=40)
    level = models.CharField(max_length=40, default="")
    problem = models.TextField(max_length=1000)
    solution = models.TextField(max_length=1000)
    date = models.DateField(default=date.today())
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)


    def __str__(self) -> str:
        return self.problem