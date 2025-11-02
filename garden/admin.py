from django.contrib import admin
from django.utils.html import format_html
from django.urls import path
from django.template.response import TemplateResponse
from .models import UserProfile, Plant, ActivityHistory, ShopItem

# 🌱 Custom Admin Site with Dashboard
class CustomAdminSite(admin.AdminSite):
    site_header = "🌱 PlantPal Admin"
    site_title = "PlantPal Dashboard"
    index_title = "Welcome to your garden control panel"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view))
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        top_user = UserProfile.objects.order_by('-streak').first()
        total_plants = Plant.objects.count()
        context = dict(
            self.each_context(request),
            top_user=top_user,
            total_plants=total_plants,
        )
        return TemplateResponse(request, "admin/dashboard.html", context)

admin_site = CustomAdminSite(name='custom_admin')

@admin.register(UserProfile, site=admin_site)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'coins', 'streak', 'water_count', 'last_login_date', 'badge')
    list_filter = ('last_login_date',)
    search_fields = ('user__username',)
    readonly_fields = ('last_login_date', 'achievements')
    fieldsets = (
        ('User Info', {
            'fields': ('user', 'last_login_date')
        }),
        ('Progress', {
            'fields': ('coins', 'streak', 'water_count', 'achievements')
        }),
    )

    def badge(self, obj):
        if obj.streak >= 30:
            return "🔥 Streak Master"
        elif obj.water_count >= 100:
            return "💧 Watering Champ"
        elif obj.coins >= 500:
            return "💰 Garden Tycoon"
        return "🌱 New Gardener"
    badge.short_description = "Badge"

    def achievements(self, obj):
        achievements = []
        if obj.streak >= 7:
            achievements.append("7-Day Streak 🌞")
        if obj.water_count >= 50:
            achievements.append("50 Waters 💦")
        if obj.coins >= 1000:
            achievements.append("Coin Collector 🪙")
        return ", ".join(achievements) or "None yet"
    achievements.short_description = "Achievements"

@admin.register(Plant, site=admin_site)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('emoji_name', 'user', 'type', 'colored_rarity', 'health', 'growth', 'planted_date')
    list_filter = ('rarity', 'type', 'planted_date')
    search_fields = ('name', 'user__username')
    readonly_fields = ('planted_date',)

    def emoji_name(self, obj):
        return f"{obj.emoji} {obj.name}"
    emoji_name.short_description = 'Plant'

    def colored_rarity(self, obj):
        color = {
            'common': 'gray',
            'uncommon': 'green',
            'rare': 'blue',
            'legendary': 'gold',
            'mythic': 'purple'
        }.get(obj.rarity, 'black')
        return format_html('<span style="color: {};">{}</span>', color, obj.get_rarity_display())
    colored_rarity.short_description = 'Rarity'

@admin.register(ActivityHistory, site=admin_site)
class ActivityHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'short_details', 'timestamp')
    list_filter = ('action', 'timestamp')
    search_fields = ('user__username', 'action', 'details')
    readonly_fields = ('timestamp',)

    def short_details(self, obj):
        return obj.details[:50] + '...' if len(obj.details) > 50 else obj.details
    short_details.short_description = 'Details'

@admin.register(ShopItem, site=admin_site)
class ShopItemAdmin(admin.ModelAdmin):
    list_display = ('emoji_name', 'type', 'cost', 'rarity', 'is_special', 'is_available')
    list_filter = ('rarity', 'is_special', 'is_available')
    search_fields = ('name',)

    def emoji_name(self, obj):
        return f"{obj.emoji} {obj.name}"
    emoji_name.short_description = 'Item'
