from django.contrib import admin

# By default when you navigate into the "Django Admin" 
# page you will notice that the table you defined is not
# present. This is because you didn't register it here.
# And you can register by using the "register()" method
# located on "admin.site".

# If you want to make the "Django Admin" more descriptive
# in terms of the different rows you can create a class that
# inherits from "admin.ModelAdmin" and set the key "list_display"
# with all the columns you wan't defined. 
class NoteAdmin(admin.ModelAdmin):
    # We can use the key "list_display" to set a list of
    # strings representing the different columns we want
    # defined on our Django Admin
    list_display = ['title', 'createdAt', 'user']
    # Now in our "Django Admin" we will see each row have its
    # "title", "slug", and "createdAt" column value defined
    # for easier viewing

    # We can use the key "ordering" to set a list of
    # strings representing the order we would like our 
    # data to presented in for our "Django Admin" panel. 
    # You can denote "DESCENDING" for a column by simply
    # prepending the string with a "-" and remove it for
    # "ASCENDING" order.
    ordering = ['-createdAt']

# Models we want registered
from .models import Note

# Register your models here.
admin.site.register(Note, NoteAdmin)