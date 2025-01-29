import os
import json
import re

def sanitize_name(name):
    """Sanitize the project name to be safe for folder creation."""
    sanitized_name = re.sub(r'[<>:"/\\|?*]', '_', name)
    return sanitized_name.strip()

def create_structure(base_path, structure, readme_content):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if content is None:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            if path.endswith("readme.md"):
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(readme_content)
            elif path.endswith(".ipynb"):
                notebook_content = {
                    "cells": [],
                    "metadata": {},
                    "nbformat": 4,
                    "nbformat_minor": 5,
                }
                with open(path, 'w') as f:
                    json.dump(notebook_content, f, indent=4)
            else:
                with open(path, 'w') as f:
                    pass
        elif isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content, readme_content)

project_name = input("Enter the project name: ").strip()
sanitized_name = sanitize_name(project_name)

if not sanitized_name:
    print("Project name cannot be empty. Please run the script again.")
else:

    template = {
        "readme.md": None,
        "data": {},
        "documents": {},
        "drafts": {},
        "final": {},
        "sql": {},
        "notebooks": {
            f"{sanitized_name}.ipynb": None,
            "in": {},
            "out": {},
        },
    }
    readme_content = f"""# {sanitized_name}

#### tmahoney@pct.edu
This document is best viewed in [vscode](https://code.visualstudio.com/) or similar.
Special project instructions and notes can be recorded / found at the bottom of this document.

## Description
This project structure was initialized automatically.

## Folders Initialized
```bash
├───data
├───documents
├───drafts
├───final
├───notebooks
│   ├───in
│   └───out
└───sql
```
- `data` is for client-provided data.
- `documents` is for special instructions or requirements.
- `drafts` is for works in progress and not-finalized products.
- `final` is for the finished products.
- `notebooks` is for notebook-based activity.
    - `in` for data loaded into notebooks.
    - `out` for exports from notebooks.
- `sql` is for ad hoc or reference queries related to this project.

## Notes
Put your project notes here.
"""
    # Create the directory structure
    base_directory = os.path.join(".", sanitized_name)
    create_structure(base_directory, template, readme_content)
    print(f"{sanitized_name} template initialized")
