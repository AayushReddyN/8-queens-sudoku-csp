# Constraint Satisfaction Problem (CSP) Solver — 8-Queens & Sudoku

## Overview
This repository contains a modular Python implementation that models and solves the **8-Queens Problem** and a **9x9 Sudoku Puzzle** as Constraint Satisfaction Problems (CSPs). The project utilizes a deterministic recursive backtracking algorithm to systematically explore search spaces, evaluate localized variables, and resolve multi-variable constraints.

## Repository Structure
* `queens_solver.py`: Contains the complete depth-first search (DFS) logic, diagonal safety tracking functions, and state output generation for the N-Queens positioning problem.
* `sudoku_solver.py`: Implements a multi-layered matrix layout validation process mapping cell constraints recursively to solve individual 9x9 subgrids.

## CSP Formulation

### 1. 8-Queens Problem
* **Variables ($X$):** $\{Q_1, Q_2, \dots, Q_8\}$, where each variable represents a row-indexed queen.
* **Domains ($D$):** $\{0, 1, 2, 3, 4, 5, 6, 7\}$, mapping to column indices on a standard $8 \times 8$ chessboard.
* **Constraints ($C$):** * *Column Constraint:* $Q_i \neq Q_j$ for all $i \neq j$.
  * *Diagonal Constraint:* $|Q_i - Q_j| \neq |i - j|$ for all $i \neq j$.

### 2. Sudoku
* **Variables ($X$):** 81 elements representing each individual grid cell $(r, c)$ where $0 \le r, c \le 8$.
* **Domains ($D$):** For empty cells: $\{1, 2, 3, 4, 5, 6, 7, 8, 9\}$; fixed cells contain a pre-assigned domain of size 1.
* **Constraints ($C$):** Evaluated locally across rows, columns, and individual $3 \times 3$ subgrids to ensure all numbers are completely distinct.

## Performance & Execution
* **8-Queens:** The backtracking solver prunes invalid search branches instantly, generating all 92 valid board configurations. The initial solution places queens at column vectors: `[0, 4, 7, 5, 2, 6, 1, 3]`.
* **Sudoku:** Resolves standard inputs in a fraction of a second by tracking cell states recursively through localized helper metrics.
