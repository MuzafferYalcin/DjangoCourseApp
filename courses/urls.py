from django.urls import path

from . import views 


urlpatterns = [
   path("",views.kurslar, name="kurs"),
   path("search",views.search, name="search"),
   path("course-list",views.course_list, name="course_list"),
   path("course-edit/<id>",views.course_edit, name="course_edit"),
   path("course-delete/<id>",views.course_delete, name="course_delete"),
   path("upload",views.upload, name="upload_images"),
   path("create-course",views.create_course, name="create_course"),
   path("<slug>",views.details, name="details"),
   path("kategory/<slug>", views.getCourseByCategory, name="courses_by_category"),
]
