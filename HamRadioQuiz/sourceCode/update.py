from Scraper import *

def update():

	#feild initilization
	host              = "https://hamstudy.org"
	first,last        = (0,5) #control variable range for extracting specific links
	print("Web Host: ")
	scraper           = Scraper(host)
	secondaryURL      = scraper.href(last)
	allQuestions      = []
	allanswers        = []
	allcorrectAnswers = []

	print()
	#gets the different sections(techician, general, Amateur Extra)
	first,last   = (5,8)
	sections     = scraper.href(first,last)

	#loops through each section and gets the questions and answers
	for type in sections:

		typeHandle = type.replace('/', '')
		link = host + type
		scraper.modifyURL(link)
		first,last   = (0,17)
		extension    = host + ''.join(scraper.href(21,22))

		#open Main Links
		scraper.modifyURL(extension)
		first,last     = (7, 17)
		mainLinks      = scraper.href(first,last)

		#getting sublinks from mainLinks
		print("\nTop Links in " + typeHandle + ": ")
		first,last   = (17, None)
		allLinks     = []
		for extension in mainLinks:
			scraper.modifyURL(host+extension)
			subLinks      = scraper.href(first,last)
			allLinks.append(subLinks)

		#clear files before adding contents
		open('Questions.txt', 'w').close()
		open('Answers.txt', 'w').close()
		open('CorrectAnswers.txt', 'w').close()

		#Opening all links
		print("\nOpening all links " + typeHandle + ": ")
		for links in allLinks:
			for link in links:
				scraper.modifyURL(host+link)
				sectionQuestions = scraper.get_web_element("div","question")
				sectionAnswers   = scraper.get_web_element("li","answer")
				correctAnswers   = scraper.get_web_element("li","answer correct")

				with open("data/" + typeHandle+'Questions.txt', 'a') as fileHandle:
					for question in sectionQuestions:
						fileHandle.write('%s\n' % question.text.strip())
				
				with open("data/" + typeHandle+'Answers.txt', 'a') as fileHandle:
					for answers in sectionAnswers:
						fileHandle.write('%s\n' % answers.div.text)

				with open("data/" + typeHandle+'CorrectAnswers.txt', 'a') as fileHandle:
					for answer in correctAnswers:
						fileHandle.write('%s\n' % answer.label.text[0].strip())


if __name__== "__main__":
	update()

