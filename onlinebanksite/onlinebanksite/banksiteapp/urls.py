from django.urls import path

from .views import home,register,login_user,logout_user,form_user,new_form,submitlink
urlpatterns = [
    path('', home,name="home"),
    path("register/", register, name="register"),
    path("login_user/", login_user, name="login_user"),
    path("logout_user/", logout_user, name="logout_user"),
    path("new_form/", new_form, name="new_form"),
    path("submitlink/", submitlink, name="submitlink"),

    path("form_user/", form_user, name="form_user"),
]