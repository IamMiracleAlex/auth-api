from django.urls import path

from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token, verify_jwt_token

from users import views



urlpatterns = [
    # path('token/', obtain_jwt_token, name='obtain_token'),
    path('token/refresh/', refresh_jwt_token, name='token_refresh'),
    path('token/verify/', verify_jwt_token, name="token_verify"),
    path('login/', views.LoginView.as_view()),
    path('signup/', views.SignUpView.as_view()),
    path('all/', views.ListUserView.as_view()),
]
