################## import ########################
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

############## Scraper Data Type #################
# - Returns web elements of a url as lists

class Scraper:
	#shared class variables
	pageSoup = ''
	
	#unique instance variables
	def __init__(self, url):
		self.url = url
		self.open()	

	def modifyURL(self, url):
		self.url = url
		self.open()	

	#opens up the connection and stores HTML in pageSoup
	def open(self):
		# Opens the connection and grabes the page
		print("Loading HTML content from: " + self.url)
		uClient = uReq(self.url)
		pageHTML = uClient.read()
		uClient.close()

		# Parses HTML 
		self.pageSoup = soup(pageHTML, "html.parser") 

	#returns a user specified web element
	def get_web_element(self, element, type_Class=None, first=None, last=None):
		if (first is None) and (last is None):
			first = 0
			last  = len(self.pageSoup)

		elif last is None:
			last  = len(self.pageSoup)

		section = self.pageSoup.findAll(element, {"class":type_Class})[first:last]
		return(section)

	#Returns a list of 'a' web elements 
	def a(self,first=None, last=None):
		if (first is None) or (last is None):
			first = 0
			last  = len(self.pageSoup)

		aSections = self.pageSoup.findAll("a")[first:last]
		return(aSections)

	#Returns a list of href web elements
	def href(self,first=None, last=None):
		hrefLinks = []

		if (first is None) and (last is None):
			first = 0
			last  = len(self.pageSoup)

		elif last is None:
			last  = len(self.pageSoup)

			for a in self.pageSoup.findAll('a', href=True)[first:last]:
				if a['href'] == '#':
					break
				else:
					hrefLinks.append(a['href'])

			return(hrefLinks)

		else:
			for a in self.pageSoup.findAll('a', href=True)[first:last]:
				hrefLinks.append(a['href'])
			return(hrefLinks)



