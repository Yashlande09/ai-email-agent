import os


RESUME_FOLDER = "resume"


def select_resume(job_text):
    text = job_text.lower()

    if any(word in text for word in [
        "data analyst",
        "power bi",
        "tableau",
        "excel",
        "data visualization"
    ]):
        return os.path.join(RESUME_FOLDER, "Yash_Lande_Resume_Data Analyst.pdf")

    elif any(word in text for word in [
        "data scientist",
        "machine learning",
        "deep learning",
        "statistics",
        "data science"
    ]):
        return os.path.join(RESUME_FOLDER, "Yash_Lande_Resume_Data science.pdf")

    elif any(word in text for word in [
        "python developer",
        "python development",
        "django",
        "flask",
        "fastapi",
        "backend developer"
    ]):
        return os.path.join(RESUME_FOLDER, "Yash_Lande_Resume_Backend_1.pdf")

    elif any(word in text for word in [
        "ai engineer",
        "artificial intelligence",
        "generative ai",
        "langchain",
        "llm",
        "rag",
        "ai agent"
    ]):
        return os.path.join(RESUME_FOLDER, "Yash_Lande_Resume_AIML.pdf")

    return None