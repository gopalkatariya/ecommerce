from django.db import models

from category.models import Category

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name