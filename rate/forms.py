from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Profile,Project,Contact,Rating

class Registration(UserCreationForm):
   '''
   User registration form.
   '''
   username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
   email= forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), max_length=64)
   password1= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
   password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))


   class Meta(UserCreationForm.Meta):
      model = User
      fields = UserCreationForm.Meta.fields + ("email","username","password1")


class LoginForm(AuthenticationForm):
   '''
   User login form.
   '''
   
   username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

   class Meta:
      model = User
      fields = ['username','password']

class ProfileUpdateForm(forms.ModelForm):
   '''
   User profile update form.
   '''

   class Meta:
      model = Profile
      fields = ['avatar', 'bio']
      widgets = {
         'bio': forms.TextInput(attrs={'placeholder': 'Enter new bio'})
      }

class ContactUpdateForm(forms.ModelForm):
   '''
   User contact update form.
   '''
   facebook = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Facebook Linkgcm '}))
   twitter = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Twitter Link'}))
   instagram = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Instagram Link'}))
   github = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Github Link'}))
   class Meta:
      model = Contact
      fields = ['facebook','twitter','instagram','github']

class ProjectForm(forms.ModelForm):
   '''
   New project creation form.
   '''

   name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Project Title'}))
   description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description'}))
   link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Project Link'}))
   description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Project Description'}))

   class Meta:
      model = Project
      fields = ['name','img','description','link']


class RatingForm(forms.ModelForm):
   '''
   Ratings form
   '''

   RATINGS = (
      (1,''),
      (2,''),
      (3,''),
      (4,''),
      (5,''),
   )

   design = forms.ChoiceField(choices=RATINGS, widget=forms.RadioSelect())
   usability = forms.ChoiceField(choices=RATINGS, widget=forms.RadioSelect())
   content = forms.ChoiceField(choices=RATINGS, widget=forms.RadioSelect())  
   review = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Give a review'})) 
   class Meta:
      model = Rating
      fields = ['design','usability','content','review']
