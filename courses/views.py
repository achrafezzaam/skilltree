from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .models import Detail, Message
from .forms import CommentForm


def index(request):
    courses_list = Detail.objects.all()[:5]
    context = {"courses_list": courses_list}
    return render(request, "courses/index.html", context)

def detail(request, course_id):
    course = get_object_or_404(Detail, pk=course_id)
    comments_list = Message.objects.filter(
            course=Detail.objects.get(pk=course_id)
            )
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            message = Message(
                    author=User.objects.get(pk=request.user.id),
                    course=Detail.objects.get(pk=course_id),
                    **form.cleaned_data
                    )
            message.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = CommentForm()
    return render(
            request,
            "courses/detail.html",
            {
                "course": course,
                "form": form,
                "comments_list": comments_list,
            })

def vote(request, course_id):
    return HttpResponse("You're voting on the course {}.".format(course_id))
