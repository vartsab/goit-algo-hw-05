# goit-algo-hw-05

# Search Algorithms Performance Analysis

## Introduction
This project compares three search algorithms: Boyer-Moore, Knuth-Morris-Pratt, and Rabin-Karp. The analysis is based on their execution times on two text files.

## Algorithms
- **Boyer-Moore**: The algorithm efficiently searches for a pattern in a text by preprocessing the pattern and skipping sections of the text. It matches from the end of the pattern and uses jumps, making it faster with longer patterns. It's ideal when the pattern is shorter or reused in multiple searches.
Time Complexity : O(m*n)

- **Knuth-Morris-Pratt (KMP)**: KMP preprocesses the pattern to create a partial match table, which indicates how much to shift the pattern upon a mismatch. This avoids rechecking previously matched characters, making it efficient. It performs well in scenarios where the pattern has repeated substrings.
Time Complexity: O(n + m)

- **Rabin-Karp**: This algorithm uses hashing to find any substring in a text that matches the pattern's hash. It is particularly useful for multiple pattern searches in the same text. However, it may encounter hash collisions, requiring additional checks.
Time Complexity: O(n + m) on average; O(nm) in the worst case due to collisions.


## Substring Selection
For Article 1:

- Existing Substring: "жадібний алгоритм"
- Fictional Substring: "недійсний пошук" ("invalid search")

For Article 2:

- Existing Substring: "бінарні діаграми рішень" ("recommendation systems")
- Fictional Substring: "неіснуючий елемент" ("nonexistent element")

## Execution Time Measurement
Execution time is measured using `timeit`. Wrapper functions are created for each algorithm and substring, then executed to collect results.

## Comparison and Conclusions
The fastest algorithm for each text is determined by comparing execution times for both real and fictional substrings.

## Efficiency Comparison of Substring Search Algorithms

### Article #1:

| Existing Substring | Boyer-Moore | Knuth-Morris-Pratt | Rabin-Karp |
|--------------------|------------:|-------------------:|-----------:|
|- Time | 0.004252 | 0.024397 | 0.035469 |
|- Number of Iterations | 738 | 8524 | 8598 |

|Fictional Substring | Boyer-Moore | Knuth-Morris-Pratt | Rabin-Karp |
|--------------------|------------:|-------------------:|-----------:|
|- Time | 0.0079 | 0.025491 | 0.061181 |
|- Number of Iterations | 1197 | 12658 | 12749 |

Results for article #1: The most efficient algorithm is Boyer-Moore with execution time of 0.004252 seconds.

###Article #2:
| Existing Substring | Boyer-Moore | Knuth-Morris-Pratt | Rabin-Karp |
|--------------------|------------:|-------------------:|-----------:|
|- Time | 0.003631 | 0.017025 | 0.0385 |
|- Number of Iterations | 615 | 8677 | 8739 |

|Fictional Substring | Boyer-Moore | Knuth-Morris-Pratt | Rabin-Karp |
|--------------------|------------:|-------------------:|-----------:|
|- Time | 0.008045 | 0.034102 | 0.086857 |
|- Number of Iterations | 1435 | 18400 | 18568 |

####Results for article #2: The most efficient algorithm is Boyer-Moore with execution time of 0.003631 seconds.

## Conclusions
The Boyer-Moore algorithm proved to be the fastest for both real and fictional substrings in all cases. It showed the shortest execution time across the board.

The Knuth-Morris-Pratt algorithm showed average execution times, being faster than Rabin-Karp but slower than Boyer-Moore.

The Rabin-Karp algorithm was the slowest among the three, especially for fictional substrings.

These results confirm the efficiency of the Boyer-Moore algorithm, particularly for long texts and fictional substrings, where it excels by skipping sections of the text.
