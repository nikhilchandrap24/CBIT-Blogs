from django.contrib import admin
from django.urls import path, include
from CbitBlogs.settings import TEMPLATES
from blogs import views
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home,name='Home'),
    path('aboutus', views.aboutus,name='aboutus'),
    path('login/', views.login,name='login'),
    path('explore/',views.explore,name='explore'),
    path('register/',views.register,name='register'),
    path('registration-successful',views.success,name='success'),
    path('writeblog',views.writeblog,name='writeblog'),
    path('blog/<int:id>',views.blog,name='blog'),
    path('explore/logout',views.logout,name='logout'),
    path('dashboard/logout',views.logout,name='logout'),
    path('dashboard',views.dashboard,name="dashboard"),
    path('dashboard/changepassword',views.changepassword,name='changepassword'),
    path('logout',views.logout,name='logout'),
    path('explore/internships',views.internships,name="internships"),
    path('explore/placements',views.placements,name="placements"),
    path('explore/general',views.general,name="general"),
    path('explore/fests_clubs',views.fests_clubs,name="fests_clubs"),
    path('explore/technical',views.technical,name="technical"),
    path('explore/search',views.search,name="search"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),

    path("reset_password", auth_views.PasswordResetView.as_view(template_name = "password_reset.html"),name="reset_password"),
    path("reset_password_sent", auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"),name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name= "password_reset_form.html"),name="password_reset_confirm"),
    path("reset_password_complete", auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"),name="password_reset_complete"),
    
    
]
