from django.shortcuts import render

def crud(request):
    if request.method == 'POST':
        data = request.POST
        word = data['word']
        print(word)
    return render(request, 'templates/index.html')

def employe(request):
    
    return render(request, 'templates/employe/employe.html')    