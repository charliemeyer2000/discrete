---
title: Practice for Quiz 2
author: Charlie Meyer
geometry: margin=0.5cm
date: MoWeFri 1:00 - 1:50
header-includes:
- \usepackage{amsmath}
- \newcommand{\doublearrow}{\leftrightarrow}
---

# Pratice 1-2: Boolean Algebra

This includes both the pratice from the worksheet Elizabeth handed out in-class on Wednesday, review from the Discord Review session on Thursday, and as many practice problems I could do from 1-2. 

## Worksheet

1: Prove $A \land (A \lor B) \equiv A$

|symbol|Equation|Reasoning|
|-|-|-|
||$A \land (A \lor B)$ | Given
$\equiv$ | $(A \lor \bot) \land (A \lor B)$ | distributive property
$\equiv$ | $A \lor (\bot \land B)$ | simplification
$\equiv$ | $A \lor \bot$ | simplification
$\equiv$ | A | simplification

2: Prove $(P \lor \neg P) \rightarrow P \equiv P$

|symbol|equation|reasoning|
|-|-|-|
||$(P \lor \neg P) \rightarrow P$ | given
$\equiv$ | $\neg(P \lor \neg P) \lor P$ | definition of implication
$\equiv$ | $(\neg P \land \neg \neg P) \lor P$ | DeMorgan's Law
$\equiv$ | $(\neg P \land P) \lor P$ | Double Negation
$\equiv$ | $\bot \lor P$ | simplification
$\equiv$ | P | simplification

An alternate solution for (2) is:

|symbol|equation|reasoning|
|-|-|-|
||$(P \lor \neg P) \rightarrow P$ | given
$\equiv$ | $\top \rightarrow P$ | simplification
$\equiv$ | $\neg \top \lor P$ | definition of implication
$\equiv$ | $\bot \lor P$ | simplification
$\equiv$ | $P$ | simplification
3: Prove $\neg A \land \neg B \equiv \neg A \land (B \rightarrow A)$

|symbol|equation|reasoning|
|-|-|-|
||$\neg A \land \neg B$ | given 
$\equiv$ | $(\neg A \land \neg B) \lor \bot$ | simplification
$\equiv$ | $(\neg A \land \neg B) \lor (\neg A \land A)$ | simplification
$\equiv$ | $\neg A \land (\neg B \lor A)$ | Distributive Property
$\equiv$ | $\neg A \land (B \rightarrow A)$ | Definition of implication

4: Prove: $R \land \neg(P \rightarrow Q) \equiv P \land (\neg Q \land R)$

|symbol|equation|reasoning|
|-|-|-|
||$R \land \neg(P \rightarrow Q)$ | Given
$\equiv$ | $R \land \neg(\neg P \lor Q)$ | definition of implication
$\equiv$ | $R \land ( \neg \neg P \land \neg Q)$ | DeMorgan's Law
$\equiv$ | $R \land (P \land \neg Q)$ | double negation
$\equiv$ | $R \land (\neg Q \land P)$ | commutative 
$\equiv$ | $(R \land \neg Q) \land P$ | associative
$\equiv$ | $P \land (R \land \neg Q)$ | commutative 
$\equiv$ | $P \land (\neg Q \land R)$ | commutative


5: Prove: $(X \rightarrow Y) \land (\neg X \rightarrow \neg Y) \equiv X \leftrightarrow Y$

|symbol|equation|reasoning|
|-|-|-|
|| $(X \rightarrow Y) \land (\neg X \rightarrow \neg Y)$ | given
$\equiv$ | $(X \rightarrow Y) \land (\neg \neg X \lor \neg Y)$ |definition of implication
$\equiv$ | $(X \rightarrow Y) \land (X \lor \neg Y)$ | Double negation
$\equiv$ | $(X \rightarrow Y) \land (\neg Y \lor X)$ | commutative
$\equiv$ | $(X \rightarrow Y) \land (Y \rightarrow X)$ | definition of implication
$\equiv$ | $X \leftrightarrow Y$ | definition of bimplication

6: Prove $\neg (P \lor M) \rightarrow \neg M \equiv \top$

|symbol|equation|reasoning|
|-|-|-|
||$\neg (P \lor M) \rightarrow \neg M$ | given
$\equiv$ | $\neg \neg (P \lor M) \lor \neg M$ | definition of implication
$\equiv$ | $(P \lor M) \lor \neg M$ | double negation
$\equiv$ | $P \lor (M \lor \neg M)$ | associativity
$\equiv$ | $P \lor \top$ | simplification
$\equiv$ | $\top$ | simplification

## Discord Review Session

