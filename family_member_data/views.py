from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Participant


def index(request):
    return render(request, 'family_member_data/index.html')


def participants(request):
    participant_list = Participant.objects.all()
    context = {
        'participant_list': participant_list,
    }
    return render(request, 'family_member_data/participants.html', context)


def participant_details(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    context = {
        'participant': participant,
        'participant_id': participant_id,
    }
    return render(request, 'family_member_data/participant_detail.html', context)
