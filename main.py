import importlib
import os
from dotenv import load_dotenv

# from update_trigger_output import generate_jsonl_file  # Replace with your actual function name
import subprocess

load_dotenv()

if __name__ == "__main__":
    # Call the function to generate the JSONL file
    # generate_jsonl_file()

    try:
        print("Running subprocess...")

        cmd = ["python3", "update_trigger_output.py"]
        subprocess.Popen(cmd)
        print("Subprocess completed.")

    except subprocess.CalledProcessError:
        print("Script execution failed.")
    except FileNotFoundError:
        print("Python interpreter or the script was not found.")
        
    print("Running app...")
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8080))
    app_advertisements = importlib.import_module("advertisements.api.app")
    app_advertisements.run(host=host, port=port)
    print("App is running.")
