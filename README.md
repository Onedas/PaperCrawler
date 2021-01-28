# PaperCrawler

- **ECCV** 
  [[2018 & 2020]](https://www.ecva.net/papers.php)

- **CVPR** 
  [[2018]](https://openaccess.thecvf.com/CVPR2018),
  [[2019]](https://openaccess.thecvf.com/CVPR2019),
  [[2020]](https://openaccess.thecvf.com/CVPR2020)

- **Open Review**
  - **ICLR** 
    [[2019]](https://openreview.net/group?id=ICLR.cc/2019/Conference),
    [[2020]](https://openreview.net/group?id=ICLR.cc/2020/Conference)

## Pre-requisites

 - Python 3
 - chromedriver


## How to start

---
### 1. Installation

---
#### - 1.1 Clone this repo:
```commandline
git clone https://github.com/Onedas/PaperCrawler.git
```
---
#### - 1.2 Install chromedriver

```commandline
cd PaperCrawler
mkdir chromedriver
```

You can download the chromedriver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)

You must download the same version of chromedriver as your Chrome.
See https://www.chromium.org/developers/version-numbers for more details.

Move the chromedriver in the `../PaperCrawler/chromedriver` directory like this .`../PaperCrawler/chromedriver/chromedriver.exe`

---
#### - 1.3 Install requests, beautifulsoup4, and selenium

- For pip users, please type the command
  
```commandline
pip install -r requirements.txt
```
or
```commandline
pip install requests
pip install beautifulsoup4
pip install selenium
```
---
- For conda users, you can create a new Conda environment and install, using 
    
```commandline
conda env create -f environment.yml
```
or
```commandline
conda create -n PaperCrawler python=3.6
conda install -c anaconda requests
conda install -c anaconda beautifulsoup4
conda install -c conda-forge selenium
```
---
### 2. How to Use

---
####  ECCV crawler
- default
```commandline
python ECCV_crawler.py 
```
- optional
```commandline
python ECCV_crawler.py --keyword [keyword]
```
---
#### CVPR crawler
- default
```commandline
python CVPR_crawler.py --years [years]
```
- optional
```commandline
python CVPR_crawler.py --years [years] --keyword Video
```
---
#### ICLR crawler
- default
```commandline
python OpenReview_ICLR_crawler.py --years [years]
```
- optional
```commandline
python OpenReview_ICLR_crawler.py --years [years] --keyword Video
```
---