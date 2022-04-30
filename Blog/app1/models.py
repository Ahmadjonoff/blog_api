from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=50)
    matn = models.TextField()
    rasm = models.URLField()
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sarlavha

class Talks(models.Model):
    sarlavha = models.CharField(max_length=50)
    video = models.URLField()
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sarlavha