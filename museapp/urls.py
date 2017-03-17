from django.conf.urls import url
from museapp import views

urlpatterns = [url(r'^$', views.homePage, name="home"),
    url(r'^testBase/', views.testBase, name="testBase"),
    url(r'^about/$',views.about),
    url(r'^login/myaccount/$',views.myAccount),
    url(r'^projects/?P<username>[\w\-]+/musicProject/$',views.musicProject),
    url(r'^projects/?P<username>[\w\-]+/?P<project_name>[\w\-]+/?P<comment_id>[\w\-]+/$',views.deleteComment),
    url(r'^projects/newproject/$',views.createProject)

               ]
