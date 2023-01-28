from rest_framework import permissions


class IsMessageOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(obj.sender == request.user)