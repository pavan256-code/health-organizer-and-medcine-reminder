"""
Family URL configuration.
"""

from django.urls import path
from apps.family.views import (
    FamilyMemberListView,
    FamilyMemberCreateView,
    FamilyMemberUpdateView,
    FamilyMemberDeleteView,
    FamilyMemberDetailView,
    SwitchActiveFamilyMemberView,
)

app_name = 'family'

urlpatterns = [
    path('', FamilyMemberListView.as_view(), name='list'),
    path('add/', FamilyMemberCreateView.as_view(), name='add'),
    path('<int:pk>/', FamilyMemberDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', FamilyMemberUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', FamilyMemberDeleteView.as_view(), name='delete'),
    path('switch/', SwitchActiveFamilyMemberView.as_view(), name='switch_direct'),
    path('switch/<int:member_id>/', SwitchActiveFamilyMemberView.as_view(), name='switch'),
]
