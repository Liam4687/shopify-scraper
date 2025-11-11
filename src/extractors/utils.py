thonimport json

def load_settings(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def log_info(message):
    print(f"[INFO] {message}")

def log_error(message):
    print(f"[ERROR] {message}")