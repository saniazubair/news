from .models import *


def category(request):
    category = Category.objects.all()
    context = {'category': category}
    return context