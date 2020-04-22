# -*- coding: utf-8 -*-
#from django.contrib import admin
from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home,name="home"),
    path('Disease/<str:crop>/', views.Disease,name="disease"),
    path('Pesticide/<str:crop>/<str:disease>/', views.Pesticide,name="pesticide"),
    path('Aboutus/', views.Aboutus,name="Aboutus"),
    re_path(r'Login$', views.Login,name="Login"),
    re_path(r'Logout$', views.Logout,name="Logout"),
    re_path(r'Register$', views.Register, name='Register'),
    path('Questions/<str:EMAIL>/', views.Questions, name='Questions'),
    re_path(r'AddQuestion$', views.AddQuestion, name='AddQuestion'),
    re_path(r'AddAnswer$', views.Addanswer, name='AddAnswer'),
    path('Pesticide/<str:crop>/<str:disease>/<str:pesticide>/', views.upvote,name="upvote"),
    path('Question/<str:qid>/', views.answers, name='answer'),
    path('Answer/<int:Aid>/', views.ans_del, name='ans_del'),
    path('QuesDel/<int:Qid>/', views.ques_del, name='ques_del'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)