from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, summarise_task, archived_tasks

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('summarise/', summarise_task),
    path('archived/', archived_tasks),

]
