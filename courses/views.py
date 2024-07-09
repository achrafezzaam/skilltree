from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from .models import Detail, Message, Question
from .forms import DetailForm, CommentForm, QuestionForm, ChoiceForm


@login_required
def index(request):
    courses = Detail.objects.all()
    paginator = Paginator(courses, 5)
    page_num = request.GET.get("page")
    courses_list = paginator.get_page(page_num)
    context = {"courses_list": courses_list}
    return render(request, "courses/index.html", context)


@login_required
@permission_required('courses.create_courses', raise_exception=True)
def admin_dashboard(request):
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            course = Detail(**form.cleaned_data)
            course.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        form = DetailForm()
    context = {
            "form": form,
            }
    return render(request, "courses/admin_dashboard.html", context)


@login_required
def detail_view(request, course_id):
    course = get_object_or_404(Detail, pk=course_id)
    comments = Message.objects.filter(course=course)
    comments_paginator = Paginator(comments, 5)
    comments_page_num = request.GET.get("comments_page")
    comments_list = comments_paginator.get_page(comments_page_num)
    questions = Question.objects.filter(course=course)
    questions_paginator = Paginator(questions, 5)
    questions_page_num = request.GET.get("questions_page")
    questions_list = questions_paginator.get_page(questions_page_num)
    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            commentform = CommentForm(request.POST)
            if commentform.is_valid():
                message = Message(
                        author=User.objects.get(pk=request.user.id),
                        course=course,
                        **commentform.cleaned_data,
                        )
                message.save()
        elif request.user.groups.all()[0].name == 'site-admin' and\
        'question_submit' in request.POST:
            questionform = QuestionForm(request.POST)
            if questionform.is_valid():
                new_question = Question(
                        course=course,
                        **questionform.cleaned_data,
                        )
                new_question.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        commentform = CommentForm()
        questionform = QuestionForm()
    return render(
            request,
            "courses/detail.html",
            {
                "course": course,
                "commentform": commentform,
                "questionform": questionform,
                "comments_list": comments_list,
                "questions_list": questions_list,
            })


@login_required
@permission_required('courses.create_questions', raise_exception=True)
def question_view(request, question_id):
    return render(request, "courses/question.html")


@login_required
def vote(request, course_id):
    return HttpResponse("You're voting on the course {}.".format(course_id))
