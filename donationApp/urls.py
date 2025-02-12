from django.urls import path,re_path
from . import views

urlpatterns = [
  path('',views.home, name='donate-home'),
  path('api/charities/',views.CharityList.as_view()),
  path('api/donors/',views.DonorList.as_view()),
  path('api/donations/',views.DonationsList.as_view()),
  path('api/users/',views.UsersList.as_view()),
  path('api/users/user-id/<int:pk>',views.UserDescription.as_view()),
  path('api/donors/donors-id/<int:pk>',views.DonorDescription.as_view()),
  path('api/donations/donations-id/<int:pk>',views.DonationsDescription.as_view()),
  path('api/charities/charities-id/<int:pk>',views.CharityDescription.as_view())


]

