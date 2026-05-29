# AI RAG System

Lightweight retrieval-augmented generation (RAG) demo using sentence-transformers
for embeddings and FastAPI for the application API.

**Status:** Ready for local development.

**Contents:** short instructions for setup, running, and troubleshooting.

**Quick Start**

- **Clone & enter project:**

```bash
git clone <repo-url> your-folder
cd your-folder
```

- **Create a virtualenv (if you don't have one):**

```bash
python3 -m venv venv
source venv/bin/activate
```

- **Install dependencies:**

```bash
python -m pip install -U pip
python -m pip install -r requirements.txt
```

**Run the app**

Start the FastAPI server (run inside the activated venv):

```bash
source venv/bin/activate
# use python -m uvicorn so the reload subprocess uses the same interpreter
python -m uvicorn app.main:app --reload
```

By default the server runs on http://127.0.0.1:8000. To change port add `--port 8001`.

**Project structure**

- `app/` — application code
	- `embeddings.py` — loads `sentence-transformers` and exposes `generate_embedding()`
	- `main.py` — FastAPI app and routes
	- `retrieval.py`, `vector_store.py`, `models.py` — retrieval and data helpers
- `requirements.txt` — Python dependencies

**Embeddings**

This project uses `sentence-transformers` (model: `all-MiniLM-L6-v2`) to convert
texts into dense vectors. `app/embeddings.py` constructs the model and exposes
`generate_embedding(text: str)` which returns a floating-point vector.

Notes:
- First run will download model weights from the Hugging Face hub. Consider setting
	`HF_TOKEN` environment variable for higher rate limits and faster downloads.

**VS Code configuration**

The workspace includes `.vscode/settings.json` pointing the interpreter to
the project's `venv` so VS Code runs and debugs with the same Python.

**Troubleshooting**

- ModuleNotFoundError for `sentence_transformers`:
	- Ensure the venv is activated, and install deps with `python -m pip install -r requirements.txt`.
	- When running `uvicorn`, prefer `python -m uvicorn ...` so the reload subprocess uses the same interpreter.

- Port already in use:
	- Find and kill the existing process: `lsof -i :8000` then `kill <PID>` or `kill $(lsof -t -i:8000)`.

- Permission or macOS-specific issues: ensure the Python version in `venv` matches the one you expect.

**Environment variables**

- `HF_TOKEN` (optional): your Hugging Face token for authenticated model downloads.

**Testing embedding locally**

```bash
source venv/bin/activate
python -c "from app.embeddings import generate_embedding; print(generate_embedding('hello world')[:8])"
```

**License**

This repository contains no license file by default — add one if you plan to share it.

