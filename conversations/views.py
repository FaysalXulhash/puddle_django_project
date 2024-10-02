from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ConversationMessageForm
from item.models import Item
from .models import Conversations


@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('home')
    conversation = Conversations.objects.filter(item=item).filter(members__in = [request.user.id])

    if conversation:
        return redirect('detail',pk = conversation.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversations.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit = False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect ('item-detail', pk=item_pk)
    else:
        form = ConversationMessageForm()
    
    return render(request, 'conversations/new_message.html', {'form': form})

#inbox page
@login_required
def inbox(request):
    conversations = Conversations.objects.filter(members__in = [request.user.id])

    return render (request, 'conversations/inbox.html', {'conversations': conversations})

#message details
@login_required
def detail(request, pk):
    conversation = Conversations.objects.filter(members__in = [request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit = False)
            conversation_message.conversation =conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            conversation.save()

            return redirect('detail', pk=pk)
    else:
        form = ConversationMessageForm()


    return render(request, 'conversations/detail.html', {'conversation': conversation, 'form': form})
