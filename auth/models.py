from django.db import models
from django.contrib.auth.models import User


class AgentPhoneNumbers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(
        max_length=15, blank=True, null=True, default=None
    )

    class Meta:
        db_table = 'agent_phone_numbers'
        verbose_name = 'Agent Phone Number'
        verbose_name_plural = 'Agent Phone Numbers'

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class AgentImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='agents/')

    class Meta:
        db_table = 'agent_images'
        verbose_name = 'Agent Image'
        verbose_name_plural = 'Agent Images'

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
