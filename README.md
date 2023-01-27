# Description

This repository is used for sharing solution for testing assignment provided by VALA in "Multiples of A & B.pdf"


## How to setup local Python environment

1. Clone the repository

    ```bash
    git clone https://github.com/smalevanny/CodingAssignment.git

    ```

2. Install Python 3 on your local machine and check its version by running:
    ```bash
    python3 --version
    ```

3. Create local python3 virtual environment folder ".env". The folder name can be anything
   and it can be located also outside of project. Here is the example when it is located in the current directory.

    ```bash
    python3 -m venv .env
    ```

    Note that if something gets broken in this virtual environment libraries, you can always delete
    the created folder and its subfolders. Then start again by creating a new folder.


4. Activate local python virtual environment

    ```bash
    source .env/bin/activate
    ```

    On Windows, please use: `.env\Scripts\activate.bat`


5. Create a new input file you want program to work with or edit current "input.txt" file located in the root folder


6. To run a program navigate to virtual environment folder and run the following command:
    ```bash
    python main.py <input_file_name> <output_file_name>

    ```
   Example:
    ```bash
    python main.py input.txt output.txt

    ```
    
    