from django.conf.urls import url
from museapp import views

urlpatterns = [url(r'^$', views.homePage, name="home"),
    url(r'^testBase/$', views.testBase, name="testBase"),
	url(r'^testAccountPage/$', views.testAccountPage, name="testAccountPage"),
               url(r'^testProjectViewPage/$', views.testProjectViewPage, name="testProjectViewPage"),
               url(r'^testProjectViewPage/comments/$', views.jsonComments, name="comments"),
               url(r'^users/(?P<user_id>[\w\-]+)/$', views.userPage, name="userPage"),
                url(r'^users/(?P<user_id>[\w\-]+)/delete/$', views.user_delete, name ="deleteUser"),
                #url(r'^users/(?P<username_slug>[\w\-]+)/changePassword/$', views.changePassword, name ="changePassword"),
               url(r'^new_project/$', views.createProject, name ="newProject"),
               url(r'^projects/$', views.getProjectPreviews, name = "getProjects"),
               url(r'^projects/(?P<project_name_slug>[\w\-]+)/$', views.project, name ="projectPage"),
               url(r'^projects/(?P<project_name_slug>[\w\-]+)/comments/$', views.comments, name ="comments"),
               url(r'^projects/(?P<project_name_slug>[\w\-]+)/newcomment/$',views.newComment, name="newComment"),
               url(r'^projects/(?P<project_name_slug>[\w\-]+)/comments/(?P<comment_id>[\w\-]+)/delete$',views.deleteComment, name="deleteComment"),
               url(r'about/$', views.about, name="about"),
			   url(r'login/$', views.user_login, name="login"),
			   url(r'register/$', views.register, name="register"),
               url(r'logout/$',views.user_logout, name="logout"),
               url(r'change_password/$',views.change_password, name = "changePassword")
               ]
