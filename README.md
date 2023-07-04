# Python 3 Installation Guide

This guide provides instructions on how to install Python 3 on different operating systems: Windows, GNU/Linux (Ubuntu), and macOS.

## Table of Contents

1. [Windows Installation](#windows-installation)
2. [GNU/Linux (Ubuntu) Installation](#gnulinux-ubuntu-installation)
3. [macOS Installation](#macos-installation)
4. [Verifying the Installation](#verifying-the-installation)
5. [Updating Python](#updating-python)
6. [Uninstalling Python](#uninstalling-python)
7. [Adding Python 3 and pip to PATH](#adding-python-3-and-pip-to-path)
8. [Additional Resources](#additional-resources)

## Windows Installation

1. Visit the official Python website: [https://www.python.org/downloads/windows](https://www.python.org/downloads/windows).
2. Scroll down to the **Python Releases for Windows** section.
3. Click on the **Latest Python 3 Release** link to download the installer.
4. Run the downloaded installer.
5. On the first installation screen, make sure to check the box **Add Python 3.x to PATH**.
6. Select the **Customize installation** option if you want to customize the installation directory and optional features.
7. Click **Next** and follow the prompts to complete the installation.

## GNU/Linux (Ubuntu) Installation

1. Open a terminal by pressing **Ctrl + Alt + T**.
2. Update the package list by running the following command:
   ```
   sudo apt update
   ```
3. Install Python 3 by running the following command:
   ```
   sudo apt install python3
   ```

## macOS Installation

1. Visit the official Python website: [https://www.python.org/downloads/macos](https://www.python.org/downloads/macos).
2. Scroll down to the **Python Releases for macOS** section.
3. Click on the **Latest Python 3 Release** link to download the installer.
4. Run the downloaded installer.
5. On the first installation screen, make sure to check the box **Install for all users** and **Add Python 3.x to PATH**.
6. Click **Install** and enter your administrator password if prompted.
7. Follow the prompts to complete the installation.

## Verifying the Installation

To verify the Python installation, follow these steps:

1. Open a terminal or command prompt.
2. Type the following command and press Enter:
   ```
   python3 --version
   ```
   This command will display the installed Python version.

## Updating Python

To update Python to the latest version, follow these steps:

1. Windows: Visit the official Python website and download the latest installer. Run the installer and select the **Upgrade Now** option.
2. GNU/Linux (Ubuntu): Open a terminal and run the following commands:
   ```
   sudo apt update
   sudo apt upgrade python3
   ```
3. macOS: Visit the official Python website and download the latest installer. Run the installer and select the **Upgrade Now** option.

## Uninstalling Python

To uninstall Python from your system, follow these steps:

1. Windows: Open the Control Panel, click on **Programs** or **Programs and Features**, locate Python in the list of installed programs, and click **Uninstall**.
2. GNU/Linux (Ubuntu): Open a terminal and run the following command:
   ```
   sudo apt remove python3
   ```
3. macOS: Locate the Python installation in the **Applications** folder and move it to the trash.

## Adding Python 3 and pip to PATH

To ensure that Python 3 and pip are added to the system's PATH variable, follow the instructions below:

### Windows

1. Press `Win + X` and select **"System"** from the context menu.
2. Click on **"Advanced system settings"** in the left sidebar.
3. In the **System Properties** window, click on the **"Environment Variables"** button.
4. Under the **"System variables"** section, find the **"Path"** variable and click **"Edit"**.
5. Click on **"New"** and add the path to your Python installation directory. It is typically `C:\Python3x` (where `x` represents the specific Python version).
6. Click **"OK"** to save the changes.

### GNU/Linux (Ubuntu) and macOS

1. Open a terminal.
2. Open the `.bashrc` or `.bash_profile` file in a text editor. For example, run the following command:
   ```
   nano ~/.bashrc
   ```
3. Add the following line at the end of the file:
   ```
   export PATH="$PATH:/path/to/python3/bin"
   ```
   Replace `/path/to/python3/bin` with the actual path to your Python 3 installation directory.
4. Save the changes and exit the text editor.
5. Run the following command to refresh the environment variables:
   ```
   source ~/.bashrc
   ```
   or
   ```
   source ~/.bash_profile
   ```

Now Python 3 and pip should be accessible from the command line. To verify, open a new terminal window and type `python3` or `pip3`, respectively.

## Additional Resources

- [Python Documentation](https://docs.python.org/): Official documentation for Python.
- [Python Package Index (PyPI)](https://pypi.org/): Repository of Python packages.
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html): Creating isolated Python environments.
- [Python Tutorial](https://docs.python.org/3/tutorial/index.html): Official Python tutorial for beginners.
- [Python Crash Course](https://ehmatthes.github.io/pcc/): A book for learning Python programming by Eric Matthes.