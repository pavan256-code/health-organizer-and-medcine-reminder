"""
Notification views for viewing, filtering, marking as read, and polling status.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib import messages
from apps.notifications.models import Notification
from apps.notifications.services import mark_all_notifications_read


class NotificationListView(LoginRequiredMixin, ListView):
    """
    Displays notification history with category filtering and read/unread toggles.
    """
    model = Notification
    template_name = 'notifications/list.html'
    context_object_name = 'notifications'
    paginate_by = 25

    def get_queryset(self):
        qs = Notification.objects.filter(user=self.request.user)
        category = self.request.GET.get('category')
        status = self.request.GET.get('status')

        if category:
            qs = qs.filter(category=category)
        if status == 'unread':
            qs = qs.filter(is_read=False)
        elif status == 'read':
            qs = qs.filter(is_read=True)

        return qs.select_related('family_member').order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_choices'] = Notification.CATEGORY_CHOICES
        context['selected_category'] = self.request.GET.get('category', '')
        context['selected_status'] = self.request.GET.get('status', '')
        return context


class MarkNotificationReadView(LoginRequiredMixin, View):
    """
    Marks a single notification as read and redirects to its action_url or back.
    """
    def post(self, request, pk):
        notification = get_object_or_404(Notification, id=pk, user=request.user)
        notification.mark_as_read()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'ok', 'id': notification.id})

        if notification.action_url:
            return redirect(notification.action_url)
        return redirect('notifications:list')

    def get(self, request, pk):
        return self.post(request, pk)


class MarkAllNotificationsReadView(LoginRequiredMixin, View):
    """
    Marks all notifications for the user as read.
    """
    def post(self, request):
        count = mark_all_notifications_read(request.user)
        messages.success(request, f"Marked {count} notifications as read.")
        return redirect('notifications:list')

    def get(self, request):
        return self.post(request)


class DeleteNotificationView(LoginRequiredMixin, View):
    """
    Deletes an individual notification.
    """
    def post(self, request, pk):
        notification = get_object_or_404(Notification, id=pk, user=request.user)
        notification.delete()
        messages.info(request, "Notification deleted.")
        return redirect('notifications:list')


class UnreadCountAPIView(LoginRequiredMixin, View):
    """
    Returns live unread count and latest 5 items in JSON format for the browser UI.
    """
    def get(self, request):
        unread_qs = Notification.objects.filter(user=request.user, is_read=False)
        count = unread_qs.count()
        recent = unread_qs.order_by('-created_at')[:5]

        items = [{
            'id': n.id,
            'title': n.title,
            'message': n.message,
            'category': n.category,
            'priority': n.priority,
            'action_url': n.action_url,
            'created_at': n.created_at.strftime('%H:%M %b %d')
        } for n in recent]

        return JsonResponse({
            'unread_count': count,
            'items': items
        })
