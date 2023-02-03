---
title: Practice for Quiz 1
author: Charlie Meyer
geometry: margin=0.5cm
date: MoWeFri 1:00 - 1:50
header-includes:
- \usepackage{amsmath}
- \newcommand{\doublearrow}{\leftrightarrow}
---
<!-- 
cd practice
pandoc -s -o quiz1practice.pdf quiz1practice.md 
-->

# Practice

This includes both practice from the website set-practice on the CS 2120 website and also practice from the 1-1 practice quiz page. 

## Practice Problems with Sets

Assume the following definitions:

|notation|meaning|
|-|-|
$\mathbb{Z}$ | the integers
$\mathbb{Z}^{+}$ | the positive integers; i.e. $\{x \vert x \in Z \land x > 0\}$
$\mathbb{N}$ | the natural numbers, i.e. $\{x \vert x \in \mathbb{Z} \land x \ge 0\}$
$\mathbb{Z}^{-}$| the negative integers, i.e. $\{x \vert x \in \mathbb{Z} \land x < 0\}$
$\mathbb{R}$ | the real numbers
$\mathbb{Q}$ | the rational numbers; i.e. $\{\frac{x}{y} \vert x \in \mathbb{Z} \land y \in \mathbb{Z}^{+}\}$
$\pi$ | the ratio of the circumference of a circle to its diameter

And assume that $\mathbb{Q}^{-}$, $\mathbb{Q}^{+}$, $\mathbb{R}^{+}$, and $\mathbb{R}^{-}$ are defined similarly to the positive/negative integers, $\mathbb{Z}^{+}$ and $\mathbb{Z}^{-}$

### Membership

#### 1.1. Simple Membership

Each of these are true or false.

1. $3 \in \mathbb{Z}$ = True
1. $3.5 \in \mathbb{Z}$ = False
1. $\pi \in \mathbb{Z}$ = False
1. $3 \in \mathbb{Q}$ = True
1. $3.5 \in \mathbb{Q}$ = True
1. $\pi \in \mathbb{Q}$ = False
1. $3 \in \mathbb{R}$ = True
1. $3.5 \in \mathbb{R}$ = True
1. $\pi \in \mathbb{R}$ = True
1. $3 \in \{\{1\}, \{2, 3\}, \{4, 5, 6\}\}$ = False
1. $\{3\} \in \{\{1\}, \{2, 3\}, \{4, 5, 6\}\}$ = False
1. $\{2, 3\} \in \{\{1\}, \{2, 3\}, \{4, 5, 6\}\}$ = True
1. $\{2, 3\} \in P(\{2, 3\})$ = True
1. $\vert \{2, 3\} \vert \in \{2, 3\}$ = True
1. $\vert \{2, 3\} \vert \in P(\{2, 3\})$ = False
1. $\infty \in \mathbb{R}$ = False

#### 1.2 Closed Sets

A set is said to be __closed over__ an operation if applying that operation to members of the set always results in another member of that set.

Which, if any or all, of the following operations is $\mathbb{Z}$ closed over?

* Addition = True
* Subtraction = True
* Multiplication = True
* Division = False
* Module = Mostly true, except for 0 divisors
* Root extraction = False

Which, if any or all, of the following operations is $\mathbb{N}$ closed over?

* Addition = True
* Subtraction = False
* Multiplication = True
* Division = False
* Modulo = Mostly true, except for 0 divisors
* Root extraction = False

Which, if any or all, of the following operations is $\mathbb{R}^{-}$ closed over?

* Addition = True
* Subtraction = False
* Multiplication = False
* Division = False
* Modulo = False
* Root extraction = False

Which, if any or all, of the following operations is $\mathbb{Q}$ closed over?

* Addition = True
* Subtraction = True
* Multiplication = True
* Division = True, except for dividing by 0
* Modulo = mostly true, except for 0 divisors
* Root extraction = False

Which, if any or all, of the following operations is $\mathbb{Q} \backslash \{0\}$ closed over?

* Addition = False
* Subtraction = False
* Multiplication = True
* Division = True
* Modulo = False, 1 mod 0 = 0
* Root extraction = False

Which, if any or all, of the following operations is $\mathbb{R}$ closed over?

* Addition = True
* Subtraction = True
* Multiplication = True
* Division = True except for dividing by 0
* Modulo = True except for 0 divisor
* Root extraction = False because $\mathbb{R}$ contains negative numbers.

### Comparison

For each of the following, fill in the blank with the first element of the following list that applies:

