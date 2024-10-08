from django.db import models


class Movie(models.Model):
    Poster_Link = models.URLField(max_length=200)
    Series_Title = models.CharField(max_length=70)
    Released_Year = models.IntegerField(default=0)
    Certificate = models.CharField(max_length=10)
    Runtime = models.CharField(max_length=10)
    Genre = models.CharField(max_length=40)
    IMDB_Rating = models.FloatField()
    Overview = models.TextField()
    Meta_score = models.IntegerField(null=True, blank=True, default=0)
    Director = models.CharField(max_length=40)
    Stars = models.CharField(max_length=100)
    
    # class Meta:
    #     ordering = ['IMDB_Rating']  # مرتب‌سازی صعودی بر اساس نمره

    def __str__(self):
        return f"{self.Series_Title} ({self.Released_Year})"
