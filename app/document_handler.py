import fitz
import docx
from io import StringIO
from typing import Union

def extract_text(file) -> Union[str, None]:
    """
    Extract text from a file (PDF, DOCX, TXT)

    Args:
        file: The file to extract text from
    Returns:
        The text extracted from the file    
    """

    filename = file.name.lower()
    
    if filename.endswith(".pdf"):
        return read_pdf(file)
    elif filename.endswith(".docx"):
        return read_docx(file)
    elif filename.endswith(".txt"):
        return read_txt(file)
    else:
        return None
    
def read_pdf(file) -> str:
    """
    Read a PDF file and return the text
    """
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)

def read_docx(file) -> str:
    """
    Read a DOCX file and return the text
    """
    doc = docx.Document(file)
    return "\n".join(p.text for p in doc.paragraphs)

def read_txt(file) -> str:
    return StringIO(file.getvalue().decode("utf-8")).read()
