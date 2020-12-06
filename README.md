# Terminolator

Are you tired of the cumbersome process of creating a terminology with excel? Fear no more, this tool will make things much easier for you.

> This project is still in progress, so the results might not be as expected. Therefore, feedbacks are welcome. 

## How to use?

**REQUIREMENTS:**
* Python3 - you need to install python3.
    * Installation for [Windows](https://realpython.com/installing-python/#how-to-install-from-the-microsoft-store)
    * Installation for [MacOS](https://realpython.com/installing-python/#how-to-install-from-the-official-installer)
* Basic command-line usage
    * Windows:
    ```
  - Press the `Windows Home` key.
  - Type `Powershell`.
  - Press `Enter`.
    ```
  `python --version`
  * MacOS
  ```
  - Press the `Cmd + Space` keys.
  - Type `Terminal`.
  - Press `Enter`.
    ```
  `python3 --version`

**STEPS:**
* You can either clone the project or download it as a [**zipfile**](https://github.com/ataknz/terminolator/archive/master.zip).
* Open your command-line, and go to the directory where you download the project.
    ```
    cd Desktop/terminolator
    ```
* Create your source file with `.txt` extension inside the project's directory. 
* Run the following command from your terminal to install required packages.
    * Windows: `pip instal requirements.txt`
    * MacOS:   `pip3 install requirements.txt`
* Run the following command from your terminal with **your** source file. 
  * Windows: `python create_terminology.py test.txt`
  * MacOS:   `python3 create_terminology.py test.txt`
## P.S

The results are not stable yet. So, comparison and revision between excel and source file is **highly recommended**. Also, process time can differ according to the source file. 
