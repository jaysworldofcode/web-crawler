# Web-Crawler
Simply input the URL of any website you want to explore, and let it do the rest. It navigates through the site, indexing every page and extracting valuable information along the way.
It exports your crawled data in CSV format

## Requirements
- **Python**<br />

**Installation and usage** :<br />
    Clone the repository ```bash git clone <repository-url>```<br />
    Go to folder ```bash cd web-crawler```<br />
    Install requirements ```bash pip install -r /path/to/requirements.txt```<br />
    Open ```.env``` file and edit the output for your exported data<br />
    Run ```bash python main.py <target-url> <recursion depth limit (a positive integer)>```<br />