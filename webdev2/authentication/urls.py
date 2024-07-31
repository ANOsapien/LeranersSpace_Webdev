from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('signup/stage1/', views.signup_stage1, name='signup_stage1'),  # Signup step 1
    path('signup/stage2/', views.signup_stage2, name='signup_stage2'),  # Signup step 2
    path('login/', views.login_view, name='login'),  # Login page
    path('logout/', views.logout_view, name='signout'),  # Logout
    path('posts/', views.all_posts, name='all_posts'),  # All posts
    path('posts/mine/', views.my_posts, name='my_posts'),  # User's own posts
    path('posts/new/', views.create_post, name='create_post'),  # Create a new post
    path('posts/<int:post_id>/edit/', views.edit_post, name='edit_post'),  # Edit a post
    path('posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),  # Delete a post
]
