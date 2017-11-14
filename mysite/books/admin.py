from django.contrib import admin
from .models import Publisher,Author,Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email') #Set Columns
    search_fields = ('first_name','last_name') #create search fields
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date',) #Set columns
    list_filter = ('publication_date',) #Create a filter on the right
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    #fields = ('title','authors','publisher','publication_date') #field order to display when editing the model
    filter_horizontal = ('authors',) #Helps with the selection of multiple many-to-many fields 
    raw_id_fields = ('publisher',) #Changes a foreignKey field to a text box instead of select


# Register your models here.
admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
