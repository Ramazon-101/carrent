from django.urls import path
from .views import blog_page, about_page, blog_single
app_name = 'blog'
urlpatterns = [
    path('', blog_page),
    path('about/', about_page),
    path('<int:pk>/', blog_single)
]
