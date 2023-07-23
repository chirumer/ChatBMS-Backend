import time

EOT = '\u2404'


def chat(prompt):
    example_response = 'this is an example response'

    for word in example_response.split():
        time.sleep(1)
        yield word