from django.contrib import admin
from django.urls import path
from myapp.views import CommentList,CommentDetail

urlpatterns = [
    path('api/Comment',CommentList.as_view()),
    path('api/Comment/<int:pk>',CommentDetail.as_view()),
    path('admin/', admin.site.urls),
    ]