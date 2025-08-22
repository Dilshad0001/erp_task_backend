
from django.urls import path
from .import views
urlpatterns = [
    path('admin/user-list/', views.UsersListAdminView.as_view()),
    path('manager/user-list/', views.UsersListManagerView.as_view()),
    path('employee/profile/', views.UserSelfProfileView.as_view()),

]
