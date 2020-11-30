import PyPDF2, os

# Get all the pdf filenames and change directory
# to where all pdf files are cntained
# os.chdir(r'C:\Users\USER\Desktop\Automate\chapter13')
pdfFiles = []
for filename in os.listdir():
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)

# Arrange the pdf files in alphabetical order
pdfFiles.sort(key=str.lower)

# Create a pdf file writer object
pdfWriter = PyPDF2.PdfFileWriter()

# Loop throuh all the pdf files
for filename in pdfFiles:
	pdfFileObj = open(filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	# Loop through all the pages except the first page
	for pageNum in range(1, pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)

# save the resulting pdf to a file
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()


