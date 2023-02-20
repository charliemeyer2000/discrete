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

This is the work that I did for the weekend quizzes. Hopefully I go back into my notes to correct the answers I get wrong. Or hopefully i get a 100% every time. 

## Mod1Multi2

Q1: For each sub-question below, indicate whether the rule can nbe directly applied (with no intermediate steps) to the expression $((P \rightarrow Q) \rightarrow R) \lor (P \land Q)$

Q1.1: Double Negation

* Yes, this can be directly applied

Q1.2: Associativity

* No, this cannot be directly applied

Q1.3: Commutativity

* Yes, this can be directly applied

Q1.4: Definition of implication

* Yes, this can be directly applied

Q1.5: Distributive Law

* Yes, this can be directly applied

Q1.6: DeMorgan's Law

* No, this cannot be directly applied

Q1.7: Definition of Exclusive Or

* Recall that definition of exclusive or is $P \oplus Q \equiv (P \lor Q) \land \neg (P \land Q)$
* Therefore, no, this cannot be directly applied

Q1.8: Simplification

* No, this cannot be directly applied

Question 2: Which of the following is equivalent to $((P \land \neg P) \lor (P \rightarrow P)) \rightarrow ((P \land \neg P) \lor \bot)$

|equation| rule used|
|-|-|
$((P \land \neg P) \lor (P \rightarrow P)) \rightarrow ((P \land \neg P) \lor \bot)$ | Given
$((P \land \neg P) \lor (P \rightarrow P)) \rightarrow (\bot \lor \bot)$ |simplification
$((P \land \neg P) \lor (P \rightarrow P)) \rightarrow \bot $ | simplification
$((P \land \neg P) \lor \top) \rightarrow \bot $ | simplification
$(\bot \lor \top) \rightarrow \bot $ | simplification
$\top \rightarrow \bot$ | simplification
$\bot$ | simplification

Question 3: For each sub-question below, indicate which expressions are logically equivalent to:
$(\neg A \lor B) \land (\neg B \lor A)$

Q3.1: $(\neg A \lor B) \land \neg (B \land \neg A)$

* Yes, this is logically equivalent through use of demorgan and double negation: $(\neg A \lor B) \land \neg(B \land \neg A) \equiv (\neg A \lor B) \land (\neg B \lor \neg \neg A) \equiv (\neg A \lor B) \land (\neg B \lor A)$

Q3.2: $A \leftrightarrow B$

* Yes, this is logically equivalent through using definition of biimplication and definition of implication. $A \leftrightarrow B \equiv (A \rightarrow B) \land (B \rightarrow A) \equiv (\neg A \lor B) \land (\neg B \lor A)$

Q3.3: $A \lor (B \land \neg B)$ 

* $A \lor (B \land \neg B) \equiv A \lor \bot \equiv A$. Thus, not equivalent.
* $A \lor (B \land \neg B) \equiv (A \lor B) \land (A \lor \neg B) \not\equiv (\neg A \lor B) \land (\neg B \lor A)$. Also just distrubute to see it's not equivalent.

Q3.4 $\neg (\neg A \lor B) \lor (\neg B \land A)$

* $\neg (\neg A \lor B) \lor (\neg B \land A) \equiv (A \land B) \lor (\neg B \land A)$. Therefore not logically equivalent.

Question 4: For each sub-question below, indicate whether the rule can be directly applied (with no intermediate steps) to the expression $P \land (\neg P \lor Q)$. 

Q4.1: Double Negation

* Yes

Q4.2: Associativity

* No

Q4.3: Commutativity

* Yes

Q4.4: Definition of Implication 

* Yes

Q4.5: Distributive Law

* Yes

Q4.6: DeMorgan's Law

* No (need an intermediate double negation step)

Q4.7: Definition of Bi-Implication

* No

Q4.8: Definition of exclusive or

* No.

Q5: Which of the following is equivalent to $\neg ((\neg Q \lor Q) \rightarrow ((Q \leftrightarrow P) \oplus Q))$?
statement | rule used|
|-|-|
$\neg ((\neg Q \lor Q) \rightarrow ((Q \leftrightarrow P) \oplus Q))$ | given 
$\neg (\top \rightarrow ((Q \leftrightarrow P) \oplus Q))$ | simplification
$\neg (\neg \top \lor ((Q \leftrightarrow P) \oplus Q))$ | definition of implication
$\neg (\bot \lor ((Q \leftrightarrow P) \oplus Q))$ | simplification
$(\top \land \neg ((Q \leftrightarrow P) \oplus Q))$ | DeMorgan's
$(\top \land \neg (\neg(P \oplus Q) \oplus Q))$ | other definition of bi-imp
$\top \land \neg (\neg P \oplus (Q \oplus Q))$ | associative
$\top \land \neg (\neg P \oplus \bot)$ | simplification
$\top \land \neg \neg P$ | simplification
$P$ | double negation + simplification

The step between "other definition of bi-imp" and "associative" is a little sus but the truth tables check out so it makes sense. Plus, the truth table for the entire equation is: 

|q|p|$\neg ((\neg Q \lor Q) \rightarrow ((Q \leftrightarrow P) \oplus Q))$|
|-|-|-|
1|1|1
1|0|0
0|1|1
0|0|0

So, it looks like no matter what _q_ is, the value of the expression $\neg ((\neg Q \lor Q) \rightarrow ((Q \leftrightarrow P) \oplus Q))$ is always just _p_!

