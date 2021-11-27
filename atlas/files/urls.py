from django.urls import path
from files import views

urlpatterns = [

    path(
        route='',
        view=views.index,
        name='feed'
    ),

]