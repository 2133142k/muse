from django.shortcuts import render
from django.http import HttpResponse
from mus.models import MusicProject, Comment, UserProfile
from mus.forms import CoomentForm, MusicProjectForm, UserForm, UserProfileForm

def about(request):
    return HttpResponse("This webapp is ment for musicians to share their work and to get from other user on how to improve.")

def home(request):
    project_list = MusicProject.objects()
    context_dict = {'projects': project_list}
    return render(request,'home.html',context=context_dict)

def myAccount(request):
    project_list = MusicProject.objects.get(user_iexact=request.user.username)
    context_dict = {'projects':project_list}
    return render(request,'login/myaccount.html',context=context_dict)

def musicProject(request,musicproject_name_slug,user_name_slug):
    context_dict = {}
    try:
        musicProject = MusicProject.objects.get(slug=musicproject_name_slug)
        user = User.objects.get(slug=user_name_slug)
        comments = Comment.objects.filter(project=musicProject)
        context_dict['comments'] = comments
        context_dict['musicProject'] = musicProject
        context_dict['user'] = user
    except MusicProject.DoesNotExist:
        context_dict['comments'] = none
        context_dict['musicProject'] = none
        context_dict['user']=none
    return render(request, 'projects/user/musicProject.html', context_dict)

def createProject(request):
    context = RequestContext(request.POST)

    if request.method=='POST':
        form = MusicProjectForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return myAccount(request)
        else:
            print form.errors
    else:
        form = MusicProjectForm()
    return render_to_response('projects/newproject.html')

#def login(request):
 #   username = request.POST['username']
  #  password = request.POST['password']
   # user = authenticate(username=username,password=password)
    #if user is not None:
     #   login(request,user)

#    else:
 #       print("Invalid username or password")
  #  return

def register(request):
    registered = False
    if request.method =='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfilerForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user=user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save

            registered=true
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,'/signup.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})



