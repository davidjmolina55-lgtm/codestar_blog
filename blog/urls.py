from . import views
from django.urls import include, path

urlpatterns = [
    path("about/", include("about.urls")),
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/edit_comment/<int:comment_id>/',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/',
         views.comment_delete, name='comment_delete'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]