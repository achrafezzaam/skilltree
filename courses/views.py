from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from .models import Detail, Message, Question
from .forms import DetailForm, CommentForm, QuestionForm, ChoiceForm


@login_required
def index(request):
    courses_list = Detail.objects.all()
    context = {"courses_list": courses_list}
    return render(request, "courses/index.html", context)


@login_required
@permission_required('courses.create_courses', raise_exception=True)
def admin_dashboard(request):
    courses_list = Detail.objects.all()
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            course = Detail(**form.cleaned_data)
            course.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        form = DetailForm()
    context = {
            "courses_list": courses_list,
            "form": form,
            }
    return render(request, "courses/admin_dashboard.html", context)


@login_required
def detail_view(request, course_id):
    course = get_object_or_404(Detail, pk=course_id)
    comments_list = Message.objects.filter(course=course)
    questions_list = Question.objects.filter(course=course)
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
