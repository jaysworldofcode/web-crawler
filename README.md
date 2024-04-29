# TEST - WEB CRAWLER

A web crawling test project to calculate and output some measurements of the crawled pages (something like page-rank)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install test - web crawler.

1. Clone the repo
   ```sh
   git clone https://bitbucket.org/ak-launch/test-web-crawler/src
   ```
3. Install pip packages
   ```sh
   pip install -r requirements.txt
   ```
4. Open .env file and change `GENERATED_REPORT` to your folder/path you want the report to be save

## Usage

```bash
python main.py {url} {recursion_depth_limit}

ex: python main.py https://news.ycombinator.com/ 2
```