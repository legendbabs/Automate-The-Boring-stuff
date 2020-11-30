import PyPDF2, os
print(os.getcwd())

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
