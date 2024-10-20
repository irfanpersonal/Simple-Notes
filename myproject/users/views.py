from django.shortcuts import render, redirect
# To get access to the built in User Creation Form we
# can then pass onto our Template to provide very easy
# registration setup.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# To add a cookie called 'session_id' which indicates a
# authenticated user. It takes in two arguments the "request" 
# object and "User Object".
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        # This is where we handle when the user submits
        # the UserCreationForm successfully.

        # Here we want to create a form object from the
        # post data provided. So this will return the data
        # they entered into the form
        form = UserCreationForm(request.POST)
        # If the form is valid then we can invoke the "save()"
        # method on it to actually create the User on the 
        # database level.
        if form.is_valid():
            # Then we need to invoke the "login" method and
            # pass in the "request" object and the "form.save()"
            # which is equal to the "User Object".
            login(request, form.save())
            return redirect('notes:list')
    # The return value of invoking a "UserCreationForm"
    # is what you need to pass in to your Django Template.
    # Think of the "UserCreationForm" as you doing 
    # something like this.
    # user = Note(column1 = 'value', column2 = 'value')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {
        'form': form
    })

def login_view(request):
    if request.method == 'POST':
        # We need to pass in the requests POST data to
        # the form to then pass on to our template. This
        # is another built in "Django Form" used to 
        # authenticate/login the user
        form = AuthenticationForm(data = request.POST)
        # If the information was correct we need to add
        # the cookie and redirect.
        if form.is_valid():
            # Then we need to invoke the "login" method and
            # pass in the "request" object and the "form.get_user()"
            # method which is equal to the "User Object".
            login(request, form.get_user())
            # We also want to check if a hidden value by the
            # name "next" exists in the POST data, and if so
            # we can redirect the user back to the page they 
            # were unable to access due to unauthentication.
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("notes:list")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {
        'form': form
    })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('notes:list')