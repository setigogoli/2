from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=20, unique=True,validators=[Minlenght(5), MaxLengthValidator(20),RegexValidator(r'^[a-zA-Z0-9_]+$')])

