from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples = [
        {'name':'Aabhash Basnet','age':16},
        {'name':'Ram Sharma','age': 22},
        {'name':'Avhijeet Gupta','age': 32},
        {'name':'Ravi Prasad','age': 52},
        {'name': 'Sam Parsad','age': 62},
    ]
    for people in peoples:
        if people['age'] > 10 :
            print("Yes")
    text = """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut expedita quos
    libero earum soluta nam dignissimos! Voluptate beatae aliquam ea illo nihil
    modi eum deserunt est, sunt rerum veritatis laborum ullam fugiat eveniet
    numquam labore id dolore quaerat officiis et eaque magni dignissimos
    perspiciatis. Voluptas ipsam pariatur facilis sunt, suscipit voluptates
    totam distinctio dignissimos repellat neque architecto ipsum beatae
    accusantium ratione cumque eaque eos iusto maxime quod aperiam, hic
    voluptate. Itaque temporibus quae doloremque veritatis velit mollitia nobis
    ipsa ad voluptatum alias nihil repellendus eos deserunt illo, consequatur
    quaerat obcaecati aliquam at eveniet et numquam quo quam repudiandae.
    Laudantium, porro.    
        """
    
    vegetables = ['Pumpkin','Tomato','Potato']

    return render(request, "home/index.html",context={'peoples':peoples,'text':text,'vegetables':vegetables,'Page':'Django 2023'})

def success_page(request):
    print("*" *10)
    return HttpResponse("<h1>Hey This is a Success Page</h1>")
def about(request):
    context = {'Page':'About'}
    return render(request,"home/about.html",context)
def contact(request):
    context = {'Page':'Contact'}
    return render(request,"home/contact.html",context)