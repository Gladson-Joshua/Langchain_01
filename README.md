# Langchain_01

A beginner LangChain project (Week 2, Day 3). It shows how to call an OpenAI chat model through LangChain and trace the calls in LangSmith.

## Project structure

```
Langchain_01/
├── main.py                 # Checks which API keys are set in .env
├── requirements.txt
├── .env.example            # Template for your own .env file
├── Langchain (1-4).png     # Screenshots of the app and LangSmith traces
└── traced-app/
    ├── traced_app.py       # Sends a prompt to gpt-4o-mini and prints the answer
    └── requirements.txt
```

## Setup

1. Clone the repo and create a virtual environment:

   ```bash
   git clone https://github.com/Gladson-Joshua/Langchain_01.git
   cd Langchain_01
   python -m venv venv
   venv\Scripts\activate        # Windows
   # source venv/bin/activate   # macOS / Linux
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and fill in your keys:

   ```env
   OPENAI_API_KEY=your-openai-key

   # Optional: LangSmith tracing
   LANGSMITH_TRACING=true
   LANGSMITH_API_KEY=your-langsmith-key
   LANGSMITH_PROJECT=Langchain_01
   ```

   `.env` is listed in `.gitignore`, so your keys are never committed.

## Usage

Check which API keys are set:

```bash
python main.py
```

Run the traced app:

```bash
cd traced-app
python traced_app.py
```

`traced_app.py` loads your keys from `.env`, then sends a prompt to `gpt-4o-mini` and prints the reply. To ask something different, change the text inside `llm.invoke(...)`.

## LangSmith tracing

When `LANGSMITH_TRACING=true`, each call appears in your LangSmith project with its input, output, token count and cost. See `Langchain (2).png` for an example.

> Every prompt and answer is stored in LangSmith while tracing is on, so don't send private data with it enabled.

## Built with

- [LangChain](https://python.langchain.com/)
- [langchain-openai](https://pypi.org/project/langchain-openai/)
- [LangSmith](https://smith.langchain.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
