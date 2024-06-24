from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages 

# Create your views here.
from bs4 import BeautifulSoup as soup
import csv
from django.conf import settings
import time
import requests

def view(request):
	full_name = []
	full_price = []
	full_rate = []
	full_url = []

	# file_name = "{}data.csv".format(settings.STATIC_URL)
	file_name = "D:\Docs\Abhi\SIT\CSE\Web Dev\Projects\Web Scraping\Django-Web-Scraping-master\static\data.csv"  #Change wrt your pc path
	file = open(file_name, 'w')
	header='Name,Price,Rate,Url\n'
	file.write(header)

	if request.method == "POST":
		url=request.POST['url']
		if 'https://' not in url:
			messages.error(request, "Error")
		else:
			headers={"User-Agent":
		        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
			page_url = requests.get(url,headers=headers)
			pagesoup = soup(page_url.text, 'html.parser')
			
			main_class = pagesoup.find_all('div', {'class': '_75nlfW'})
			for i in main_class:

				#Change Class and tags according to latest website tags and classes
				pdt_name= i.find('div', {'class': 'KzDlHZ'}).text.replace(',', '').replace('\r', '').replace('\n', '') #
				pdt_price = i.find('div', {'class': 'Nx9bqj _4b5DiR'}).text.replace(',', '').replace('\r', '').replace('\n', '') # 
				pdt_rate = i.find('span', {'class': 'Y1HWO0'}).text.replace(',', '').replace('\r', '').replace('\n', '') #
				pdt_url = i.find('a', {'class': 'CGtC98'})['href'] #
				pdt_main_url = 'https://www.flipkart.com'+pdt_url
				
				pdt_price_Int=pdt_price[1:]

				full_name.append(pdt_name)
				full_price.append(pdt_price_Int)
				full_rate.append(pdt_rate)
				full_url.append(pdt_main_url)

				file.write(pdt_name+','+str(pdt_price_Int)+','+pdt_rate+','+pdt_main_url+'\n')

		mylist=zip(full_name,full_price,full_rate,full_url)
		file.close()
		return render(request,'index.html',{'mylist':mylist})
	return render(request,'index.html')