Prove: $A \oplus B \equiv \neg (A \leftrightarrow B)$

|operator|expression|reached by|
|-|-|-|
||$A \oplus B$ | given
$\equiv$ | $(A \lor B) \land \neg (A \land B)$ | definition of XOR
$\equiv$ | $((A \land \neg (A \land B)) \lor (B \land \neg (A \land B)))$ | distribute
$\equiv$ | $((A \land (\neg A \lor \neg B)) \lor (b \land (\neg A \lor \neg B)))$ | DeMorgan
$\equiv$ | $((A \land \neg A) \lor (A \land \neg B)) \lor (B \land (\neg A \lor \neg B)))$ | distribute
$\equiv$ | $((A \land \neg A) \lor (A \land \neg B)) \lor ((B \land \neg A) \lor (B \land \neg B))$ | distribute
$\equiv$ | $(\bot \lor (A \land \neg B)) \lor (B \land \neg A) \lor (B \land \neg B))$ | simplify
$\equiv$ | $(\bot \lor (A \land \neg B)) \lor ((B \land \neg A) \lor \bot)$ | simplify
$\equiv$ | $(A \land \neg B) \lor ((B \land \neg A) \lor \bot)$ | simplify
$\equiv$ | $(A \land \neg B) \lor (B \land \neg A)$ | simplify
$\equiv$ | $(\neg \neg A \land \neg B) \lor (\neg \neg B \land \neg A)$ | double negation
$\equiv$ | $\neg (\neg A \lor B) \land \neg (\neg B \lor A)$ | De Morgan
$\equiv$ | $\neg ((\neg A \lor B) \land (\neg B \lor A))$ | De Morgan
$\equiv$ | $\neg ((A \rightarrow B) \land (B \rightarrow A))$ | definition of implication
$\equiv$ | $\neg (A \leftrightarrow B)$ | definition of bi implication 

