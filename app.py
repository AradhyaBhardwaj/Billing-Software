import os

if __name__ == "__main__":
    script_path = os.path.join(".", "Homepage.py")
    if os.path.exists(script_path):
        # Dynamically execute Homepage.py with explicit encoding
        with open(script_path, "r", encoding="utf-8") as file:
            script_code = file.read()
        exec(script_code, globals())
    else:
        print(f"Error: The script '{script_path}' does not exist.")
