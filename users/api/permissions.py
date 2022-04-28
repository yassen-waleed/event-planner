from rest_framework.permissions import BasePermission



class IsCustomerUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_customer)


class IsVendorUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_vendor)

class IsManagerUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_manager)