Another Solution (not sure if it's legal though)

* Use Definition of xor: $A \oplus B \equiv \neg (A \rightarrow B)$. The purpose of the question above was to show another way to do that, though. 



## Practice 1-2: Boolean Algebra

### Question 1:

Prove $P \rightarrow Q \equiv \neg Q \rightarrow \neg P$

|operator|expression|reached by|
|-|-|-|
||$P \rightarrow Q$ | given
$\equiv$ | $\neg P \lor Q$| definition of implication
$\equiv$ | $Q \lor \neg P$ | commutativity 
$\equiv$ | $\neg \neg Q \lor \neg P$ | double negation
$\equiv$ | $\neg Q \rightarrow \neg P$ | definition of implication

### Question 2

Prove $\neg (P \land Q \land R) \equiv (\neg P \lor \neg Q \lor \neg R)$

|operator|expression|reached by|
|-|-|-|
||$\neg (P \land Q \land R)$ | given
$\equiv$ | $\neg ((P \land Q) \land R)$| Associativity 
$\equiv$ | $(\neg (P \land Q) \lor \neg R)$ | DeMorgan's Law
$\equiv$ | $((\neg P \lor \neg Q) \lor \neg R)$ | DeMorgan's Law
$\equiv$ |$(\neg P \lor \neg Q \lor \neg R)$ | associativity

In the solution on the website, their first step was to do $\neg(P \land (Q \land R))$ but I did $\neg((P \land Q) \land R)$. Doesn't matter.

### Question 3

Prove $P \land (P \rightarrow Q) \equiv P \land Q$ 

|operator|expression|reached by|
|-|-|-|
||$P \land (P \rightarrow Q)$ | given
$\equiv$ | $P \land (\neg P \lor Q)$ | definition of implication
$\equiv$ | $(P \land \neg P) \lor (P \land Q)$ | Distributive 
$\equiv$ | $(\bot) \lor (P \land Q)$ | simplification
$\equiv$ | $(P \land Q)$ | simplification
$\equiv$ | $P \land Q$ | associativity

The answer on the website has the stripping of parenthesis around $(\bot)$ and therefore does one less step than me but same difference.


### Question 4

Prove $\neg(P \land Q) \equiv (Q \rightarrow (\neg P))$

|operator|expression|reached by|
|-|-|-|
||$\neg (P \land Q)$ | given
$\equiv$ | $(\neg P) \lor (\neg Q)$ | DeMorgan's Law
$\equiv$ | $(\neg Q) \lor (\neg P)$ | commutative property
$\equiv$ | $Q \rightarrow (\neg P)$ | definition of implication

### Question 5

Prove $(P \land \neg Q) \equiv \neg (P \rightarrow Q)$ 

|operator|expression|reached by|
|-|-|-|
||$(P \land \neg Q)$ | given
$\equiv$ | $(\neg \neg P \land \neg Q)$ | double negation
$\equiv$ | $\neg(\neg P \lor Q)$ |DeMorgan's Law
$\equiv$ | $\neg (P \rightarrow Q)$ | definition of implication

Cringe double negation but whatever don't forget to do that. It's easy to overlook that step when you're DeMorgans-ing.

### Question 6

Prove $P \rightarrow (A \lor Q) \equiv (P \land \neg A) \rightarrow Q$ 

|operator|expression|rule used|
|-|-|-|
||$P \rightarrow (A \lor Q)$ | given
$\equiv$ | $\neg P \lor (A \lor Q)$ | definition of implication
$\equiv$ | $(\neg P \lor A) \lor Q$ | associativity
$\equiv$ | $\neg \neg (\neg P \lor A) \lor Q$ | double negation
$\equiv$ | $\neg(P \land \neg A) \lor Q$ | DeMorgan
$\equiv$ | $(P \land \neg A) \rightarrow Q$ | definition of implication

The answer online took extra steps but I think my answer is cleaner (and still valid).

### Question 7

Did this over discord, see discord review section


### Question 8.

Prove $(P \rightarrow Q) \equiv \neg (\neg Q \rightarrow \neg P)$ 

|operator|expression|rule|
|-|-|-|
||$(P \rightarrow Q)$ | given
$\equiv$ | $\neg P \lor Q$ | definition of implication
$\equiv$ | $(\neg P \lor Q)$ | associativity
|this|cannot|be proven|

Working backwards... 
$\neg (\neg \neg Q \lor \neg P)$

$\neg(Q \lor \neg P)$

$\neg Q \land P$

As you can see there is no way to work backwards to get $(\neg P \lor Q)$ from $(\neg Q \land P)$ therefore it is unsolvable. 

Another way to see that it is unsolvable: If P and Q are both $\bot$, the left-hand side is $\top$ and the right-hand side is $\bot$. So they're not $\equiv$.

### Question 9

Prove $A \rightarrow (B \rightarrow C) \equiv (A \land B) \rightarrow C$

|operator|expression|rule|
|-|-|-|
||$A \rightarrow (B \rightarrow C)$ | given
$\equiv$ | $A \rightarrow (\neg B \lor C)$ | DeMorgan's
$\equiv$ | $\neg A \lor (\neg B \lor C)$ | DeMorgan's
$\equiv$ | $(\neg A \lor \neg B) \lor C$ | Associativity
$\equiv$ | $\neg (A \land B) \lor C$ | DeMorgan's
$\equiv$ | $(A \land B) \rightarrow C$ | Definition of implication

### Question 10

For more practice, prove

$A \oplus B \oplus C \equiv (A \land \neg B \land \neg C) \lor (\neg A \land B \land \neg C) \lor (\neg A \land \neg B \land C) \lor (A \land B \land C)$, or prove any [equivalence rule](https://www.cs.virginia.edu/luther/2102/S2021/axioms.html) using other equivalence rules, or prove $\forall_{x}$ chapter 15 exercise C or $\forall_{x}$ chapter 17 exercise B or all exercises in $\forall_{x}$ chapter 19$

### Questions 11-21

"The Team wins or I am sad. If the team wins, then I go to a movie. My dog is quiet. If i am sad, then my dog barks."

* W: the team wins
* S: I am sad
* M: I go to a movie
* B: my dog barks

We can express the passage above as: $(W \lor S) \land (W \rightarrow M) \land \neg B \land (S \rightarrow B)$. 

The following proof is one way to show that: 

* my dog doesn't bark
* the team won
* I am not sad, and
* I went to the movies

|expression| rule used|
|-|-|
$(W \lor S) \land (W \rightarrow M) \land \neg B \land (S \rightarrow B)$| given
$(W \lor S) \land (\neg W \lor M) \land \neg B \land (S \rightarrow B)$ | definition of implication
$(W \lor S) \land (\neg W \lor M) \land \neg B \land (\neg S \lor B)$ | definition of implication
$(W \lor S) \land (\neg W \lor M) \land (\neg B \land (\neg S \lor B))$ | associativity
$(W \lor S) \land (\neg W \lor M) \land ((\neg B \land \neg S) \lor (\neg B \land B))$ | distributive
$(W \lor S) \land (\neg W \lor M) \land ((\neg B \land \neg S) \lor \bot)$ | simplification
$(W \lor S) \land (\neg W \lor M) \land (\neg B \land \neg S)$ | simplification
$(W \lor S) \land (\neg W \lor M) \land \neg B \land \neg S$ | associativity
$\neg S \land (W \lor S) \land (\neg W \lor M) \land \neg B$ | commutativity
$(\neg S \land (W \lor S)) \land (\neg W \lor M) \land \neg B$ | associativity
$(( \neg S \land W) \lor (\neg S \land S)) \land (\neg W \lor M) \land \neg B$ | distributive
$((\neg S \land W) \lor \bot) \land (\neg W \lor M) \land \neg B$ | simplification
$((\neg S \land W)) \land (\neg W \lor M) \land \neg B$ | simplification
$\neg S \land W \land (\neg W \lor M) \land \neg B$ | associativity
$\neg S \land \neg B \land W \land (\neg W \lor M)$ | commutativity
$\neg S \land \neg B \land (W \land (\neg W \lor M))$ | associativity 
$\neg S \land \neg B ((W \land \neg W) \lor (W \land M))$ | distributive
$\neg S \land \neg B \land (\bot \lor (W \land M))$ | simplification
$\neg S \land \neg B \land ((W \land M))$ | simplification
$\neg S \land \neg B \land W \land M$ | associativity

Note: removing redundant parenthesis like $((W \land M)) \text{ to } W \land M$ is associativity, _not_ simplification.

### Questions 22 - 24

Some lists of loical axioms will include the contrapositive, for example $(P \rightarrow Q) \equiv ((\neg Q ) \rightarrow (\neg P))$. We can derive the contrapositive from other rules as follows:

|Expression|Reached by|
|-|-|
$P \rightarrow Q$ | given
$\neg P \lor Q$ | definition of implication
$Q \lor \neg P$ | commutativity
$\neg \neg Q \lor \neg P$ | double negation
$(\neg Q) \rightarrow (\neg P)$ | definition of implication

### Question 25: 

Given the expression $(P \land Q) \lor (O \land \neg Q)$, which __two__ of the following can be reached by a single application of a rule listed on our equivalences?

* $((P \land Q) \lor P) \land ((P \land Q) \lor \neg Q)$ - distributive
* $P \land (Q \lor \neg Q)$ - Distributive (backwards)

## Questions 26-30:

Consider the following proof that "if you challenge me to a game, I'll play and win. But I can't win against you" means  that you won't challenge me. We can formalize this passage into several propositions, as follows:

* C: if you challenge me to game
* P: I'll play
* W: I'll win

We can symbolize this passage as: $(C \rightarrow (F \land W)) \land \neg W$

|expression|rule used| 
|-|-|
$(C \rightarrow (F \land W)) \land \neg W$ | given 
$(\neg C \lor (P \land W)) \land \neg W$ | definition of implication
$\neg W \land (\neg C \lor (P \land W))$ | commutativity
$(\neg W \land \neg C) \lor (\neg W \land (P \land W))$ | distributive
$(\neg W \land \neg C) \lor ((P \land W) \land \neg W)$ | commutative
$(\neg W \land \neg C) \lor (P \land (W \land \neg W))$ | associativity
$(\neg W \land \neg C) \lor (P \land \bot)$ |simplification
$(\neg W \land \neg C) \lor \top$ | simplification
$\neg W \land \neg C$ | simplification
$\neg C \land \neg W$ | simplification
$\neg C$ | entailment rule $A \land B \vDash A$

### Question 31 

Which of the following statements are tautologies? (A tautology is an expression that always evaluates to true):

* $(P \land \neg P) \rightarrow Q$ - Tautology
* $(P \lor \neg P) \rightarrow Q$ - Not a tautology
* $(P \land Q) \rightarrow (P \lor Q)$ - Tautology

### Question 32

Select the correct formalism of "If I were rich and famous you wouldn't treat me like this!" Assume each parenthesized english statement becomes one symbol.

* ((I'm rich) $\land$ (I'm famous)) $\rightarrow \neg$ (you treat me like this)
* ((I'm rich) $\land$ (im famous)) $\rightarrow$ (you wouldn't treat me like this)

### Question 33 

Starting from $(A \land \neg B) \lor (B \land \neg C)$, which of the following can be reached by only one application of the distributive rule?

* $((A \land \neg B) \lor B) \land ((A \land \neg B) \lor \neg C)$

### Question 34 

I have an expression consisting of a disjunction of several conjunctions. I want to get some of the terms of the conjunctions to cancel out. To do this, I should first:

* Know what a disjunction and a conjunction is:
    * disjunction is $\lor$ and conjunction is $\land$
* Use the distributive law to change it into a conjunction of disjunctions OR use the distributive law to factor out common terms. 
    * The second option is probably better tho :grin:












