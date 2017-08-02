from rest_framework import exceptions, permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.method == 'GET' or request.user.is_superuser or request.user.is_staff:
            return True
        return False
        # raise exceptions.PermissionDenied

        # print(request.method)
        # print(permissions.SAFE_METHODS)
        # print('super {}, staff {}'.format(request.user.is_superuser, request.user.is_staff))
        # rtn = True if request.method == 'GET' or request.user.is_superuser or request.user.is_staff else False
        # print('Going to return {rtn}'.format(rtn=rtn))
        # return rtn
        #
