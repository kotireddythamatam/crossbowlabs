from django.urls import path
from . import views

urlpatterns = [
path('signup',views.Student_signup_view),
path('login',views.Student_login_view),
path('update<int:id>',views.update),
path('delete<int:id>',views.delete),
path('display',views.display),
]
