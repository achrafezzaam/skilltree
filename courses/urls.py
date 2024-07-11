from django.urls import path
from . import views


app_name = "courses"
urlpatterns = [
    path("", views.index, name="courses"),
    path("admin_dashboard/", views.admin_dashboard, name="admin-dashboard"),
    path("<int:course_id>/", views.detail_view, name="detail"),
    path("delete/<int:course_id>/", views.delete_course, name="delete_course"),
    path("question/<int:question_id>/", views.question_view, name="question"),
    path("<int:course_id>/vote/", views.vote, name="vote"),
]
