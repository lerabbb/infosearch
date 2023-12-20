from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.template.response import TemplateResponse
from . import forms, models

def index(request):
    return TemplateResponse(request, "index.html")


def get_university(request, id):
    try:
        res = models.University.objects.get(id=id)
        data = {
            "un_id": id,
            "name": res.name,
            "short_name": res.short_name,
            "create_date": res.create_date
        }
        return TemplateResponse(request, "university.html", data)
    
    except models.University.DoesNotExist:
        return HttpResponseNotFound(f"Нет такого университета с id={id}")


def university_list(request):
    all_universities = models.University.objects.all()
    data = {"university_list": all_universities }
    return TemplateResponse(request, "university_list.html", data)


def create_university(request):
    if request.method == "POST":
        new_university = models.University.objects.create(
            name = request.POST.get("name"),
            short_name = request.POST.get("short_name"),
            create_date = request.POST.get("create_date")
        )
        new_id = new_university.id
        return HttpResponseRedirect(f"/app/university/{new_id}")
    else:
        data = {
            "title": "University",
            "form": forms.UniversityForm()
        }
        return TemplateResponse(request, "create_entity.html", data)


def update_university(request, id):
    try:
        if request.method == "POST":
            models.University.objects.filter(id=id).update(
                name = request.POST.get("name"),
                short_name = request.POST.get("short_name"),
                create_date = request.POST.get("create_date")
            )
            return HttpResponseRedirect(f"/app/university/{id}")
        else:
            university = models.University.objects.get(id=id)
            data = {
                "title": "University",
                "form": forms.UniversityForm(instance=university)
            }
            return TemplateResponse(request, "create_entity.html", data)
        
    except models.University.DoesNotExist:
        return HttpResponseNotFound(f"Нет такого университета с id={id}")


def delete_university(request, id):
    try:
        university = models.University.objects.get(id=id)
        university.delete()
        return HttpResponseRedirect("/app/university")
    except models.University.DoesNotExist:
        return HttpResponseNotFound(f"Нет такого университета с id={id}")



def get_student(request, id):
    try:
        res = models.Student.objects.get(id=id)
        data = {
            "student_id": id,
            "firstname": res.firstname,
            "lastname": res.lastname,
            "patronymic": res.patronymic,
            "birthdate": res.birthdate,
            "university": res.university,
            "entrance_date": res.entrance_date 
        }
        return TemplateResponse(request, "student.html", data)
    
    except models.Student.DoesNotExist:
        return HttpResponseNotFound(f"Нет такого студента с id={id}")


def student_list(request):
    res = models.Student.objects.all()
    data = {"student_list": res }
    return TemplateResponse(request, "student_list.html", data)


def create_student(request):
    try:
        if request.method == "POST":
            university_id = request.POST.get("university")
            university = models.University.objects.get(id=university_id)
            new_student = models.Student.objects.create(
                firstname = request.POST.get("firstname"),
                lastname = request.POST.get("lastname"),
                patronymic = request.POST.get("patronymic"),
                birthdate = request.POST.get("birthdate"),
                university = university,
                entrance_date = request.POST.get("entrance_date")
            )
            new_id = new_student.id
            return HttpResponseRedirect(f"/app/student/{new_id}")
        else:
            data = {
                "title": "Student",
                "form": forms.StudentForm()
            }
            return TemplateResponse(request, "create_entity.html", data)
    except models.Student.DoesNotExist:
        return HttpResponseNotFound(f"Нет такого университета с id={university_id}")
    

def update_student(request, id):
    try:
        if request.method == "POST":
            university_id = request.POST.get("university")
            university = models.University.objects.get(id=university_id)
            models.Student.objects.filter(id=id).update(
               firstname = request.POST.get("firstname"),
                lastname = request.POST.get("lastname"),
                patronymic = request.POST.get("patronymic"),
                birthdate = request.POST.get("birthdate"),
                university = university,
                entrance_date = request.POST.get("entrance_date")
            )
            return HttpResponseRedirect(f"/app/student/{id}")
        else:
            student = models.Student.objects.get(id=id)
            data = {
                "title": "Student",
                "form": forms.StudentForm(instance=student)
            }
            return TemplateResponse(request, "create_entity.html", data)
        
    except models.University.DoesNotExist:
        return HttpResponseNotFound(f"Нет такого университета с id={id}")


def delete_student(request, id):
    try:
        res = models.Student.objects.get(id=id)
        res.delete()
        return HttpResponseRedirect("/app/student")
    except models.Student.DoesNotExist:
        return HttpResponseNotFound(f"Нет такого студента с id={id}")