from django.urls import path

from .views import AdminView, EditorView, StaffView, StudentView

urlpatterns = [
    path("admin/", AdminView.as_view(), name="admin-page"),
    path("editor/", EditorView.as_view(), name="editor-page"),
    path("staff/", StaffView.as_view(), name="staff-page"),
    path("student/", StudentView.as_view(), name="student-page"),
]
