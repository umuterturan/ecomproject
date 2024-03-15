from django.contrib import admin
from .models import Category,Product
from django.utils.html import format_html

admin.site.site_header = 'Admin Panel'

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  
    
class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'price', 'category', 'is_sale', 'sale_price', 'discount_percentage')
    list_filter = ('category', 'is_sale')
    search_fields = ('name', 'category__name')

    fieldsets = (
        ('General Information', {
            'fields': ('name', 'description', 'category')
        }),
        ('Pricing Information', {
            'fields': ('price', 'is_sale', 'sale_price')
        }),
        ('Image Information', {
            'fields': ('image',)
        }),
    )

    def discount_percentage(self, obj):
        if obj.is_sale and obj.price and obj.sale_price:
            discount = ((obj.price - obj.sale_price) / obj.price) * 100
            return f'{discount:.2f}%'
        return 'N/A'

    discount_percentage.short_description = 'Discount Percentage'

    def save_model(self, request, obj, form, change):
        obj.save()

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product, ProductAdmin)