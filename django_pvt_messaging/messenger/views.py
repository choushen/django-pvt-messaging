from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from .models import Message, Notification, Connection


# Create your views here.
@login_required
def inbox(request):
    connections = Connection.objects.filter(user1=request.user) | Connection.objects.filter(user2=request.user)
    users = set()
    for connection in connections:
        if connection.user1 == request.user:
            users.add(connection.user2)
        else:
            users.add(connection.user1)
    
    unread_counts = {user.id: 0 for user in users}
    for message in Message.objects.filter(receiver=request.user, read=False):
        if message.sender.id in unread_counts:
            unread_counts[message.sender.id] += 1

    # Convert unread_counts to a list of tuples for easier template handling
    unread_counts_list = [(CustomUser.objects.get(id=user_id), count) for user_id, count in unread_counts.items()]

    context = {'users': users, 'unread_counts_list': unread_counts_list}
    return render(request, 'messenger/inbox.html', context)



@login_required
def chat(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    # Get all messages between the current user and the user with the given id
    if not Connection.objects.filter(user1=request.user, user2=user).exists() and not Connection.objects.filter(user1=user, user2=request.user).exists():
        return redirect('inbox')
    # Get all messages between the current user and the user with the given id
    messages = Message.objects.filter(sender=request.user, receiver=user) | Message.objects.filter(sender=user, receiver=request.user)
    # Order the messages by timestamp
    messages = messages.order_by('timestamp')
    for message in messages.filter(receiver=request.user):
        message.read = True
        message.save()
    context = {'messages': messages, 'user': user}
    return render(request, 'messenger/chat.html', context)


@login_required
def send_message(request, user_id):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=user_id)
        if not Connection.objects.filter(user1=request.user, user2=user).exists() and not Connection.objects.filter(user1=user, user2=request.user).exists():
            return redirect('inbox')
        content = request.POST.get('content')
        message = Message.objects.create(sender=request.user, receiver=user, content=content)
        Notification.objects.create(user=user, message=message)
        return redirect('chat', user_id=user.id)
    return redirect('inbox')


@login_required
def fetch_notifications(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    data = {
        'count': notifications.count(),
        'notifications': [
            {'message': f'New message from {n.message.sender.email}', 'url': f'chat/{n.message.sender.id}/'}
            for n in notifications
        ]
    }
    return JsonResponse(data)