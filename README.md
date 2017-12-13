

# README #
- [English Version](#english-version)
  - [Introduction](#introduction)
  - [Corpus](#corpus)
  - [How to Use](#how-to-use)
  - [Screenshot](#screenshot)
  - [Credits](#credits)
  - [License](#license)

## Introduction ##

Simple Indonesian Syntatic Parsing/ Parse Tree program using NLTK lib written in python 3

## Corpus ##
Corpus cited from Tagged UI Corpus
- famrashel, [Github](https://github.com/famrashel/idn-tagged-corpus)  (from http://bahasa.cs.ui.ac.id/)

This Corpus is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

## How to Use ##

1. Install Python 3
2. Install NLTK Lib using pip `pip install nltk` or read description [here](http://www.nltk.org/install.html)
3. Run [ParseTree.py](./ParseTree.py)
4. Parsing process use ``parsetree()`` method,
	example:
	```python
	parsetree("ibu dan ayah pergi ke pasar di Jakarta")
	```
## Screenshot ##
Sentence:

`ibu dan ayah pergi ke pasar di Jakarta`

Console output:

[![image.png](https://s5.postimg.org/af2brar7b/image.png)](https://postimg.org/image/8ahyq7pkj/)

Tree visualization:


[![image.png](https://s5.postimg.org/wpq6rsjhz/image.png)](https://postimg.org/image/pz9picwc3/)



## Credits ##

- famrashel, [Github](https://github.com/famrashel/idn-tagged-corpus)


## License
This source code is licensed under the [GPL v3](https://opensource.org/licenses/gpl-3.0.html) 
license, see the [LICENSE](./LICENSE) file in the project root for the full license text.


