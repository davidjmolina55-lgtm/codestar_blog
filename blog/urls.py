from . import views
from django.urls import include, path

urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]