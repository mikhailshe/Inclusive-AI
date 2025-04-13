from django.urls import include, path
from settings.settings import (
    AUTHENTICATION_BACKENDS,
    MIDDLEWARE)


AUTHENTICATION_BACKENDS += [
    # allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

MIDDLEWARE += [
    # Add the account middleware:
    'allauth.account.middleware.AccountMiddleware',
]


# Поля, используемые при регистрации
# Звездочка (*) указывает на обязательное поле
ACCOUNT_SIGNUP_FIELDS = [
    # 'email*',       # Обязательное поле для email
    'username*',    # Обязательное поле для имени пользователя
    'password1*',   # Обязательное поле для пароля
    'password2*',   # Обязательное поле для подтверждения пароля
]

# Адрес страницы аторизации
LOGIN_URL = '/accounts/login/'

# Адрес на который переходим после аторизации
LOGIN_REDIRECT_URL = '/'

# Адрес на который переходим после выхода из системы
LOGOUT_REDIRECT_URL = '/'

# Указывает используемый класс адаптера, позволяющий изменять
# определенное поведение по умолчанию.
ACCOUNT_ADAPTER = 'allauth.account.adapter.DefaultAccountAdapter'

# True - перенаправление аутентифицированных пользователей на
# LOGIN_REDIRECT_URL при попытке доступа к страницам входа/регистрации.
# False - вошедшие в систему пользователи не будут перенаправлены
# при доступе к страницам входа/регистрации.
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True

# Определяет, будет ли адрес электронной почты автоматически
# подтвержден GET запросом. GET не предназначен для изменения состояния
# сервера, хотя обычно используется для подтверждения по электронной почте.
# Чтобы избежать необходимости взаимодействия с пользователем, рассмотрите
# возможность использования POST через Javascript в шаблоне подтверждения
# электронной почты в качестве альтернативы установке значения True.
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

# URL-адрес для перенаправления после успешного подтверждения по электронной
# почте, если ни один пользователь не вошел в систему.
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL

# URL-адрес для перенаправления после успешного подтверждения по электронной
# почте, в случае аутентифицированного пользователя.
# None - использовать настройки LOGIN_REDIRECT_URL.
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None

# Определяет количество дней действия подтверждающих писем электронной почты.
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

# Для проверки адреса электронной почты по почте отправляется ключ,
# идентифицирующий адрес электронной почты, подлежащий проверке. В предыдущих
# версиях запись хранилась в базе данных для каждого текущего подтверждения
# электронной почты, отслеживая эти ключи. Текущие версии используют ключи на
# основе HMAC, которые не требуют состояния на стороне сервера.
ACCOUNT_EMAIL_CONFIRMATION_HMAC = True


# Подтверждение email
ACCOUNT_EMAIL_VERIFICATION = 'none'  # none | mandatory | optional

# Префикс темы, используемый для отправки сообщений электронной почты.
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''

# Протокол по умолчанию, используемый при генерации URL-адресов,
# например, для процедуры забытый пароль.
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'

# Максимальная длина поля электронной почты.
ACCOUNT_EMAIL_MAX_LENGTH = 100

# Метод входа пользователя в систему (Устаревший метод)
# Установка этого параметра в “email” требует ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_LOGIN_METHODS = {'username'}

ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_USERNAME_REQUIRED = True


# Максимальное количество адресов электронной почты, которые пользователь
# может связать со своей учетной записью.
ACCOUNT_MAX_EMAIL_ADDRESSES = None

# Используется для переопределения форм
ACCOUNT_FORMS = {
    'login': 'allauth.account.forms.LoginForm',
    'signup': 'allauth.account.forms.SignupForm',
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
}

# Автоматический вход в систему после подтверждения своего адреса электронной
# почты. Это работает только при подтверждении адреса электронной почты сразу
# после регистрации, предполагая, что пользователи не закрывали свой браузер
# или использовали какой-то режим приватного просмотра.
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# Определяет, будет ли пользователь автоматически
# выходить из системы по запросу GET.
ACCOUNT_LOGOUT_ON_GET = False

# Определяет, будет ли пользователь автоматически выходить из системы после
# изменения или установки своего пароля.
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
# True  - Пользователи автоматически войдут в систему после сброса пароля
# False - Перенаправляются на страницу сброса пароля.
ACCOUNT_LOGIN_ON_PASSWORD_RESET = False

# Адрес на который перенаправляется пользователь после выхода из системы
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

# Параметр render_value, передаваемый в поля PasswordInput.
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False

# Будет ли имя пользователя храниться в нижнем регистре
ACCOUNT_PRESERVE_USERNAME_CASING = True

# Период восстановления (в секундах) после отправки подтверждающего письма,
# в течение которого дальнейшие письма не отправляются.
# Количество неудачных попыток входа в систему.
# При превышении числа неудачных попыток входа в систему пользователю
# запрещается входить в систему в течение указанных секунд
ACCOUNT_RATE_LIMITS = {
    'confirm_email': '3/180s',  # 3 запроса в течение 180 секунд (3 минуты)
    'login_failed': '5/300s',   # 5 неудачных попыток в течение 300 секунд (5 минут)
}

# Управляет временем жизни сеанса.
# None  - спросить пользователя (“Помнишь меня?”)
# False - чтобы не помнить
# True  - чтобы всегда помнить
ACCOUNT_SESSION_REMEMBER = None


# Строка, указывающая на пользовательский класс форм
# (например, ‘myapp.forms.SignupForm’), который используется во
# время регистрации, чтобы запросить у пользователя дополнительные
# данные (например, регистрация на рассылку новостей, дата рождения).
# Этот класс должен реализовывать метод def signup(self, request, user),
# где user представляет только что подписанного пользователя.
ACCOUNT_SIGNUP_FORM_CLASS = None


# URL-адрес (или имя URL-адреса) для перенаправления непосредственно
# после регистрации. Обратите внимание, что пользователи перенаправляютс
# на этот URL-адрес только в том случае, если регистрация прошла непрерывно,
# например, без каких-либо побочных шагов из-за проверки электронной почты.
# Если ваш проект требует, чтобы пользователь всегда проходил через
# определенные бортовые представления после регистрации, вам придется
# отслеживать состояние, указывающее, успешно ли пользователь вошел в систему,
# и обрабатывать его соответствующим образом.
ACCOUNT_SIGNUP_REDIRECT_URL = LOGIN_REDIRECT_URL

# Строка, определяющая расширение шаблона для использования.
ACCOUNT_TEMPLATE_EXTENSION = 'html'

# Список имен пользователей, которые не могут быть использованы пользователем.
ACCOUNT_USERNAME_BLACKLIST = [
    'admin', 'administrator', 'master', 'manager', 'root', 'super',
    'director', 'moderator', 'top',
]

# Обеспечение уникальности адресов электронной почты.
ACCOUNT_UNIQUE_EMAIL = True

# Вызываемый объект (или строка вида 'some.module.callable_name'),
# который принимает пользователя в качестве единственного аргумента и
# возвращает отображаемое имя пользователя. Реализация по умолчанию
# возвращает user.username.
# ACCOUNT_USER_DISPLAY = user.username
# Имя поля, содержащего электронное письмо, если таковое имеется.
ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'

# Имя поля, содержащего имя пользователя, если таковое имеется.
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'

# Целое число, задающее минимально допустимую длину имени пользователя.
ACCOUNT_USERNAME_MIN_LENGTH = 4


# Путь ('some.module.validators.custom_username_validators') к списку
# пользовательских валидаторов имен пользователей. Если этот параметр
# не задан, то используются настройки валидаторов в поле имя пользователя
# модели пользователя.
ACCOUNT_USERNAME_VALIDATORS = None
