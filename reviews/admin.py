from django.contrib import admin
from .models import ProductSize, Product, ProductSite, Company, Category, Comment, Image


# For advanced model configuration we must use
#  ModelAdmin Class. The ModelAdmin class is a 
# representation of user-defined models in the 
# admin panel. It can be used to override various
#  actions. First we need to create and register
#  ModelAdmin Class. We can use @admin.register 
# decorator or admin.site.register() method for 
# registiration. We can use @register decorator.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    # Open the products model from the admin panel. There you will see a list of Product objects. It only shows the names of the products.
    # To change the list view, type the following lines of code: 

    list_display = ('pk', 'name', 'content')

    # to filter the data with built in widget
    list_filter = ('category',)

admin.site.register(Category)
admin.site.register(Company)
admin.site.register(ProductSize)
admin.site.register(ProductSite)
admin.site.register(Comment)
admin.site.register(Image)




# to change the title written in the top-left corner of the web-page.

admin.site.site_header = "Product Review Admin"