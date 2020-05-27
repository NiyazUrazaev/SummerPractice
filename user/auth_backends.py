from django.contrib.auth.backends import ModelBackend

from SummerPractice.settings import INSTALLED_APPS
from .models import ClassicStudent


class CustomUserModelBackend(ModelBackend):

    def get_user_by_name_pass(self, model, username, password):
        user = model.objects.get(username=username)
        if user.check_password(password):
            return user

    def get_user_by_id(self, model, user_id):
        return model.objects.get(pk=user_id)

    def authenticate(self, request, username=None, password=None, **kwargs):
        gamification_flag = 'gamification' in INSTALLED_APPS
        mindfulness_flag = 'mindfulness' in INSTALLED_APPS

        try:
            user = self.get_user_by_name_pass(
                ClassicStudent, username, password)
            return user
        except ClassicStudent.DoesNotExist:
            if gamification_flag or mindfulness_flag:
                pass
            else:
                return None

        if gamification_flag:
            from gamification.models import GamificationStudent
            try:
                user = self.get_user_by_name_pass(
                    GamificationStudent, username, password)
                return user
            except GamificationStudent.DoesNotExist:
                if mindfulness_flag:
                    pass
                else:
                    return None

        if mindfulness_flag:
            from mindfulness.models import MindfulnessStudent
            try:
                user = self.get_user_by_name_pass(
                    MindfulnessStudent, username, password)
                return user
            except MindfulnessStudent.DoesNotExist:
                return None

    def get_user(self, user_id):

        gamification_flag = 'gamification' in INSTALLED_APPS
        mindfulness_flag = 'mindfulness' in INSTALLED_APPS

        if gamification_flag:
            from gamification.models import GamificationStudent
            try:
                return self.get_user_by_id(GamificationStudent, user_id)
            except GamificationStudent.DoesNotExist:
                return None

        if mindfulness_flag:
            from mindfulness.models import MindfulnessStudent
            try:
                return self.get_user_by_id(MindfulnessStudent, user_id)
            except MindfulnessStudent.DoesNotExist:
                return None

        try:
            return self.get_user_by_id(ClassicStudent, user_id)
        except ClassicStudent.DoesNotExist:
            return None