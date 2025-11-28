# Import required libraries
import os
import logging

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('log/user-dashboard.log'),
        logging.StreamHandler()
    ]
)

# Check if the project is installed as a package
if os.path.isfile('requirements.txt'):
    # If it's installed, check if all dependencies are installed
    try:
        import pkg_resources
        installed = {pkg.key for pkg in pkg_resources.working_set}
        reqs = {req.key for req in pkg_resources.parse_requirements('requirements.txt')}
        missing = reqs - installed
        if missing:
            logging.error(f"Missing dependencies: {missing}")
            exit(1)
    except ImportError:
        logging.error("Missing 'pkg_resources' module")
        exit(1)

# If the project is not installed, check if it's a git repository
if os.path.exists('.git'):
    # If it's a git repository, check if the repository is up-to-date
    try:
        import subprocess
        subprocess.run(['git', 'fetch', '--all'], check=True)
        subprocess.run(['git', 'pull', 'origin', 'master'], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to update repository: {e}")
        exit(1)

# If the project is not installed and not a git repository, exit with an error
logging.error("This script must be run in a user-dashboard project directory")
exit(1)