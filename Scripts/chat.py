import json
from datetime import datetime
from openai import OpenAI
from argparse import ArgumentParser
import os

def generate_fname():
    # Get the current time
    now = datetime.now()

    # Format the date and time
    timestamp = now.strftime("%Y%m%d-%H%M%S")

    # Create a filename with the current date and time
    filename = f"file-{timestamp}.json"
    return filename

def dump_reply(data):
    # Generate a filename
    filename = generate_fname()

    # Create a folder that will contain model replies
    path = "Data/"
    if not os.path.exists(path):
        os.mkdir(path)

    # Save LM Studio reply to a json file
    with open(path + filename, 'w') as f_out:
        json.dump({"reply": data}, f_out)

def request(kwargs):
    # Set up request inputs
    port = kwargs['port']
    user_text = kwargs['input']
    system_prompt = kwargs['system_prompt']
    
	# Point to the local server
    client = OpenAI(base_url=f"http://localhost:{port}/v1", api_key="not-needed")
    completion = client.chat.completions.create(
        model="local-model", # this field is currently unused
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ],
        temperature=0.7,
    )
    
    return completion.choices[0].message.content

def main(kwargs):
    # Request a model reply from the LM Studio Local Server
    response = request(kwargs)

    # Save the reply to a file
    dump_reply(response)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", "--port", dest="port", type=int, help="a port number")
    parser.add_argument("-i", "--input-prompt", dest="input", type=str, help="user input text")
    parser.add_argument("-s", "--system-prompt", dest="system_prompt", type=str, help="system prompt text")
    args = parser.parse_args()
    main(vars(args))
    pass