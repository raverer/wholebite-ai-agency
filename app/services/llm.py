import requests
import json
import re


def extract_json(text):
    if isinstance(text, dict):
        return text

    if not isinstance(text, str):
        return {
            "error": "Invalid LLM response",
            "raw": str(text)
        }

    cleaned = text.strip()

    cleaned = re.sub(
        r"^\s*```(?:json)?\s*|\s*```\s*$",
        "",
        cleaned,
        flags=re.IGNORECASE
    ).strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    decoder = json.JSONDecoder()

    for index, character in enumerate(cleaned):
        if character == "{":
            try:
                result, _ = decoder.raw_decode(cleaned[index:])

                if isinstance(result, dict):
                    return result

            except json.JSONDecodeError:
                continue

    return {
        "error": "JSON parse failed",
        "raw": cleaned
    }


def call_llm(prompt, model="llama3:latest"):

    def make_request(model_name):
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model_name,
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )

        response.raise_for_status()

        data = response.json()
        raw_output = data.get("response")

        if not isinstance(raw_output, str) or not raw_output.strip():
            raise ValueError("Ollama returned an empty response")

        return raw_output

    primary_error = None

    # PRIMARY MODEL
    try:
        raw_output = make_request(model)

        print("\n===================")
        print("MODEL:", model)
        print("RAW OUTPUT")
        print("===================")
        print(raw_output)

        result = extract_json(raw_output)

        if not isinstance(result, dict) or "error" in result:
            raise ValueError("Primary model returned invalid JSON")

        return result

    except Exception as exc:
        primary_error = exc
        print("\nPrimary model failed:", str(primary_error))

    # Do not retry Phi-3 if Phi-3 itself failed
    if model.split(":")[0] == "phi3":
        return {
            "error": "LLM failed",
            "details": str(primary_error)
        }

    # FALLBACK MODEL
    fallback_model = "phi3:latest"

    print("Switching to fallback model:", fallback_model)

    try:
        raw_output = make_request(fallback_model)

        print("\n===================")
        print("FALLBACK MODEL:", fallback_model)
        print("===================")
        print(raw_output)

        result = extract_json(raw_output)

        if not isinstance(result, dict) or "error" in result:
            raise ValueError("Fallback model returned invalid JSON")

        return result

    except Exception as fallback_error:
        return {
            "error": "LLM completely failed",
            "primary_error": str(primary_error),
            "fallback_error": str(fallback_error)
        }
