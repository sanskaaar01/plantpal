from django.core.management.base import BaseCommand
from garden.models import ShopItem

class Command(BaseCommand):
    help = 'Populate shop with initial items'

    def handle(self, *args, **kwargs):
        items = [
            {'name': 'Lavender', 'type': 'Aromatic', 'cost': 50, 'rarity': 'common', 'emoji': '🌿'},
            {'name': 'Cactus', 'type': 'Desert', 'cost': 45, 'rarity': 'common', 'emoji': '🌵'},
            {'name': 'Sunflower', 'type': 'Flowering', 'cost': 60, 'rarity': 'common', 'emoji': '🌻'},
            {'name': 'Rose', 'type': 'Flowering', 'cost': 75, 'rarity': 'uncommon', 'emoji': '🌹'},
            {'name': 'Orchid', 'type': 'Exotic', 'cost': 85, 'rarity': 'uncommon', 'emoji': '🌸'},
            {'name': 'Bamboo', 'type': 'Exotic', 'cost': 95, 'rarity': 'uncommon', 'emoji': '🎋'},
            {'name': 'Bonsai', 'type': 'Miniature', 'cost': 120, 'rarity': 'rare', 'emoji': '🎋'},
            {'name': 'Venus Flytrap', 'type': 'Carnivorous', 'cost': 200, 'rarity': 'legendary', 'emoji': '🪴'},
            {'name': 'Moonflower', 'type': 'Mystical', 'cost': 300, 'rarity': 'mythic', 'emoji': '🌙', 'is_special': True},
        ]
        
        for item_data in items:
            ShopItem.objects.get_or_create(
                name=item_data['name'],
                defaults=item_data
            )
        
        self.stdout.write(self.style.SUCCESS('✅ Successfully populated shop with items!'))