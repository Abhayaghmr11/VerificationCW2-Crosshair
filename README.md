# Verification of Python Function using Crosshair

This project involves formal verification of selected Python functions using CrossHair tool. Goal is to analyse correctness of functioon under various execution paths through Contracts.

# Project Structure

Python Functions included
- smallest_range
- camel_to_snake_case
- longest_subsequence

Functions were annoted with formal contracts using asserts

# Setup Instruction

To replicate the verification process, follow these steps:

Ensure that Python and CrossHair are installed
- Python Version: 3.12.9 (or any 3.x version)
- CrossHair Versoin: 0.0.84

# Installation

Install CrossHair via pip
```bash
pip install crosshair-tool
```

# Running Verification

To analyse the functions, use the following command:
```bash
crosshair watch --analysis_kind=asserts <filename>
```
OR
```bash
crosshair check --analysis_kind=asserts <filename>
```
This runs symbolic execution 

For detailed logging:
```bash
crosshair check --analysis_kind=asserts --verbose --report_all --report_verbose function_name > function.log 2>&1
```