from django.core.management.base import BaseCommand
from goods.models import MaleClothes

class Command(BaseCommand):
    help = 'Insert mock data into the MaleClothes model'

    def handle(self, *args, **kwargs):
        clothes_data = [
            {
                'name': 'Henley Shirt',
                'category': 'SHIRT',
                'size': 'S',
                'color': 'Gray',
                'price': 21.99,
                'stock': 75,
                'description': 'A comfortable gray henley shirt.',
            },
            {
                'name': 'Sweatpants',
                'category': 'PANTS',
                'size': 'XL',
                'color': 'Black',
                'price': 27.99,
                'stock': 40,
                'description': 'Comfortable black sweatpants.',
            },
            {
                'name': 'Bomber Jacket',
                'category': 'JACKET',
                'size': 'L',
                'color': 'Green',
                'price': 99.99,
                'stock': 20,
                'description': 'A stylish green bomber jacket.',
            },
            {
                'name': 'Linen Shirt',
                'category': 'SHIRT',
                'size': 'M',
                'color': 'White',
                'price': 34.99,
                'stock': 55,
                'description': 'A lightweight white linen shirt.',
            },
            {
                'name': 'Corduroy Pants',
                'category': 'PANTS',
                'size': 'M',
                'color': 'Brown',
                'price': 42.99,
                'stock': 30,
                'description': 'Comfortable brown corduroy pants.',
            },
            {
                'name': 'Peacoat',
                'category': 'JACKET',
                'size': 'L',
                'color': 'Navy',
                'price': 159.99,
                'stock': 12,
                'description': 'A classic navy peacoat.',
            },
        ]

        for item in clothes_data:
            MaleClothes.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Mock data inserted successfully!'))