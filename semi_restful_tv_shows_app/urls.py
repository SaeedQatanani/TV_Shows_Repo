from django.urls import path
from . import views

urlpatterns = [
    path('shows/new/', views.add),
    path('shows/create/', views.create),
    path('shows/<id>/', views.show),
    path('shows/', views.display_all),
    path('shows/<id>/edit/', views.edit),
    path('shows/<int:id>/update/', views.update),
    path('shows/<int:id>/destroy/', views.delete),
    path('', views.main),
]