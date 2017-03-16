from django import forms
from django.contrib.auth.models import User
from mus.models import MusicProject, UserProfile, Comment



class CommentForm(forms.modelForm):
	text = models.CharField(widget=forms.Textarea,help_text="Comment")
	date = models.DateTimeField(auto_now_add=true,blank=true)
	audio = models.FileField()

	class Meta:
		model=Comment
		fields = ('text','audio')

class ProjectForm(forms.modelForm):
	MusicFile = models.FileField(help_text="Please input the file to upload.")
	tab = models.FileField(help_text="Please input the file to upload.",required=False)
	LyricAndChord = models.FileField(help_text="Please input the file to upload.",required=False)
	ClassicalNotation = models.FileField(help_text="Please input the file to upload.",required=False)
	PageDescription = models.CharField(max_length=500,help_text="Please enter the description for the project")
	date = models.DateTimeField(auto_now_add=true,blank=true)
	genre = models.CharField(max_length=128,help_text="Please input the genre.")
	name = models.CharField(max_length=128, help_text="Please input naem of the project.",unique=True)

	class Meta:
		model = Project
		fields =('MusicFile','tab','PageDescription','LyrinAndChoed','ClassicalNotation','PageDescription','genre','name')

class UserForm(forms.modelForm):
	username = forms.Charfield(max_length=128,help_text="Please enter your username.")
	email = forms.EmaiField()
	password = forms.CharField(widget=forms.passwordInput(),help_text="Please enter a password.")
	name = forms.CharField(max_length=128,help_text="Please enter your name.")

	class Meta:
		model = User
		fields = ('username','password','email','name')

class UserProfileForm(forms.ModelForm):
	picture = forms.ImageField(help_text-"Select a profile picture to upload.",required=False)
	class Meta:
		model = UserProfile
		field=['picture']