* = if the two are identical; otherwise
* $\subset$ or $\supset$ if those are true; otherwise
* $\subseteq$ or $\supseteq$ if those are true; otherwise
* "disjoint" if the intersection of the two is $\emptyset$; otherwise
* $\neq$

|Set 1| Operator | Set 2|
|-|-|-|
$\mathbb{R}$ | $\supset$ | $\mathbb{Q}$
$\mathbb{N}$ | $\supset$ | $\mathbb{Z}^{+}$
even numbers | disjoint | odd numbers
prime numbers | $\neq$ | odd numbers
{1, 3, 5} | disjoint | {{1}, {3}, {5}}
{1, 3, 5} | = | {5, 3, 1}
{1, 3, 5} | $\supset$ | {5, 3}
$\mathbb{R} \backslash \mathbb{Z}$ | $\supset$ | $\mathbb{R} \backslash \mathbb{Q}$
$\mathbb{Q} \backslash \mathbb{Z}$ | disjoint | {1, 2, 4}
$\emptyset$ | $\subset$ | P($\emptyset$)
$\{1\}$ | disjoint | P({1})

### Listing Members & Cardinality

For each of the following, list the members of the set:

* P(P($\emptyset$)) = { {}, {{}} }
* P(P(P($\emptyset$))) = { {}, {{}}, {{{}}}, {{}, {{}}} }
* Assume that A = {25, 0, 1}; find $A \cup P(A)$
    * {25, 0, 1, {25}, {0}, {1}, {0, 1},{1, 25}, {0, 25}, {25, 0, 1} }
* Assume that A is the set of all 2-digit numbers, find $\vert P(A) \vert$
    * $2^{\vert A \vert}$ = $2^{90}$
* Assume that A is the set of all 2-digit numbers, find $\vert P(A) \cap A \vert$
    * 0
* Assume that A is the set of all 2-digit numbers, find $\vert P(A) \cup A$ 
    * $2^{90} + 90$

### Set-Builder Notation

Assume A = {1, 2, 3} and B = {2, 3, 5}. Write out the following in full.

* $\{x \vert x \in A\}$ = {1, 2, 3}
* $\{x \vert + 1 \in A\}$ = {0, 1, 2}
* $\{x \vert x \in A \land x \in B\}$ = {2, 3}
* $\{x \vert x \in A \lor x \in B\}$ = {1, 2, 3, 5}
* $\{x \vert x \in A \land x \notin B\}$ = {1}
* $\{x+1 \vert x \in A\}$ = {2, 3, 4}
* $\{x+y \vert x \in A \land y \in B\}$ = {3, 4, 5, 6, 7, 8}
* $\{\{x\} \vert x \in A\}$ = {{1}, {2}, {3}}
* $\{\{x, y\} \vert x \in A \land x \in B \land x \neq y \}$ = {{1, 2}, {1, 3}, {1, 5}, {2, 3}, {2, 5}, {3, 5}}
* $\{\{x, y\} \vert x \in A \land x \in B\}$ = {{1, 2}, {1, 3}, {1, 5}, {2}, {2, 3}, {2, 5}, {3, 5}, {3}}
* $\{x \vert x \subseteq A\}$ = {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
* $\{x \vert x \subset A\}$ = {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}}
* $\{x \vert x \subseteq A \land x \subseteq B \}$ = {{}, {2}, {3}, {2, 3}}
* $\{x \vert x \subseteq (A \cap B)\}$ = {{}, {2}, {3}, {2, 3}}
* $\{x \vert x \subseteq A \lor x \subseteq B\}$ = {{},{1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}, {5}, {2, 5}, {3, 5}, {2, 3, 5} }
* $\{x \vert x \subseteq (A \cup B)\}$ = {{}, {1}, {2}, {3}, {5}, {1, 2}, {1, 3}, {1, 5}, {2, 3}, {2, 5}, {3, 5}, {1, 2, 3}, {1, 2, 5}, {1, 3, 5}, {2, 3, 5}, {1, 2, 3, 5}}
* $\{P(\{x\})\} \vert x \in A \}$ = { {{}, {1}}, {{}, {2}}, {{}, {3}} }
* $\{x \vert x \notin A\}$ = poorly defined set
* $\{x \vert x \in \mathbb{Z} \land x \notin A\}$ = All integers except 1, 2, and 3. 

## 1-1 Practice

1. Write out the set in full: {1, 2, 3} $\cup$ {4, 3, 2}
    * {1, 2, 3, 4}
