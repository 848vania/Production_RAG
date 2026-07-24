import pytest 
from fastapi.testclient import TestClient
import io 

# import FastAPI instances
from app.api.main import app 

# Crete the test client instance 
client = TestClient(app)

def test_health_check():
    """
    Test the simple GET health endpoint
    """
    print("testing")
    response = client.get("/health")

    # Assertions check if the code behaves as expected 
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}

def test_chat_post_endpoint():
    """
    Tests a POST endpoint inside chat router
    """
    # 1. Prepare the dictionary payload you want to send 
    payload = {
        "question": "Can employees work from Mars?"
    }

    # 2. Send the POST request with the JSON body 
    response = client.post("/chat/", json=payload)

    # 3. Verify the server's output response 
    assert response.status_code == 200 

    response_data = response.json()

    assert "answer" in response_data
    assert response_data['refused'] == True

def test_route_document_endpoint(mocker):
    """
    Test a POST endpoint inside document router
    """

    # 1. Mock 'ingest_documents' so it doesn't process real vectors or disk data 
    mock_ingest = mocker.patch("app.api.routes_documents.ingest_documents")
    mock_ingest.return_value = {"documents_processed": 1, "chunks_create": 1, "chunks_indexed": 1}

    # 2. Create an in-memory mock file using io.BytesIO
    file_content = b"This is dummy enterprise text data for the RAG testing."
    file_payload = {
        "file": ("sample_policy_testing_mock.txt", io.BytesIO(file_content), "text/plain")
    }

    # 3. Target your fully qualified route path inside 'files'
    response = client.post("/documents/ingest", files=file_payload)

    response_data = response.json()

    # 4. Assert response validation
    assert response.status_code == 200 
    assert response_data['documents_processed'] == 1

    mock_ingest.assert_called_once()

# test_health_check()
# test_chat_post_endpoint()
# test_route_document_endpoint()