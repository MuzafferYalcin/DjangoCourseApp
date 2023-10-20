from django.contrib import admin

from .models import Course, Category, Slider

class CourseAdmin(admin.ModelAdmin):
   list_display = ("title","isActive","isHome")
   list_display_links = ("title",)
   readonly_fields = ("slug",)
   search_fields = ("title","isHome")
   list_filter = ("categories",)

   
class CategoryAdmin(admin.ModelAdmin):
   list_display = ("name","slug","course_count",)
   readonly_fields = ("slug",)

   def course_count(self, obj):
      return obj.course_set.count()

admin.site.register(Course,CourseAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Slider)