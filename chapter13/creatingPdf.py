import PyPDF2

# Open the first and second pdf file
pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

# Create reader object for both files
pdf1FileReader = PyPDF2.PdfFileReader(pdf1File)
pdf2FileReader = PyPDF2.PdfFileReader(pdf2File)

# Create a pdfwriter object
pdfWriter = PyPDF2.PdfFileWriter()

# loop through the pages of pdf1FileReader
for numPage in range(pdf1FileReader.numPages):
	pageObj = pdf1FileReader.getPage(numPage)
	pdfWriter.addPage(pageObj)

# loop through the pages of pdf2FileReader
for numPage in range(pdf2FileReader.numPages):
	pageObj = pdf2FileReader.getPage(numPage)
	pdfWriter.addPage(pageObj)

# Create an output file
pdfOutPutFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutPutFile)
pdfOutPutFile.close()
pdf1File.close()
pdf2File.close()
