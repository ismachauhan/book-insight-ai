from django.db import models

from django.db import models

class BookData(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    rating = models.FloatField(null=True, blank=True)
    source_url = models.URLField()

  
    ai_summary = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)

   
    uploaded_at = models.DateTimeField(auto_now_add=True)

    recommendation = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title