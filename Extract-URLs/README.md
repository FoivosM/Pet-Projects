# 🔗 URL Extractor
This is a simple personal project that takes a text file of exported bookmarks and extracts the URLs, for archival purposes. The result is a `.txt` file with one URL per line. The extraction could be done with an add-on like [this](https://github.com/igorlogius/export-bookmarks-as-text?tab=readme-ov-file). Later, the output file could be piped in an other CLI tool 🐱‍💻, possibly with the `-a` prefix.

### Example
Input file:
```txt
> Tutorials
 > R
   R tutorial : https://michaelgastner.com/R_for_QR/
 > Python
   The Python Tutorial — Python 3.12.0 documentation : https://docs.python.org/3/tutorial/index.html
   The Python Standard Library — Python 3.11.5 documentation : https://docs.python.org/3/library/index.html#library-index
   PEP 8 – Style Guide for Python Code | peps.python.org : https://peps.python.org/pep-0008/
   Google Python StyleGuide : https://github.com/google/styleguide/blob/gh-pages/pyguide.md
```
Output file:
```txt
https://michaelgastner.com/R_for_QR/
https://docs.python.org/3/tutorial/index.html
https://docs.python.org/3/library/index.html#library-index
https://peps.python.org/pep-0008/
https://github.com/google/styleguide/blob/gh-pages/pyguide.md
```
## Quick Start
1. Execute the `extractURLs.py`. Input the full path of the `bookmarks.txt`.