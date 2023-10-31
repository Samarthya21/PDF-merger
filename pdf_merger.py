import PyPDF2
import sys
import os

merger=PyPDF2.PdfMerger()
current_directory = os.getcwd()
for file in os.listdir(current_directory):
    
    if file.endswith(".pdf"):
        print(file)
        merger.append(file)
    merger.write("combinedPDF.pdf")
        