# Django Installation Guide

This guide provides instructions on how to install the Django web framework in Windows, GNU/Linux (Ubuntu), or macOS using a virtual environment.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Windows Installation](#windows-installation)
3. [GNU/Linux (Ubuntu) Installation](#gnulinux-ubuntu-installation)
4. [macOS Installation](#macos-installation)
5. [Creating a Virtual Environment](#creating-a-virtual-environment)
6. [Installing Django](#installing-django)
7. [Verifying the Installation](#verifying-the-installation)
8. [Additional Resources](#additional-resources)

## Prerequisites

Before installing Django, make sure you have the following:

- Python 3 installed (Refer to the [Python Installation Guide](https://github.com/Axlfc/python3-course/blob/master/README.md) for installation instructions).
- Pip package manager installed (Usually comes with Python by default).

## Windows Installation

1. Open a command prompt.
2. Create a new directory for your Django project (optional).
3. Navigate to the directory where you want to create your Django project (if applicable).
4. Create a new virtual environment by running the following command:
   ```
   python -m venv myenv
   ```
   Replace `myenv` with the desired name for your virtual environment.
5. Activate the virtual environment:
   - Command Prompt:
     ```
     myenv\Scripts\activate
     ```
   - PowerShell:
     ```
     myenv\Scripts\Activate.ps1
     ```
6. Continue with the [Installing Django](#installing-django) section.

## GNU/Linux (Ubuntu) Installation

1. Open a terminal.
2. Create a new directory for your Django project (optional).
3. Navigate to the directory where you want to create your Django project (if applicable).
4. Install the virtual environment package by running the following command:
   ```
   sudo apt install python3-venv
   ```
5. Create a new virtual environment by running the following command:
   ```
   python3 -m venv myenv
   ```
   Replace `myenv` with the desired name for your virtual environment.
6. Activate the virtual environment:
   ```
   source myenv/bin/activate
   ```
7. Continue with the [Installing Django](#installing-django) section.

## macOS Installation

1. Open a terminal.
2. Create a new directory for your Django project (optional).
3. Navigate to the directory where you want to create your Django project (if applicable).
4. Create a new virtual environment by running the following command:
   ```
   python3 -m venv myenv
   ```
   Replace `myenv` with the desired name for your virtual environment.
5. Activate the virtual environment:
   ```
   source myenv/bin/activate
   ```
6. Continue with the [Installing Django](#installing-django) section.

## Creating a Virtual Environment

1. Open a command prompt or terminal.
2. Navigate to the directory where you want to create your Django project (if not already there).
3. Create a new virtual environment by running the following command:
   ```
   python3 -m venv myenv
   ```
   Replace `myenv` with the desired name for your virtual environment.

## Installing Django

1. Activate the virtual environment:
   - Windows (Command Prompt):
     ```
     myenv\Scripts\activate
     ```
   - Windows (PowerShell):
     ```
     myenv\Scripts\Activate.ps1
     ```
   - GNU/Linux or macOS:
     ```
     source myenv/bin/activate
     ```
2. Use pip to install Django by running the following command:
   ```
   pip install django
   ```

## Verifying the Installation

To verify the Django installation, follow these steps:

1. Make sure the virtual environment is activated.
2. Open a command prompt or terminal.
3. Run the following command:
   ```
   python -m django --version
   ```
   This command will display the installed Django version.

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/): Official documentation for Django.
- [Django Tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/): Official Django tutorial for beginners.
- [Django Girls Tutorial](https://tutorial.djangogirls.org/): A beginner-friendly Django tutorial.
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html): Creating isolated Python environments.
- [Python Package Index (PyPI)](https://pypi.org/): Repository of Python packages.