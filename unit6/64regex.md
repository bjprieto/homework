Regex Quick Reference
=====================

Make your own regex cheat sheet
Format it in Markdown

### Matching exact single characters in a string
+ for letters, matches case; e.g. a = a, B = B
+ for digits, matches digit
+ for special characters, preceded by a fwd slash, e.g. \( = (

### Matching general string patterns
+ \w = a word; can be include digits and underscores
+ \w+ = any number of word symbols
+ \W = non-word symbols, i.e. "special characters"
+ \d = any number
+ . = any one character

### Matching multiple options
+ [xyz] = matches any characters in the set, e.g. either "x", "y", or "z"
+ [x-z] = matches any characters in the sequence, e.g. either "x", "y", or "z"
+ (xyz) = matches the group of characters, e.g. "xyz"
