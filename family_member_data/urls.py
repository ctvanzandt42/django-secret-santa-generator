from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('participants', views.participants, name='participants'),
    path('participants/<int:participant_id>/', views.participant_details, name='participant_details')
]