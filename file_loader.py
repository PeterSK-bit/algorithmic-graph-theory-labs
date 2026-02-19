def load_file(file_path):
    try:
        return open(file_path, "r", encoding="utf-8")
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return None