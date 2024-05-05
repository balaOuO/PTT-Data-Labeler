import os
import json
from rich.console import Console
from rich.table import Table
from rich.traceback import install

console = Console()
install(show_locals=True)

class FormatException(Exception):
    def __init__(self, message: str):
        super().__init__(message) 

def find_json_files(directory : str) -> list[str]:
    json_files : list[str] = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

def read_json_file(file_path : str) -> list | dict:
    try:
        with open(file_path, 'r') as file:
            data : list | dict = json.load(file)
            file.close()
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        raise json.JSONDecodeError(f"Unable to decode JSON from '{file_path}'.", "")
    
def count_json_length(json_file) -> int:
    if isinstance(json_file, list):
        return len(json_file)
    else:
        raise FormatException("JSON file does not contain a list.")

def main():
    target_directory = './result'
    json_files = find_json_files(target_directory)

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("File", justify="left")
    table.add_column("Count" , justify="center")
    total_count = 0
    for file in json_files:
        json_object = read_json_file(file)
        json_length = count_json_length(json_object)
        
        total_count += json_length
        table.add_row(file, f"{json_length}")

    table.add_row("[green]Total", f"[green]{total_count}")
    console.print(table)

if __name__ == "__main__":
    main()

