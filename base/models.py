from django.db import models


class House(models.Model):

    img = models.ImageField(upload_to='houses/')
    type = models.CharField(max_length=15)
    price = models.FloatField()
    address = models.CharField(max_length=100)
    description = models.TextField()
    room_count = models.IntegerField()
    floor = models.IntegerField()
    floor_count = models.IntegerField()
    area = models.FloatField()
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'houses'
        verbose_name = 'House'
        verbose_name_plural = 'Houses'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
