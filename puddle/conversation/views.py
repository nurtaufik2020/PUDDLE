from django.shortcuts import render,get_object_or_404,redirect

from item.models import Item
from .forms import ConversationMessageForm
from .models import Conversation
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def new_conversation(request,item_pk):
    item=  get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', pk=conversation.first().id)
        #pass #redirect to conversation

    if request.method == 'POST':
        form= ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation=Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message= form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail',pk=item_pk)
    else:
        form=ConversationMessageForm()

    return render(request,'conversation/new.html',{
        'form':form
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    context={
        "conversations":conversations
    }
    return render(request,'conversation/inbox.html',context)

@login_required
def detail(request,pk):
    conversations = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
   
    if request.method =="POST":
        form=ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message=form.save(commit=False)
            conversation_message.conversation= conversations
            conversation_message.created_by=request.user
            conversation_message.save()

            conversations.save()
            return redirect("conversation:detail",pk=pk)
    else:
        form=ConversationMessageForm()

    context={
        "conversations":conversations,
        "form":form,
    }
    return render(request,"conversation/detail.html",context)