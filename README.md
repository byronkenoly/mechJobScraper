# Job web scraper

Scrapes the web for recently posted mechanical engineering jobs in Kenya
## Installation Guide

1. Make sure python 3.9 or higher is installed in your machine
2. Create virtual environment

    ```python3 -m venv venv```
    
3. Activate virtual environment with following commands. Check [here](https://docs.python.org/3/library/venv.html)

    ```source venv/bin/activate``` for linux distros
    
    and
    
    ```venv\Scripts\activate.bat``` for Windows cmd
 
4. Install required dependencies (BeautifulSoup, lxml, requests) from requirement.txt file using the command 

    ```pip install -r requirement.txt```

5.  Run the command below in your terminal to get top job suggestions.Internet connection required

    ```python main.py```
