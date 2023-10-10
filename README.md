# Scrape ChatGPT

**Scrape ChatGPT** is a Python application designed to scrape all your chat interactions from your ChatGPT account and convert them into Markdown (.md) files. These Markdown files are optimized for compatibility with the [Editor Syntax Highlight plugin for Obsidian](https://github.com/deathau/cm-editor-syntax-highlight-obsidian), ensuring that your chat conversations are not only easily readable but also editable, searchable, and accessible offline.

## Installation
To set up Scrape ChatGPT on your system, follow these steps:

1. Clone or Download the Repository: You can either clone this repository using Git or download it as a ZIP file and extract it to your preferred directory.
```
git clone https://github.com/radovan-sendek/scrapeChatGPT.git
```
2. Create a Virtual Environment (Optional, but recommended): It's a good practice to create a virtual environment to isolate your project dependencies. Here is an example of doing it with pipenv:

    2.1 First install pipenv if not already installed.
    ```
    pip install pipenv
    ```
    2.2 Change directory to the project folder (if not already there).
    ```
    cd /path/to/the/project
    ```
    2.3 Create and activate a virtual environment using `pipenv` and `Pipfile.lock`. You will need python 3.10 or later.
    ```
    pipenv install --ignore-pipfile
    ``` 
    or
    
    You can also create and activate a virtual environment using `pipenv` and `requirements.txt` file. You will     need python 3.10 as well.
    ```
    pipenv install -r requirements.txt
    ```
3. Activate the virtual environment.
    ```
    pipenv shell
    ```
4. Start the app.
    ```
    python main.py
    ```

At this point the app window should show up and the app should be ready to run.

## License

This project is open-source and free for everyone to use, modify, and distribute. You are encouraged to contribute to its development and improvement. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions, issues, or suggestions related to this project, you can reach out to me on GitHub or via email at radovan.sendekovic91@gmail.com.

## Known Issues

SSL Certificates: If you have SSL certificates installed from the Serbian government, the application may encounter issues. We are actively working to address this problem in future releases.
