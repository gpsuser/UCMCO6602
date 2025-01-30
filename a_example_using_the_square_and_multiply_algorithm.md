# The Square and Multiply Algorithm

## Calculating 3^29 Using the Square-and-Multiply Algorithm

Below we walk through calculating 3^29 step by step, explaining the thought process and calculations in detail.

## Converting the Exponent to Binary

First, we need to convert 29 to binary, as this will determine our sequence of operations:

* 29 ÷ 2 = 14 remainder 1
* 14 ÷ 2 = 7  remainder 0
* 7 ÷ 2 = 3   remainder 1
* 3 ÷ 2 = 1   remainder 1
* 1 ÷ 2 = 0   remainder 1

Reading from bottom to top: 29₁₀ = 11101₂

## Applying Square-and-Multiply Algorithm

Now let's follow each bit in 11101₂, starting from the leftmost bit. Remember our base number is now 3 instead of 2.

### Bit 1 (leftmost)

Starting position:

* Begin with x = 3
* Result = 3

### Bit 2 (next 1)

For this step we need to:

* Square previous result: 3² = 9
* Multiply by 3 (because bit is 1): 9 × 3 = 27
* Result = 27

### Bit 3 (middle 1)

Moving to the third bit:

* Square previous result: 27² = 729
* Multiply by 3 (because bit is 1): 729 × 3 = 2,187
* Result = 2,187

### Bit 4 (the 0)

For this zero bit:

* Square previous result: 2,187² = 4,782,969
* Don't multiply (because bit is 0)
* Result = 4,782,969

### Bit 5 (rightmost 1)

Final step:

* Square previous result: 4,782,969² = 22,876,792,454,961
* Multiply by 3 (because bit is 1): 22,876,792,454,961 × 3 = 68,630,377,364,883
* Final result = 68,630,377,364,883

## Summary Table

| Step | Bit | Operation | Calculation | Result |
|------|-----|-----------|-------------|---------|
| 1 | 1 | Initial | 3 | 3 |
| 2 | 1 | Square & Multiply | 3² × 3 | 27 |
| 3 | 1 | Square & Multiply | 27² × 3 | 2,187 |
| 4 | 0 | Square only | 2,187² | 4,782,969 |
| 5 | 1 | Square & Multiply | 4,782,969² × 3 | 68,630,377,364,883 |

## Efficiency Analysis

This calculation demonstrates why the square-and-multiply algorithm is so powerful:

* To calculate 3^29 directly would require 28 multiplications
* Using square-and-multiply, we only needed:
  * 5 squaring operations (one for each bit position)
  * 4 multiplications by 3 (one for each 1 in the binary representation)
* Total operations: 9 instead of 28
* The algorithm's efficiency becomes even more apparent with larger exponents


## Verification
We can verify our result is correct because:

* Each step followed the binary representation 11101₂
* Each operation was performed accurately
* The pattern of squares and multiplications matches the binary expansion of 29
* This method is mathematically proven to give the same result as direct multiplication

This example shows how the same algorithm we used for 2^29 works equally well with any base number, demonstrating its versatility in cryptographic applications where we often need to work with various bases and large exponents.