from django.urls import path
from blog import views

urlpatterns = [
    path('list/', views.blog_list, name='blog-list'),
    path('<int:pk>/detail/', views.blog_content, name="blog-detail")
]