Q6: Which of the following expressions are equivalent to $(P \land Q) \lor (\neg R \leftrightarrow Q)$? 

Q6.1: $(P \land Q) \lor ((R \lor Q) \land (\neg Q \lor R))$

|expression|rule used|
|-|-|
$(P \land Q) \lor ((R \lor Q) \land (\neg Q \lor R))$ | given
$(P \land Q) \lor ((\neg R \rightarrow Q) \land (Q \rightarrow \neg R))$ | def bi implication
$(P \land Q) \lor ((R \lor Q) \land (\neg Q \lor R))$ | definition of implication (twice)

Not equivalent, consider the instance when p = 0, q = 1, and r = 0.

Q6.2: $(P \land Q) \lor (R \lor Q)$

|expression|rule used|
|-|-|
$(P \land Q) \lor (R \lor Q)$ | given
$((P \land Q) \lor R) \lor ((P \land Q) \lor Q)$ | distributive
$((P \land Q) \lor R) \lor (Q \lor (P \land Q))$ | commutative
$(P \land Q) \lor (R \lor Q) \lor (P \land Q)$ | associative
$((P \land Q) \lor (P \land Q)) \lor (R \lor Q)$ | associative and commutative in one step cuz im lazy
$(P \land Q) \lor (R \lor Q)$ | simplification

I just went in a circle there so I don't see any way to get to $\neg R \leftrightarrow Q)$. So I think they're not equivalent. Also consider the case where p = 0, q = 0, and r = 1; they're not the same.

6.3: $(P \land Q) \lor (R \oplus Q)$ 

|expression|rule used|
|-|-|
$(P \land Q) \lor (R \oplus Q)$ | given
$(P \land Q) \lor \neg(R \leftrightarrow Q)$ | simplification / xnor

Through truth tables these are equivalent.

6.4: $(P \lor R) \land (Q \lor R) \oplus (P \lor Q)$ 

|statement|rule|
|-|-|
$(P \lor R) \land (Q \lor R) \oplus (P \lor Q)$ | given
$(R \lor (Q \land P)) \oplus (P \lor Q)$ | associativity and distributive

There's no way! Therefore, not equivalent. Also check through truth tables, in the instance where p = 1, q = 1, and r = 0 they are not equivalent.

6.5: $(P \oplus R) \oplus (P \lor Q)$

* $\neg ((P \oplus R) \leftrightarrow (P \lor Q))$
* $\neg ( ((P \oplus R) \rightarrow (P \lor Q)) \land ((P \lor Q) \rightarrow (P \oplus R)))$
* $\neg((\neg(P \oplus R) \lor (P \lor Q) \land \neg (P \lor Q) \lor (P \oplus R)))$

Using truth tables, not equivalent. If $P = \top \land Q = \top \land R = \bot$, this is a counterexample.

For $(P \land Q) \lor (\neg R \leftrightarrow Q)$, you get $\bot$, but when you do the same for $(P \oplus R) \oplus (P \lor Q)$

Question 7: 

Which expressions are equivalent to $A \lor B$?

Q7.1 $(((A \land B) \lor B) \oplus (A \lor B)) \oplus B$

* yes (truth table)

Q7.2: $((A \lor B) \rightarrow (A \land B)) \oplus (A \land B)$

* No (truth table). In fact, it's the exact opposite truth table output.

Q7.3: $((\neg B \land A) \oplus \neg B) \lor (A \land B)$

* no (truth table)

Q7.4: $\neg (\neg (A \lor B) \land \neg A)$

* yes (truth table)

Q7.5: $(\neg (A \leftrightarrow B) \rightarrow B) \rightarrow B$

* Yes (truth table)

Q8: Consider the proof: 

![Question 8 Table](images/Question8Table.png)

Q8.1: What goes in blank A?

* $\neg(\neg A \lor B) \lor \neg (B \rightarrow A)$

Q8.2: What goes in blank B?

* $(\neg \neg A \land \neg B) \lor \neg (\neg B \lor A)$

Q8.3: What goes in blank C?

* $(B \land \neg A) \lor (A \land \neg B)$


Question 9: Consider the following proof: 

![Question 9 Table](images/Question9Table.png)

Q9.1: What is blank A?

* $(\top \rightarrow \neg (P \land \neg Q)) \land (\neg \top \lor (Q \rightarrow P))$

Q9.2: What is blank B?

* DeMorgan's

Q9.3: What is blank C?

* $\top \lor ((P \rightarrow Q) \land (Q \rightarrow P))$


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
* {{(1, 0)}, {(2, 0)}, {(2,1)}}

Q3: For each subquestion below, indicate whether the provided set is disjoint with its own power set. Recall that a set is disjoint with another set when the only element it shares is teh empty set.

Q3.1 - $\{0, \{0\}\}$

* P($\{0, \{0\}\}$) = $\{\emptyset, \{0\}, \{\{0\}\}, \{0, \{0\}\}\}$
* since the original set and the power set of the original set both contain  the set {0}, They are not disjoint.

Q3.2 - $\{\{\}, 0\}$

* P($\{\{\}, 0\}$) = {{{}}, {0}}. Thus, the original set and its power set are NOT disjoint.

Q3.3 - $\{\{\}\}$

* P({ {} }) = { {} {{}} }. , the set is NOT disjoint with its own powerset.

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



