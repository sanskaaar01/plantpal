from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    coins = models.IntegerField(default=50)
    streak = models.IntegerField(default=1)
    water_count = models.IntegerField(default=0)
    last_login_date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

class Plant(models.Model):
    RARITY_CHOICES = [
        ('common', 'Common'),
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('legendary', 'Legendary'),
        ('mythic', 'Mythic'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plants')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    emoji = models.CharField(max_length=10, default='🌱')
    bio = models.TextField(blank=True, null=True)
    health = models.FloatField(default=100)
    growth = models.IntegerField(default=10)
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES, default='common')
    planted_date = models.DateTimeField(default=timezone.now)
    last_watered = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.emoji} {self.name}"
    
    class Meta:
        ordering = ['-planted_date']
        verbose_name = "Plant"
        verbose_name_plural = "Plants"

class ActivityHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    action = models.CharField(max_length=100)
    details = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username} - {self.action}"
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Activity"
        verbose_name_plural = "Activity History"

class ShopItem(models.Model):
    RARITY_CHOICES = [
        ('common', 'Common'),
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('legendary', 'Legendary'),
        ('mythic', 'Mythic'),
    ]
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    cost = models.IntegerField()
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES)
    emoji = models.CharField(max_length=10, default='🌱')
    is_special = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.emoji} {self.name} - {self.cost} coins"
    
    class Meta:
        verbose_name = "Shop Item"
        verbose_name_plural = "Shop Items"