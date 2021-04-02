def bisec_sqrt(n):
    '''input : a number to get the sqrt of
    output : its approximate sqrt'''

    start = 0
    end = n
    mid = (start + end) / 2
    delta = 0.01

    while mid**2 > n + delta or mid**2 < n - delta:

        if mid**2 > n + delta:
            end = mid
            mid = (start + end) / 2
        elif mid**2 < n - delta:
            start = mid
            mid = (start + end) / 2

    return round(mid, 3)


'''
Get sqrt of a number using bisection search

### Instructions

- Create a function that will use bisection search to compute the approximative value of the square root of a number
- This function will use any integer or float as argument
- Use a delta variable of 0.01 to know when a result is valid :
(i.e. if the result squared is between (n - delta) and (n + delta), it is considered to be valid)

### Examples
```
bisec_sqrt (69) --> 8.307

bisec_sqrt (16) --> 4.0

bisec_sqrt (12984771) --> 3603.439

bisec_sqrt (12.21) --> 3.494
```

### Notes
- Round values up to 3 digits (round() method)
- Please use bisection search : it may take some more lines (I am also a one-liner lover) but the efficiency of it is incredible !
'''