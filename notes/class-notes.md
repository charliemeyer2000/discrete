---
title: Discrete Mathematics and Theory (2120)
author: Charlie Meyer
geometry: margin=2cm
date: MoWeFri 1:00 - 1:50
---

<!-- 

class website: https://www.cs.virginia.edu/~emo7bf/cs2120/s2023/

cd notes
pandoc -f markdown-implicit_figures -s -o class-notes.pdf class-notes.md

-->

# Feb 1 - Popular Sets, Power Set, Set-Builder Notation, Disjoint Sets

## Some Popular Sets

|Symbol|Set|elements|
|-|-|-|
$\emptyset$ | the empty set | none
$\mathbb{N}$ | nonnegative integers | 0, 1, 2, 3...
$\mathbb{Z}$ | integers |...3, 2, 1, 0, 1, 2, 3...
$\mathbb{Q}$ | rational numbers | $\frac{1}{2}$ 16, etc
$\mathbb{R}$ | real numbers | $\pi$, $e$, $\sqrt{2}$
$\mathbb{C}$ | complex numbers | $i$, $\frac{19}{2}$, etc. 

A superscript restricts its set to its positive elements, for example $\mathbb{R}^{+}$ denotes the set of positive real numbers, and for example $\mathbb{Z}^{-}$ denotes the set of negative integers.

## Power Sets

The set oef all subsets of a set, _A_, is called a _power set_, pow(A), of _A_. So: $B \in pow(A) \leftrightarrow B \subseteq A$

For example, the elements of pow({1, 2}) are $\emptyset$, {1}, {2}, and {1, 2}.

Questions:

* What is pow({})?
    * $\{\emptyset \}$ (the set containing the empty set).
* What is pow({a, b, c})?
    * pow({a, b, c}) = $\{\emptyset, \{a\}, \{b\}, \{c\}, \{a, b\}, \{b, c\}, \{a, b, c\}\}$
    * note the distinction between what pow(stuff) evaluates to versus the _elements_ of pow(stuff).
* What is the power set of {W, X, Y, Z}?
    * pow({W, X, Y, Z}) = {{$\emptyset$}, {W}, {X}, {Y}, {Z}, {W, X}, {W, Y}, {W, Z}...}

How can we determine a rule/pattern to determine the cardinality of a powerset?

* $\vert P(X) \vert = 2^{\vert X \vert}$

## Disjoint Sets

Formal definition for disjoint sets: _two sets are disjoint if their intersection is the empty set_. An example of two sets that are __not__ disjoint are {1, 2, 3} and {3, 4, 5} since they both share the element 3. However, the set {New York, Washington} and {3, 4} are disjoint.

* {1, 2} and $\emptyset$ are disjoint.
* the empty set is always disjoint with any set
* $\emptyset$ and $\emptyset$ are disjoint!

## Set builder Notation

Example: $S = \{x \in A \vert \text{x is blue}\}$

* The set of all _x_ in A "such that" property (or properties) of _x_ that must be met in order to be an element of _S_. 

A common breakdown of set-builder notation is with numbers:  $E = \{x \in \mathbb{N} \vert x \ge 3\}$

* "the set of all x in the natural numbers such that x is greater than 2."

Let's formalize our set operations in "set-builder notation." Quick side note - we need to link together multiple "conditions" with "and's," "not's," and "or's."

* $\lor$ is "or." (notice similarity to $\cup$)
* $\land$ is "and." (notice similarity to $\cap$)
* $\neg$ is "not."

### Intersection

We want to define __intersection__: $S \cap T$: the elements that belong both to _S_ and to _T_. 

* $S \cap T =  \{x \in U \vert x \in T \land x \in S \}$
    * Note that "U" is the "universe."
* Another interesting answer: $S \cap T = \{x \in S \vert x \in T\}$

### Union

We want to define the __union__: $S \cap T$: the elements that belong in either _S_ or _T_ (or both):

* $S \cup T\{x \in U \vert x \in T \lor x \in S\}$
* the "or" $\lor$ symbol is inclusive - includes All elements in S, T, __or__ both.

### Difference

We want to define __difference__ $S \backslash T$: 

* $S \backslash T = \{x \in U \vert x \in S \land x \notin T\}$
* "Better" answer: $S \backslash T = \{x \in U \vert x \in S \land \neg(x \in T)\}$
* Another cheeky answer: $S \backslash T = \{x \in S \vert x \notin T\}$

### Complement

