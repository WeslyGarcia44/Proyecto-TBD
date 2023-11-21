from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=100, unique=True, default='default_subdomain')


    # Otros campos relevantes para tu tenant

    def __str__(self):
        return self.name
