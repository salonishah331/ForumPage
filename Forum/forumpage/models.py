from django.db import models
# from .settings import DBNAME




# connect(DBNAME)

class Post(models.Model):
    text = models.TextField(blank= True, null = False)

    def __str__(self):
        return self.text




