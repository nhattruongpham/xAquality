from huggingface_hub import HfApi
import os

repo_id = "cbbl-skku-org/xAquality"
repo_type = "space"

api = HfApi()


def upload_files():
    print(f"Checking if repository {repo_id} exists...")
    try:
        api.repo_info(repo_id=repo_id, repo_type=repo_type)
    except Exception:
        print(f"Creating repository {repo_id}...")
        api.create_repo(repo_id=repo_id, repo_type=repo_type, space_sdk="gradio")

    print(f"Uploading files to {repo_id}...")

    # Upload app.py
    api.upload_file(
        path_or_fileobj="app.py",
        path_in_repo="app.py",
        repo_id=repo_id,
        repo_type=repo_type,
    )

    # Upload README.md
    api.upload_file(
        path_or_fileobj="README.md",
        path_in_repo="README.md",
        repo_id=repo_id,
        repo_type=repo_type,
    )

    # Upload requirements.txt
    api.upload_file(
        path_or_fileobj="requirements.txt",
        path_in_repo="requirements.txt",
        repo_id=repo_id,
        repo_type=repo_type,
    )

    # Upload checkpoints
    checkpoints_dir = "checkpoints"
    for root, dirs, files in os.walk(checkpoints_dir):
        for file in files:
            file_path = os.path.join(root, file)
            path_in_repo = os.path.join(checkpoints_dir, file)
            print(f"Uploading {file_path}...")
            api.upload_file(
                path_or_fileobj=file_path,
                path_in_repo=path_in_repo,
                repo_id=repo_id,
                repo_type=repo_type,
            )

    # Upload figures
    figures_dir = "figures"
    if os.path.exists(figures_dir):
        for root, dirs, files in os.walk(figures_dir):
            for file in files:
                file_path = os.path.join(root, file)
                path_in_repo = os.path.join(figures_dir, file)
                print(f"Uploading {file_path}...")
                api.upload_file(
                    path_or_fileobj=file_path,
                    path_in_repo=path_in_repo,
                    repo_id=repo_id,
                    repo_type=repo_type,
                )

    citations_dir = "citations"
    if os.path.exists(citations_dir):
        for root, dirs, files in os.walk(citations_dir):
            for file in files:
                file_path = os.path.join(root, file)
                path_in_repo = os.path.join(citations_dir, file)
                print(f"Uploading {file_path}...")
                api.upload_file(
                    path_or_fileobj=file_path,
                    path_in_repo=path_in_repo,
                    repo_id=repo_id,
                    repo_type=repo_type,
                )


if __name__ == "__main__":
    try:
        upload_files()
        print("Upload successful!")
    except Exception as e:
        print(f"Error during upload: {e}")
