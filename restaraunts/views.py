from django.shortcuts import render
from .models import Restaraunt
from .forms import RestarauntForm
from django.shortcuts import redirect


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

def create(request):
	form = RestarauntForm()
	if request.method == "POST":
		form = RestarauntForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect ("list")

	context = {
		"create_form": form,
	}

	return render(request,'restaraunt_create.html', context)

def update(request, restaraunt_id):
	restaraunt_obj = Restaraunt.objects.get(id=restaraunt_id)
	form = RestarauntForm(instance = restaraunt_obj)
	if request.method == "POST":
		form = RestarauntForm(request.POST, instance = restaraunt_obj)
		if form.is_valid():
			form.save()
			return redirect ("list")

	context = {
		"restaraunt_obj": restaraunt_obj,
		"update_form": form,
	}

	return render(request,'restaraunt_update.html', context)

def restaraunt_delete(request, restaraunt_id):
	Restaraunt.objects.get(id=restaraunt_id).delete()
	return redirect("list")

# Create your views here.
