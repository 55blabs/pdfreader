import pyttsx3 #importing packages
import PyPDF2 #imported packages
from tkinter.filedialog import * #from tkinter and importing all modules

pdf = askopenfilename() #variable for the pdf that is going to be read
pdfreader = PyPDF2.PdfFileReader(pdf) #variable going to be read in 
pages = pdfreader.numPages #variable for the number of pages in the pdf file*return page number of pdf

#read all the data from the number of pages in the pdf
for num in range(0, pages): #created an iterative variable called num to read the pages with a for loop
    page = pdfreader.getPage(num) #inside the for loop we will get all the single pages, next we extract the text from pdf
    text = page.extract_text() #created a variable called text to extract 
    player = pyttsx3.init() #define our text to speech object initatize it 
    player.say(text) #player
    player.runAndWait() #run engine and wait