from .views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'students-controller', StudentViewSet)


urlpatterns = router.urls

urlpatterns += [
    path('get-all-students',get_all_students,name='Get all Students'),
    path("add-student",add_student,name="Add Student using post"),
    path('get-student',get_student,name="get student by id"),
    path('get-student/<id>',get_student_id,name="get student by id"),
    path('update-student',update_student,name="update student"),
    path('update-student/<id>',update_student_id,name="update student by id"),
    path('delete-student',delete_student,name="delete student"),
    path('delete-student/<id>',delete_student_id,name="delete student"),
    path("student-api",student_api.as_view()),
path('register/',RegisterUser.as_view()),
path('login/',LoginUser.as_view()),
path('get-user',get_user)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
