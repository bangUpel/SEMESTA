from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from voting.models import Candidate
from .models import Voter
# Create your views here.

def vote_request(request):
    if request.method == "POST":
        NIK = request.POST["NIK"]
        candidate_id = request.POST["candidate"]
        nik_list = Voter.objects.values_list("NIK", flat=True)
        if NIK not in nik_list or Voter.objects.get(NIK=NIK).voted == True:
            return render(request, "users/vote.html", {
                "context": "Masukkan nilai yang valid.",
                "candidates": Candidate.objects.all(),
                "voters": Voter.objects.filter(voted=True)
            })
        voter = Voter.objects.get(NIK=NIK)
        voted_candidate = Candidate.objects.get(id=candidate_id)
        voted_candidate.total_point += 1
        voter.voted = True
        voter.save()
        voted_candidate.save()
        return HttpResponseRedirect(reverse("vote"))
    return render(request, "users/vote.html", {
        "candidates": Candidate.objects.all(),
        "voters": Voter.objects.filter(voted=True)
        })


