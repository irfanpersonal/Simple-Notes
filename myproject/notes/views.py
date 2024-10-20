from django.shortcuts import render, redirect
from .models import Note
# To make a specifc view protected (only accessible upon
# authentication) we can use the "login_required" method.
from django.contrib.auth.decorators import login_required
# To use our Custom Django Form
from .forms import NoteForm
# To perform file deletion
import os

# Create your views here.
@login_required(login_url = 'users:login')
def notes_list(request):
    # Fetch All the Notes
    notes = Note.objects.filter(
        user = request.user
    ).order_by('-createdAt')
    # We will use the third argument to pass in any values 
    # we want to the template.
    return render(request, 'notes/notes_list.html', {
        'notes': notes
    })

# We are getting the "note_slug" as a Route Parameter.
def note_page(request, note_slug):
    # Find the Note associated with the "note_slug"
    # and pass it into the Template.
    note = Note.objects.get(slug = note_slug)
    return render(request, 'notes/note_page.html', {
        'note': note
    })

# We will invoke the decorator here to ensure only 
# authenticated users are allowed access to this route
# Something super cool about the "login_required" 
# decorator is that you can also provide logic for
# where it should navigate to if its NOT authenticated
# by using teh keyword argument "login_url".
@login_required(login_url = '/users/login/')
def note_new(request):
    if request.method == 'POST':
        # File uploads are not in "request.POST" they
        # are instead in "request.FILES". 
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            # To save it to our database we first want 
            # to get the values of this form input. But
            # we want to set it to "commit" "False". So
            # it doesn't actually add it to the database
            # because youll get an error as no value is 
            # set for "user". 
            new_note = form.save(commit = False)
            # Set a value for "user" on the "note"
            # request.user is equal to the user value
            new_note.user = request.user
            # Now you can actually create it on the 
            # database without error.
            new_note.save()
            return redirect('notes:list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_new.html', {
        'form': form
    })

@login_required(login_url = 'auth')
def edit_note(request, note_slug):
    if request.method == 'POST':
        # Get access to the note so we can provide the 
        # already existing values inputted in the form
        note = Note.objects.get(slug = note_slug)
        note_background = note.background
        form = NoteForm(request.POST, request.FILES, instance = note)
        # Check if the form was submitted without error
        if form.is_valid():
            # If the current image is not set to the fallback
            # image and a new image is provided then delete
            currentImage = f"media/{note_background}"
            if note_background != 'fallback.png' and request.FILES.get('background'):
                os.remove(currentImage)
            # Update the "note" on the database side
            form.save()
            return redirect('notes:list')
    else:
        note = Note.objects.get(
            slug = note_slug,
            user = request.user
        )
        # To set a initial value (aka default value)
        # you can use the "initial" keyword argument and
        # set it to a dictionary with key/value pairs
        # indicating the different columns and their
        # values. Or if you wan't it to set all the 
        # default values of all the columns just pass
        # in the "note" to the "instance" keyword 
        # argument.
        form = NoteForm(
            instance = note
        )
    return render(request, 'notes/note_edit.html', {
        'form': form,
        'note_slug': note.slug
    })

@login_required(login_url = 'auth')
def delete_note(request):
    if request.method == 'POST':
        # Delete Note
        # Whenever you make a POST request using html 
        # "forms", you only have two options. It can
        # either be a "GET" or "POST" method. And on
        # the "views" side of it you can access a 
        # dictionary in "request.POST" to get the
        # different form values. For example if your
        # "form" has an "input" field with the "name"
        # set to "note_id", you can access it like 
        # this.
        note_id = request.POST.get('note_id')
        # Find the note with the id provided and 
        # also make sure its created by the user 
        # logged in. This way you can't delete a
        # note that is not yours.
        note = Note.objects.filter(
            id = note_id,
            user = request.user
        )
        # Remove Image
        note_background = note[0].background
        path = f"media/{note_background}"
        if note_background != 'fallback.png' and os.path.exists(path):
            os.remove(path)
        # Perform the actual deletion
        note.delete()
        return redirect('notes:list')