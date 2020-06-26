from django.urls import path
from .views import NewsPage,Home,Contact,NewsDate,SignUp,AddUser,ModelForm,addModelForm

# first parameter defines the url name and second is the function from the views
#the name paramter is used on url navigation
urlpatterns = [
    path('news/',NewsPage,name ="news"),
    path('',Home,name = "home"),
    path('contact/',Contact , name = "contact"),
    path('newsdate/<int:year>',NewsDate , name = "newsdate"),
    path('signup/',SignUp,name = "register"),
    path('register/',AddUser,name = 'addUser'),
    path('modelform/',ModelForm, name = 'modelform'),
    path('addmodelform/',addModelForm,name = "addmodelform")
]
