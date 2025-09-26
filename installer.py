import os
import sys
import subprocess

def run_command(cmd, desc):
    print(f"\n▶ {desc} ...")
    try:
        subprocess.check_call(cmd, shell=True)
        print(f"✓ {desc} completed")
    except subprocess.CalledProcessError as e:
        print(f"❌ {desc} failed: {e}")
        sys.exit(1)

def main():
    print("🚀 Starting ATTools installation...")

    # Ensure pip.ini exists
    pip_dir = os.path.join(os.environ["APPDATA"], "pip")
    os.makedirs(pip_dir, exist_ok=True)
    pip_ini_path = os.path.join(pip_dir, "pip.ini")

    pip_ini_content = """[global]
extra-index-url = https://ausartifactory.amd.com/artifactory/api/pypi/hw-cpe-prod-virtual/simple
trusted-host = ausartifactory.amd.com
"""
    with open(pip_ini_path, "w") as f:
        f.write(pip_ini_content)
    print(f"📂 pip.ini written to {pip_ini_path}")

    # Set AT_PATH
    at_path = r"C:\Scripts\atlogs"
    os.makedirs(at_path, exist_ok=True)
    os.system(f'setx AT_PATH "{at_path}" /M')
    print(f"📂 AT_PATH set to {at_path}")

    # Upgrade pip
    run_command(f'"{sys.executable}" -m pip install --upgrade pip', "Upgrading pip")

    # Install AT packages
    packages = ["attools", "atpsim", "atm", "atreboot", "attestsuite"]
    run_command(f'"{sys.executable}" -m pip install --upgrade ' + " ".join(packages),
                "Installing AT packages")

    # Ensure Scripts folder is on PATH
    scripts_path = os.path.join(os.path.dirname(sys.executable), "Scripts")
    os.system(f'setx PATH "%PATH%;{scripts_path}" /M')
    print(f"📂 Added {scripts_path} to PATH")

    print("\n🎉 Installation finished! Open a new Command Prompt and try:")
    print("   atm --version")
    print("   attools --help")

if __name__ == "__main__":
    main()
