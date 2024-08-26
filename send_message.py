#!/home/violet/git/violet/automation/matrix_notifier/.venv/bin/python
import argparse
from typing import Optional
import requests
import sys


class SendMessageNamespace(argparse.Namespace):
    message: str
    file: Optional[str]


def read_message(args:SendMessageNamespace):
    # Read from stdin if no arguments or files are provided
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()

    # Read from command line argument if provided
    if args.message:
        return args.message

    # Read from a file if the filename is provided
    if args.file:
        with open(args.file, 'r') as file:
            return file.read().strip()

    raise ValueError("No message provided. Please provide a message via stdin, as an argument, or in a file.")


def send_message(message):
    url = 'http://127.0.0.1:31471/send'
    headers = {'Content-Type': 'application/json'}
    data = {'message': message}
    response = requests.post(url, json=data, headers=headers)
    return response.json()


def main():
    parser = argparse.ArgumentParser(description='Send a message to the Matrix server.')
    parser.add_argument('message', nargs='?', help='Message to send', default=None)
    parser.add_argument('-f', '--file', help='Read message from a file', default=None)
    args = parser.parse_args(namespace=SendMessageNamespace())

    try:
        message = read_message(args)
        response = send_message(message)
        print("Response from server:", response)
    except Exception as e:
        print("Error:", e)


if __name__ == '__main__':
    main()
