from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def announcements_list(request):
    announcements = [
        {'id': 1, 'title': 'Announcement 1'},
        {'id': 2, 'title': 'Announcement 2'},
        {'id': 3, 'title': 'Announcement 3'},
    ]
    return render(request, 'announcements_list.html', {'announcements': announcements})

def announcement_detail(request, id):
    announcements = {
        1: {'title': 'Announcement 1', 'content': 'This is the full content of Announcement. It contains detailed information about the topic, including key points, examples, and additional insights.'},
        2: {'title': 'Announcement 2', 'content': 'This is the full content of Announcement. It provides an in-depth explanation of the subject matter, with supporting evidence and further elaboration.'},
        3: {'title': 'Announcement 3', 'content': 'This is the full content of Announcement. It highlights important aspects of the topic, offering a comprehensive overview and additional context.'},
    }
    announcement = announcements.get(id, {'title': 'Not Found', 'content': 'No details available.'})
    return render(request, 'announcement_detail.html', {'announcement': announcement})