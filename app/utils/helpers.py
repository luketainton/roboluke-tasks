import re


def validate_email_syntax(email: str) -> bool:
    """Validate email syntax.

    Args:
        email (str): Email address.

    Returns:
        bool: True if valid, else False.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None
