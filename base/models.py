from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='cities/', blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


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
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'houses'
        verbose_name = 'House'
        verbose_name_plural = 'Houses'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
