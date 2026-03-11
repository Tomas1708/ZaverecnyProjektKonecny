from django.urls import path
from . import views
urlpatterns = [
    #CRUD ADMIN - správa poistencov
    path('', views.PolicyholderListView.as_view(), name='policyholder_list'),
    path('create/',views.PolicyholderCreateView.as_view(), name='policyholder_create'),
    path('<int:pk>/',views.PolicyholderDetailView.as_view(), name='policyholder_detail'),
    path('<int:pk>/update/',views.PolicyholderUpdateView.as_view(), name='policyholder_update'),
    path('<int:pk>/delete/', views.PolicyholderDeleteView.as_view(), name='policyholder_delete'),

    #CRUD POISTENIA (kombinácia admin + user cez mixiny)
    path("insurances/", views.InsuranceListView.as_view(), name='insurance_list'),
    path('insurance/<int:pk>/', views.InsuranceDetailView.as_view(), name='insurance_detail'),
    path('insurance/create/',views.InsuranceCreateView.as_view(), name='insurance_create'),
    path("insurance/<int:pk>/update/", views.InsuranceUpdateView.as_view(), name='insurance_update'),
    path("insurance/<int:pk>/delete/",views.InsuranceDeleteView.as_view(), name="insurance_delete"),

    #Dashboard
    #path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('my_account/', views.MyAccountDetailView.as_view(), name='my_account'),
    path('my-account/update/', views.MyAccountUpdateView.as_view(), name='my_account_update'),
]