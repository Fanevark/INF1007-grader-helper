# Correction helper INF1007

Before TPs use Git in INF1007 (first half), this is a script that might help you reach to students the correction. It is mostly based on my workflow so you will need to change it to your usage. 

## My workflow 

1) Download Moodle group csv 
2) Download all .zip assignments files 
3) Use `inflate.sh` to unzip the file and filter only files starting with my lab number
4) Manually replace test files and copy `gabarit-grading.md`.
5) Go over each folder and grade each assignment
6) Use `main.py` to:
    - Copy all `grading.md` with team name into a single folder 
    - Extract all grades and put them into a csv file
    - Send an email to all groups with respective `grading.md` file.

## How to use

### Requirements 
- [Poetry](https://python-poetry.org/docs/)
- Python 3.12

### Environments 
- CORRECTOR_MAIL: your polymtl email 
CORRECTOR_MAIL_USERNAME: imp username
CORRECTOR_MAIL_PASSWORD: imp password