def format_linkedin_post(text):

    lines = text.split(". ")

    formatted = ""

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Add spacing
        formatted += line + ".\n\n"

    return formatted.strip()