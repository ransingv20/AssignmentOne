from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Category(models.Model):
        name= models.CharField(max_length=50)
    
        @staticmethod
        def get_all_categories():
            return Category.objects.all()
    
        def __str__(self):
            return self.name

class SubCategory(models.Model):
        name = models.TextField(max_length=50)
        child_categories = models.ManyToManyField(Category)

        def __str__(self):
            return self.name
        
        class Meta:
            db_table = "subcategories"

class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category= models.ForeignKey(Category, on_delete=models.CASCADE ,related_name="category")

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name   
    
    
    @staticmethod
    def get_all_products():
        return Products.objects.all()
    
    @staticmethod
    def get_products_by_id_by_list(ids):
        return Products.objects.filter(id__in=ids)

    @staticmethod
    def get_product_by_id(category_id):
        if category_id:
            return Products.objects.filter(category = category_id)
        else:
            return Products.objects.all()
  

