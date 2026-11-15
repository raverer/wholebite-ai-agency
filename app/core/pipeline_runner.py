from pathlib import Path


class PromptLoader:
    """
    Loads Markdown prompt templates from the prompts directory.
    """

    def __init__(self):

        # app/core -> app -> prompts
        self.prompt_dir = (
            Path(__file__)
            .resolve()
            .parent.parent
            / "prompts"
        )

    def load(self, filename: str) -> str:

        filepath = self.prompt_dir / filename

        if not filepath.exists():
            raise FileNotFoundError(
                f"Prompt not found: {filepath}"
            )

        return filepath.read_text(
            encoding="utf-8"
        )


# Singleton
prompt_loader = PromptLoader()