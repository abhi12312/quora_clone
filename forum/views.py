from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, TemplateView, View, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Question, Answer
from .forms import AnswerForm

# User registration
class RegisterView(FormView):
    template_name = 'forum/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('question_list')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)  # Log the user in after registration
        return super().form_valid(form)

# User login
class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('question_list')

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request  # AuthenticationForm requires request
        return kwargs

# User logout
class LogoutView(View):
    template_name = 'registration/logout.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect(reverse('logged_out'))

# Logged out confirmation
class LoggedOutView(TemplateView):
    template_name = 'registration/logged_out.html'

# List all questions
class QuestionListView(ListView):
    model = Question
    template_name = 'forum/question_list.html'
    context_object_name = 'questions'

# View question details and handle answer posting
class QuestionDetailView(View):
    template_name = 'forum/question_detail.html'

    def get(self, request, pk, *args, **kwargs):
        question = get_object_or_404(Question, pk=pk)
        form = AnswerForm()
        answers = question.answers.all()
        return render(request, self.template_name, {
            'question': question,
            'answers': answers,
            'form': form
        })

    def post(self, request, pk, *args, **kwargs):
        question = get_object_or_404(Question, pk=pk)
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.posted_by = request.user
            answer.save()
            return HttpResponseRedirect(reverse('question_detail', kwargs={'pk': pk}))
        answers = question.answers.all()
        return render(request, self.template_name, {
            'question': question,
            'answers': answers,
            'form': form
        })

# Post a new question
class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'text']
    template_name = 'forum/question_form.html'
    success_url = reverse_lazy('question_list')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

# Like an answer
class LikeAnswerView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        answer = get_object_or_404(Answer, pk=pk)
        if request.user not in answer.likes.all():
            answer.likes.add(request.user)
        return HttpResponseRedirect(reverse('question_detail', kwargs={'pk': answer.question.pk}))