from django.shortcuts import render

from django.shortcuts import render

def detail(request):
	context = { 
	"my_food_blog":[
{
	"item": "Mozerella Pizza",
	"item_discription": "This mozerella pizza is delicious. Try this mozeralla pizza tonight!",
	"created": "2017-08-12",
	"updated": "2017-08-12",
	},

	{
	"item": "Lasgña",
	"item_discription": "This mozerella pizza is delicious. Try this mozeralla pizza tonight!",
	"created": "2017-08-12",
	"updated": "2017-08-12",
	},

{
	"item": "Turkey Sandiwch",
	"item_discription": "This mozerella pizza is delicious. Try this mozeralla pizza tonight!",
	"created": "2017-08-12",
	"updated": "2017-08-12",
	},
{
	"item": "French Fries w/Cheese",
	"item_discription": "This mozerella pizza is delicious. Try this mozeralla pizza tonight!",
	"created": "2017-08-12",
	"updated": "2017-08-12",
	},

	],

	}

	return render(request,'Menu.html', context)
# Create your views here.
