from openai import OpenAI
from argparse import ArgumentParser

def main(kwargs):
	# Point to the local server
	client = OpenAI(base_url=f"http://localhost:1234/v1", api_key="not-needed")
	completion = client.chat.completions.create(
        model="local-model", # this field is currently unused
        messages=[
            {"role": "system", "content": "Always answer in rhymes."},
            {"role": "user", "content": "Introduce yourself."}
        ],
        temperature=0.7,
	)
	return completion.choices[0].message

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", "--port", dest="port", help="a port number")
    args = parser.parse_args()
    main(vars(args))
    pass