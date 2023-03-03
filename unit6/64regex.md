Regex Quick Reference
=====================

Make your own regex cheat sheet
Format it in Markdown

## Setting patterns

### Matching exact single characters in a string
+ for letters, matches case; e.g. a = a, B = B
+ for digits, matches digit
+ for special characters, preceded by a fwd slash, e.g. \( = (

### Matching general string patterns
+ `\w` = a word; can be include digits and underscores
+ `\W` = non-word symbols, i.e. "special characters"
+ `\d` = any number
+ `\s` = whitespace character
+ `\S` = any non-whitespace character
+ adding `+` to any of the previous patterns extends it to capture multiple chr
+ `?` = prevents greedy pattern pulling when `+` is used
+ `.` = any one character
+ `\.` = an actual dot

### Matching multiple options
+ `[xyz]` = matches any characters in the set, e.g. either "x", "y", or "z"
+ `[x-z]` = matches any characters in the sequence, e.g. either "x", "y", or "z"
+ `(xyz)` = matches the group of characters, e.g. "xyz"


## Patterns

### Searching for patterns
+ import `re` module
+ `re.search(pattern, string)` finds first instance of pattern in the string,
  returns a re.Match object with the span of each instance of the found pattern
+ `re.search()` can be used as a condition on its own for conditionals if
  the pattern was found
+ `re.finditer()` is like `re.search()`, but finds multiple instances
+ `re.findall()` is like `re.findall()`, but only returns the found patterns
  in a list
  
## Get patterns and instances
+ methods for `re.search()`, `re.finditer()` outputs
+ `.group()` method returns the found pattern
+ if multiple subpatterns are given and found, returned by the above method as
  a tuple
+ `.start()` returns position of first instance of pattern
+ `.end()` returns position of last instance of pattern