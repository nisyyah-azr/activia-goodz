from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406495823',
        'name': 'Nisyyah Azzahra',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)