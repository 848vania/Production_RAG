from app.schemas import Document, Chunk
import re


def split_by_markdown_sections(document: Document) -> list[dict]:
    """
    Split a markdown document by H2 sections.
    Return section title and section text.
    """
    sections = []
    current_heading = document.title
    current_lines = []

    for line in document.text.splitlines():
        match = re.match(r'^##\s+(.*)', line.strip())

        if match:
            if current_lines:
                sections.append({"heading": current_heading, "text": "\n".join(current_lines)})
            current_heading = match.group(1)
            current_lines = [line]  # Keep the heading in the section
        else:
            current_lines.append(line)

    if current_lines:
        sections.append({"heading": current_heading, "text": "\n".join(current_lines)})

    return sections



def chunk_text(
    text: str,
    chunk_size: int=800,
    overlap: int=100
    ) -> list[str]:
    """
    Split long text into overlapping chunks.
    """
    chunks = []
    start = 0 
    while start < len(text):
        end = min(len(text), start + chunk_size)
        chunk = text[start:end].strip()
        if chunk:
            # chunks.append((start, chunk))
            chunks.append(chunk)
        start = end - overlap
        if start < 0:
            start = 0 
        if end == len(text):
            break
    return chunks


def chunk_document(
    document: Document,
    chunk_size: int=800,
    overlap: int=100
    ) -> list[Chunk]:
    """
    Convert one Document into a list of Chunk objects.
    """
    index = 0
    chunks = []
    # Parse per sections 
    sections = split_by_markdown_sections(document)

    # Chunk each section
    for section in sections:
        heading = section['heading']
        content = section['text']
        # print(content)
        if len(content) >= chunk_size:
            text_chunks = chunk_text(content, chunk_size, overlap)
        else:
            text_chunks = [content]

        for text_chunk in text_chunks:
            # print("HERE")
            chunk = Chunk(
                chunk_id = str(index),
                doc_id = document.doc_id,
                doc_title = document.title,
                text = text_chunk,
                section_title= heading,
                metadata = document.metadata,
            )
            # print("HERE2222")
            chunks.append(chunk)
            index += 1
    
    return chunks

def chunk_documents(
    documents: list[Document],
    chunk_size: int=800,
    overlap: int=100
    ) -> list[Chunk]:
    """
    Convert many documents into chunks.
    """
    id = 0
    chunk_docs = []
    for el_doc in documents:
        chunks = chunk_document(el_doc, chunk_size, overlap)

        for i, chunk in enumerate(chunks):
            # print(f"INDEX FROM CHUNK: {chunk.chunk_id}")
            index = i + id
            # print(f"INDEX AFTER: {index}")
            chunk.chunk_id = str(index)
        
        id = index + 1

        chunk_docs += chunks

    return chunk_docs