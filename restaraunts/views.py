from django.shortcuts import render, redirect
from .models import Restaraunt, Item, FavouriteRestaraunt
from .forms import RestarauntForm, UserRegisterForm, LoginForm, ItemForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

def favourite_restaraunt(request, restaraunt_id):
	rest_obj = Restaraunt.objects.get(id=restaraunt_id)
	print("USER: ")
	print(request.user)
	fave_rest_obj, created = FavouriteRestaraunt.objects.get_or_create(user=request.user, restaraunt=rest_obj)

	if created:
		action="favourite"
	else:
		action="unfavourite"
		fave_rest_obj.delete()

	favourite_count = rest_obj.favouriterestaraunt_set.all().count()

	context = {
	"action":action,
	"count": favourite_count
	}

	return JsonResponse(context, safe=False)

def user_register(request):
	form = UserRegisterForm()
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			person = form.save(commit = False)
			person.set_password(person.password)
			person.save()
			login(request, person)
			return redirect ("list")

	context ={
	"form":form
	}

	return render(request, 'register.html', context)

def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            my_username = form.cleaned_data['username']
            my_password = form.cleaned_data['password']
            auth_user = authenticate(username=my_username, password=my_password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect ("list")

    context = {
        "form": form,
    }
    return render(request, 'user_login.html', context)

def user_logout(request):
    logout(request)
    return redirect('user_login')

def list(request):

	if (request.user.is_anonymous):
		return redirect("user_login")

	my_food_blog = Restaraunt.objects.all().order_by('name','description')

	query=request.GET.get('q')

	if query:
		my_food_blog= my_food_blog.filter(name__contains=query)

	favourited_restaraunts = []
	favourites = request.user.favouriterestaraunt_set.all()
	for favourite in favourites:
		favourited_restaraunts.append(favourite.restaraunt)

	context = {
	"restaraunts": my_food_blog,
	"my_favourites": favourited_restaraunts

	}

	return render(request,'list.html', context)

def restaraunt_detail(request,restaraunt_id):
	restaraunt_obj = Restaraunt.objects.get(id=restaraunt_id)
	items = Item.objects.filter(restaraunt=restaraunt_obj)

	context = {
	"restaraunt": restaraunt_obj,
	"items": items


	}

	return render(request, 'detail.html', context)

def create(request):
	if (request.user.is_annonymous):
		return redirect("user_login.html")
	form = RestarauntForm()
	if request.method == "POST":
		form = RestarauntForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect ("list")

	context = {
		"create_form": form,
	}

	return render(request,'restaraunt_create.html', context)

def create_item(request, restaraunt_id):
	restaraunt_obj = Restaraunt.objects.get(id=restaraunt_id)
	form = ItemForm()
	if request.method == "POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			item = form.save(commit = False)	
			item.restaraunt= restaraunt_obj	
			item.save()
			return redirect ("list")

	context = {
		"create_form": form,
		"restaraunt_obj": restaraunt_obj,
	}

	return render(request,'create_item.html', context)

def update(request, restaraunt_id):

	restaraunt = Restaraunt.objects.get(id=restaraunt_id)
	if not(request.user.is_staff or request.user == restaraunt.owner):
		
		return HttpResponse ("<h1>  No Response 404 </h1>")


	restaraunt_obj = Restaraunt.objects.get(id=restaraunt_id)
	form = RestarauntForm(instance = restaraunt_obj)
	if request.method == "POST":
		form = RestarauntForm(request.POST, request.FILES or None, instance = restaraunt_obj)
		if form.is_valid():
			form.save()
			return redirect ("list")

	context = {
		"restaraunt_obj": restaraunt_obj,
		"update_form": form,
	}

	return render(request,'restaraunt_update.html', context)

def restaraunt_delete(request, restaraunt_id):
	restaraunt = Restaraunt.objects.get(id=restaraunt_id)
	if not(request.user.is_staff):
		return HttpResponse ("<h1>  No Response 404 </h1>")


	Restaraunt.objects.get(id=restaraunt_id).delete()
	return redirect("list")


# Create your views here.
