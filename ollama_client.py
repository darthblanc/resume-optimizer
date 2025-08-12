import ollama
from prompt_loader import PromptLoader
from response_handler import ResponseHandler


class OllamaClient:
    def __init__(self, model="codellama"):
        self.loader: PromptLoader = PromptLoader()
        self.model = model
        self.handler: ResponseHandler = ResponseHandler()

    def load_base_system_prompt(self, prompt_name):
        self.loader.load_system_prompt(prompt_name)

    def set_job_description(self, job_description):
        self.loader.set_job_description(job_description)

    def set_resume_content(self, resume_content):
        self.loader.set_resume_content(resume_content)

    def load_existing_resume(self, prompt_name):
        self.loader.load_user_prompt(prompt_name)

    def send_chat(self, option=None) -> str:
        response = ""
        try:
            response = ollama.chat(model=self.model, messages=self.compose_messages())['message']['content']
            if option == "print":
                self.handler.print_response(response)
            elif option == "write":
                self.handler.write_to_file(response)

        except RuntimeError as error:
            print(f"Error: {error}")

        return response

    def compose_messages(self) -> list[dict]:
        return [
            {
                "role": "user",
                "content": "\n".join(self.loader.system_prompt)
            },
            # {
            #     "role": "user",
            #     "content": "\n".join(self.loader.user_prompt)
            # }
        ]
