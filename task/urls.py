from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "task"
router = routers.DefaultRouter()

router.register("", viewset=views.TaskViewSets)


urlpatterns = [
    path("", include(router.urls)),

]
