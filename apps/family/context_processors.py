"""
Context processor for the currently selected active family member.
"""

from apps.family.models import FamilyMember


def active_family_member(request):
    """
    Exposes the active family member and full list of family members
    to every template, enabling patient switching across all views.
    """
    if not request.user.is_authenticated:
        return {
            'active_family_member': None,
            'user_family_members': [],
        }

    # First read from request populated by ActiveFamilyMemberMiddleware
    active_member = getattr(request, 'active_family_member', None)
    members = getattr(request, 'user_family_members', None)

    if members is None:
        members = FamilyMember.objects.filter(user=request.user, is_active=True)

    if not active_member and members.exists():
        active_member_id = request.session.get('active_family_member_id')
        if active_member_id:
            active_member = members.filter(id=active_member_id).first()
        if not active_member:
            active_member = members.filter(relationship='SELF').first() or members.first()
            if active_member:
                request.session['active_family_member_id'] = active_member.id

    request.active_family_member = active_member

    return {
        'active_family_member': active_member,
        'user_family_members': members,
    }
