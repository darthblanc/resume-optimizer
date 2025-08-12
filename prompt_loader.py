import re
from prompt_cleaner import PromptCleaner


class PromptLoader:
    def __init__(self):
        self.system_prompt: list[str] = []
        self.user_prompt: list[str] = []
        self.cleaner: PromptCleaner = PromptCleaner()

    def load_system_prompt(self, prompt_name):
        with open(f"prompts/system/{prompt_name}.txt", "r") as fd:
            self.system_prompt = fd.readlines()

    def load_user_prompt(self, prompt_name):
        with open(f"prompts/user/{prompt_name}.txt", "r") as fd:
            self.user_prompt = fd.readlines()

    def set_job_description(self, job_description):
        self._fit_into_system_prompt("sjd", job_description)

    def set_resume_content(self, resume_content):
        self._fit_into_system_prompt("src", resume_content)

    def _fit_into_system_prompt(self, mode, content):
        for i, line in enumerate(self.system_prompt):
            line = line.strip()
            if mode == "sjd":
                if re.match("The job description you will be working with:", line):
                    self.system_prompt[i] += " " + self.cleaner.remove_new_line_char(content)
            if mode == "src":
                if re.match("The resume you will be working with:", line):
                    self.system_prompt[i] += " " + self.cleaner.remove_new_line_char(content)
