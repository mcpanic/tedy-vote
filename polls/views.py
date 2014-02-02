# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Choice, Poll, Voter
from django.db import IntegrityError

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    try:
        if 'vote_subscribe_check' in request.POST.keys():
            subscribe_check = True
        else:
            subscribe_check = False
        print subscribe_check
        print request.POST['voter_email']
        print p, selected_choice
        new_voter = Voter(poll=p, 
                    choice=selected_choice, 
                    email=request.POST['voter_email'], 
                    subscription=subscribe_check)
        print vars(new_voter)
        new_voter.save()
    except Exception as err:
        print err.message, type(err)

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    #return HttpResponseRedirect(reverse('results', args=(p.id,)))
    return render(request, 'polls/results.html', {'poll': p})

def add_choice(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        new_choice = Choice(    poll = p,
                choice_text = request.POST['choice_text'],
                choice_desc = request.POST['choice_desc'],
                proposer = request.POST['proposer'],
                votes = 1
               );
        new_choice.save()
    except IntegrityError:
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_propose_message': request.POST['choice_text'] + u": 이미 존재하는 이름입니다.",
        })

    try:
        if 'suggest_subscribe_check' in request.POST.keys():
            subscribe_check = True
        else:
            subscribe_check = False
        new_voter = Voter(poll=p, 
                    choice=new_choice, 
                    email=request.POST['proposer'], 
                    subscription=subscribe_check)
        new_voter.save()
    except:
        print "some error"

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    #return HttpResponseRedirect(reverse('results', args=(p.id,)))
    return render(request, 'polls/results.html', {'poll': p})
