from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
    path('', views.home, name='base'),
    path('articles/', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment,
         name='leave_comment')
]
