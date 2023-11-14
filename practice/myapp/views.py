from django.http import HttpResponse

def first(request):
    return HttpResponse('This statement here '
                        'is coming from the app '
                        'Nonetheless written by Masino')

