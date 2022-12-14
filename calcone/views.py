from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def cal(request):
    return render(request,"index.html")


def calculate(request):

    
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    val3 = int(request.POST['num3'])
    val4 = val2 / (12*100)
    EMI= (val1 * val4) * (1+val4)**val3 / ((1+val4)**val3 - 1)


    return render(request, "index.html",{'emi':EMI})