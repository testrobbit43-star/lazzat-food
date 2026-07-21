from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Extended User model with role-based access control.
    """
    class Role(models.TextChoices):
        CLIENT = "CLIENT", "Mijoz (Customer)"
        OWNER = "OWNER", "Restoran Egasi (Restaurant Owner)"
        ADMIN = "ADMIN", "Admin"
    
    role = models.CharField(
        max_length=15,
        choices=Role.choices,
        default=Role.CLIENT,
        help_text="Foydalanuvchining roli"
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True,
        help_text="Telefon raqami +998XXXXXXXXX formatida"
    )
    is_phone_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'core_user'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['phone_number']),
            models.Index(fields=['role']),
            models.Index(fields=['email']),
        ]
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_role_display()})"

    @property
    def is_owner(self):
        return self.role == self.Role.OWNER

    @property
    def is_client(self):
        return self.role == self.Role.CLIENT
