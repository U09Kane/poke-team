
## Setup

Create a virtual environment.
```bash
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

Startup the development server
```bash
uvicorn main:app --reload --port 5000
```
