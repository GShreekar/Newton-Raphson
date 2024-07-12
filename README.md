# Newton-Raphson Method for Finding Roots
This Python script utilizes `sympy` to find an initial value for the Newton-Raphson method and subsequently finds the root of a user-provided function.

## Overview
The script performs the following tasks:
1. **Finding Initial Value (`x0`):**
   - Evaluates the user-provided function at consecutive integer values to detect a sign change, indicating a potential interval where the root lies.
2. **Newton-Raphson Method:**
   - Uses the initial value `x0` found to iteratively apply the Newton-Raphson method until the desired precision is achieved.

## Requirements
- Python 3.x
- `sympy` library (`pip install sympy`)

## Usage
1. **Input:**
   - Enter the simplified function in terms of `x` when prompted (e.g., `x**3 + x - 5`).
2. **Output:**
   - The script will output the initial value `x0` found and the approximate root of the function with a precision of 5 decimal places.

## Notes
- Ensure the function provided is simplified and valid for symbolic manipulation using `sympy`.
- The script handles basic arithmetic operations (`+`, `-`, `*`, `/`), powers (`**`), and common functions like logarithmic and trigonometric functions.

## Further Development
- This script can be further modified and simplified to improve efficiency and handle more complex functions.
- Consider enhancements such as better error handling, input validation, and optimization of the Newton-Raphson method implementation.
