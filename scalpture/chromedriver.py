import os
import platform
import requests

# Get the operating system and architecture information
os_info = platform.system() + "_" + platform.architecture()[0]

# URL to download the ChromeDriver binary
url = f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{os_info}"

# Get the latest version number
response = requests.get(url)
version = response.text.strip()

# URL to download the binary
url = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_{os_info}.zip"

# Download the binary
response = requests.get(url)

# Create a directory to store the ChromeDriver binary
program_files = os.environ["ProgramFiles"]
chromedriver_dir = os.path.join(program_files, "ChromeDriver")
os.makedirs(chromedriver_dir, exist_ok=True)

# Write the binary to disk
chromedriver_path = os.path.join(chromedriver_dir, "chromedriver")
with open(chromedriver_path, "wb") as f:
    f.write(response.content)