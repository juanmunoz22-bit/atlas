from django.urls import path
from users import views

urlpatterns = [

    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/', 
        view=views.LogoutView.as_view(), 
        name='logout'
        ),

]