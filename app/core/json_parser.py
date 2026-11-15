import json
import re


class JSONParser:
    """
    Safely extracts and parses JSON returned by the LLM.

    Features
    --------
    • Removes Markdown code blocks
    • Extracts the first JSON object
    • Attempts to repair common formatting issues
    • Returns a Python dictionary
    """

    def parse(self, response: str) -> dict:

        if not response:
            raise ValueError("Empty response from LLM.")

        # ---------------------------------
        # Remove Markdown code fences
        # ---------------------------------

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        # ---------------------------------
        # First attempt
        # ---------------------------------

        try:
            return json.loads(response)

        except Exception:
            pass

        # ---------------------------------
        # Extract first JSON object
        # ---------------------------------

        match = re.search(
            r"\{.*\}",
            response,
            re.DOTALL
        )

        if match:

            candidate = match.group(0)

            try:
                return json.loads(candidate)

            except Exception:
                response = candidate

        # ---------------------------------
        # Common Repairs
        # ---------------------------------

        repaired = response

        # Remove trailing commas
        repaired = re.sub(
            r",\s*([}\]])",
            r"\1",
            repaired
        )

        # Replace smart quotes
        repaired = repaired.replace("“", '"')
        repaired = repaired.replace("”", '"')
        repaired = repaired.replace("’", "'")

        # Remove control characters
        repaired = re.sub(
            r"[\x00-\x1f]",
            "",
            repaired
        )

        # ---------------------------------
        # Second attempt
        # ---------------------------------

        try:

            return json.loads(repaired)

        except Exception as e:

            raise ValueError(
                f"Unable to parse JSON.\n\n{e}\n\nResponse:\n{response}"
            )


# Singleton

json_parser = JSONParser()


def parse_json(response: str) -> dict:
    return json_parser.parse(response)