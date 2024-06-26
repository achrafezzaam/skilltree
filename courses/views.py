from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Detail


def index(request):
    courses_list = Detail.objects.all()[:5]
    context = {"courses_list": courses_list}
    return render(request, "courses/index.html", context)

def detail(request, course_id):
    course = get_object_or_404(Detail, pk=course_id)
    return render(request, "courses/detail.html", { "course": course })

def vote(request, course_id):
    return HttpResponse("You're voting on the course {}.".format(course_id))
