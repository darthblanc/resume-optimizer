
class PromptCleaner:
    def __init__(self):
        pass

    @staticmethod
    def remove_new_line_char(string: str) -> str:
        return string.replace("\n", "")

    @staticmethod
    def add_tab_to_start(string) -> str:
        return f"\t{string}"
