import re

def normalize_output(raw_text):
    try:
        raw_text = raw_text.replace("```json", "").replace("```", "")

        result = {
            "strategy": {},
            "copy": {},
            "design": {}
        }

        # Strategy
        topic = re.search(r'"topic"\s*:\s*"([^"]+)"', raw_text)
        hook = re.search(r'"hook"\s*:\s*"([^"]+)"', raw_text)
        angle = re.search(r'"angle"\s*:\s*"([^"]+)"', raw_text)

        if topic:
            result["strategy"]["topic"] = topic.group(1)
        if hook:
            result["strategy"]["hook"] = hook.group(1)
        if angle:
            result["strategy"]["angle"] = angle.group(1)

        # Captions
        insta = re.search(r'instagram_caption"\s*:\s*"([^"]+)"', raw_text, re.IGNORECASE)
        linkedin = re.search(r'linkedin_caption"\s*:\s*"([^"]+)"', raw_text, re.IGNORECASE)

        if insta:
            result["copy"]["instagram_caption"] = insta.group(1)
        if linkedin:
            result["copy"]["linkedin_caption"] = linkedin.group(1)

        # Hashtags
        hashtags = re.findall(r"#\w+", raw_text)
        result["copy"]["hashtags"] = list(set(hashtags))

        # Design
        image_prompt = re.search(r'"image_prompt"\s*:\s*"([^"]+)"', raw_text)
        style = re.search(r'"style"\s*:\s*"([^"]+)"', raw_text)

        if image_prompt:
            result["design"]["image_prompt"] = image_prompt.group(1)
        if style:
            result["design"]["style"] = style.group(1)

        return result

    except Exception as e:
        return {"error": str(e), "raw": raw_text}


def clean_text_fields(data):
    try:
        for section in data:
            if isinstance(data[section], dict):
                for key in data[section]:
                    if isinstance(data[section][key], str):
                        data[section][key] = data[section][key].replace("\n", " ").strip()
        return data
    except:
        return data

def extract_slides(raw_text):
    import re

    slides = []

    matches = re.findall(
        r'\{\s*"image_prompt"\s*:\s*"([^"]+)"\s*,\s*"text"\s*:\s*"([^"]+)"\s*\}',
        raw_text
    )

    for match in matches:
        slides.append({
            "image_prompt": match[0],
            "text": match[1]
        })

    return slides