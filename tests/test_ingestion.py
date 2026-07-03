from pathlib import Path 
from app.rag.ingestion import extract_title, clean_text

def test_extract_title_from_markdown():
    text = "# Remote Work Policy\n\nSome content"
    assert extract_title(text, "falback") == "Remote Work Policy"

def test_clean_text_removes_extra_spaces():
    text="Hello     world\n\n\nTest"
    cleaned = clean_text(text)
    print(f"Cleaned:\n{cleaned}")
    assert "     " not in cleaned

# Uncomment for testing 
# test_extract_title_from_markdown()
# test_clean_text_removes_extra_spaces()