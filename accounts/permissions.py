from rest_framework.permissions import IsAuthenticated


class IsBenefactor(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.is_benefactor


class IsCharityOwner(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.is_charity
