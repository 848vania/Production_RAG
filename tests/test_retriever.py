from app.rag.retriever import * 
from app.rag.keyword_search import * 
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

def test_hybrid_retrieval():
    chunks = chunk_document(
        document = document,
        chunk_size = 800, 
        overlap = 100
    )
    for i, chunk in enumerate(chunks):
        print(f"Chunk_number {i}\n{chunk}")
        print("*"*15)

    query = "Which are the available work models?"
    top_k = 10

    results = hybrid_retrieve(query, top_k) 

    return results

results = test_hybrid_retrieval()
for resu in results:
    print("*"*15)
    print(resu)