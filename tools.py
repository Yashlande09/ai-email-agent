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

    message = MIMEMultipart()

    message["From"] = SENDER_EMAIL
    message["To"] = to
    message["Subject"] = subject

    # Email body
    message.attach(MIMEText(body_text, "plain"))

    # Attach resume
    if attachment_path:

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
    Send an email with the appropriate resume attached.

    The resume is selected automatically based on the job description.
    """

    # Select resume
    resume_path = select_resume(
        subject + "\n" + body + "\n" + job_description
    )

    # Send email
    send_email_by_gmail(
        to=to,
        subject=subject,
        body_text=body,
        attachment_path=resume_path
    )

    if resume_path:
        return (
            f"Email sent successfully with resume: "
            f"{os.path.basename(resume_path)}"
        )

    return "Email sent successfully without a resume."


ALL_TOOLS = [send_email]