from rest_framework import mixins, viewsets
from .models import Job as JobModel
from .serializers import JobSerializer, CreateJobSerializer
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import JSONRenderer
from .filters import JobsFilter
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from channels.layers import get_channel_layer
from notifications.create_notification import createNotification
from asgiref.sync import async_to_sync
from .permissions import VerifiyJobIsAssigned, VerifiyJobIsCompleted

class JobViewSet(
    viewsets.GenericViewSet ,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    renderer_classes=(JSONRenderer,)
    queryset = JobModel.objects.all()
    serializer_class = JobSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, filters.SearchFilter)
    filterset_class = JobsFilter
    ordering_fields = ('title', 'budget', 'created_at')
    ordering = ('-created_at',)
    search_fields = ('title',)
    permission_classes = (VerifiyJobIsAssigned, VerifiyJobIsCompleted)

    def create(self, request, *args, **kwargs):
        serializer = CreateJobSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        res_serializer = JobSerializer(serializer.instance)
        return Response(res_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        if request.data.__contains__('status'):
            status = request.data.__getitem__('status')
            if status == 2:
                jobId = instance.id
                jobTitle = instance.title
                postulantId = request.data.__getitem__('postulant')
                message = 'Se ha aceptado su postulación al trabajo {}, \
                    puede comenzar a comunicarse por medio de nuestras salas de chat \
                    con el titular del pituto para arreglar los detalles '.format(
                    jobTitle
                )
                href = '/cuenta/mensajes/{}/'.format(jobTitle)
                sendNotification(jobId, message, href, postulantId)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    


def sendNotification(job_id, message, href, identificator_room):
    channel_layer = get_channel_layer()
    room_name = 'notifications_{}'.format(identificator_room)
    notification = createNotification(
        identificator_room,
        'asignacion',
        message,
        href
    )
    if notification:
        async_to_sync(channel_layer.group_send)(
            room_name,
            {
                'type': 'notification',
                'message': notification
            }
        )
    
