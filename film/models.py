from django.db import models

class Films(models.Model):
    title = models.CharField(max_length=200)
    caption = models.TextField()
    poster = models.ImageField(upload_to='poster_films/', null=True, blank=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    release_year = models.IntegerField()
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, related_name='genre')

    class Meta:
        db_table = 'Films'

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Genre'

    def __str__(self):
        return self.name

class FeedBack(models.Model):
    name = models.CharField(max_length=120)
    message = models.TextField()

    class Meta:
        db_table = 'FeedBack'

    def __str__(self):
        return self.name