1. Write the set in full: P({1, 2})
    * {{}, {1}, {2}, {1, 2}}
1. Wite out the set in full: P({1}) $\cap$ P({2})
    * {{}}
1. Write out the set in full: P({1}) $\cup$ {1}
    * {{}, {1}, 1}
1. Write out the following set in full $\{x + y \vert (x \in \{1, 2\}) \land (y \in \mathbb{N}) \land (x < x)\}$
    * {1, 2, 3}
1. Assume A = {1, 2, 3, 4, 5, 6} and B = {2, 4, 6, 8, 10}. What goes in the blank of ($A \cap B$)____($A \cup B$)?
    * $\subset$

The following differ only in one operator. Pick the most inclusive true answer for each:

1. if $G \in P(G)$, then G is:
    * Any set (this is always true)
1. If $G \subseteq$ P(G)$, then G is:
    * The empty set, $\emptyset$

Let H = {1, 2, 3} and K be the set of positive odd integers {1, 3, 5, ...}

1. Which of the following contain the number zero as a member?
    * $\mathbb{N}$
    * $\mathbb{Z}$ 
    * $\{x-y \vert (x \in K) \land (y \in H)\}$
1. Which of the following contain the empty set as a member?
    * $P(\mathbb{Z})$
    * $\{x \vert (x \subseteq K) \land (x \subseteq H)\}$
1. What is $\vert H \vert$?
    * 3
1. What is $\vert H \cap K \vert$?
    * 2
1. What is $\vert \{\{x, y\} \vert x, y \in H\}$?
    * 6
1. What is $\vert P(H) \vert$
    * 8

Write out the following in full.

1. {1, 2} X {3} X {1,4}
    * Think of it as ({1, 2} X {3}) X {1, 4}
    * This is {(1, 3), (2, 3)} X {1, 4} = {(1, 3, 1), (1, 3, 4), (2, 3, 1), (2, 3, 4)}
1. $\{56\}^{3}$ 
    * {(56, 56, 56)}
* {1, 2} X P({1})
    * This is {1, 2} X {{}, {1}}
    * {(1, {}), (1, {1}), (2, {}), (2, {1})}
* {4, 1} X {1, 2}
    * {(4, 1), (4, 2), (1, 1), and (1, 2)}
* {4} X {1, 2} X $\{3\}^{3}$
    * ({4} X {1, 2}) X {(3, 3, 3)} => {(4, 1), (4, 2)} X {(3, 3, 3)} = {(4, 1, 3, 3, 3), (4, 2, 3, 3, 3)}
* P({})^2
    * {({}, {})}

Assume that A, B, and C are non-empty sets that:

* $A \cap B = \emptyset$
* $A \cap C \neq \emptyset$

