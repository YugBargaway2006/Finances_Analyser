import subprocess
import sys

def main():
    install_package("pandas")
    install_package("colorama")
    install_package("sqlalchemy")
    install_package("requests")
    install_package("prettytable")
    
    
def install_package(package_name):
    try:
        # Run pip install command
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"Successfully installed {package_name}")
        
    except Exception as err:
        print(f"Error occurred while installing {package_name}: {err}")


main()