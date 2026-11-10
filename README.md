# GenAI Text Summarizer

A beginner-friendly Generative AI integrated web app. A user pastes long text, selects a summary style and length, and receives an AI-generated summary.

## Features
- Three output styles: bullet points, paragraph, and study notes
- Four summary lengths
- Uses Google's Gemini API through the official `google-genai` Python SDK
- Download generated summary as a `.txt` file
- Basic error handling and an explanation of the workflow

## Requirements
- Python 3.10 or newer
- A Gemini API key
- Internet connection

## Run locally
1. Extract this ZIP file.
2. Open a terminal in the project folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set your API key as an environment variable. Do not paste your key into `app.py` or share it.
   - Windows PowerShell:
     ```powershell
     $env:GEMINI_API_KEY="YOUR_API_KEY"
     ```
   - macOS/Linux:
     ```bash
     export GEMINI_API_KEY="YOUR_API_KEY"
     ```
5. Start the app:
   ```bash
   streamlit run app.py
   ```

## Project structure
- `app.py` — Streamlit user interface and Gemini API integration
- `requirements.txt` — Python dependencies
- `.env.example` — environment-variable name reminder (no real key)
- `sample_input.txt` — sample text to test
- `sample_output.txt` — illustrative sample output
- `docs/project_report.md` — full project documentation

## Important
This project requires a valid Gemini API key to generate live AI summaries. The included sample output is illustrative and is not a live API response. Never upload your API key to a public repository.
