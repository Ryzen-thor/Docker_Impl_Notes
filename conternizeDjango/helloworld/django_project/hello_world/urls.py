from hello_world import views

from django.urls import path

urlpatterns = [
    path("",views.home_page_view,name="home")
]