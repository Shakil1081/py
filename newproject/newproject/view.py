from django.shortcuts import render

def student(request):
   return render(request, 'student.html')
   
def addstudent(request):
    return render(request,'addstudent.html')
def reagistation(request):
    return render(request,'reagistation.html')