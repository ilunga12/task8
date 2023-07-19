from django.urls import path

from Newapp import views

urlpatterns = [
    path("",views.New,name="New"),
    path("log",views.log,name="log"),
    path("studentregbase",views.studentregbase,name="studentregbase"),
    path("studentreg",views.studentreg,name="studentreg"),

]
