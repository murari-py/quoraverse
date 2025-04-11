from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """
    Represents a question posted by a user.

    Fields:
        - title (CharField): The title of the question.
        - body (TextField): The detailed description or content of the question.
        - author (ForeignKey): The user who asked the question.
        - created_at (DateTimeField): Timestamp when the question was created.
    """
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    """
    Represents an answer to a specific question, posted by a user.

    Fields:
        - question (ForeignKey): The question that this answer is associated with.
        - body (TextField): The content of the answer.
        - author (ForeignKey): The user who provided the answer.
        - created_at (DateTimeField): Timestamp when the answer was created.
        - likes (ManyToManyField): Users who liked this answer.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_answers', blank=True)

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f'Answer to "{self.question.title}" by {self.author.username}'
