from app.rag.chunking import *
from app.rag.embeddings import * 
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

def test_embedding_chunk():
    print("Chunking")
    chunks = chunk_document(
        document = document,
        chunk_size = 800, 
        overlap = 100
    )
    texts = [chunk.text for chunk in chunks]
    print("Initializing")
    embedding = FakeEmbeddingProvider()
    print("Embedding")
    vector_texts = embedding.embed_texts(texts)
    print(f"Vectors:\n")
    for i,text in enumerate(vector_texts):
        print(f"N: {i}:\n{text}")

test_embedding_chunk()