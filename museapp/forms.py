from django import forms
from django.contrib.auth.models import User
from museapp.models import MusicProject, UserProfile, Comment



class CommentForm(forms.ModelForm):
	text = forms.CharField(max_length=500,help_text="Comment")
	
	date = forms.DateTimeField()
	audio = forms.FileField()

	class Meta:
		model=Comment
		fields = ('text','audio')

class ProjectForm(forms.ModelForm):
	MusicFile = forms.FileField(help_text="Please input the file to upload.")
	tab = forms.FileField(help_text="Please input the file to upload.",required=False)
	LyricAndChord = forms.FileField(help_text="Please input the file to upload.",required=False)
	ClassicalNotation = forms.FileField(help_text="Please input the file to upload.",required=False)
	PageDescription = forms.CharField(max_length=500,help_text="Please enter the description for the project")
	#date = forms.DateTimeField.auto_now_add(widget=forms.Hiddentinput())
	genre = forms.CharField(max_length=128,help_text="Please input the genre.")
	name = forms.CharField(max_length=128, help_text="Please input naem of the project.")

	class Meta:
		model = MusicProject
		fields =('MusicFile','tab','PageDescription','LyricAndChord','ClassicalNotation','PageDescription','genre','name')

class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=128,help_text="Please enter your username.")
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput(),help_text="Please enter a password.")
	name = forms.CharField(max_length=128,help_text="Please enter your name.")

	class Meta:
		model = User
		fields = ('username','password','email','name')

class UserProfileForm(forms.ModelForm):
	picture = forms.ImageField(help_text="Select a profile picture to upload.",required=False)
	class Meta:
		model = UserProfile
		fields=['website', 'picture']