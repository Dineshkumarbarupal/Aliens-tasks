import os

# Base project folder
base = "ci-cd-ecommerce-project"

# Folder structure with files
structure = {
    "src": [
          "app.py",
          "templates/.keep", 
          "static/.keep"
    ],

    "tests": [
        "test_login.py",
        "test_products.py",
        "test_checkout.py",
        "conftest.py"
    ],

    "infrastructure": [
        "docker-compose.yml",
        "nginx.conf",
        "Dockerfile"
    ],

    ".github/workflows": [
        "ci-pipeline.yml",
        "cd-pipeline.yml",
        "security-scan.yml"
    ],

    "scripts": [
        "deploy.sh",
        "health-check.sh",
        "backup.sh"
    ]
}

# Extra root files
root_files = [
    "requirements.txt",
    "playwright.config.js",
    "pytest.ini",
    "README.md"
]

# Create directories + files
for folder, files in structure.items():
    folder_path = os.path.join(base, folder)
    os.makedirs(folder_path, exist_ok=True)

    for file in files:
        file_path = os.path.join(folder_path, file)

        # Create subfolders for templates/static if needed
        if "/" in file:
            subfolder = os.path.dirname(file_path)
            os.makedirs(subfolder, exist_ok=True)

        # Create empty file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("")  # blank file

# Create root files
for file in root_files:
    with open(os.path.join(base, file), "w", encoding="utf-8") as f:
        f.write("")

print("✅ Project structure created successfully!")
