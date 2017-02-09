from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, Http404,redirect
from django.db.models import Q
from .forms import EventForm
from .models import Event



'''def d_popup(request,event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request,'mycalender/event_detail.html', {'event': event})'''
    
def event_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404 
        
    form = EventForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        context = {
        'form': form,
        }
        return redirect("mycalender:index")

def event_update(request, slug=None):
    instance = get_object_or_404(Event, slug=slug)
    form = EventForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Event</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
    }
    return render(request, "event_form.html", context)



def event_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Event, slug=slug)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("mycalender:index")

def index(request):
    form = EventForm()
    event = Event.objects.all()
    return render(request, 'mycalender/base.html',{'event': event,'form': form})

