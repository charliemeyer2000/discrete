---
title: Practice for Quiz 1
author: Charlie Meyer
geometry: margin=0.5cm
date: MoWeFri 1:00 - 1:50
header-includes:
- \usepackage{amsmath}
- \newcommand{\doublearrow}{\leftrightarrow}
---

# Weekend Quizzes

This is the work that I did for the weekend quizzes. Hopefully I go back into my notes to correct the answers I get wrong, but I doubt it. Sorry!

## Mod1Multi1

Q1 Set builder Triple {x, y, z}: What is the cardinality of $\{\{x, y, z\} \vert (x \in \{0, 1, 2\}) \land (y \in \{0, 1, 2\}) \land (z \in \{1, 8\})\}$?


* An intuitive way to think about this problem is find the set of all sets where x can be either {0,1, 2}, y can be either {0, 1, 2} and z can be either {1, 8}. So here's the output of all of those, disregarding duplicates and stuff at first.
* {{0,0,1},{0,0,8},{0,1,1},{0,1,8},{0,2,1},{0,2,8},{1, 0, 1}, {1,0,8}, {1,1,1}, {1,1,8},{1,2,1},{1,2,8},{2,0,1},{2,0,8},{2,1,1},{2,1,8},{2,2,1},{2,2,8} }
* now, just cut down all the sets that have duplicate elements in them:
* {{0,1},{0,8},{0,1},{0,1,8},{0,2,1},{0,2,8},{0, 1}, {1,0,8}, {1}, {1,8},{2,1},{1,2,8},{2,0,1},{2,0,8},{2,1},{2,1,8},{2,1},{2,8} }
* now remove duplicate sets within the bigger set:
* {{0,1},{0,8},{0,1,8},{0,2,1},{0,2,8}, {1},{1,8},{2,1},{1,2,8},{2,8} }. The cardinality thus is 10.

Q2: What is the following set: $\{\{x\} \times \{y\} \vert x \in \{-1, 0,1, 2\} \land y \in \mathbb{N} \land y < x\}$

* This is the set of ordered pairs (x, y) such that $x \in \{-1, 0, 1, 2\} \land y \in \mathbb{N} \land y < x$
* {(1, 0), (2, 0), (2,1)}

Q3: For each subquestion below, indicate whether the provided set is disjoint with its own power set. Recall that a set is disjoint with another set when the only element it shares is teh empty set.

Q3.1 - $\{0, \{0\}\}$

* P($\{0, \{0\}\}$) = $\{\emptyset, \{0\}, \{\{0\}\}, \{0, \{0\}\}\}$
* since the original set and the power set of the original set both contain  the set {0}, They are not disjoint.

Q3.2 - $\{\{\}, 0\}$

* P($\{\{\}, 0\}$) = {{{}}, {0}}. Thus, the original set and its power set are disjoint.

Q3.3 - $\{\{\}\}$

* P({ {} }) = { {} {{}} }. , the set is disjoint with its own powerset.

Q3.4 - $\{\{0\}, \{1\}\}$

* P({ {0}, {1} }) = { {},  {{0}}, {{1}}, {{0}, {1}} }. Thus, this set is disjoint wtih its own powerset.

Q3.5 - $\{0, \{0\}, 1, \{1\}\}$

* P($\{0, \{0\}, 1, \{1\}\}$) = { {0}, {{0}}, {1}, {{1}},...etc}. I don't need to write it all out, but you can see that they are not disjoint.

Question 4 - each sub-question includes a blank. Fill in the blank with an operation that makes the statement true for every choice of _S_ that is a non-empty subset of the natural numbers. 

Q4.1 - $\vert S \vert$___$\vert S \times P(S)\vert$

* <

Q4.2 - $\vert S \vert$____$\vert S \times \{0\} \vert$

* =
* Since the cartesian product of any (non-empty) subset of the natural numbers with a set with one element produces a set with the cardinality of the subset of the natural numbers. So, it's equal!

Q4.3 - $\vert S \vert$____$\vert S \times \emptyset \vert$

* $>$

Q4.4 - $\vert S \vert$____$\{\{x, y\} \vert x \in S \land y \in S \land y = x\} \vert$

* =

Question 5 - is {3, 5} a subset? For each of the choices below, indicate whether {3,5} $\subset S$

Q5.1 - S = {1, 3, 5, 7} $\cap$ {1, 2, 3, 4}

* S = {1, 3} -> {3, 5} is not a proper subset of S.

Q5.2 - S={1, 3, 5, 7} \ {1, 2, 3, 4}

* S = {5, 7} -> {3,5} is not a proper subset of S

