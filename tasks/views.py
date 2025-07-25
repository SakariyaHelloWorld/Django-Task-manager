from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def archived_tasks(request):
    tasks = Task.objects.filter(archived=True)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter(archived=False)
    serializer_class = TaskSerializer

    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        task.archived = True
        task.save()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
def summarise_task(request):
    return Response({"summary": "This is a mock summary of your task."})

# Create your views here.
