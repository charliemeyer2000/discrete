---
title: Practice for Quiz 2
author: Charlie Meyer
geometry: margin=0.5cm
date: MoWeFri 1:00 - 1:50
header-includes:
- \usepackage{amsmath}
- \newcommand{\doublearrow}{\leftrightarrow}
---


# Practice 2-2: Functions and Relations

## Questions 1-3

Consider the _and_operator as a function, that is $f(x, y) = x \land y$. 

### Question 1

What is this function's domain ?

* $\{\top, \bot\}^2$

### Question 2

What is the function's codomain?

* $\{\top, \bot\}$

### Question 3

Which of the following properties does this function have? (Total, injective, surjective, bijective)?

* Total, surjective

## Questions 4-6

Consider the factorial operator as a funciton; that is $f(x) = x!$.

### Question 4

What is this function's domain?

* $\mathbb{Z}^+$

### Question 5 

What is the function's codomain?

* $\mathbb{Z}^+$

### Question 6

Which of the following properties does this funciton have? (total, injective, surjective, bijective)?

* total, injective

## Questions 7-9

Consider the choose notation as a function, that is $f(n, k) = \binom{x}{y}$. The mathematical definition of the "choose" function is $f(x, y) = \frac{x!}{y!(x-y)!}$.

### Question 7

What is this function's domain?

* $(\mathbb{Z}^+)^2$

### Question 8

What is the function's codomain?

* $\mathbb{Z}^+$

### Question 9

Which of the following properties does this function have? (total, injective, surjective, bijective)?

* Surjective

## Question 10

Consider the XOR operator as a relation; that is $R = (x, y) : x \oplus y\$. Which of the following properties does this relation have (reflexive, symmetric, transitive)?

* Symmetric

## Questions 11-12

Consider ar elation defined over integers as $R(x, y) : (x^2 > 4y) \rightarrow ((x / 2) \in \mathbb{Z})$. Note that the above $\rightarrow$ is the _implies_ operator.

### Question 11

Which of the following are related under this relation? ((0,0), (1,1), (5,5), (6, 5))?

* (0,0) (since false implies trye is true)
* (1,1) (since false implies false is true)
* (6, 5) (since true implies true is true)

### Question 12

Which of the following properties does this relation have(Reflexive, transitive, symmetric)?

* None
    * Not reflexive, since (5,5) is not related to itself
    * Not transitive, since R(3, 4) and R(4, 2) are true but R(3, 2) is false
    * not symmetric, since R(3, 4) is true but R(4, 3) is false

## Question 13

Consider the floor-equals operator as a relation defined over the rational numbers, that is $R(x, y) : \lfloor x \rfloor = \lfloor y \rfloor$. Which of the following properties does this relation have? (Reflexive, transitive, symmetric)?

* Reflexive, transitive, symmetric
    * Reflexive, since $\lfloor x \rfloor = \lfloor x \rfloor$ is true for all $x \in \mathbb{Q}$
    * transitive since $\lfloor x \rfloor = \lfloor y \rfloor$ and $\lfloor y \rfloor = \lfloor z \rfloor$ implies $\lfloor x \rfloor = \lfloor z \rfloor$
    * Symmetric since $\lfloor x \rfloor = \lfloor y \rfloor$ implies $\lfloor y \rfloor = \lfloor x \rfloor$

## Questions 14-16

Consider the division operator as a function, that is $f(x, y) = x / y$.

### Question 14

If this function is _total_, what is the function's domain?

$\mathbb{R} \times (\mathbb{R} \backslash \{0\})$

### Question 15

What is this function's range?

* $\mathbb{R}$

## Question 16

Consider the function $f(x) = 0.5^x$ with domain and co-domain are both $\mathbb{R}$. Which of the following properties does this function have? (total, injective, surjective, bijective)?

* Total, injective

## Questions 17-19

Consider the $\log_2$ operator as a function, that is $f(x) = \log_2 x$.

### Question 17

If the function is _total_, what is its domain?

* $\mathbb{R}^+$

### Question 18

What is this function's codomain?

* $\mathbb{R}$

### Question 19

Which of the following properties does this function have? ( injective, surjective, bijective)?

* injective, surjective, bijective

## Question 20

