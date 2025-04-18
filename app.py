import os

if __name__ == "__main__":
    script_path = os.path.join(".", "Homepage.py")
    if os.path.exists(script_path):
        # Import and execute Homepage.py directly
        import Homepage
    else:
        print(f"Error: The script '{script_path}' does not exist.")
