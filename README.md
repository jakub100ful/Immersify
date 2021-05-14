# Immersify

A final year project.

# Prerequisities

You need to ensure that Python 3.6 or later is installed.

# Installation

1. Download a copy of the project.
2. Open a command prompt or terminal in the root folder (Immersify by default).
3. Type the following command to create a virtual environment: `python3 -m venv env`.
4. Enter the following command to activate the virtual environment depending on your operating system.

** On Windows: **
`env\Scripts\activate`

** On Unix or MacOS: **
`source env/bin/activate`

5. Install the required packages using pip by entering this command: `pip install -r requirements.txt`.
6. Navigate to the app folder within your command prompt `cd app`.
7. Start the application through this command `flask run`.

** If you are using MacOS and are having issues with SSL certificates **
Ensure that you have installed the neccessary SSL bundle. You can do this either by running the native Certificates.command file in the Python directory found in your Applications folder, or by installing the certifi package through pip.

For more information view this article: https://stackoverflow.com/questions/40684543/how-to-make-python-use-ca-certificates-from-mac-os-truststore
