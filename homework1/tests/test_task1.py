import subprocess
import os

def test_output():
    task1_path = os.path.join("src", "task1.py")
    result = subprocess.run(["python", task1_path], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello, World!"