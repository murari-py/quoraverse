from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseRedirect


class QuestionListCreateView(ListView):
    """
    Displays a paginated list of all questions and allows authenticated users to post new questions.

    - Uses `ListView` to show questions ordered by creation date (latest first).
    - Renders the `QuestionForm` in the same view for posting new questions.
    - Supports both GET (listing) and POST (creating a new question) methods.
    """
    model = Question
    template_name = 'questions/question_list.html'
    context_object_name = 'questions'
    ordering = ['-created_at']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """
        Adds the question creation form to the context for rendering in the template.
        """
        context = super().get_context_data(**kwargs)
        context['form'] = QuestionForm()
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST request to create a new question.
        Associates the question with the logged-in user and redirects to the list view.
        """
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('question_list')
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


class QuestionDetailView(DetailView):
    """
    Displays the details of a single question along with its answers.
    Also provides a form for authenticated users to post an answer.
    """
    model = Question
    template_name = 'questions/question_detail.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        """
        Adds the answer form to the context so users can submit answers on the detail page.
        """
        context = super().get_context_data(**kwargs)
        context['answer_form'] = AnswerForm()
        return context


@login_required
def post_answer(request, pk):
    """
    Handles posting a new answer to a question.

    Requires login. Validates and saves the answer, linking it to the appropriate question and user.
    Redirects to the question's detail page after submission.
    """
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('question_detail', pk=question.pk)


@login_required
def like_answer(request, pk):
    """
    Toggles a like/unlike action for a specific answer.

    - If the user has already liked the answer, their like is removed.
    - Otherwise, a like is added.
    Redirects back to the referring page.
    """
    answer = get_object_or_404(Answer, pk=pk)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
