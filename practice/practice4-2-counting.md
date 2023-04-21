---
title: Practice for Quiz 2
author: Charlie Meyer
geometry: margin=0.5cm
date: MoWeFri 1:00 - 1:50
header-includes:
- \usepackage{amsmath}
- \newcommand{\doublearrow}{\leftrightarrow}
---

# Practice for Quiz 4 - Counting

## Review from unfinished slides problems

### Question 1

A local US telephone number has 7 digits and cannot start with 0, 1, or the three digits 555. How many such telephone numbers are possible? 

* The first digit has 8 possibilities (the digits 2 through 9) and the other six digits each have 10 possibilities. 
* However, we have included the numbers that start with 555 - each of these has 10 choices for the last four digits.
* Subtracting the disallowed yields: $8 \times 10^6 - 10^4 = 7999900$.
* _Addendum_: Another method is to count all $10^7$ numbers and subract the $10^6$ starting with 0, the $10^6$ starting with 1, and the $10^4$ starting with 555. This yields the same answer.


### Question 2

How many sequences are there with exactly 8 characters taken from the 26 lower-case ASCII letters and 10 ASCII digits, __with no digits repeated twice back-to-back__?

* $36 * 35^7$

### Question 3

Exactly 8 characters taken from the 26 lower-case ASCII letters and 10 ASCII digits, with no repeated characters (neither abcdaefg nor abcddefg are allowed). 

* $\frac{36!}{(36-8)!}$. 

### Question 4

How many 21-element subsets of a 31 element set are there? 

* $31 \choose 21$

### Question 5

How many unique shufflings of "alabama" are there?

* $\frac{7!}{4!}$

## Counting Problems from Website

### Question 1

Prove that $\vert P(S) \vert = 2^{\vert S \vert}$.

We proceed by induction on the cardinality of S.

* __Base case__: $\vert S \vert S = 0$.
    * In this case, $S = \emptyset$ and $P(S) = \{\emptyset\}$. Thus, $\vert P(S) \vert = 1 = 2^0$.
* __Inductive step__: Suppose $\vert S \vert > 0$ and all sets of cardinality $\vert S \vert -1$ have $2^{\vert S \vert -1}$ elements tin their powerset. Pick an arbitrary member $x$ of $S$ and define $T = S - \{x\}$. For every member $y$ of $P(T)$, we know that $P(S)$ has two members: $y$ and $y \cup \{x\}$. We also know that: 
    * Those members are distinct because one contains $x$ and the other does not.
    * All members of P(S) can be generated in this way
    * no single member of P(S) is generated from two distinct $y$

Thus, $\vert P(S) \vert = 2 * \vert P(T) \vert$. Because $\vert T \vert = \vert S \vert - 1, \vert P(T) \vert = 2^{\vert S \vert -1}$. Thus, $\vert P(S) \vert = 2 \{ \{ \vert S \vert \}\}$.

### Question 2

Prove by induction that the number of distinct $k$ member subsets of an $n$ member set is denoted $n \choose k$ and is equal to $\frac{n!}{k!(n-k)!}$.

* I won't write this out. We aren't being tested on this at the moment, you can read the proof yourself on the website. 

### Question 3

Prove that the number of permutations of a sequence with $n$ distinct elements is $n!$.

We proceed by induction on $n$. 

* __Base case__: Consider the case when $n= 0$. By definition, $0! = 1$. Further, consider the case where $n=1$. $1! = 1$. Thus, we have shown that $0! = 1! = 1$.
* __Inductive step__: Assume that a $n-1$ element sequence with distinct elements has $(n-1)!$ permutations. Then we construct and count all permutations of an $n$ element sequence, $S_n$, as follows:
    1. Consider the $n-1$ element sequence $S_{n-1}$ defined as all elements of $S_n$ except for the last. 
    1. Create the $(n-1)!$ permutations of $S_{n-1}$
    1. From each permutation of $S_{n-1}$, generate $n$ permutations of $S_n$ where the _i_th permutation generated from s is s with the last element of $S_n$ in the _i_th spot.

Because all elements of $S_n$ are unique, resulting permutations are distinct. We generated $n$ permutations for each of $(n-1)!$ sub-permutations, for a total of $n \times (n-1)! = n!$ permutations. By the principle of induction, it holds that the number of permutations of any sequence of n distinct elements is $n!$. 

### Question 4

Prove that for all the finite sets $S$, $\vert S^k \vert = \vert S \vert^k$.

We proceed by induction on $k$. 

* __Base Case__: Consider when $k=0$. Then $S^k = \{\emptyset \}$, and therefore the cardinality is 1. 
* __Inductive Step__: Assume that $\vert S^{k=1} \vert = \vert S \vert^{k-1}$. Then we can enumerate the elements of $S^k$ as follows: 
    * For each element $x$ of $S^{k-1}$, create $\vert S \vert$ sequences of length $k$; each starts with a different element of $S$ and then is followed by the elements of $x$ in order. This results in $\vert S \vert \vert S^{k-1} \vert = \vert S \vert^k$ elements in total. 

By the principle of induction, it follows that $\vert S^k \vert = \vert S \vert^k$.


### Question 5

Assume that a "digit" is an integer between 0 and 9, inclusive. Choose the corret answer:

* there are more length-5 sequences of digits than cardinality-5 sets of digits.
* there are fewer length-5 sequences of digits than cardinality-5 sets of digits
* there are the same number of length-5 sequences of digits and cardinality-5 sets of digits. 

Answer:

* To calculate the amount of length-5 sequences of digits, we can get that by multiplying 10 by itself 5 times. This gives us 10^5.
* to calculate the amount of cardinality-5 sets of digits, we can get this by doing $10 \choose 5$. This gives us 252.
* We can see that there are more length-5 sequences of digits than cardinality-5 sets of digits.


