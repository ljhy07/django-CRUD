from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from .models import Student
from exprj.urls import *

class view():
    def home(request):
        students = Student.objects.all()
        return render(request, '../templates/index.html', {'students': students})


    # 생성
    def create_student(request):
        if request.method == 'POST':
            stdNum = request.POST.get('stdNum')
            name = request.POST.get('name')
            major = request.POST.get('major')

            if stdNum and name and major:
                student = Student(stdNum=stdNum, name=name, major=major)
                student.save()
                return redirect('home')
        
        return render(request, '../templates/create.html')


    # 읽기
    def read_student(request):
        if request.method == 'POST':
            stdNum = request.POST.get('stdNum')
            try:
                student = Student.objects.get(stdNum=stdNum)
                return render(request, '../templates/read.html', {'student': student})
            except ObjectDoesNotExist:
                # 학생을 찾을 수 없는 경우 예외 처리
                return render(request, '../templates/error.html')
            except ValueError:
                # ValueError 예외 처리
                return render(request, '../templates/error.html')


    def input_read(request):
        return render(request, '../templates/input_read.html')


    # 수정
    def update_student(request):
        if request.method == 'POST':
            stdNum = request.POST.get('stdNum')

            try:
                student = Student.objects.get(stdNum=stdNum)
                
                student.stdNum = request.POST.get('stdNum')
                student.name = request.POST.get('name')
                student.major = request.POST.get('major')
                student.save()
                return redirect('home')
            except ObjectDoesNotExist:
                return render(request, '../templates/error.html')
            except ValueError:
                # ValueError 예외 처리
                return render(request, '../templates/error.html')
        
        return render(request, '../templates/update.html')

    def input_update(request):
        return render(request, '../templates/input_update.html')


    # 삭제
    def delete_student(request):
        stdNum = request.GET.get('stdNum')
        

        try:
            if request.method == 'POST':
                student = Student.objects.get(stdNum=stdNum)
                student.delete()
                return redirect('home')
        except ObjectDoesNotExist:
            return render(request, '../templates/error.html')
        except ValueError:
            # ValueError 예외 처리
            return render(request, '../templates/error.html')
        
        return render(request, '../templates/delete.html', {'student' : student})

    def input_delete(request):
        return render(request, '../templates/input_delete.html')