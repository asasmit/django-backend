from django.db import models
import uuid
import random

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True

class Question(BaseModel):
    question = models.TextField()
    marks = models.IntegerField(default=4)
    attempted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.question

    def get_options(self, include_correct=False):
        option_objs = list(Option.objects.filter(question=self))
        random.shuffle(option_objs)

        data = []
        for option_obj in option_objs:
            option_data = {'option': option_obj.option}
            if include_correct:
                option_data['is_correct'] = option_obj.is_correct
            data.append(option_data)

        return data

class Option(BaseModel):
    option = models.CharField(max_length=250)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.option} (Correct: {self.is_correct})"
    
class Attempt(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    given_answer = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True, blank=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Question: {self.question.question} | Given Answer: {self.given_answer.option if self.given_answer else 'None'}"

    def save(self, *args, **kwargs):
        
        if self.given_answer:
            self.is_correct = self.given_answer.is_correct
        super().save(*args, **kwargs)