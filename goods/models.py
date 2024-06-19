from django.db import models

class MaleClothes(models.Model):
    CATEGORY_CHOICES = [
        ('SHIRT', 'Shirt'),
        ('PANTS', 'Pants'),
        ('JACKET', 'Jacket'),
        ('SUIT', 'Suit'),
        ('TIE', 'Tie'),
        ('OTHER', 'Other'),
    ]

    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES)
    color = models.CharField(max_length=50, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='male_clothes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.size}"
