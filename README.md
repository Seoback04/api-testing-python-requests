# API Testing with Python (Requests + Pytest)
Python-based API testing for JSONPlaceholder using Requests and Pytest.

## Tech Stack
- Python 3.9+
- requests
- pytest
- pytest-html
- pytest-xdist

## Setup
```bash
pip install -r requirements.txt
pytest tests/ -v
```

## Run Commands
- `pytest tests/ -v`
- `pytest tests/test_posts_api.py -v`
- `pytest tests/ -v --html=reports/report.html --self-contained-html`
- `pytest tests/ -n auto`

## Test Cases
- TC-API-001 Get all posts
- TC-API-002 Get single post
- TC-API-003 Create post
- TC-API-004 Update post
- TC-API-005 Delete post
- TC-API-006 Query params
- TC-API-007 Non-existent post

## Structure
```text
api-testing-python-requests/
├── tests/
│   └── test_posts_api.py
├── utils/
│   └── api_client.py
├── fixtures/
│   └── test_data.json
├── reports/
├── config/
│   └── settings.py
├── conftest.py
├── requirements.txt
└── README.md
```
