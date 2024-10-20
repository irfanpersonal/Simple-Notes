from django.urls import path
from . import views

# You can create a namespace for your path "name" such
# that its easier to differentiate them as well as 
# duplicate the same name but have different effects.
app_name = "notes"

urlpatterns = [
    path('', views.notes_list, name = 'list'),
    # An excellent use case for needing a Protected Route is when you
    # want to add some data. For example "Creating a Note".
    path('new-note/', views.note_new, name = "new-note"),
    path('delete/', views.delete_note, name = 'delete'),
    path('<slug:note_slug>/edit/', views.edit_note, name = 'edit'),
    # To create a Route Parameter simply specify the Path Converter
    # so what type should the Route Parameter be, you have a couple 
    # options: str, int, slug, uuid, and path. Once you have defined
    # the Path Converter add a colon ":" and then specify the Route
    # Parameter name. In this case we will just name it "note_slug".
    # Now we have to add the "note_slug" as an argument of the
    # view function we are referencing.
    path('<slug:note_slug>', views.note_page, name = 'page'),
]

# Because we created the "namespace" by creating a variable
# called "app_name" we can now reference it by doing the 
# following in our Template "anchor" tags.

# <a href="{% url 'notes:list' %}">Notes Page</a>
# <a href="{% url 'notes:page' %}">{{ note.title }}</a>