Q5.3 - S = {1, 3, 5, 7} $\cup$ {1, 2, 3, 4}

* S = {1, 2, 3, 4, 5, 7}, so $\{3, 5\} \subset S$ is true!

Q5.4 - S = {1, 2, 3, 4} $\cap$ {5, 7}

* S = {}, so $\{3, 5\} \subset S$ is false.

Q5.5 - S = {1, 2, 3, 4} \ {5, 7}

* S = {1, 2, 3, 4}, so $\{3, 5\} \subset S$ is false.

Q5.6 - S = {1, 2, 3, 4} $\cup$ {5, 7}

* S = {1, 2, 3, 4, 5, 7}, so $\{3, 5\} \subset S$ is True!

5.7 - $S = \{x-y \vert (x, y) \in (\{8\} \times \{3, 5\})\}$

* First of all, $\{8\} \times \{3, 5\}$ is {(8, 3), (8, 5)}. So, S = {8-3, 8-5} = {5, 3} = {3, 5}. Therefore, $\{3, 5\} \subset S$ is false. 

5.8 - S = $\mathbb{N}$

* $\{3, 5\} \subset S$ is true

5.9 - S = $\mathbb{Z} \backslash \mathbb{N}$

* $\{3, 5\} \subset S$ is false, since $\mathbb{Z} \backslash \mathbb{N}$ is the negative integers.

5.10 - $S = \mathbb{N} \backslash \mathbb{Z}$ 

* $\{3, 5\} \subset S$ is false since $\mathbb{N} \backslash \mathbb{Z}$ is the empty set. 

Question 6 - Elements of P({0, P({0})})

Select all elements of the set P({0,P({0})})

* First, what is P({0,P({0})})? Let's break it down first. We need to first solve P({0}).
    * P({0}) = {{}, {0}}
* Next, we need to find P({0, {{},{0}} }). This is the set containinig four elements:
    1. the empty set -> $\emptyset$
    1. the set containing 0 -> $\{0\}$
    1. the set containing $\{\emptyset,\{0\}\}$ -> $\{\{\emptyset, \{0\}\}\}$
    1. the set $\{0, \{\emptyset, \{0\}\}\}$
* So, the final output is $\{\emptyset, \{0\}, \{\{\emptyset, \{0\}\}, \{0, \{\emptyset, \{0\}\}\}$

Thus:

Q6.1 - $0 \in P(\{0,P(\{0\})\})$?

* False

Q6.2 - $\{0\} \in P(\{0,P(\{0\})\}$? 

* True

Q6.3 - $\{\{0\}\} \in P(\{0,P(\{0\})\}$? 

* False

Q6.4 - $\emptyset \in P(\{0,P(\{0\})\}$? 

* True

Q6.5 - $\{\emptyset \} \in P(\{0,P(\{0\})\}$?

* False

Q6.6 - $\{\{\empty \}\} \in P(\{0,P(\{0\})\}$? 

* False

Q6.7 - $\{\{\{0\}, \emptyset \}\} \in P(\{0,P(\{0\})\}$? 

* True

6.8 - $\{0, \{\emptyset, \{0\}\}\} \in P(\{0,P(\{0\})\}$? 

* True

Question 7 - Select exactly the elements of the set $\{0\} \times \{0, \{0\}\}$. 

First of all, we need to find what the cartesian product actually is. We know that the outcome of a cartesian product is a set of ordered pairs. So, we can evaluate it imagining it as a table to get this output:

* $\{0\} \times \{0, \{0\}\} = \{(0,0), (0, \{0\})\}$.

Q7.1 - $\emptyset \in \{0\} \times \{0, \{0\}\}$

* False

Q7.2 - $0 \in \{0\} \times \{0, \{0\}\}$

* False

Q7.3 - $(\emptyset) \in \{0\} \times \{0, \{0\}\}$ 

* False

Q7.4 - $(0,0) \in \{0\} \times \{0, \{0\}\}$

* True

Q7.5 - Same as Q7.2

Q7.6 - $(0, \{0\}) \in \{0\} \times \{0, \{0\}\}$ 

* True

Q7.7 - $(\{0\}, \{0\}) \in \{0\} \times \{0, \{0\}\}$

* False

Question 8 - What is the cardinality of $\vert (A \times B) \cap (B \times A) \vert$ where A = {1, 2, 3} and B = {2, 3}?

Break the problem down into parts. 

* $(A \times B)$ = {(1, 2), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3)}
* $(B \times A)$ = {(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)}
* $(A \times B) \cap (B \times A)$ = {(3, 3), (2, 2), (3, 2), (2, 3)}
* $\vert (A \times B) \cap (B \times A) \vert$ = 4



