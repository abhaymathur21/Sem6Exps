import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint

app = typer.Typer()


@app.command("hi")
def sample_func():
    rprint("[red bold]Hi[/red bold] [yellow]World[yellow]")

@app.command("hello")
def sample_func():
    rprint("[red bold]Hello[/red bold] [yellow]World[yellow]")
    
@app.command("list")
def sample_func():
    subprocess.run('dir', shell=True)
    
@app.command("new_dir")
def sample_func():
    subprocess.run('mkdir new_dir', shell=True)
    
@app.command("custom_new_dir")
def sample_funct():
    module_list_question = questions = [
        {
            'type': 'list',
            'name': 'username',
            'message': 'Select any one username: ',
            'choices': [
                        {
                            'name': 'Abhay',
                        },
                        {
                            'name': 'Naman',
                        },
                        {
                            'name': 'Shreya ',
                        },
                        {
                            'name': 'Shruti ',
                        },
            ],
        }
    ]

    username = prompt(module_list_question)

    rprint("[yellow]=============================================[yello]")
    rprint("[green bold]Enter folder name :[green bold]")
    folder_name = input()


    subprocess.run(f"mkdir {folder_name}_created_by_{username['username']}", shell=True)


@app.command("new_file")
def sample_funct():
    module_list_question = questions = [
        {
            'type': 'list',
            'name': 'file_type',
            'message': 'Select the file you want to create: ',
            'choices': [
                        {
                            'name': 'README.md',
                        },
                        {
                            'name': 'requirements.txt',
                        },
                        {
                            'name': 'setup.sh ',
                        },
            ],
        }
    ]

    file_type = prompt(module_list_question)

    rprint("[yellow]=============================================[yello]")
    rprint("[green bold]Enter content to be put in file :[green bold]")
    file_content = input()


    subprocess.run(f"echo {file_content} > {file_type['file_type']}", shell=True)


if __name__ == "__main__":
    app()   