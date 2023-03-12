#----------------------- tambahan setelah membuat app dashboard yaitu import models dan login
from django.contrib.auth.decorators import login_required
from item.models import Item
#-----------------------
from django.shortcuts import render,get_object_or_404

# Create your views here.
@login_required
def index(request):
    items= Item.objects.filter(created_by=request.user)

    context={
        "items":items,
    }
    return render(request,'dashboard/index.html',context)


