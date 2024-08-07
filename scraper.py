from splinter import Browser
from bs4 import BeautifulSoup as soup
import re
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from splinter.driver.webdriver import BaseWebDriver, WebDriverElement
from urllib.parse import quote
from datetime import timedelta
import smtplib
from email.mime.text import MIMEText
import time
import schedule

ignoreKeywords = ['https://www.ununll.top','waya7.com','www.t8999.shop']

def convert_price(price_str):
	try:
	    if price_str.lower() == 'free':
	        return 0
	    else:
	        # Remove any non-numeric characters
	        numeric_str = ''.join(filter(str.isdigit, price_str))
	        return int(numeric_str)
	except:
		print("convert price error !!!!!!")
		return 10000

def getVisitURL(item):
	a_tag = item.find('a', href=True)
	href = a_tag['href'] if a_tag else None
	match = re.match(r"(/marketplace/item/\d+/)", href)

	return  "https://www.facebook.com/" + match.group(1)

def getItemDesc(url):

	browser.visit(url)
	browser.driver.maximize_window()
	# if browser.is_element_present_by_css('div[aria-label="Close"]', wait_time=10):
	#     # Click on the element once it's found
	# 	browser.find_by_css('div[aria-label="Close"]').first.click()
	try:
		outer_desc = browser.find_by_css('div[class="xz9dl7a x4uap5 xsag5q8 xkhd6sd x126k92a"]')
		button = outer_desc.find_by_css('div[class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1n2onr6 x87ps6o x1lku1pv x1a2a7pz"]')
		if(button):
			button.click()
	except:
		print("error !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		return ""




	html = browser.html
	item_soup = soup(html,'html.parser')


	desc_div = item_soup.find('div', class_="xz9dl7a x4uap5 xsag5q8 xkhd6sd x126k92a")
	res = desc_div.find('span', class_="x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u")
	
	return res.text.strip()



def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")





def reportSweetItem(item,url):

	subject = "捡到漏了！物品是 " + item['title'] + " 价格为 " + str(item['price'])
	body = "捡到漏了！物品是 " + item['title'] + " 价格为 " + str(item['price']) +'\n' + item['description'] + 'item link: '+url
	sender = "alyh1339@gmail.com"
	recipients = ["lol1339783292@gmail.com"]
	password = "xidk xrfm vxyq aeop"
	send_email(subject, body, sender, recipients, password)



def isSweetItem(item, keywords, maxPrice):


	for badword in ignoreKeywords:
		if badword in item['title'] or badword in item['description']:
			print('scam detected')
			return False




	for keyword in keywords:

		matchKey = False

		for synonym in keyword:

			if synonym in item['title'] or synonym in item['description']:
				matchKey = True
				print(synonym)


		if not matchKey:
			return False



	return item['price'] <= maxPrice


def writeItemId(_id):

	with open('visitedItem.txt', 'a') as file:
		# Write the data followed by a newline character
		file.write(_id + '\n')

def isItemVisted(_id):

	with open('visitedItem.txt', 'r') as file:
		lines = file.readlines()
		if _id + '\n' not in lines:
			return False
	return True






def job():
	start_time = time.monotonic()


	scroll_count = 0
	scroll_delay = 2
	#base_url = 'https://www.facebook.com/marketplace/perth/search?daysSinceListed=1&query=graphics%20card&exact=false'
	base_url = 'https://www.facebook.com/marketplace/perth/electronics'
	free_url = 'https://www.facebook.com/marketplace/perth/free'
	try_url ='https://www.facebook.com/marketplace/perth/search?query=graphics%20card'
	general_url = 'https://www.facebook.com/marketplace/perth'
	electronics_url = 'https://www.facebook.com/marketplace/perth/electronics'
	home_url = 'https://www.facebook.com/marketplace/perth/home'
	gpu_url1 = 'https://www.facebook.com/marketplace/perth/search?daysSinceListed=1&query=graphics%20card&exact=false'
	gpu_url2 = 'https://www.facebook.com/marketplace/perth/search?daysSinceListed=1&query=rtx&exact=false'
	metaquest_url = 'https://www.facebook.com/marketplace/perth/search?daysSinceListed=1&query=meta%20quest&exact=false'
	applewatch_url = 'https://www.facebook.com/marketplace/perth/search?daysSinceListed=1&query=apple%20watch&exact=false'
	macbook_url = 'https://www.facebook.com/marketplace/perth/search?daysSinceListed=1&query=macbook&exact=false'
	laptop_url = 'https://www.facebook.com/marketplace/perth/search?daysSinceListed=1&query=laptop&exact=false'
	pc_url = 'https://www.facebook.com/marketplace/perth/search?daysSinceListed=1&query=gaming%20pc&exact=false'
	headphone_url = 'https://www.facebook.com/marketplace/perth/search?daysSinceListed=1&query=headphone&exact=false'
	monitor_url = 'https://www.facebook.com/marketplace/perth/search?daysSinceListed=1&query=monitor&exact=false'
	tv_url = 'https://www.facebook.com/marketplace/perth/search?daysSinceListed=1&query=tv&exact=false'
	ps4pro_url = 'https://www.facebook.com/marketplace/perth/search?daysSinceListed=1&query=ps4%20pro&exact=false'
	ps5_url = 'https://www.facebook.com/marketplace/perth/search?daysSinceListed=1&query=ps5&exact=false'
	iphone_url = 'https://www.facebook.com/marketplace/perth/search?daysSinceListed=1&query=iphone&exact=false'
	ipad_url = 'https://www.facebook.com/marketplace/perth/search?daysSinceListed=1&query=ipad&exact=false'


	searchUrls = [
		general_url, electronics_url, home_url, gpu_url1, gpu_url2,
		metaquest_url, applewatch_url, macbook_url, laptop_url,
		pc_url, headphone_url, monitor_url, ps4pro_url, ps5_url, ipad_url, iphone_url
	]




	gpu_keywords = ["graphics card","rtx"]
	gpu_keywords = [quote(i) for i in gpu_keywords]



	interestedGPUs = [([['3060', '6600xt', '4060']],350),([['1080ti']],250),([['1070','2060']],180),([['rx580','rx 580']],80),([['2070','1080']],180), ([['3060ti','6700xt','2080']], 350),
	([['2080ti','3070', '4060ti']], 400), ([['3070ti']], 450), ([['3080','7700xt']], 600), ([['3080ti','7800xt']], 650), ([['3090']], 1000), ([['4070']], 800), ([['4070ti']], 1300), 
	([['4080','7900xtx']], 1500),([['7900xt']], 900),([['7900gre']], 800),   ([['6800']], 500), ([['6800xt']], 600), ([['6900xt']], 650),  ([['6950xt']], 700),  
	([['4090']], 3000), 
	]

	interestedOthers = [
	([['metaquest 2', 'meta quest 2', 'oculus quest 2']], 250), ([['metaquest 3', 'meta quest 3', 'oculus quest 3']], 500),
	([['apple watch'],['se']], 150), ([['apple watch'],['8','9']], 250),([['mac book','macbook']], 150),([['mac book','macbook'],['m1','m2','m3']], 650)
	,([['mac book','macbook'],['m1','m2','m3'],['16']], 1300),([['mac book','macbook'],['16','15']], 500)
	,([['laptop'],['3070','4060','4050','2080']], 1300)
	,([['laptop'],['2070']], 800)
	,([['laptop'],['3080','4070']], 1500)

	,([['pc','computer'],['1080ti','3060','6700xt']], 750)
	,([['pc','computer'],['2080ti','3070','3060ti','6800','6700xt']], 900)
	,([['pc','computer'],['3080','6800xt','6900xt','6950xt']], 900)
	,([['pc','computer'],['3090','4070','7800','7700']], 1200)
	,([['pc','computer'],['4080','7900']], 1700)

	,([['wh-1000xm3']], 200), ([['wh-1000xm4']], 230),([['wh-1000xm5']], 300)


	,([['headphone'],['bose quiet']], 200)

	,([['headphone'],['bose quiet'],['ultra']], 400)

	,([['bose quiet'],['ultra']], 300)



	,([['4k','uhd'],['monitor'],['144','165','120','240']], 500)
	,([['qhd','1440'],['monitor'],['144','165','120','240']], 250)
	,([['monitor'],['49']], 500)
	,([['monitor'],['ultrawide','ultra wide','wqhd']], 500)

	,([['fhd','1080'],['monitor'],['144','165','120','240']], 150)


	,([['oled'],['monitor', 'tv']], 700)
	,([['tv'],['c1','c2','c3','c4']], 1000)
	# ,([['tv'],['65','75','85','83'],['4k','uhd']], 500)
	# ,([['tv'],['65','75','85','83']], 250)
	# ,([['tv'],['75','85','83'],['4k','uhd']], 700)



	,([['ps4'],['pro']], 150)
	,([['ps5','playstation 5']], 500)#ps5 sell price 450



	,([['secretlab','secret lab']], 500)
	,([['ergohuman','ergo human']], 300)
	,([['herman miller','hermanmiller']], 800)
	
	,([['ssd','solid state drive'],['1000gb','1tb']], 60)
	,([['ssd','solid state drive'],['2000gb','2tb']], 150)
	,([['hdd','hard drive'],['4000gb','4tb']], 70)

	,([['iphone'],['15']], 900)
	,([['iphone'], ['14']], 700)
	,([['iphone'],['13']], 600)
	,([['iphone'],['12']], 400)
	,([['iphone'],['11']], 250)

	,([['ipad'],['air']], 400)
	,([['ipad'],['air'],['5']], 650)
	,([['ipad'],['air'],['13']], 900)
	,([['ipad'],['10']], 450)
	,([['ipad'],['pro'],['12.9']], 600)
	,([['ipad'],['pro'],['12.9'],['5','4']], 900)
	]








	#x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g x1sur9pj xkrqix3 x1lku1pv


	for current_url in searchUrls:

		browser.visit(current_url)
		browser.driver.maximize_window()


		# if browser.is_element_present_by_css('div[aria-label="Close"]', wait_time=10):
		#     # Click on the element once it's found
		# 	browser.find_by_css('div[aria-label="Close"]').first.click()


		for _ in range(scroll_count):
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(scroll_delay)

		html = browser.html
		market_soup = soup(html,'html.parser')


		Oitems_div = market_soup.find_all('span', class_="x1lliihq x1iyjqo2")
		items = []
		for item in Oitems_div:
			title_div = item.find_all('span', class_="x1lliihq x6ikm8r x10wlt62 x1n2onr6")
			price_div = item.find_all('span', class_="x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x1lkfr7t x1lbecb7 x1s688f xzsf02u")
			if len(title_div) != 0 and len(price_div) != 0:


				url = getVisitURL(item)
				pattern = re.compile(r'item/(\d+)/')
				item_id = pattern.search(url).group(1)

				if isItemVisted(item_id):
					continue
				else:
					writeItemId(item_id)
				
				desc = getItemDesc(url)

				newItem = {"title": title_div[0].text.strip().lower(),
								"price": convert_price(price_div[0].text.strip()),
									"description": desc.lower()}
				items.append(newItem)



				for i in range(len(interestedGPUs)):

					keywords = interestedGPUs[i][0]

					maxPrice = interestedGPUs[i][1]

					if isSweetItem(newItem, keywords, maxPrice):
						reportSweetItem(newItem,url)
						print("sweeet item found!!!!")
						print(newItem)

				for i in range(len(interestedOthers)):

					keywords = interestedOthers[i][0]

					maxPrice = interestedOthers[i][1]

					if isSweetItem(newItem, keywords, maxPrice):
						reportSweetItem(newItem,url)
						print("sweeet item found!!!!")
						print(newItem)


		

	end_time = time.monotonic()
	print(timedelta(seconds=end_time - start_time))




chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs',{'profile.default_content_setting_values.notifications':2})
# chrome_options.add_argument("--use-fake-ui-for-media-stream")


browser = Browser('chrome', options=chrome_options) 
#selects facebook as the website to load in the browser
browser.visit('http://www.facebook.com')

# fills the email field in the facebook login section 
browser.fill('email', 'youremail')
browser.fill('pass', 'yourpass')

#selects the login button on the facebook page to log in with details given
button = browser.find_by_css('button[class="_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy"]')

button.click()

schedule.every(15).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)