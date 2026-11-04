# Deployment Notes

## Local

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Configuration

Runtime defaults live in `skilldispatch/config/settings.py`.
Human-editable mirrors live in:

- `configs/default.yaml`
- `configs/scoring.yaml`

## Production swap plan

1. Replace `LLMAdapter` stub with local model router
2. Replace `LaborMarketAdapter` stub with authenticated API client
3. Persist pivot snapshots via a real `StorageAdapter`
4. Keep the FastAPI contract unchanged
