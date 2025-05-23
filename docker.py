import subprocess
from rich.console import Console
from rich.table import Table
from rich import print
import sys

def docker_ps():
    docker = subprocess.run(['docker', 'ps', '-a'], capture_output=True, text=True)
    if docker.returncode == 0:
        print(docker.stdout)
    else:
        print(docker.stderr)


def docker_images():
    docker = subprocess.run(['docker', 'images'], capture_output=True, text=True)
    if docker.returncode == 0:
        print(docker.stdout)
    else:
        print(docker.stderr)


def docker_system_info():
    docker = subprocess.run(['docker', 'system', 'info'], capture_output=True, text=True)
    if docker.returncode == 0:
        print(docker.stdout)
    else:
        print(docker.stderr)

def docker_system_df():
    docker = subprocess.run(['docker', 'system', 'df'], capture_output=True, text=True)
    if docker.returncode == 0:
        print(docker.stdout)
    else:
        print(docker.stderr)

def docker_start():
    docker = subprocess.run(['docker', 'ps', '-a'], capture_output=True, text=True)
    if docker.returncode == 0:
        print(docker.stdout)
    else:
        print(docker.stderr)
    start = input("Enter a container id to start: ")
    subprocess.run(['docker', 'start', start], capture_output=True, text=True)

def docker_stop():
    docker = subprocess.run(['docker', 'ps', '-a'], capture_output=True, text=True)
    if docker.returncode == 0:
        print(docker.stdout)
    else:
        print(docker.stderr)
    stop = input("Enter a container id to stop: ")
    subprocess.run(['docker', 'stop', stop], capture_output=True, text=True)

def check(test):
    if test == "2":
        return test
    if test == "1":
        sys.exit()
    sel = ["1", "2"]
    while test not in sel:
            console.log("Please enter either 1 or 2")
            test = console.input("[bold red]Select 1 to exit |""[bold green]| Select 2 to continue: ")
    return test



# Main
test = ""
while test != "1":
    print()
    table = Table(title="Docker Commands")
    table.add_column("NUM", style="green")
    table.add_column("TASK", style="red")
    table.add_column("Description", style="blue")

    table.add_row("1", "docker_ps", "This command will list all of the current running containers.")
    table.add_row("2", "docker_images", "This command will list all of the images.")
    table.add_row("3", "docker_system_info", "This command will show the information of the docker install")
    table.add_row("4", "docker_df", "This command will show the disk space used for the docker build.")
    table.add_row("5", "docker_start", "This command will start a container for you.")
    table.add_row("6", "docker_stop", "This command will stop a container for you.")
    console = Console()
    console.print(table)
    print()
    selection = input("enter a number to execute the command: ")
    if selection == "1":
        docker_ps()
    elif selection == "2":
        print()
        docker_images()
        print()
    elif selection == "3":
        print()
        docker_system_info()
        print()
    elif selection == "4":
        print()
        docker_system_df()
        print()
    elif selection == "5":
        print()
        docker_start()
        print()
    elif selection == "6":
        print()
        docker_stop()
        print()
    else:
        console.log("[bold red]Please enter a valid choice!")
    print()
    test = console.input("[bold red]Select 1 to exit |""[bold green]| Select 2 to continue: ")
    if test != "1":
        x = check(test)
        if x == "1":
            sys.exit()
