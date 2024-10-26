from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages 

# Create your views here.
import collections
collections.Callable = collections.abc.Callable
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
			proxies={
				"http": "http://xxxxxxxxx-rotate:xxxxxx@p.webshare.io:80/",		#Add your proxy if needed
				"https": "http://xxxxxx-rotate:xxxxxxx@p.webshare.io:80/"
			}
			headers={
				'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
				'Accept-Language': 'en-us,en;q=0.5'
			}
			# page_url = requests.get(url,proxies=proxies)       #Uncomment this if requests is blocked
			page_url = requests.get(url,headers=headers)       #Uncomment this if requests is blocked
			# page_url = requests.get(url)
			
			page_url_text = requests.get(url).text
			print(page_url_text)

			pagesoup = soup(page_url.text, 'html.parser')

			main_class = pagesoup.find_all('a', {'class': 'CGtC98'})

			print("hello1")
			print(pagesoup.prettify())
			print("hello2")


			for i in main_class:
				#Change Class and tags according to the latest website tags and classes
				try:
					pdt_name_elem = i.find('div', {'class': 'KzDlHZ'})
					pdt_price_elem = i.find('div', {'class': 'Nx9bqj _4b5DiR'})
					pdt_rate_elem = i.find('span', {'class': 'Y1HWO0'})
					# pdt_url = i.find('a', {'class': 'CGtC98'})['href'] 
					pdt_url_elem = i.get('href')
					
					print(f"Element: {i}")
					print(f"Name element: {pdt_name_elem}")
					print(f"Price element: {pdt_price_elem}")
					print(f"Rate element: {pdt_rate_elem}")
					print(f"URL element: {pdt_url_elem}")
					
					if not all([pdt_name_elem, pdt_price_elem, pdt_rate_elem, pdt_url_elem]):
						raise ValueError("One or more elements not found")

					pdt_name = pdt_name_elem.text.replace(',', '').replace('\r', '').replace('\n', '')
					pdt_price = pdt_price_elem.text.replace(',', '').replace('\r', '').replace('\n', '')
					pdt_rate = pdt_rate_elem.text.replace(',', '').replace('\r', '').replace('\n', '')
					pdt_main_url = 'https://www.flipkart.com' + pdt_url_elem
				
					pdt_price_Int=pdt_price[1:]

					full_name.append(pdt_name)
					full_price.append(pdt_price_Int)
					full_rate.append(pdt_rate)
					full_url.append(pdt_main_url)

					file.write(pdt_name+','+str(pdt_price_Int)+','+pdt_rate+','+pdt_main_url+'\n')

				except Exception as e:
					print(f"Not found: {str(e)}")
		mylist=zip(full_name,full_price,full_rate,full_url)
		file.close()
		return render(request,'index.html',{'mylist':mylist})
	return render(request,'index.html')
