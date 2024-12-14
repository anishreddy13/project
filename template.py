import os

def create_project_structure(base_dir):
    """
    Create the project directory hierarchy.
    """
    folders = [
        os.path.join(base_dir, "models"),  # Saved models folder
        os.path.join(base_dir, "notebooks"),  # Jupyter notebooks folder
        os.path.join(base_dir, "webapp"),
        os.path.join(base_dir, "webapp", "static"),  # Static files for frontend
        os.path.join(base_dir, "webapp", "templates"),  # HTML templates
        os.path.join(base_dir, "logs"),  # Logs folder
        os.path.join(base_dir, "scripts"),  # Utility scripts
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    print(f"Project structure created under '{base_dir}'")

def create_placeholder_files(base_dir):
    """
    Create placeholder files for initial project setup.
    """
    placeholders = {
        os.path.join(base_dir, "README.md"): "# Project Title\n\nThis project involves building and deploying models for disease prediction.",
        os.path.join(base_dir, "requirements.txt"): "# Add project dependencies here\nflask\npandas\njoblib\nsklearn\n",  # Example dependencies
        os.path.join(base_dir, "notebooks", "template.ipynb"): "",  # Empty notebook template
        os.path.join(base_dir, "webapp", "app.py"): """
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Disease Prediction App"

if __name__ == '__main__':
    app.run(debug=True)
""",
        os.path.join(base_dir, "logs", "log.txt"): "# Log file\n",
    }

    for file_path, content in placeholders.items():
        with open(file_path, "w") as f:
            f.write(content)

    print("Placeholder files created.")

if __name__ == "__main__":
    # Define the base directory for the project
    base_directory = os.path.abspath(".")  # Current directory

    # Create the directory hierarchy
    create_project_structure(base_directory)

    # Create placeholder files
    create_placeholder_files(base_directory)

    print("Project setup is complete. You can now start adding your code and data.")
