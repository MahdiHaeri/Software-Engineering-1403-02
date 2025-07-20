
from django.shortcuts import render
from group1.models import Question

def home(request):
    return render(request, 'group1.html', {'group_number': '1'})

def grammar_quiz_question(request):
    question = Question.objects.filter(type='GRAMMAR').first()

    if not question:
        return render(request, 'grammar_quiz_question.html', {'error': 'No grammar questions available.'})

    choices = question.choices.all()
    correct_choice = choices.filter(is_correct=True).first()

    context = {
        'question': {
            'id': question.id,
            'text_or_prompt': question.text_or_prompt
        },
        'choices': choices,
        'current_index': 1,
        'total_questions': 10,
        'quiz_progress': 10,
        'correct_choice': correct_choice,
<<<<<<< HEAD
        'next_url': '#',  # Placeholder for next question
        'quiz_title': 'Grammar Quiz',
    }
    return render(request, 'grammar_quiz_question.html', context)

def vocabulary_quiz_question(request):
    context = {
        'quiz_title': 'Vocabulary Quiz',
        'current_index': 1,
        'total_questions': 5,
        'quiz_progress': 20,
    }
    return render(request, 'vocabulary_quiz_question.html', context)

def image_quiz_question(request):
    context = {
        'quiz_title': 'Image Quiz',
        'current_index': 2,
        'total_questions': 5,
        'quiz_progress': 40,
    }
    return render(request, 'image_quiz_question.html', context)

def writing_quiz_question(request):
    context = {
        'quiz_title': 'Writing Quiz',
        'current_index': 3,
        'total_questions': 5,
        'quiz_progress': 60,
    }
    return render(request, 'writing_quiz_question.html', context)

def sentence_building_question(request):
    context = {
        'quiz_title': 'Sentence Building',
        'current_index': 4,
        'total_questions': 5,
        'quiz_progress': 80,
    }
    return render(request, 'sentence_building_question.html', context)

def listening_quiz_question(request):
    context = {
        'quiz_title': 'Listening Quiz',
        'current_index': 5,
        'total_questions': 5,
        'quiz_progress': 100,
    }
    return render(request, 'listening_quiz_question.html', context)

=======
    }

    return render(request, 'grammar_quiz_question.html', context)
>>>>>>> a695494 (connecting to database)
