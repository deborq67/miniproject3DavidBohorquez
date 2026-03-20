### INF601 - Advanced Programming in Python
### David Bohorquez
### Mini Project 3
 
 
# Organelle Ambiguity Search
 
A search engine that shows the most incomplete
DNA records of organelle genomes from Genbank.
![DNA.png](https://images.pexels.com/photos/35967917/pexels-photo-35967917.png)

## Description

All DNA sequences contain four distinct bases: adenine (A), thymine (T), 
cytosine (C), and guanine (G). A DNA sequence uploaded to a genetic
databank like NCBI GenBank most likely looks like the following:

```
GCTTATTCTCTATGCGGGG
```
Sometimes, however, due to either the quality of the DNA sample, the sequencing
technology, or human error, ambiguities arise and are usually represented by
letters that are not A, T, C, or G. Take, for example, the first 2 `N`s in 
this sequence:

```
NNACTAATGACTAATCAGC
```
Calculating ambiguity can be done by taking these other letters and dividing them by
the total length of the DNA sequence. This is what the project aims to do.

## How to Use

The homepage of this program

## Getting Started

### Installing

This program was made using Python 3.13.11.
 
### Dependencies
 
You need the actual ZIP file the with database to start.

Download it [here.](https://www.gbif.se/ipt/archive.do?r=fishbase)

* ZIP file should be called `dwca-fishbase-v4.5.zip`. Put into your directory of execution.
* From it extract `occurrence.txt`, **file is over 300 MB.**
  * If you forget, the program would send you a friendly reminder to have it in your directory anyway.

All other dependencies needed are listed in the requirements.txt document. To install them, execute this command on Python:
 
```
pip install -r requirements.txt
```

 
### Executing program
 
* How to run the program
* Step-by-step bullets
```
pip install -r requirements.txt
```
```
flask --app flaskr init-db
```

```
flask --app flask 
```
## Help

* **Why do I have to make an account to search?**

Because the API (Entrez in this case) requires an email in order to conduct a search. The email
you use to make your account is the one that is used for said search to be executed.

* **Why is the program so slow?**

Once again, it's because of API limits. Without an API key, the maximum amount of requests you
can make is 3 per second. Same reason the maximum amount of results shown is 500.
This has already been accounted for in the script and a limit was placed so even if
you misspell your email, you shouldn't be blocked. However, please try to put a valid




* **I downloaded the ZIP file but the program is telling me `Download ZIP file and extract occurrence.txt at https://www.gbif.se/ipt/archive.do?r=fishbase`.**

You might have forgotten to extract `occurrence.txt` from *within* the ZIP file and should do so within the same directory as the `main.py` file. Also, please do not tamper with the spaces in the text file as it is tab-delimited and doing so could corrupt the way Pandas reads it.
 
## Authors
 
David Bohorquez
 
## Version History

* Released as main.py
 
## License
 
This project is licensed under the GNU General Public License - see the LICENSE.md file for details
 
## Acknowledgments
 
* [Fayette Reynolds for the background image.](https://www.pexels.com/photo/cell-seen-under-microscope-11198505/)
* [Bootstrap Template for Search Bar](https://bootstrapexamples.com/@anonymous/search-bar)
* [Bootstrap Template for Error Page](https://bootstrapexamples.com/@valeria/404-page-template-2)
* [Stack Overflow post that helped filter orders.](https://stackoverflow.com/questions/18358938/get-row-index-values-of-pandas-dataframe-as-list)
* [This other post also assisted immensely in filtering orders.](https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values)
* [This source helped make the subset for the line graph.](https://stackoverflow.com/questions/35268817/unique-combinations-of-values-in-selected-columns-in-pandas-data-frame-and-count)