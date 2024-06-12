from django.shortcuts import render


def index(request):

    return render(request, 'index.html', {'title': 'Main manu', 
                                         'content_title': 'NONAME restaurant', 
                                         })
    
def statistics(request):
    return render(request, "statistics.html", {'title': 'Statistics', 
                                         'content_title': 'Statistics', 
                                         })

def menu(request):
    return render(request, "menu.html", {'title': 'Menu', 
                                         'content_title': 'Menu', 
                                         })
    

