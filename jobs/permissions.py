from rest_framework import permissions

class VerifiyJobIsAssigned(permissions.BasePermission):
    message = 'Este trabajo ya fué asignado'
    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT':
            data = request.data
            status = data.__getitem__('status')
            if int(status) == 2:
                return obj.status != 2
        return True

class VerifiyJobIsCompleted(permissions.BasePermission):
    message = 'Este trabajo ya fué completado anteriormente'
    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT':
            data = request.data
            status = data.__getitem__('status')
            if int(status) == 3:
                return obj.status != 3
        return True