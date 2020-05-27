from django.contrib import auth
from django.forms.models import model_to_dict
from rest_framework.authtoken.models import Token

from rest_framework.views import APIView
from rest_framework.response import Response


class LoginView(APIView):
    """'Аутентификация пользователя"""

    def post(self, request):

        login = request.POST.get('login', None)
        if login is None:
            return Response(status=400, data='Укажите ваш логин!')

        password = request.POST.get('password', None)
        if password is None:
            return Response(status=400, data='Укажите ваш пароль!')

        user = auth.authenticate(username=login, password=password)

        if user is not None:
            token = Token.objects.get_or_create(user=user)
            auth.login(request, user)
            return Response(
                status=200, data={
                    'token': token[0].key,
                    'csrftoken': request.COOKIES.get('csrftoken'),
                    'class': request.user.__class__.__name__,
                    'student': model_to_dict(request.user, exclude=(
                        'user_permissions', 'practices')),
                })
        else:
            return Response(
                status=401, data={'message': 'Неверный логин или пароль'})


class LogoutView(APIView):
    """'Выход пользователя"""

    def post(self, request):

        auth.logout(request)

        return Response(
                status=200, data={'message': 'Выход прошел успешно'})
