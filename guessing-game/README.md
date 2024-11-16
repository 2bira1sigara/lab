## Number Guessing Game

### Description

Enhanced version of the classic number guessing game with additional features.
### Features

* Random number generation
* Limited attempts
* High/low guidance
* Best score tracking
* Multiple game rounds

### Sample Output

```
=== NUMBER GUESSER ===
I picked a number (1-100)
Attempts left: 7

> 50
Too high!
Attempts left: 6

> 25
You win! 🎉
Attempts used: 2
Best score: 2

Play again? (y/n):
```

### Hint

#### Track attempts and best score:
```python
best_score = float('inf')  # Start with infinity
if attempts < best_score:
    best_score = attempts
```
