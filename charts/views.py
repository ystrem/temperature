from django.shortcuts import render

t = {}

def readFile():
	with open('/home/ystrem/chartkick.py/examples/demo/charts/temperature.log','r') as f:
		data = f.readlines()
		
	for line in data:
		t[line.split(';')[0]] = line.split(';')[1]

	print t
	
	return t

def charts(request):
	
	readFile()
	
	temperature = [{u'data': t, u'name': u'Kuchyne'}]
	
	
	return render(request, 'charts.html', locals())

