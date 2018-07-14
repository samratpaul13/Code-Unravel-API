from django.urls import path,re_path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('login/',views.UserLoginAPIView.as_view(),name='login'),
    path('sign-up/', views.UserList.as_view()),
    path('users/', views.UserList.as_view()),
    re_path(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    path('questions/', views.QuestionList.as_view()),
    re_path(r'^question/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view()),
    path('candidates/', views.CandidateList.as_view()),
    re_path(r'^candidate/(?P<pk>[0-9]+)/$', views.CandidateDetail.as_view()),
    path('getcandidate/', views.GetCandidate.as_view()),

    path('results/', views.ResultList.as_view()),
    re_path(r'^result/(?P<pk>[0-9]+)/$', views.ResultDetail.as_view()),
    path('assigned_tasks/', views.TaskAssignList.as_view()),
    re_path(r'^assigned_task/(?P<pk>[0-9]+)/$', views.TaskAssignDetail.as_view()),
    path('user_ids/', views.GetUserIds.as_view()),
   
]