We want to define __complement__: $\bar{S}$: elements (of the universe) that don't belong to _S_. 

* $\bar{S} = \{x \in U \vert x \notin S\}$
* $\bar{S} = \{x \notin S\}$

### Evaluation Practice

$\{\{a, b\} \vert (a \in X) \land (b \in Y)\}$ = ?

* = { {1, 2}, {1, 3}, {1, 4}, {2}, {2, 3}, {2, 4}, {3}, {3, 4} }













# Jan 30 - propositions, operators, set-builder notation

<!-- 
notes from the week of Jan 23 - Jan 30:
https://docs.google.com/presentation/d/1BXSO-TkmlSSkd3IIVM2yxjG03KVn0roCMBNhjLEHjK0/edit?usp=sharing 
-->

## Describing Sets

Listing out the elements of a set works well for sets that are small and finite. What about larger sets? Use set builder notation!!

$S = \{x \in A \vert x \space is \space blue\}$
* _S_ us the set of all _x_ in A such that...

$E = \{x \in \mathbb{N} \vert x > 2\}$ 
* E is {3, 4, 5, ..., $\infty$} 
* Recall that 0 is a natural number btw. 
* The cardinality of _E_ is infinity. 


# Jan 27 - intersection, union, difference, complement, and cartesian (cross) product

## $\cap, \cup, \backslash$

### $\cap$ : the __intersection__ of two sets

The intersection of two sets S and T, denoted by $S \cap T$, that is the set containing all elements of S that also belong in T.  (or equivalently, all elements of T that also belong in S)

![intersection](images/intersection.png){height=20%}

### $\cup$: the __union__ of two sets

The union of two sets S and T, denoted by $S \cup T$, is the set containing all the elements of S and also all the elements in T. (or equivalently, everything either in S or T or both)

![union](images/union.png){height=20%}

### __Difference__ $S \backslash T$: the element that belong to S but not T

Note that the difference of two sets is _not_ commutative. It's like division!

![difference](images/difference.png){height=20%}

### Complement: $\bar{S}$ or $S^{C}$: All the elements of the universe that don't belong to S. 

You have to consider the universe _u_, not just the "venn diagram" too. See images attached! 

![complement](images/complement.png){height=20%}

## High Level Sets and Sequences

1. Sequences vs. Sets
1. Cartesian Product
3. Set builder notation
4. Set Operator Review

### High Level: Sets vs Sequences

* Sets:
    * no duplicates
    * no order
    * has cardinality
* Sequences
    *can have duplicates
    * has order
    * has length
    * lists, arrays, ordered pairs, tuples, etc!
* Both: 
    * Contain anything
    * Can have a sequence of sequences, set of sets, sequence of sets, set of sequences
    * Cannot be modified

### Cartesian Products of Sets

__Ordered Pair:__ An ordered pair is a __sequence with 2 elements.__ It is a pair of obejcts where one element is designated as first and the other element is designated as second, denoted (a, b)

__Cartesian Product:__ The Cartesian product of two sets A and B is denoted $A \times B$, si the set of all possible ordered pairs where the elements of A are the first and the elements of B are second. This is also called the "cross product." 

Example: {1, 2} $\times$ {3, 4, 5} = {(1, 3), (1, 4), (1, 5), (2, 3), (2, 3), (2, 4), (2, 5)}. This returns a set of sequences. The cardinality of this cross product is 6. 

Example: {1, 2} $\times$  {3, 4} $\times$ {4, 5} = ... 

What is {1, 2} $\times$ {2, 3} = {(1, 2), (1, 3), (2, 2), (2, 3)}

* note sequences can have duplicates so (2, 2) is valid! 
* Cardinality is 4

### Cardinality of Cross Product

$\vert A \times B \vert = \vert A \vert \vert B \vert$ (aka, the cardinality of the cross product of two sets is the product of the cardinality of each set)

* Weird Question $\vert$ { {} } $\times$ {1, 2, 3} $\vert$ = ??? 
    * 3 ... since the cross product is = { ({}, 1), ({}, 2), ({}, 3) } !!
* Weird Question $\vert$ {} $\times$ {1, 2} $\vert$ = ?  
    * 0 ... since $\vert \emptyset \vert$ = 0
* Let A= $\{-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6\}$. What is $A^{2}$ = ?
    * $A^{2} = A \times A$
    * $A^{3} = A \times A \times A$
    * etc...
    * Note that $A^{2}$ is every single (x, y) coordinate that falls in the grid created by A. So, $\mathbb{R} \times \mathbb{R}$ is the coordinate plane!

