from django.urls import path
from . import views

urlpatterns = [
	path('', views.ApiOverview, name='home'),
	path('create', views.add_guests, name='add-guests'),
	path('all', views.view_guests, name='view-guests'),
	path('update/<int:pk>', views.update_guests, name='update-guests'),
	path('guest/<int:pk>/delete', views.delete_guests, name='delete-guest'),

]
