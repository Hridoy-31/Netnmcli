#!/usr/bin/env python3

# for parsing command line arguments
import argparse

# for interacting with the operating system's CLI
import subprocess

def create_nmspace(namespace_name):
    try:
        # check = True is used for checking errors in command execution
        subprocess.run(["ip", "netns", "add", namespace_name], check=True)
        print(f"Network namespace \"{namespace_name}\" created successfully.")
    except subprocess.CalledProcessError:
        print(f"Error: Failed to create network namespace \"{namespace_name}\".")


def connect_nmspaces(namespace_name1, namespace_name2):
    try:
        subprocess.run(["ip", "link", "add", f"veth-{namespace_name1}", "type", "veth", "peer", "name", 
                        f"veth-{namespace_name2}"], check=True)
        # setting up one end of the veth pair 
        subprocess.run(["ip", "link", "set", f"veth-{namespace_name1}", "netns", namespace_name1], check=True)
        # setting up another end of the veth pair
        subprocess.run(["ip", "link", "set", f"veth-{namespace_name2}", "netns", namespace_name2], check=True)

        # setting the veth pairs in up (active) state
        subprocess.run(["ip", "netns", "exec", namespace_name1, "ip", "link", "set", f"veth-{namespace_name1}",
                       "up"], check=True)
        subprocess.run(["ip", "netns", "exec", namespace_name2, "ip", "link", "set", f"veth-{namespace_name2}",
                        "up"], check=True)
        
        # adding different ip addresses to both ends of the veth pair
        subprocess.run(["ip", "netns", "exec", namespace_name1, "ip", "addr", "add", "10.0.0.100/24", "dev",
                        f"veth-{namespace_name1}"], check=True)
        subprocess.run(["ip", "netns", "exec", namespace_name2, "ip", "addr", "add", "10.0.0.200/24", "dev",
                        f"veth-{namespace_name2}"], check=True)
        
        print(f"Network namespaces {namespace_name1} and {namespace_name2} are connected with veth pair successfully.")
    except subprocess.CalledProcessError:
        print(f"Error: Failed to connect network namespaces {namespace_name1} and {namespace_name2}.")
        

def list_nmspaces():
    try:
        namespace_list = subprocess.check_output(["ip", "netns", "list"])
        # subprocess.check_output returns byte strings. So, decode() method is used to convert the byte strings
        # to the regular strings.
        namespaces = namespace_list.decode().splitlines()
        print("Existing network namespaces: ")
        for namespace in namespaces:
            print(namespace)
    except subprocess.CalledProcessError:
        print("Error: Failed to list existing network namespaces.")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""A Tool for Network Namespace Management 
                                     and Veth Connection""")
    # for creating multiple arguments in the command with their own set of functionalities
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    """
    "create" command subparsers
    """
    create_parser = subparsers.add_parser("create", help="Create a new network namespace.")
    create_parser.add_argument("namespace_name", help="Name of the new network namespace.")

    """
    "connect" command subparsers
    """
    connect_parser = subparsers.add_parser("connect", help="Connect two network namespaces with veth pair.")
    connect_parser.add_argument("namespace_name1", help="Name of the first network namespace for creating a connection.")
    connect_parser.add_argument("namespace_name2", help="Name of the other network namespace to be connected with the first network namespace")

    """
    "list" command subparsers
    """
    list_parser = subparsers.add_parser("list", help="List all existing network namespaces.")



    # parsing the arguments from command and storing in args
    args = parser.parse_args()

    if args.command == "create":
        create_nmspace(args.namespace_name)
    elif args.command == "connect":
        connect_nmspaces(args.namespace_name1, args.namespace_name2)
    elif args.command == "list":
        list_nmspaces()
