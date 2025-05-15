from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogsListView, BlogsCreateView, BlogsDetailView, BlogsUpdateView, BlogsDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path("blogs_list/", BlogsListView.as_view(), name="list"),
    path("blogs_create/", BlogsCreateView.as_view(), name="create"),
    path("blogs_detail/<int:pk>/", BlogsDetailView.as_view(), name="detail"),
    path("blogs_update/<int:pk>/", BlogsUpdateView.as_view(), name="update"),
    path("blogs_delete/<int:pk>/", BlogsDeleteView.as_view(), name="delete"),
]
