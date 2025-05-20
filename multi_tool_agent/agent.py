from google.adk.agents import Agent
import re

def mask_pii(log_entry: str) -> str:
    """
    Detects and masks PII in the log entry.
    """
    # Mask email addresses
    log_entry = re.sub(r'[\w\.-]+@[\w\.-]+', '[EMAIL]', log_entry)
    # Mask phone numbers (simple pattern)
    log_entry = re.sub(r'\b\d{10}\b', '[PHONE]', log_entry)
    # Add more patterns as needed
    return log_entry


root_agent = Agent(
    model="gemini-2.0-flash",
    name="log_processor_agent",
    description="Processes logs and masks PII.",
    tools=[mask_pii],
    instruction="Use the pii_masking_tool to sanitize log entries."
)