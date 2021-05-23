from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "compredict_interview_task.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import compredict_interview_task.users.signals  # noqa F401
        except ImportError:
            pass
