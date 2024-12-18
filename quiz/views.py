from django.http import JsonResponse, HttpResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt


import random
from django.http import JsonResponse, HttpResponse
from .models import Question

def get_random_quiz(request):
    try:
        questionObjs = Question.objects.filter(attempted=False)

        if not questionObjs.exists():
            return JsonResponse({"detail": "No questions available."}, status=404) 

        random_question = random.choice(questionObjs)

        optionsObjs = random_question.get_options()

        data = {
            "uid": str(random_question.uid),
            "question": random_question.question,
            "marks": random_question.marks,
            "options": optionsObjs
        }

        return JsonResponse(data, status=200)
    
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong", status=500)

@csrf_exempt
def submit_answer(request):
    if request.method == 'POST':
        try:
            
            data = json.loads(request.body)
            question_id = data.get('question_id')
            selected_option_text = data.get('option')

            
            question = Question.objects.filter(uid=question_id).first()
            if not question:
                return JsonResponse({'error': 'Question not found'}, status=404)

            
            selected_option = Option.objects.filter(question=question, option=selected_option_text).first()
            if not selected_option:
                return JsonResponse({'error': 'Selected option not valid'}, status=400)

            
            correct_option = Option.objects.filter(question=question, is_correct=True).first()

            
            question.attempted = True
            question.save()

            
            Attempt.objects.create(
                question=question,
                given_answer=selected_option,
                is_correct=(selected_option == correct_option)
            )

            return JsonResponse({
                'message': 'Question marked as attempted and attempt recorded',
                'is_correct': selected_option == correct_option
            }, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'error': 'Something went wrong'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_attempted_questions(request):

    questions = Question.objects.filter(attempted=True)

    response_data = []

    for question in questions:

        correct_option = Option.objects.filter(question=question, is_correct=True).first()

        attempts = Attempt.objects.filter(question=question)

        given_answers = [
            {
                'given_answer': attempt.given_answer.option if attempt.given_answer else None,
                'is_correct': attempt.is_correct,
            }
            for attempt in attempts
        ]

        response_data.append({
            'question_id': question.uid,
            'question_text': question.question,
            'marks': question.marks,
            'correct_option': correct_option.option if correct_option else None,
            'given_answers': given_answers,
        })

    return JsonResponse({'questions': response_data}, safe=False)
