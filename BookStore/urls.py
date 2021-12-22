from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post_view'),
    path("posts/<int:id>/",views.PostDetailView.as_view(),name ='post_detail_view'),
    path("posts/<int:id>/update/", views.PostUpdateView.as_view(), name='post_update_view'),
    path("posts/<int:id>/delete/", views.PostDeleteView.as_view(), name='post_delete_view'),
    path('add-post/', views.PostCreateView.as_view(), name='add_post_view'),
]


