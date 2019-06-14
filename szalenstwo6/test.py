import PyPDF2

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

        page = pdf.getPage(4)
        page_content = page.extractText()

    print(page_content)
    return information

if __name__ == '__main__':
    path = 'repaired.pdf'
    extract_information(path)
