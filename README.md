# Fade-It

A tool to bypass censor filters by modifying text.

<img src="ss.png" width="50%" style="display: block; justify-content: center; margin: 0 auto; border-radius: 15px;">

## Compatibility 

- Linux
- Android (termux app)
- Windows (command prompt)
- Ios (ish app)

## Install Python3:

   Make sure you have Python 3 installed on your system. If it's not already installed, use the appropriate command for your platform:

   - For Linux:
     ```bash
     sudo apt-get update
     sudo apt-get install python3
     ```

   - For Android (using Termux):

     First download the `termux` app from playstore and use the commands.

     Install Python by running:
     ```bash
     pkg install python3
     ```

   - For Windows:

     You can download Python from the official website [Python.org](https://www.python.org/downloads/) or use a package manager like [Chocolatey](https://chocolatey.org/).

     ```powershell
     choco install python3
     ```

   - For Apple (ios):

     Since there is an issue with the app which can't clone directly from github so we will do the steps manually. (Skip the python installation as its already installed)

     1. Download the ish app from appstore.
     2. Open safari browser and open this repository from this [link](https://github.com/anonfaded/fade-it)
     3. Download from the `download` button, and the folder will be downloaded in `My Files` of your phone.
     4. Now open `My Files` app and navigate to `downloads` folder, you will find a folder named as `Fade-it`, copy or move this folder to ish's `root` directory. `ish > root > paste_folder_here`.
     5. Done! Now open the ish app and use command `ls`, you will see a folder on terminal as `Fade-it`, now navigate to it by `cd Fade-it/` and do `ls` again, now thats the script which we will use.
     6. Now run the script by command: `python3 fade-it.py`


## **Clone the Repository**

   Open your terminal or command prompt and clone this repository:

   ```bash
   git clone https://github.com/anonfaded/fade-it.git
   cd fade-it
   ```
   - The first command will clone this repo to your system.
   - The second will change the directory to fade-it where you will run the script.

## **Run the Script**

Execute the script with:

```bash
python3 fadeit.py
```
or this command:
```bash
./fadeit.py
```

The tool will guide you through the rest.