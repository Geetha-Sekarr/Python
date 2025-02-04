from django.db import models

class Question(models.Model):
    name=models.CharField(max_length=250)
    contact=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    class meta:
        db_table="data"
