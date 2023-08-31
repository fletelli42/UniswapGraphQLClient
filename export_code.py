import os

def walk_dir(directory, output_file):
    for root, dirs, files in os.walk(directory):
        if 'venv' in root:  # Skip the virtual environment directory
            continue
        for file in files:
            if file.endswith('.py'):  # Only include Python files
                # Skip the script itself
                if file == 'export_script.py':
                    continue
                output_file.write(f"===== {os.path.join(root, file)} =====\n")
                with open(os.path.join(root, file), 'r') as f:
                    output_file.write(f.read())
                output_file.write("\n\n")

with open('project_export.txt', 'w') as output_file:
    walk_dir('.', output_file)
