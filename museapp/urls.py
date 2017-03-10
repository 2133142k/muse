from django.conf.urls import url
from museapp import views

urlpatterns = [url(r'^$', views.homePage, name="home"),
    url(r'^testBase/', views.testBase, name="testBase"),
	url(r'^testAccountPage/', views.testAccountPage, name="testAccountPage"),
               ]
