# apiap

- Python 3.9
- FastAPI

## 起動方法

```
uvicorn main:app --reload
```

## Test Request

```
url -X GET http://localhost:8000/amida/hJqDzsXImQOkU0fgiVnX -H "Content-Type: application/json" -d '{"Names":["A","B","C","D","E","F","G"],"NumberInGroup":0}'
```