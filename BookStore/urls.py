from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_posts, name='post_view'),
    path('posts/<int:id>/', views.post_detail, name='post_detail_view'),
    path('add-post/', views.add_post, name='add_post_view'),
    path('add-comment/', views.add_comment, name='add_comment_view'),
]