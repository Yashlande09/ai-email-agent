# Email Agent Project

A Streamlit email assistant that drafts and sends job application emails with a role-specific resume attachment.

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with:

```env
MODEL=your_groq_model
GROQ_API_KEY=your_groq_api_key
GMAIL_EMAIL=your_gmail_address
GMAIL_APP_PASSWORD=your_gmail_app_password
```

4. Add your resume PDFs inside a local `resume/` folder. Resume PDFs are ignored by Git to avoid publishing personal documents.

## Run

```bash
streamlit run app.py
```
