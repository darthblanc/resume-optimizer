from ollama_client import OllamaClient
import sys

if "__main__" == __name__:
    args = sys.argv
    # print(args)
    client = OllamaClient()
    with open(f"prompts/job_descriptions/{args[1]}.txt", "r") as fd:
        job_description = fd.read()
    client.set_job_description(job_description, "prompt0")
    with open(f"prompts/resumes/{args[2]}.txt", "r") as fd:
        resume_content = fd.read()
    client.set_resume_content(resume_content)
    print("sending...")
    response = client.send_chat(option="write")
    print("done")
