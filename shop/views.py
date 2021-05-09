from django.shortcuts import render
from .models import product
from math import ceil
# Create your views here.


def main(request):
	products = product.objects.all()
	catprods = product.objects.values('category','id')
	cats = {item['category'] for item in catprods}
	allprods = []
	for cat in cats:
		prod = product.objects.filter(category=cat)
		n = len(prod)
		nslides = n//4 + ceil((n/4) - (n//4))
		allprods.append([prod,range(1,nslides),nslides])
#	print(allprods)
	params = {'allprods':allprods,'product':products}

	return render(request,'page.html',params)
	
	