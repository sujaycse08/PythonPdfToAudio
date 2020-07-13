import PyPDF2
import pyttsx3

book = open('hacking_for_dummies.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
page = pdfReader.getPage(10)


theMan = pyttsx3.init()
text = page.extractText()
theMan.say(text)
theMan.runAndWait()

# page range
# pages=pdfReader.numPages
# theMan = pyttsx3.init()

# for num in range(10,pages)
#     page = pdfReader.getPage(num)
#     text = page.extractText()
#     theMan.say(text)
#     theMan.runAndWait()
