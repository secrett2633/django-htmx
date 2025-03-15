from django.db import models
from django.contrib.auth.models import AbstractUser


class ServiceUser(AbstractUser):
    email = models.EmailField()
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, blank=True)
    bio = models.TextField(blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    provider = models.CharField(max_length=255, blank=True)

    @property
    def is_authenticated(self):
        return True

    class Meta:
        app_label = "user"
        db_table = "service_user"
        constraints = [
            models.UniqueConstraint(fields=["email"], name="unique_email"),
        ]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
