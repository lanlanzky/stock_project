from django.contrib import admin
from stock.models import New_stock,Author
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'date','high','low','open','close','volume','adjclose')
    search_fields = ('name','date','high', )
    list_filter = ('name','date',)
admin.site.register(New_stock, StockAdmin)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', )
admin.site.register(Author, AuthorAdmin)
'''
class Stock_Admin(admin.ModelAdmin):
    list_display = ('name', 'date', 'open')
    search_fields = ('name')
admin.site.register(New_stock, Stock_Admin)

# Register your models here.
'''
