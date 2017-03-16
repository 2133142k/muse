from django.shortcuts import render
from django.http import HttpResponse
from mus.models import MusicProject, Comment, UserProfile
from mus.forms import CoomentForm, MusicProjectForm, UserForm, UserProfileForm, UploadFileForm

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

def musicProject(request,musicproject_name_url,user_name_url):

    context = RequestContext(request)
    project_name = decode_url(musicproject_name_url)
    user_name = decode_url(user_name_url)

    context_dict={'project_name':project_name,'user_name':user_name,'musicproject_name_url':musicproject_name_url}
    try:
        musicProject = MusicProject.objects.get(name=project_name)
        user = User.objects.get(user=user_name)
        comments = Comment.objects.filter(project=musicProject)
        context_dict['comments'] = comments
        context_dict['musicProject'] = musicProject
        context_dict['user'] = user
        if request.method=='POST':
            comment_form = CoomentForm(request.POST)
            if comment_form.is_valid():
                comment_form.save()
                return HttpResponse('projects/user/musicProject.html')
    except MusicProject.DoesNotExist:
        context_dict['comments'] = none
        context_dict['musicProject'] = none
        context_dict['user']=none
    return render(request, 'projects/user/musicProject.html', context_dict)

def createProject(request, user_name_url):
    context = RequestContext(request)

    if request.method=='POST':
        project_form = MusicProjectForm(request.POST,request.FILES)
        if project_form.is_valid():
            project_form.save(commit=True)

            return HttpResponse('/login/myaccount.html')
        else:
            print project_form.errors
    else:
        form = MusicProjectForm()
    return render_to_response('projects/newproject.html',context)

def login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponse('/muse/home.html')
        else:
            print("Invalid username or password")
            return render_to_response('muse/login.html',context_dict,context)

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



