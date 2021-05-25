from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from rest_framework import viewsets
from .serializers import MemSerializer
from .forms import MemCreateForm
from .models import Mem

class MemViewSet(viewsets.ModelViewSet):
    queryset = Mem.objects.all().order_by('id')
    serializer_class = MemSerializer

@login_required
def mem_create(request):
    if request.method == 'POST':
        form = MemCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Mem added successfully')

            #return redirect(new_item.get_absolute_url())
    else:
        form = MemCreateForm(data=request.GET)
    return render(request, 'mainboard/mem/create.html', {'section': 'mems', 'form': form})

def post_list(request):
    posts = Mem.objects.all()
    return render(request, 'mainboard/post/list.html', {'mems': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Mem,  slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,'mainboard/post/detailed.html', {'mem': post})