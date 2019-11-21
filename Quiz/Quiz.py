from Scraper import *

#menu for the diffent classes
def menu(sections):
	print("Choose a license class to study for:\n",
		"1)Technician\n 2)General\n 3)Amateur Extra\n")

	userInput = input("Choose a class (1-3) or any other key to quit: ")
	licenseType = int(userInput)

	if licenseType == 1:
		return ''.join(sections[0])
	elif licenseType == 2:
		return ''.join(sections[1])
	elif licenseType == 3:
		return ''.join(sections[2])
	else:
		return exit()

def main():

	#feild initilization
	baseUrl           = "https://hamstudy.org"
	first,last        = (0,5) #control variable range for extracting specific links
	allQuestions      = []
	allanswers 	  	  = []
	allcorrectAnswers = []
	scraper           = Scraper(baseUrl)
	secondaryURL      = scraper.href(last)
	sections          = []

	#gets the different sections(techician, general, Amateur Extra)
	first,last   = (21,22)
	for extension in secondaryURL:
		scraper.modifyURL(baseUrl+extension)
		sections.append(scraper.href(first,last))

	#user picks section and loads the link to the questions page
	scraper.modifyURL(baseUrl + menu(sections))
	first,last   = (7,17)
	links        = scraper.href(first,last)

	#open Main Links
	print("Opening Main Sections:")
	for extension in links:
		scraper.modifyURL(baseUrl+extension)
		sections.append(scraper.href(last))

	#open All links from main links
	print("Opening All Sections:")
	for extension in sections:
		for sub_link in extension:
			scraper.modifyURL(baseUrl+sub_link)

			#web elements
			sectionQuestions = scraper.get_web_element("div","question")
			sectionAnswers   = scraper.get_web_element("li","answer")
			correctAnswers   = scraper.get_web_element("li","answer correct")

			#extract text form web elements
			for question in sectionQuestions:
				allQuestions.append(question.text)
			for answers in sectionAnswers:
				allanswers.append(answers.text)
			for answer in correctAnswers:
				allcorrectAnswers.append(answer.label.text[0])

	#Quiz format
	index = 0
	number_of_choices = 4
	userAnswer = ''

	for question in allQuestions:
		print(question)

		for choice in range(index,index+number_of_choices):
			print(allanswers[choice])
			index = index+1

		print("Correct Answer: ",allcorrectAnswers[allQuestions.index(question)])
		userAnswer = input("Choose a letter:")
		if (userAnswer == (allcorrectAnswers[allQuestions.index(question)]).lower()) or (userAnswer == (allcorrectAnswers[allQuestions.index(question)]).upper()):
			pass
		else:
			break


if __name__== "__main__":
  main()

