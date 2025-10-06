from django.shortcuts import render, redirect
from .form import DiaryForm
from .models import Diary

def home_page(request):
    return render(request, 'diary_html/home.html')

def createDiary(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewDiary')
    else:
        form = DiaryForm()
    return render(request, 'diary_html/creatediary.html', {'form': form})

def deleteDiary(request, id):
    diary = Diary.objects.get(id=id)
    if request.method == 'POST':
        diary.delete()
        return redirect('viewDiary')
    return render(request, 'diary_html/deletediary.html', {'id': id})

def updateDiary(request, id):
    diary = Diary.objects.get(id=id)
    if request.method == 'POST':
        form = DiaryForm(request.POST, instance=diary)
        if form.is_valid():
            form.save()
            return redirect('viewDiary')
    else:
        form = DiaryForm(instance=diary)
    return render(request, 'diary_html/updatediary.html', {'id': id, 'form': form})

def viewDiary(request):
    diary = Diary.objects.all()
    return render(request, 'diary_html/viewdiary.html', {'diary': diary})