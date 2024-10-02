from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message
from django.shortcuts import get_object_or_404

@login_required
def outbox(request):
    messages = Message.objects.filter(sender=request.user)
    return render(request, 'messaging_app/outbox.html', {'messages': messages})

# Vista para mensajería
@login_required
def inbox(request):
    received_messages = Message.objects.filter(receiver=request.user)
    return render(request, 'messaging_app/inbox.html', {'received_messages': received_messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'messaging_app/send_message.html', {'form': form})

@login_required
def view_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.user != message.receiver:
        return redirect('inbox')
    return render(request, 'messaging_app/view_message.html', {'message': message})
@login_required
def delete_message(request, pk):
    message = get_object_or_404(Message, pk=pk, receiver=request.user)
    if request.method == 'POST':
        message.delete()
        return redirect('inbox')
    return render(request, 'messaging_app/delete_message_confirm.html', {'message': message})