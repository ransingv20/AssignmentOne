from django.shortcuts import render, HttpResponse
from .models import *
from django.views import View
# Create your views here.
class Index(View):
    def get(self, request):
        all_products = None
        all_categories = Category.get_all_categories()
        category_id = request.GET.get('category')
        if category_id:
            all_products = Products.get_product_by_id(category_id)
        else:
            all_products = Products.get_all_products()
        data = {}
        data['products'] = all_products
        data['categories'] = all_categories
        print(data)
        return render(request, "home.html", data)
    
    def post(self, request):
        """To add product details into database """
        return render(request, 'addproduct.html')

    

def addCategory(request):
    if request.method == "GET":
        obj = Category.objects.all()[0]
        # print(obj.subcategory_set.all())    #<QuerySet [<SubCategory: Womens Fashion>, <SubCategory: Mens Fashion>]>
        return render(request, 'addCategory.html')
    
    elif request.method == "POST":
        name = request.POST.get("category")
        all_categories = Category.objects.all()
        for i in all_categories:
            if str(name) == str(i):
                return HttpResponse("Already exists")
            else:
                Category.objects.create(name=name)
        print(name)
        return HttpResponse("Success")    
    