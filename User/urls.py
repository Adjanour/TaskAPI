"""URL mappings for the user API"""

from django.urls import path,include
from rest_framework.routers import DefaultRouter

from User import views

router = DefaultRouter()
router.register('users',views.UsersView)

urlpatterns = [
    path('create/',views.CreateUserView.as_view(),name='create'),
    path('token/',views.CreateTokenView.as_view(),name='token'),
    path('me/',views.ManageUserView.as_view(),name="me"),
    path('',include(router.urls))

]
