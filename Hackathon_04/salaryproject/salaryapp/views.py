from django.shortcuts import render
import random

def salary_form(request):
    return render(request, 'salary_form.html')

def salary_result(request):
    if request.method == 'POST':
        name = request.POST['name']
        gross = float(request.POST['gross'])
        tax = float(request.POST['tax'])
        bonus = float(request.POST['bonus'])

        net = gross + (bonus / 100 * gross) - (tax / 100 * gross)
        return render(request, 'salary_result.html', {'name':name, 'net': net})
    return render(request, 'salary_form.html')

def jumble_word(request):
    word = request.GET.get('word', '')
    jumbled = ''.join(random.sample(word, len(word))) if word else ''
    return render(request, 'jumble.html', {'word': word, 'jumbled': jumbled})
