from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    data = {
        'title': 'Home Page',
        'name': 'Worachai Khamnuan',
        'content': 'My Portfolio',
        'image': 'https://cdn.pixabay.com/photo/2016/11/21/06/53/beautiful-natural-image-1844362_1280.jpg',
        'programming_skills': ['Python', 'Django', 'Web Development', 'JavaScript', 'HTML', 'CSS'],
        'Embedded_Skills': ['C', 'C++', 'Arduino', 'Raspberry Pi'],
        'certifications': [
            {'date': '14-15 March 2026', 'photo': '/static/profiles/images/show1.png', 'detail': 'This is to certify that Worachai Khamnuan has successfully completed Embedded System Bootcamp', 'from': 'DevCommu x CEDT'},
            {'date': '14-15 March 2026', 'photo': '/static/profiles/images/show2.png', 'detail': 'This is to certify that Worachai Khamnuan has successfully completed their project in Embedded System Bootcamp', 'from': 'DevCommu x CEDT'},
        ],
    }
    return render(request, 'home.html', data)

# Create your views here.