Consider the _implies_ operator as a relation, that is $R(x, y) : x \rightarrow y$. Which of the following does this relation have (reflexive, symmetric, transitive)?

 * Reflexive, transitive

 ## Questions 21-23

 ### Question 21

 Which of the following functions are _total_, assuming both domain and co-domain are $\mathbb{Z}$? ($f(x) = 2x$ and $f(x) = x/2$)

 * Only $f(x) = 2x$

 ### Question 22

 Which of the following functions are injective (1-to-1), assuming both domain and co-domain are $\mathbb{Z}$? ($f(x) = 2x$ and $f(x) = x/2$)

 * Both $f(x) = 2x$ and $f(x) = x/2$

 ### Question 23

 Which of the following functions are surjective (onto), assuming both domain and co-domain are $\mathbb{Z}$? ($f(x) = 2x$ and $f(x) = x/2$)

 * Only $f(x) = x/2$

 ## Questions 24-26

 ### Question 24

 Which of the following relations are _reflexive_, assuming a domain of $\mathbb{Z} \times \mathbb{Z}$? (R(x,y) : xy is even and $R(x, y) : \vert x \vert \ge \vert y \vert$)

* Only $R(x, y) : \vert x \vert \ge \vert y \vert$

### Question 25

Which of the following relations are _transitive_, assuming a domain of $\mathbb{Z} \times \mathbb{Z}$? (R(x,y) : xy is even and $R(x, y) : \vert x \vert \ge \vert y \vert$)

 * only $R(x,y) : \vert x \vert \ge \vert y \vert$

### Question 26

Which of the following relations are symmetric, assuming a domain of $\mathbb{Z} \times \mathbb{Z}$? (R(x,y) : xy is even and $R(x, y) : \vert x \vert \ge \vert y \vert$)

* Just R(x,y) : xy is even

## Questions 27-30

Consider the function $f(x,y) = x/y$ defined over the domain $\mathbb{Z} \times \mathbb{Z}^+$.

### Question 27

THe codomain of _f_ is (if multiple answers work, pick the one that is a subset of the others)

* $\mathbb{Q}$ (rational numbers)

### Question 28

Is _f_ total?

* yes, since the denominator is only defined on the positive integers

### Question 29

Is _f_ injective?

* no, since $f(2, 4) = f(4, 8) = 1/2$

### Question 30

Is _f_ surjective?

* yes.

## Questions 31-33

Consider the relation p(x, y) which is true if x and y are co-prime, i.e. the greatest common divisor of x and y is 1.

### Question 31

Is p symmetric or antisymmetric (or neither)?

* symmetric

### Question 32

Is p reflexive or irreflexive (or neither)?

* Irreflexive (if you didn't consider 1 in your domain)
* Neither (if you did consider 1 in your domain)

### Question 33

Is _p_ transitive?

* no

## Question 34

An _equivalence relation_ must be (check all that apply):

* reflexive, symmetric, transitive

## Question 35

A _partial order_ must be (check all that apply):

* antisymmetric, transitive

## Questions 36-38

Consider the relation $R(x, y)$ which is constructed froma function $f(x, y) = 2+3x$ where $f: \mathbb{R} \rightarrow \mathbb{R}$. as R(x, y) being true iff y = f(x)

### Question 36

Is R symmetric or antisymmetric?

* Antisymmetric. the system of equations $y=2+3x$ and $y=2+3y$ has only one solution (x, y) = (-1, -1). 

### Question 37

Is R reflexive or irreflexive?

* Irreflexive. (0,0) is not related 

### Question 38

Is R transitive?

* No. (0,2) and (2, 8) are related byt (0,8) is not.

## Question 39:

Give an example function f:$\mathbb{Q} \rightarrow \mathbb{Q}$ which is _total_ and _injective_ but NOT _surjective_.

* f(x) = 2x

## Question 40:

Give five different functions f:$\mathbb{Q} \rightarrow \mathbb{N}$ which is _total_ and _surjective_. 

## Question 41:

Consider R(x, y) defined over $\mathbb{Z} \times \mathbb{Z}$ as $x > 0 \lor y > 0$. Which of the following properties does this have (reflexive, transitive, symmetric)?

* Not reflexive (consider (0, 0))
* Not transitive (consider (0,1) and 1, 2)
* Symmetric, since $x > 0 \lor y > 0$ is equivalent to $y > 0 \lor x > 0$










