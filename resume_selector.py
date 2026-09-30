
import os


RESUME_FOLDER = "resume"


RESUMES = {
    "data_analyst": os.path.join(
        RESUME_FOLDER,
        "Yash_Lande_Resume_Data Analyst.pdf"
    ),

    "data_scientist": os.path.join(
        RESUME_FOLDER,
        "Yash_Lande_Resume_Data science.pdf"
    ),

    "data_engineer": os.path.join(
        RESUME_FOLDER,
        "Yash_Lande_Resume_Data Engineer.pdf"
    ),

    "backend": os.path.join(
        RESUME_FOLDER,
        "Yash_Lande_Resume_Backend_1.pdf"
    ),

    "ai_ml": os.path.join(
        RESUME_FOLDER,
        "Yash_Lande_Resume_AIML.pdf"
    )
}


# Higher number = stronger indication of that role
KEYWORDS = {

    "data_analyst": {
        "data analyst": 10,
        "business analyst": 5,
        "power bi": 8,
        "tableau": 8,
        "excel": 5,
        "data visualization": 7,
        "dashboard": 5,
        "business intelligence": 7,
        "reporting": 4,
    },


    "data_scientist": {
        "data scientist": 10,
        "data science": 8,
        "machine learning": 5,
        "deep learning": 5,
        "statistical modeling": 7,
        "statistics": 4,
        "predictive modeling": 7,
        "scikit-learn": 5,
        "xgboost": 5,
        "model development": 5,
    },


    "data_engineer": {
        "data engineer": 10,
        "junior data engineer": 12,
        "data engineering": 9,
        "etl": 7,
        "elt": 7,
        "data pipeline": 8,
        "data pipelines": 8,
        "pyspark": 8,
        "apache spark": 8,
        "airflow": 8,
        "databricks": 8,
        "snowflake": 7,
        "data warehouse": 7,
        "data lake": 7,
        "azure data factory": 8,
        "kafka": 6,
        "hadoop": 6,
        "big data": 6,
        "sql": 2,
        "python": 2,
    },


    "backend": {
        "python developer": 10,
        "backend developer": 10,
        "backend engineer": 10,
        "python development": 7,
        "django": 7,
        "flask": 7,
        "fastapi": 8,
        "rest api": 7,
        "api development": 7,
        "backend": 5,
    },


    "ai_ml": {
        # VERY strong AI Engineer indicators
        "ai engineer": 15,
        "ai/ml engineer": 15,
        "artificial intelligence engineer": 15,
        "generative ai engineer": 15,
        "llm engineer": 15,

        # Strong GenAI indicators
        "generative ai": 12,
        "large language model": 12,
        "large language models": 12,
        "llm": 12,
        "rag": 12,
        "retrieval augmented generation": 12,
        "retrieval-augmented generation": 12,
        "ai agent": 12,
        "ai agents": 12,
        "agentic ai": 12,
        "agentic": 10,

        # AI frameworks
        "langchain": 10,
        "langgraph": 10,
        "llamaindex": 9,
        "llama index": 9,

        # Other AI technologies
        "prompt engineering": 8,
        "vector database": 8,
        "vector databases": 8,
        "embeddings": 7,
        "transformers": 7,
        "hugging face": 7,
        "openai": 6,
        "fine tuning": 7,
        "fine-tuning": 7,

        # General ML
        "machine learning": 3,
        "deep learning": 3,
    }
}


def select_resume(job_text):

    text = job_text.lower()

    scores = {}
    matched_keywords = {}

    # Calculate weighted scores
    for role, keywords in KEYWORDS.items():

        score = 0
        matches = []

        for keyword, weight in keywords.items():

            if keyword in text:
                score += weight
                matches.append(keyword)

        scores[role] = score
        matched_keywords[role] = matches

    # Find highest scoring role
    best_role = max(
        scores,
        key=scores.get
    )

    # No relevant role detected
    if scores[best_role] == 0:
        return None

    return {
        "role": best_role,
        "score": scores[best_role],
        "matched_keywords": matched_keywords[best_role],
        "resume": RESUMES[best_role]
    }
