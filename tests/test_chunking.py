from app.rag.chunking import *
from app.schemas import Document

text = """# Access Control Policy
    **Nexora Technologies, Inc.**
    **Version 2.5 | Effective Date: January 1, 2026**

    ---

    ## 1. Purpose and Scope

    This Access Control Policy establishes Nexora Technologies, Inc.'s ("Nexora") requirements for managing logical and physical access to systems, data, networks, and facilities. Its goal is to ensure that access is granted only to authorized individuals, for legitimate business purposes, and at the minimum level required to perform their function.

    This policy applies to:
    - All employees, contractors, temporary workers, and vendors
    - All Nexora-owned or Nexora-managed systems, networks, cloud environments, and physical locations
    - All access types: user accounts, service accounts, API keys, privileged access, physical badges

    Questions should be directed to the IT Security team at security@nexora-internal.com.

    ---

    ## 2. Governing Principles

    ### 2.1 Least Privilege
    Every user, process, and system component must be granted only the minimum access required to perform its intended function. Broad or permissive access should never be used as a convenience.

    ### 2.2 Need to Know
    Access to data is governed by whether the user has a legitimate need to view, process, or modify it—not solely by their role or seniority.
    """

document = Document(
    doc_id = "testing",
    source_path = "/testing",
    text = text,
    title = "Title_testing",
    metadata = {}
    )

text_2 = """# Employee Handbook
**Nexora Technologies, Inc.**
**Version 4.2 | Effective Date: January 1, 2026**

---

## 1. Welcome to Nexora

Welcome to Nexora Technologies, Inc. ("Nexora" or "the Company"). We are a B2B software company headquartered in Austin, Texas, with offices in Chicago, New York, and Toronto. Our platform helps mid-market and enterprise clients automate financial operations workflows.

This handbook outlines our policies, expectations, and the resources available to you as a Nexora employee. All employees are expected to read this handbook in full during their first week of employment and to comply with its contents throughout their tenure.

Questions about this handbook should be directed to the People Operations team at people@nexora-internal.com.

---

## 2. Employment Classifications

### 2.1 Full-Time Employees
Employees who work a minimum of 40 hours per week on a regular schedule. Full-time employees are eligible for the full benefits package described in Section 7.

### 2.2 Part-Time Employees
Employees who work fewer than 30 hours per week. Part-time employees are eligible for prorated vacation accrual and may qualify for limited health benefits depending on hours worked.

### 2.3 Contractors and Consultants
Individuals engaged through a services agreement who are not employees of Nexora. Contractors are not eligible for employee benefits and are subject to their individual contracts rather than this handbook."""

document_2 = Document(
    doc_id = "testing_2",
    source_path = "/testing_2",
    text = text_2,
    title = "Title_testing_2",
    metadata= {}
)

def test_split_markdown_section():
    splits = split_by_markdown_sections(document)
    for el in splits:
        print(el)
        print("*"*15)

def test_chunk_text():
    chunks = chunk_text(
        text= text, 
        chunk_size = 800,
        overlap= 100
    )
    for i,chunk in enumerate(chunks):
        print(f"Chunk Number {i}\n{chunk}")
        print("*"*15)

def test_chunk_document():
    chunks = chunk_document(
        document = document,
        chunk_size = 800, 
        overlap = 100
    )
    for i,chunk in enumerate(chunks):
        print(f"Chunk Number {i}\n{chunk}")
        print("-"*15)

def test_chunk_documents():
    documents = [document, document_2]
    chunks = chunk_documents(
        documents = documents,
        chunk_size = 800, 
        overlap= 100    
    )
    for i, chunk in enumerate(chunks):
        print(f"Chunk Number {i}\n{chunk}")
        print("*"*15)

# test_split_markdown_section()
# test_chunk_text()
# test_chunk_document()
# test_chunk_documents()