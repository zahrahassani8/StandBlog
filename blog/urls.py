from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('detail/<int:id>/', views.article_detail, name="detail"),
]