# # -*- coding: utf-8 -*-
from rest_framework import permissions


class ObjAndOwnerPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            return True
        elif request.method == 'PATCH':
            return True
        elif request.method == 'DELETE':
            return request.user.is_staff
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        elif request.method == 'POST':
            if request.user.is_staff:
                return True
            elif hasattr(request.user, 'profile'):
                return obj.zakazchik == request.profile
            else:
                return False

        elif request.method == 'PATCH': 
            if request.user.is_staff:
                return True
            elif hasattr(request.user, 'profile'):
                return obj.zakazchik == request.profile
            else:
                return False

        elif request.method == 'DELETE':
            return request.user.is_staff
        return False


class ReadOrAdminOnlyPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if request.user.is_staff:
                return True
            else:
                return False
        
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if request.user.is_staff:
                return True
            else:
                return False
