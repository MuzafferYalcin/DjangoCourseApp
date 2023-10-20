from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse 
from django.core.paginator import Paginator

from courses.forms import CreateCourseForm, EditCourseForm, UploadForm
from .models import Course,Category, Slider


def kurslar(req):
    courses = Course.objects.filter(isActive = True, isHome = True)
    categories = Category.objects.all()
    slider = Slider.objects.filter(is_active = True)
    return render(req, "courses/index.html",{"courses":courses,"categories":categories, 'sliders':slider})


def search(req ):
    if "q" in req.GET and req.GET["q"] !="": 
        q = req.GET["q"]
        kurslar = Course.objects.filter( isActive = True , title__contains = q)
        kategoriler = Category.objects.all()
    else:
        return redirect("kurs")
    

    return render(req, "courses/search.html",{"courses":kurslar,"categories":kategoriler})


def create_course(req ):
    if req.method == 'POST':
        form = CreateCourseForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect("kurs")
        
    else:
        form = CreateCourseForm()    
    return render(req, "courses/create-course.html", {"form":form} )


def course_edit(req, id):
    course = Course.objects.get(id = id)
    if req.method == "POST":
        form = EditCourseForm(req.POST,req.FILES ,instance=course)
        form.save()
        return redirect("kurs")
    else:
        form = EditCourseForm(instance=course)
    return render(req, 'courses/edit-course.html',{"form":form})


def course_delete(req, id):
    course = get_object_or_404(Course, pk = id)

    if req.method == 'POST':
        course.delete()
        return redirect("course_list")

    return render(req, 'courses/delete-course.html', { "course": course})


def course_list(req):
    courses = Course.objects.all()
    return render(req, "courses/course-list.html",{"courses":courses})


def details(req,slug):
    course = Course.objects.get(slug = slug)
    return render(req , 'courses/details.html', {"course":course})


def upload(req):
    if req.method == 'POST':
        form = UploadForm(req.POST, req.FILES)
        if form.is_valid():
            uploaded_image = req.FILES["image"]
            return render(req, 'courses/success.html')
    else:
        form = UploadForm()
    return render(req, "courses/upload.html", {"form":form})



def getCourseByCategory(req , slug):
    kurslar = Course.objects.filter(categories__slug = slug, isActive = True)
    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar, 3)
    page =  req.GET.get("page",1)
    
    page_obj = paginator.page(page)

    return render(req, "courses/list.html",{"page_obj":page_obj,"categories":kategoriler,"secilikategori":slug})