# title2doi
Converts journal article title(s) to DOI(s).

## Usage
0. Download this repository.
1. In Zotero, click: `Tools>Developer>Style Editor` and replace the existing code in the top box with the content of `title-list.csl`. Then click `refresh`.
2. That generates a bibliography list containing only the titles, in the bottom half of the screen. Copy this list and paste it into/over `list_of_titles.txt`. E.g.:
<img src="https://github.com/a-t-0/title2doi/blob/main/example_zotero.png" alt="How to export list of titles from Zotero" width="600px"/>
4. Create the conda environment, activate it and then run the code with:

```
conda env create --file environment.yml
conda activate title2doi
python title2doi
```
That generates a list of dois for the titles in `list_of_titles.txt`, if it can find them. These dois are exported to a file named: `dois_csv.txt`. Now you can add these dois from `dois_space.txt` all at once into zotero by clicking:
```
Magic Wand Icon>Paste the dois>Enter
```
