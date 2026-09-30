
import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from langchain.tools import tool
from resume_selector import select_resume
from dotenv import load_dotenv


load_dotenv()


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = os.getenv("GMAIL_EMAIL")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")


def send_email_by_gmail(
    to: str,
    subject: str,
    body_text: str,
    attachment_path: str = None
):
    """
    Send an email through Gmail SMTP.
    """

    message = MIMEMultipart()

    message["From"] = SENDER_EMAIL
    message["To"] = to
    message["Subject"] = subject

    
    message.attach(
        MIMEText(body_text, "plain")
    )

    

    if attachment_path:

        if not isinstance(attachment_path, (str, bytes, os.PathLike)):
            raise TypeError(
                f"attachment_path must be a file path, "
                f"but received: {type(attachment_path).__name__}"
            )

        if not os.path.exists(attachment_path):
            raise FileNotFoundError(
                f"Resume not found: {attachment_path}"
            )

        with open(attachment_path, "rb") as file:

            attachment = MIMEApplication(
                file.read(),
                _subtype="pdf"
            )

        attachment.add_header(
            "Content-Disposition",
            "attachment",
            filename=os.path.basename(attachment_path)
        )

        message.attach(attachment)

    server = None

    try:

        server = smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT
        )

        server.starttls()

        server.login(
            SENDER_EMAIL,
            GMAIL_APP_PASSWORD
        )

        server.sendmail(
            SENDER_EMAIL,
            to,
            message.as_string()
        )

        return "Email sent successfully."

    finally:

        if server:
            server.quit()


@tool
def send_email(
    to: str,
    subject: str,
    body: str,
    job_description: str = ""
):
    """
    Send a professional email with the appropriate resume attached.

    The resume is automatically selected based on the
    job description, subject, and email body.
    """

    combined_text = (
        subject
        + "\n"
        + body
        + "\n"
        + job_description
    )

    resume_info = select_resume(
        combined_text
    )

    if resume_info is None:

        send_email_by_gmail(
            to=to,
            subject=subject,
            body_text=body,
            attachment_path=None
        )

        return (
            "Email sent successfully without a resume "
            "because no suitable resume was detected."
        )

    

    resume_path = resume_info["resume"]

    
    print(
        "Selected role:",
        resume_info["role"]
    )

    print(
        "Resume score:",
        resume_info["score"]
    )

    print(
        "Matched keywords:",
        resume_info["matched_keywords"]
    )

    print(
        "Resume path:",
        resume_path
    )

    
    send_email_by_gmail(
        to=to,
        subject=subject,
        body_text=body,
        attachment_path=resume_path
    )

    return (
        "Email sent successfully with resume: "
        f"{os.path.basename(resume_path)} "
        f"(Role: {resume_info['role']}, "
        f"Score: {resume_info['score']})"
    )



ALL_TOOLS = [
    send_email
]
