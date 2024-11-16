## Simple ATM Machine

### Description

ATM simulation system with basic banking operations.

### Features

* Balance checking
* Deposit processing
* Transaction validation
* Continuous operation until user exit


### Sample Output

```
=== PYTHON ATM ===
Balance: $1000

1. View Balance
2. Deposit
3. Withdraw
4. Exit

Choice: 2
Amount: $500
Success! New balance: $1500
```

### Hint

#### Validate withdrawals with:
```python
if amount <= balance and amount > 0:
    balance -= amount
else:
    print("Invalid amount!")
```
