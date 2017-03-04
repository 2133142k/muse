from django.conf.urls import url
from museapp import views

urlpatterns = [url(r'^testBase/', views.testBase, name="testBase"),]
