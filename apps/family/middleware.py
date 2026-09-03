"""
Middleware to ensure request.active_family_member is populated on every request
before views execute, and auto-provisions a SELF profile for any user without one.
"""
from apps.family.models import FamilyMember


class ActiveFamilyMemberMiddleware:
    """
    Ensures request.active_family_member is available across all views and querysets.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            members = FamilyMember.objects.filter(user=request.user, is_active=True)
            active_member_id = request.session.get('active_family_member_id')
            active_member = None

            if active_member_id:
                active_member = members.filter(id=active_member_id).first()

            # Auto-create SELF profile if user has none (e.g. superuser/admin)
            if not members.exists():
                active_member = FamilyMember.objects.create(
                    user=request.user,
                    first_name=request.user.first_name or request.user.username,
                    last_name=request.user.last_name or 'Profile',
                    relationship='SELF',
                    is_active=True
                )
                members = FamilyMember.objects.filter(user=request.user, is_active=True)
                request.session['active_family_member_id'] = active_member.id
            elif not active_member:
                self_member = members.filter(relationship='SELF').first()
                active_member = self_member or members.first()
                request.session['active_family_member_id'] = active_member.id

            request.active_family_member = active_member
            request.user_family_members = members
        else:
            request.active_family_member = None
            request.user_family_members = []

        response = self.get_response(request)
        return response
