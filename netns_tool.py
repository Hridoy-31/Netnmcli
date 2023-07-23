#!/usr/bin/env python3

# for parsing command line arguments
import argparse

# for interacting with the operating system's CLI
import subprocess

def create_nmspace(namespace_name):
    try:
        # check = True is used for checking errors in command execution
        subprocess.run(['ip', 'netns', 'add', namespace_name], check=True)
        print(f"Network namespace \"{namespace_name}\" created successfully.")
    except subprocess.CalledProcessError:
        print(f"Error: Failed to create network namespace \"{namespace_name}\".")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""A Tool for Network Namespace Management 
                                     and Veth Connection""")
    # for creating multiple arguments in the command with their own set of functionalities
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    """
    "Create" command subparsers
    """
    create_parser = subparsers.add_parser("create", help="Create a new network namespace.")
    create_parser.add_argument("namespace_name", help="Name of the new network namespace.")

    # parsing the arguments from command and storing in args
    args = parser.parse_args()

    if args.command == "create":
        create_nmspace(args.namespace_name)
