from django.shortcuts import render, get_object_or_404,redirect
from .models import Item,Category #ditambahkan category ketika sudah membuat menu search
# Tambahkan ini untuk membuat decorator bahwa setiap proses akan membutuhkan login terlebih dahulu
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm,EditItemForm
#tambahan untuk membuat search
from django.db.models import Q #(question)
#untuk membuat menu search 
def items(request):
    #tambahan ketika sudah membuat search bar terlebih dahulu
    query=request.GET.get('query','')
    #lihat baris 20
    category_id=request.GET.get('category',0)
    #untuk membawa nilai dari category
    categories=Category.objects.all()
    #ini defaultnya ditampilin semua lebih dahulu
    items=Item.objects.filter(is_sold=False)
    
    if category_id:
        items=items.filter(Category_id=category_id)
    #baru masuk query pencarian
    if query:
        items=items.filter(Q(name__icontains=query)|Q(description=query))
    context={
        "items":items,
        "query":query,
        "categories":categories,
        "category_id":int(category_id),
    }
    return render(request,'item/items.html', context)

# Create your views here.
#halaman detail
def detail(request,pk):
    item = get_object_or_404(Item, pk=pk)
    #untuk filter untuk yang memiliki category yang sama
    related_items= Item.objects.filter(Category=item.Category,is_sold=False).exclude(pk=pk)[0:3]

    context={
        "item":item,
        "related_items":related_items
    }
    return render(request, 'item/detail.html',context)

# ini untuk menambahkan item
@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST,request.FILES)
        if form.is_valid:
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()

            return redirect('item:detail',pk=item.id)
    else:
        form = NewItemForm()
    
    context={
        "form":form,
        "title":'New Item',
    }

    return render(request,'item/form.html',context)

#untuk menghapus item
@login_required
def delete(request, pk):
    item = get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

#untuk mengedit item
@login_required
def edit(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid:
            form.save()
            return redirect('item:detail',pk=item.id)
    else:
        form = EditItemForm(instance=item)
    
    context={
        "form":form,
        "title":'Edit Item ',
    }

    return render(request,'item/form.html',context)