# Yoficator

> A Russian text yoficator (ёфикатор).

## What does it do?
It conservatively replaces every `е` to `ё` when it's unambiguously a case of the latter. No context is used; it relies entirely on a lack of dictionary entries for a correspondent "truly `е`" homograph. 

Yoficating Russian texts removes some unnecessary ambiguities.

To learn more, check Wikipedia in [English](https://en.wikipedia.org/wiki/Yoficator) or [Russian](https://ru.wikipedia.org/wiki/Ёфикатор).

## Usage
Depends on yoficator.dic, which is used for the lookup and should remain in the same folder.

`yoficator.py [text-file-in-Russian | string-in-Russian]`

## Examples
Running the command without arguments parses the test file:

`yoficator.py`

Or just use it with a file or string:
```bash
yoficator.py russianfile.txt    # prints to STDOUT
yoficator.py russianfile.txt > russianfile-yoficated.txt
zcat russianfile.txt.gz | yoficator.py -    # input 0f STDIN
zcat russianfile.txt.gz | yoficator.py - | gzip > russianfile-yoficated.txt.gz
yoficator.py "Где ее книга?"
```

## Limitations
* The code being conservative and not looking for context, it won't correct when a "truly `е`" homograph exists. Thus a "`все`" will never be corrected, because both `все` and `всё` exist as different words.
* Prone to wrongly yoficate other Cyrillic-based languages, such as Bulgarian, Ukrainian, Belarussian.
* It's not the fastest thing in the world, mind you. But does the job.

---  
2018  
zvezdochiot  
https://github.com/zvezdochiot/python-yoficator  
