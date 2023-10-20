from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
   name= models.CharField(max_length=40)
   slug = models.SlugField(blank=True,unique=True,db_index=True,)

   class Meta:
         verbose_name_plural = "Categories"
         ordering= ["name"]

   def save(self, *args, **kwargs):
         self.slug = slugify( self.name )
         super().save(args, kwargs)

   def __str__(self):
        return self.name

class Course(models.Model):
   title = models.CharField(max_length=100)
   subtitle = models.CharField(max_length=100, default='' ) 
   description = RichTextField()
   image = models.FileField(upload_to='images',default='')
   date = models.DateField(auto_now=True)
   isActive = models.BooleanField(default=False)
   isHome = models.BooleanField(default=False)
   slug = models.SlugField(default="",blank=True,unique=True , db_index=True)
   categories = models.ManyToManyField(Category)


   class Meta:
      ordering= ["-date"]

   def save(self, *args, **kwargs): #veri tababına kaydedilirken slug oluşturmak
      self.slug = slugify( self.title )
      super().save(args, kwargs)

   def __str__(self):
      return f'{self.title}'
      
   
class Slider(models.Model):
   title = models.CharField( max_length=100)
   image = models.ImageField(upload_to="images")
   course = models.ForeignKey(Course, on_delete=models.SET_NULL,null=True, blank=True)
   is_active = models.BooleanField(default=False)
   def __str__(self):
       return f'{self.title}'