If there are multiple correct options, pick an equals option if one is true; otherwise pick the tightest bound. (I don't want to write out all the answers, so these are just the correct answers for each question)

1. $\vert A \cup B \vert = \vert A \vert + \vert B \vert$
1. $\vert A X B \vert = \vert A \vert \cdot \vert B \vert$
1. $\vert A \cup C \vert < \vert A \vert + \vert C \vert$
1. $\vert A \times C \vert = \vert A \vert \cdot \vert C \vert$

Consider A = {1, 2, 4}, B = {2, 3, 5}, C = P({3, 4}). Show the members of each set.

1. C = {{}, {3}, {4}, {3, 4}}
1. $A \cup B$ = {1, 2, 3, 4, 5}
1. $A \cap B$ = {2}
1. $A \backslash B$ = {1, 4}
1. $P(B) \cap C$ = {{}, {3}}
1. $\{x \vert x (x \in \mathbb{N}) \land (2x \in A)\}$ = {1, 2}
1. $\{x \vert (2x \in A) \land (x \in B)\}$ = {2}
1. $\{\{a, b\} \vert (a \in A) \land (b \in B) \land (a > b)\}$ = {{2, 4}, {4, 3}}
1. $\vert \{1, \{2, 3\}, 4\} \vert$ = 3
1. $\vert P(P(\{1, 2\})) \vert$ = 16

Consider the following sets: A = {1, 2, 3}, C = P({3, 4})

1. $\vert P(A) \vert$ = 8
1. $3 \in C$ = False
1. $\{3\} \in C$ = True
1. $\{\{3\}\} \in C$ = False

Let A = {1, 2, 3, 4}, $B = \{2x \vert (x \in \mathbb{N}) \land x < 5\}$, C = P({2, 3}). Show the full set of members in each of the following sets using curly brace notation.

1. B = {0, 2, 4, 6, 8}
1. C = {{}, {2}, {3}, {2, 3}}
1. $\vert C \vert$ = 4
1. $A \cup B$ = {0, 1, 2, 3, 4, 6, 8}
1. $A \cap B$ = {2, 4}
1. $A \backslash B$ = {1, 3}
1. $A \cup C$ = {1, 2, 3, 4, {}, {2}, {3}, {2, 3}}
1. $A \cap C$ = {}
1. $\{x \vert x \in A \land x \in B \}$ = {2, 4}
    * Note that this is the same as $A \cap B$
1. $\{x \vert x \in A \lor x \in B\}$ = {0, 1, 2, 3, 4, 6, 8}
    * Note that this is the same as $A \cup B$
1. $\{x \vert x \in A \land 2x \in A \}$ = {1, 2}

Let A = {0, 2, 3}, $B = \{x^{2} \vert (x \in \mathbb{N}) \land x^{2} < 10 \}$ and C = P({4, 9})

1. B = {0, 1, 4, 9}
1. C = {{}, {4}, {9}, {4,9}}
1. $A \cup B$ = {0, 1, 2, 3, 4, 9}
1. $A \cap B$ = {0}
1. $B \cup C$ = {0, 1, 4, 9, {}, {4}, {9}, {4, 9}}
1. $\{x \vert (x \in A) \oplus (x \in B)\}$ = {1, 2, 3, 4, 9}$

Consider the following sets: A = {8, 4, 5}, B={2, 3, 4}, C=P({8, 2}). Show all members of each set:

1. C = {{}, {8}, {2}, {8, 2}}
1. $A \cup B$ = {2, 3, 4, 5, 8}
1. $A \cap B$ = {4}
1. $A \backslash B$ = {8, 5}


_The following next couple problem sets don't have answer keys to them so I didn't bother doing them - they looked somewhat repetitive and also not worth putting wrong answers in_

Select the true statements below using the following definitions:

* E(x): x is even
* Q = {2, 3, 5, 7}

Also, as a hint, P($\mathbb{Z}$) can be read "the set of all sets of integers" and includes both $\mathbb{N}$ (natural numbers) and $\mathbb{Q}$ (rational numbers).

* $\{7\} \in Q$ = False
* $\{7\} \subseteq Q$ = True
* $\mathbb{Q} \in P(\mathbb{Q})$ = True
* $\mathbb{N} \in P(\mathbb{N})$ = True
* $\mathbb{Q} \subseteq P(\mathbb{Q})$ = False
* $\mathbb{N} \subseteq P(\mathbb{N})$ = False
* $\{3\} \in \{\{x, y\} \vert x \in \mathbb{Q} \land y \in \mathbb{Q}\}$ = True
* {7, 2, 3, 5} = Q = True
* $Q \cup Q$ = Q = True
* $Q \cup (Q \backslash Q) = Q$ = True
* $\mathbb{N} \backslash (\mathbb{N} \cap \mathbb{Q}) = \mathbb{N} \backslash \mathbb{Q}$ = True
* $3 \in \{x \vert x \in \mathbb{Q} \land E(2x)\}$ = True
* $2 \in \{2x \vert x \in \mathbb{Q} \land E(2x)\}$ = False
* $\{3, 7\} \in \{X \vert X \in P(\mathbb{Q}) \land E(\vert X \vert)\}$ = True
* $2 \in \{X \vert X \in P(\mathbb{Q})\}$ = False
* $2 \in \{X \vert X \in P(\mathbb{Q}) \land E(\vert X \vert)\}$ = False
* $\emptyset \in P(\mathbb{Z})$ = True
* $P(\mathbb{Q}) \in P(P(\mathbb{Q}))$ = True
* $\mathbb{Q} = P(P(\mathbb{Q}))$ = False

More questions

1. What is $\vert P(P(P\{-1, , 1\}))$?
    * 258
1. Which of the following are valid notation to describe a set?
    * {1, 2, 3} = True
    * {1, 3, 2} = True
    * {1, 2, 2} = False
    * {1, {1}, {{1}}} = True
    * $\{x \vert x \neq 0\}$ = False
    * $\{x + y \vert x, y \in \mathbb{N}\}$ = True
    * {} = True
    {{}} = True
    * [1, 2, 3] = False
    * (1, 2, 3) = False
1. Which of the following sets contain the number one as a member? 
    * 









