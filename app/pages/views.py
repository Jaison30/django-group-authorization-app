from django.views import generic
from braces.views import LoginRequiredMixin, GroupRequiredMixin


class EditorView(LoginRequiredMixin, GroupRequiredMixin, generic.TemplateView):
    template_name = "pages/editor.html"
    group_required = "editor"
    raise_exception = True


class StaffView(LoginRequiredMixin, GroupRequiredMixin, generic.TemplateView):
    template_name = "pages/staff.html"
    group_required = "staff"
    raise_exception = True


class StudentView(LoginRequiredMixin, GroupRequiredMixin, generic.TemplateView):
    template_name = "pages/student.html"
    group_required = "student"
    raise_exception = True


class AdminView(LoginRequiredMixin, GroupRequiredMixin, generic.TemplateView):
    template_name = "pages/admin.html"
    group_required = "admin"
    raise_exception = True
