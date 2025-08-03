import os


class ResponseHandler:
    def __init__(self):
        pass

    @staticmethod
    def print_response(response: str):
        print(response)

    @staticmethod
    def write_to_file(response: str):
        index = len(os.listdir("responses"))
        with open(f"responses/response_{index}.txt", "w") as fd:
            fd.write(response)
