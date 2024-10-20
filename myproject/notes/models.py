from django.db import models
from django.utils.text import slugify
# Load in User Model for Assocation
from django.contrib.auth.models import User

# A Django Model is basically you defining the details of 
# a table.
class Note(models.Model):
    # Every Django Model needs atleast ONE field (column)
    # Notice how I didn't define any id column, Django does that for us
    # by default if we don't do it ourselves. Super awesome.
    title = models.CharField(
        # Anytime you use the "models.CharField" you must 
        # define a value for the keyword argument of 
        # "max_length"
        max_length = 255,
        null = False
    )
    body = models.TextField(
        # The reason we are using a "models.TextField" is
        # because it does not require the input of a 
        # "max_length". So its perfect for large amounts
        # of text input.
        null = False
    )
    slug = models.SlugField(
        # This will be used to create a slug or formatted
        # string of text that identified some row. For example
        # say someone created a note with the title "United States"
        # You wouldn't want the user to navigate to "notes/UnitedStates"
        # That looks clunky and not user friendly. Instead you
        # can use a slug which will format it for better viewing
        # by stuff like lowerccase letters, underscores, and hyphens.
        # And you may think you can just use a regular "CharField" for
        # this but this "SlugField" is specifically meant to make the
        # entire process of making the slug super easy.
        
        # By setting "null" to true we have made it so that on the 
        # database level you can set the value for this column to
        # NULL. 
        null = True,

        # By setting "blank" to "True" we have made it so that when
        # inputting a value for this in forms your allowed to not
        # pass a value in for this. 
        blank = True
    )
    background = models.ImageField(
        # This will be used to collect input for an image

        # The "default" keyword argument is used to set a value upon
        # no value. So if the user doesn't wan't to provide it we can
        # set some fallback image.
        default = 'fallback.png',

        # By setting "blank" to "True" we have made it so that when
        # inputting a value for this in forms your allowed to not
        # pass a value in for this. 
        blank = True
    )
    createdAt = models.DateTimeField(
        # The "DateTimeField" has a very useful keyword
        # argument called "auto_now_add" which makes it
        # so that anytime a row is added to this table
        # it will automatically set the time it was created
        auto_now_add = True
    )
    updatedAt = models.DateTimeField(
        # The "auto_now" keyword argument will update the 
        # value of an instance everytime the "save()" method
        # is used on it. Perfect for a column like "updatedAt"
        auto_now = True
    )

    # Associations

    # Before we can start defining our association we first
    # need to load in the built in "User" model. 

    # Now lets define our relationship
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    # Here we are defining a Foreign Key on this column
    # and saying that if the "User" its referencing is
    # deleted, "CASCADE". So delete the entry that is 
    # referencing that "User". Notice how I didn't name
    # it "user_id", this is because behind the scenes Django
    # will automatically add "_id" at the end. So it will be
    # internally saved as "user_id".

    def save(self, *args, **kwargs):
        # Generate slug only if it's not provided
        if not self.slug: 
            # Create slug based off the title value, of course
            # you can set this to whatever but the convention is 
            # to use something like "title" or "name".
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # To create a human readable representation of an instance
    # of a "Note" you can define a method called "__str__".
    
    def __str__(self):
        return self.title

    # By default Django will create the table name itself,
    # but if you want to do that yourself simply create a
    # class within this class called "Meta" and add a key
    # of "db_table" with the value you would like the table
    # to be. So something like this.

    class Meta:
        db_table = "notes"

# Django will automatically create a table in your database 
# with the following format

# <app_name>_<model_name>

# So in our case it would be : notes_note

# And say your model name is something like "NoteCool", the 
# table name would then be : notes_note_cool