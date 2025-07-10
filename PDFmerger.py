import tkinter 
from tkinter.filedialog import askopenfilename
from pypdf import PdfReader,PdfWriter
writer = PdfWriter()
window = tkinter.Tk()
window.withdraw()
file_path1 = askopenfilename(title = "Select any PDF file:", filetypes = [("PDF files", "*.pdf")])

reader1 = PdfReader(file_path1)
print("Selected file is:", file_path1)
for page in reader1.pages:
    writer.add_page(page)

file_path2 = askopenfilename(title = "Select any PDF file:", filetypes = [("PDF files", "*.pdf")])

reader2 = PdfReader(file_path2)
print("Selected file is:", file_path2)
for page in reader2.pages:
    writer.add_page(page)

with open("merged_pdf.pdf", 'wb') as output_pdf:
    writer.write(output_pdf)