# Jan 25 - subsets & supersets

## $\subseteq, \subset, \supseteq, \supset$

These operators compare two sets. 

* $\subseteq$: subset: think about as $\le$
* $\supset$: superset: think about as $\ge$
* $\subset$: proper subset: think about as <
* $\supset$: proper superset: think about as >

### $\subseteq$

Set A is a __subset__ of B, or $A \subseteq B$, if and only if __all elements of A are also in B__. 

### $\supseteq$

Same thing as subset, but flipped direction!

### $\subset$

Set a is a __proper subset__ of B, $A \subset B$ if and only if $A \subseteq B$ and $A \neq B$. 

Consequences of this definition, $A \subset B$:
* $A \subseteq A$  (this is trivial but true)
* $\vert A \vert < \vert B \vert$ 

Example:

Given P={1, 2, 3}, Q={1, 3}, R={1, 3, 4}, determine whether to use subset, superset, proper subset, or proper superset to have all these equations evaluate to $\top$. 

* $P \supseteq Q$ $\land$ $P \supset Q$ = $\top$ 
    * (however, $\supset$ is more specific)
* $P \not\subseteq R$ $=\top$ 
    * There is no answer for this one!
* $P \supseteq P \land P \subseteq P = \top$

Example 2:

Given P={$\emptyset$, {1, 2}, 3}, Q={1, 2}, R={}, S={3}. Determine how to evaluate to $\top$:

* $P \not\supseteq Q = \top$
    * Think about it!
* $P \supseteq R = \top$
    * Think about it, $\emptyset$ is in P! $\emptyset \subseteq$ every set!
    * And, by extension, $\emptyset \subseteq \emptyset$
* $P \supseteq S \land P \supset S = \top$

if you're tripped up on the first and third bullets, notice the difference and see why they're different.

# Jan 23

## Set Definition

A __set__ is a structure that contains elements.  A __set__ has no other properties other than the _elements_ it contains. A set can contain other sets. Duplicate values aren't allowed, and order doesn't matter! A __member__ or __element__ is something inside the set. A set is written with curly braces, its members separated by commas. 

* {1, 3} or {dog, cat, mouse} or {3, thimble, Jules} or {{1, 2}, 1}
* Sets can be members of other sets!: 
    * {{1, 2}, {3, 4}}
* Sets order doesn't matter;
    * {1, 3, 4} and {4, 3, 1} are the same set
* No duplicates!
    * {1, 3, 4, 1} will "knock" out the duplicate, should be {1, 3, 4}
    * {{1, 2}, {2, 1}} is redundant - this is not a set! It can be just written as {{1, 2}}

The __empty set__ is a set with no members, which is expressed as $\{\}$ or $\emptyset$ (or sometimes "null")

__Cardinality__ is the number of elements in a set. Cardinality is denoted using $\vert A \vert$. What are the cardinality of these sets: 

* $\vert \{1, -13, 4, -13, 1\} \vert$: 3
* $\vert \{3, {1, 2, 3, 4}, 0\} \vert$: 3
    * note that {1, 2, 3, 4} is an element of the bigger set, _not_ a subset.
* $\vert \emptyset \vert$: 0
* |{{}, {{}}, {{{}}} }|: 3

Examples of Infinite Sets

* $\mathbb{N}$: Natural numbers
    * includes 0!
* $\mathbb{Z}$: Integers
* $\mathbb{Q}$: Rational - the ratio of two integers, $\frac{a}{b}$ that is a finite or repeating decimal
* $\mathbb{R}$: Real - 
    * $\infty$ is not a real number!!!
* $\mathbb{C}$: Complex
* $\mathbb{I}$: Imaginary

## $\in \space :$ "Element of"

checks membership of aan element

Examples:

* $2 \in \{1, 2\} = \top$ 
* $3 \in \{1, 2\} = \bot$ 
* $3 \notin \{1, 2\} = \top$ 
* $\{2\} \in \{1, 2\} = \bot$
* $\{2\} \in \{1, \{2\}\} = \top$
* $2 \in \{\{1, 2\}\} = \bot$
* $2 \in \{\{\}\} = \bot$
* $2 \in \{\{\{2\}\}\} = \bot$
* $\{2\} \in \{\{1, 2\}\} = \bot$
* $\{2\} \in \{\{2\}\} = \top$
* $\{2\} \in \{\{\{2\}\}\} = \bot$




    




















