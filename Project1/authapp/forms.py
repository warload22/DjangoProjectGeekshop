from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from authapp.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fileds = ('username', 'password')

    def __init__(self, *args, **kwargs):
            super(UserLoginForm, self).__init__(*args,**kwargs)
            self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
            self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
            self.fields['username'].required = True
            self.fields['password'].required = True
            for filed_name , field in self.fields.items():
                field.widget.attrs['class'] = 'form-control py-4'


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'last_name', 'first_name', 'email')

    def __init__(self, *args, **kwargs):
            super(UserRegisterForm, self).__init__(*args,**kwargs)
            self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
            self.fields['username'].required = True
            self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
            self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
            self.fields['password1'].required = True
            self.fields['password2'].required = True
            self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилия'
            self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
            self.fields['email'].widget.attrs['placeholder'] = 'Введите email'

            for filed_name , field in self.fields.items():
                field.widget.attrs['class'] = 'form-control py-4'