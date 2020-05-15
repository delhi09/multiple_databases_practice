from django.contrib.auth.models import User
from django.http import HttpResponse


def index(request):
    user1 = User(username="fizz")
    user1.set_password("password")
    user1.save()

    user2 = User(username="buzz")
    user2.set_password("password")
    user2.save(using="dbserver2")
    return HttpResponse("Hello, world. You're at the polls index.")
