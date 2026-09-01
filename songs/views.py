from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def song_list(requests):
    return HttpResponse("List of Songs is diplayed here")

def songsDetail(request,id):
    response_text = f'Songs detail: {id} from ip: {request.META.get} + id'
    return HttpResponse(response_text)
