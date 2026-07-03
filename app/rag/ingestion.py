from pathlib import Path
from app.schemas import Document
from pypdf import PdfReader
import pymupdf
import datetime
import re
import unicodedata

RAW_DIR = Path("data/synthetic_documents") 
TEXT_SUFFIXES = {".md", ".txt"}
PDF_SUFFIXES = {".pdf"}

def extract_pdf_text(path: Path) -> str:
    # 1) PyMuPDF
    try: 
        with pymupdf.open(path) as doc:
            parts = []
            for page in doc:
                parts.append(page.get_text("text"))
        text  = "\n\n".join(parts)
        return text
    except Exception as e:
        print("There was an error EXTRACTING the pdf through PyMuPDF. Retrying thorugh PyPDF")
        pass 

    # 2) Fallback: pypdf
    try: 
        reader = PdfReader(str(path))
        parts = []
        for page in reader.pages:
            parts.append(page.extract_text() or "")
        return "\n\n".join(parts)
    except Exception as e:
        print("There was an error EXTRACTING the pdf through PyPDF. Returning empty texts")

def get_file_metadata(path: Path):
    stats = path.stat()

    metadata = {
        "file_extension": path.suffix,
        "absolute_path": str(path.resolve()),
        "file_size_bytes": stats.st_size,

        # Convert timestamps to readable dates 
        "last_modified": datetime.datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
        "last_accessed": datetime.datetime.fromtimestamp(stats.st_atime).strftime('%Y-%m-%d %H:%M:%S')
    }
    # Get creation date (Platform-dependent behavior)
    try:
        # Works on WIndows; gives metadata change time on Linux/Mac
        creation_time = stats.st_ctime
        metadata["created_or_changed"] = datetime.datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
    except AttributeError:
        metadata["created_or_changed"] = "Unknown"

    return metadata    

def load_documents_from_folder(path: Path = RAW_DIR) -> list[Document]:
    """Load all Markdown files from a folder"""
    documents = []
    for path in RAW_DIR.rglob("*"):
        if not path.is_file():
            continue
        suffix = path.suffix.lower()

        if suffix in TEXT_SUFFIXES:
            text = path.read_text(encoding="utf-8", errors="ignore")
        elif suffix in PDF_SUFFIXES:
            text = extract_pdf_text(path)
        else:
            continue

        document = Document(
            doc_id=path.name,
            source_path=str(path),
            text=clean_text(text),
            title = extract_title(text, path.name),
            metadata=get_file_metadata(path),
        )

        documents.append(document)
    
    return documents

def clean_text(text: str) -> str:
    """Normalize whitespace and remove unnecesary artifacts"""
    if not text:
        return ""

    # Normalize unicode variants (smart quotes, ligatures, etc.) to a consistent form
    text = unicodedata.normalize("NFKC", text)

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Strip control characters (e.g. null bytes from PDF extraction), keep newline/tab
    text = "".join(
        ch for ch in text if ch in ("\n", "\t") or unicodedata.category(ch)[0] != "C"
    )

    # Rejoin words split across a line wrap, e.g. "informa-\ntion" -> "information"
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)

    # Collapse runs of spaces/tabs (but not newlines) into a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Strip trailing whitespace on each line
    text = "\n".join(line.rstrip() for line in text.split("\n"))

    # Collapse 3+ consecutive blank lines down to a single blank line
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()

def extract_title(text: str, fallback: str = "Untitled Document") -> str:
    """Extract the first Markdown H1 title"""
    # Search for the first line starting with '#' followed by a space 
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)

    # Extract the text if a match is found 
    first_title = match.group(1) if match else fallback
    
    return first_title