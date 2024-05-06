from django.shortcuts import render
from django.http import HttpResponse

def form(request):
     data = {"heading1": "Mini Project", "heading2": "Enter a Number"}
     return render(request, "getinput.html", data)


def findTheNumber(request):
     givenNumber = int(request.GET.get("value1"))
     userChoice = request.GET.get("choice")
     if userChoice == 'armstrong':
          output = findArmstrong(givenNumber)
     elif userChoice == 'prime':
          output = findPrime(givenNumber)
     return HttpResponse(output)

def findArmstrong(number):
     sum = 0
     temp = number
     while temp > 0:
          digit = temp % 10
          sum += digit ** 3
          temp //= 10
          if number == sum:
               print(number, " is an Armstrong number")
               result = number, " is an Armstrong number"
          else:
               print(number, " is not an Armstrong number")
               result = number, " is not an Armstrong number"
          return result
def findPrime(number):
     flag = False
     if number == 1: print(number, " is not a prime number")
     elif number > 1:
          for i in range(2, number):
               if (number % i) == 0:
                    flag = True
                    break
               if flag:
                    print(number, " is not a prime number")
                    result = number, " is not a prime number"
               else:
                    print(number, " is a prime number")
                    result = number, " is a prime number"
     return result