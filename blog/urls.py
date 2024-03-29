from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('detail/<int:id>/', views.article_detail, name="detail"),
    path('post_list', views.post_list, name="post_list"),
    path('search/', views.search, name='search'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('about_us/', views.about_us, name='about_us'),
]