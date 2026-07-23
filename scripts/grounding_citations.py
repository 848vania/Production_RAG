from app.rag.grounding import * 

answer = "Primary approval for remote work arrangements comes from the employee’s manager and People Operations. [Source 134]\n\nFor location-specific changes: extended stays or changes beyond the 20-business-day allowance require written approval from the employee’s manager and the Legal team at least 30 days in advance. [Source 135]\n\nExceptions to the international-work restriction (up to 10 consecutive business days) require Legal and People Operations approval. [Source 136]"

sources = [{"chunk_id": str(i)} for i in [134,135,136]]
print(sources)

result = validate_citations(answer=answer, sources=sources)
print(result)