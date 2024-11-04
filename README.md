# Correction helper INF1007

Before TPs use Git in INF1007 (first half), this is a script that might help you reach to students the correction. It is mostly based on my workflow so you will need to change it to your usage.

## My workflow

1) Download Moodle group csv
2) Download all .zip assignments files
3) Unzip with `-z` flag # TODO
4) Prepare the submissions by:
    - Filtering thes files to only my lab section (`-f` flag)
    - Copy grading template to each submission (from `./template/{PR/TP}X-correction.md`)
    - Copy VSCode config files to each submission (from `./.vscode`) to have the same settings for all students
5) Correct each submission
6) With the `-g` flag:
    - Extract all grade files into a single folder in `./results` following the naming convention `L0X-TP0X.md` or `L0X-{matricule}.md`
    - Create a CSV file with the grades and comments for each student
    - Send an email to each student with their grade and comments (with `-s` flag)

## How to use

### Requirements

- [Poetry](https://python-poetry.org/docs/)
- Python 3.12

### Environments

View env file to see them with their definitions.  
