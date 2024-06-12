from audioop import reverse
from select import select
from urllib import request, response
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from polls.models import Question
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ",".join([q.question_text for q in latest_question_list])
    context = {'latest_question_list': latest_question_list}
    # return HttpResponse(output)
    return render(request, 'polls/polls_index.html', context)
    
    
def detail(request, question_id):
    # return HttpResponse(f"You're looking at question {question_id}")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/polls_detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/polls_results.html", {"question": question})
    # return HttpResponse(f"You're looking at the results of question {question_id}")
    
# def vote(request, question_id):
#     return HttpResponse(f"You're votting on question {question_id}")

def vote(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(
            request, 
            'polls/polls_detail.html', 
            {
                'question': question,
                'error_message': "You didn't select a choice."
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id)))