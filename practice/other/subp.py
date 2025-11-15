import subprocess

chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" # Adjust for your OS and path
profile_name = "Profile 1" # Replace with the name of your desired profile

# Construct the command to open Chrome with the specified profile
command = [
    chrome_path,
    f"--profile-directory={profile_name}"
]

try:
    subprocess.Popen(command)
    print(f"Opened Chrome with profile: {profile_name}")
except FileNotFoundError:
    print(f"Error: Chrome executable not found at {chrome_path}")
except Exception as e:
    print(f"An error occurred: {e}")