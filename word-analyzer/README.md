## Word Analyzer

### Description

Text analysis tool that processes a word and provides detailed statistics about its characters.

### Features

* Counts vowels and consonants
* Identifies most frequent letter
* Generates ASCII art histogram
* Character frequency analysis


### Sample Output

```
Enter word: programming

Analysis Results:
============
Vowels: 3
Consonants: 8
Most common: g (2 times)

Frequency:
p: *
r: *
o: *
g: **
a: *
m: *
i: *
n: *
```

### Hint

#### Create a frequency dictionary easily with:
```python
freq = {}
for char in word:
    freq[char] = freq.get(char, 0) + 1
```
