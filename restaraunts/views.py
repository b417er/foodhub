from django.shortcuts import render
from .models import Restaraunt
def list(request):
	context = { 
	"my_food_blog": Restaraunt.objects.all(),

	}

	return render(request,'list.html', context)

def restaraunt_detail(request,restaraunt_id):
	context = {
	"restaraunt": Restaraunt.objects.get(id=restaraunt_id),
	

	}


	return render(request, 'detail.html', context)
# Create your views here.
