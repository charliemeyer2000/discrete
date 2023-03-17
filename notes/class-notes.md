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

Slides:
    Sets Slides: 
        (First Week) https://docs.google.com/presentation/d/1BXSO-TkmlSSkd3IIVM2yxjG03KVn0roCMBNhjLEHjK0/edit?usp=sharing 

        (set-builder, power set, disjoint) https://docs.google.com/presentation/d/1T2rP6N1PVJkJpt6T9g6k48b1BzLF9N6d-X0LG6QqvV8/edit?usp=sharing

    Proofs Slides: 
        https://docs.google.com/presentation/d/1GfThSz_a312bNEBVl7QGt09YsBJgfgn4CdYqCV03OZc/edit?usp=sharing 
    Week of Feb 20 (Predicates, Quantifiers, Group Activity 1)
        https://docs.google.com/presentation/d/1p8KMkLQc4YXO913QA5ObaHqo7mTHaUkwNxtfW0Ka_bs/edit?usp=sharing
    Week of Feb 27 (Quantifiers, Quiz)
        https://docs.google.com/presentation/d/1gC3FGG-Y8UvYKBntYS6yFn1g867PqTj8g3sVSRhaphY/edit?usp=sharing 

    Week of March 13: 
        https://docs.google.com/presentation/d/1yt7ccKng-_423gbQGQrlX_lPDlShJJHI9WJsVLqv_ug/edit?usp=sharing 
-->

# March 17

## Quiz Study Guide



###  Finding CounterExamples

* Counterexamples for Transitivity

$(x, y) \vert R(x, y) = \top$ and $(y, z) \vert R(y, z) = \top$ but $(x, z) \vert R(x, z) = \bot$

# March 13, 15:

## Relation

Today we'll learn that a _relation_ can be defined as a subset of a cross product.

$$R(x, y) \subseteq X \times Y$$

Given this definition, which of the following is __NOT__ a valid relation over $A \times B$? I.e., select which of the following are NOT subsets of $A \times B$. Recall that a cross product is a set of sequences. 

Let A = {2, 3, 4} and B = {4, 5}

a. {(4, 4)}

b. {(2, 4), (3, 4), (4, 5)}

c. {(4, 4), (5, 4)}

d. $\{(a, b) \vert a \in A \land b \in B\}$

e. $\{(a, b) \vert a \in A \land b \in B \land b = a + 1\}$

f. $\empty$

Correct answer: c is not a subset of $A \times B$ since (5, 4) is not in $A \times B$. 

## Relations

|Math|English|
|-|-|
$A \times B$ | the cross product, $A \times B$
$R \subseteq A \times B$ | R is a relation from A to B
$a R b; (a,b) \in R$ | a is related to b
$a R b; (a, b) \not\in R$ | a is not related to b

For sets $A, B \subseteq u$, any subset of $A \times B$ is called a _relation_ from A to B. 

## Binary (Homogenous) Relations and Notation

Let R be a binary homogenous relation on a Set A, that is: 

$x R y$ where $R \subseteq A \times A$. Note that:

$$x R y = R(x, y) := ((x, y) \in R)$$

### Properties of Binary Relations: Reflexivity

__Definition__: A binary relation R on a set is reflexive iff: 

$$\forall_x \in A . x R x$$ - "All members of the domain are related to themselves."

Some examples of this include $x = x$ or $x \leq x$.

### Properties of Binary Relations: Irreflexivity

__Definition:__ A binary relation R on a set A is _irreflexive_ iff:

$$\forall_x \in A . \neg x R x$$ 

Some examples of this include $x \neq x$ or $x > x$ or $x < x$.

__Definition__: A function is irreflexive iff its complement is reflexive: $R_{irreflexive} = (R_{reflexive})^C$

Irreflexive relations have zeroes down the main diagonal.

#### Proof

* A function is irreflexive iff its complement is reflexive: $R_{irreflexive} = (R_{reflexive})^C$
* consider any reflexive relation, R(x, y) over any set A.
* By definition, if R is reflexive, then all members of A must relate to themselves (define these as reflexive pairs). So, the reflexive pairs are a subset of R: $\{(x, x) \in A^2 | R(x, x)\} \subseteq R$

Consider the adjacency matrix for reflexive relations: 

![Adjacency Matrix](images/adjacencymatrix.png)

Now for the irrefleive relation, we can see that the main diagonal will have 0 rather than 1.

* Consider the relation $I = R^C$. Now we will prove that I must be irreflexive. By definition, if I is irreflexive, then we know then none of the reflexive pairs will be present (since a relation R is defined as irreflexive if $\forall_x \in A . \neg x R x$.
* We know that this is the case for I(x, y) because if an ordered pair is present in R, it will not be a member of $I = R^C$ since by definition

$$I = R^C = \{ (x, y) \in A^2 \vert \neg R(x, y)\}$$

* Following from this definition, for any subset $P \subseteq R \subseteq A^2$, we know those pairs __cannot__ be in the complement ie $R^C \backslash P = R^C = I$. Now consider P to be defined as the reflexive pairs, $\{(x, x) \vert x \in A\}$. Finally, since removing the reflexive pairs resulted in the same set, we know that none of them are present in I. By definition, if no reflexive pairs are present in I(x,y), then the relation is irreflexive. 


### Properties of Binary Relations:  Reflexivity over $\mathbb{R}^2$

$$\forall_x \in \mathbb{R} . x R x$$

All members of the domain are related to themselves

* x = y
* $x \ge y$
* x < y+1

Look at the [desmos example below](https://www.desmos.com/calculator/a7kal08kp3). If x = y is in the graph (shaded), then it is reflexive. 

* So, for equations like $(x-1)^2 + 3 > y$, x=y is always in it. Therefore, it is a reflexive relation. If any part of x=y is not in the graph, then it is not reflexive.


### Properties of Binary Relations: Symmetry

__Definition:__ A binary relation R on a set A is _symmetric_ iff:

$$\forall_{x, y} \in A . x R y \rightarrow y R x$$

Since x and y are both quantified over the same set A, it follows that $\forall_{x, y} \in A . (x R y \rightarrow y R x) \land (y R x \rightarrow x R y)$ then $\forall_{x, y} \in A . x R y \leftrightarrow y R x$. This is the same thing as commutativity!!

Symmetric matrices can be transposed and the result will be the same matrix.

* $A = A^T$ if and only if $A$ is symmetric.

#### Symmetry Example 1

is < symmetric? NO!!

#### Symmetry Example 2

R = {(1, 1), (1, 2), (2, 1), (1, 3), (3, 1)} on the set A = {1, 2, 3}

![Symmetric Matrix](images/symmetricrelation.png)


#### Symmetry over $\mathbb{R}^2$

__Definition__: a binary relation R is symmetric iff:

$\forall_{x, y} \in \mathbb{R} . x R y \rightarrow y R x$

A symmetric relation over the reals must include its reflection over y=x and y=-x

#### Examples: Symmetry

Example 1: Let $R \subseteq \mathbb{R}^2$ be defined as: "less than," <

* Not symmetric!!

Example 2: Let R be equal to $L \subseteq P \times P$ be defined as L(x, y) means "x loves y," where P is the set of people.

#### Reflexivity vs. Symmetry

Reflexivity relates to ITSELF vs. Symmetry is relating to something else! However, being symmetric doesn't mean you are reflexive (necessarily). 


### Properties of Binary Relations: Antisymmetry and Asymmetry

Asymmetry: __Definition__: A binary relation R on a set A is __asymmetric__ iff $\forall_{x, y} \in A . x R y \rightarrow \neg y R x$

If it is asymmetric, it is irreflexive and thus all values on the "main diagonal" are zeroes.

![Asymmetric Relation](images/asymmetricrelation.png)

Antisymmetry: __Definition__: A binary relation R on a set A is __antisymmetric__ iff $\forall_{x, y} \in A  (x R y \land y R x) \rightarrow x = y$

![Antisymmetric Relation](images/antisymmetricrelation.png)

In antisymmetric relations, reflexivity is allowed but not required. 


__Conclusion:__ Asymmetry entails antisymmetry.


#### Examples: Less than Sign

The less than sign is asymmetric and thus entails antisymmetry.

#### Examples: Loves

If loves is asymmetric, love is not reciprocated and no one loves themselves. If loves is antisymmetric, love is not reciprocated but you can love yourself.

### Transitivity

__Definition__: A binary relation R on a set A is transitive iff: $\forall_{x, y, z} \in A . (x R y \land y R z) \rightarrow x R z$

![Transitivity](images/transitivity.png)

Note that the arrows are not going in a circle. x goes to y, y goes to z, and then x goes to z. It's hard to visualize in a matrix, easier with vectors. Below is the matrix. Note that the reflexive relationships don't change transitivity.

![Transitivity Matrix](images/transitivitymatrix.png)

#### Examples: Less than Sign. Transitive or Not?

* Transitive! If 3 > 5 and 5 > 8, then 3 > 8

### Equivalence Relation

__Definition:__ A binary relation R on a set A is _an equivalence relation_ iff it is _reflexive, symmetric and transitive_.

* Example: "The equals sign"

### Partial Order

__Definition:__ A binary relation R on a set A is a _partial order_ iff it is _antisymmetric and transitive_.

* Example: "the less than sign < or "A is a subset of B", $A \subseteq B$

### Relations Vocab

* FILL IN


### Function

Functions assign an element of one set to another set. Functions are a subset of relation. Functions are special, though - every A can map to _at most_ one B. For example, if we consider $f_1 (x) : \mathbb{R} \rightarrow \mathbb{R}$, then $f_1 (x) = 1/x^2$. In this there are parts of the function that are not mapped.

$$f : A \rightarrow B$$

We are used to the notation $f(a) = b$ indicated that f assigns the element $b \in B$ to the element $a \in A$. 


__Codomain__: A function need not be able to return every lement of its codomain. 

__Range__: subset of the codomain

__Domain__: inputs

### Surjective

A surjective function is a function where: $\forall_b \in B, \exists_a \in A, f(a) = b$

#### Examples: $x^2$

Is $x^2$ a surjective function over $\mathbb{R} \rightarrow \mathbb{R}$? NO! It is not surjective because it does not map to every element of the codomain. You can't reach the negatives!! But, $x^2$ is surjective over $\mathbb{R} \rightarrow [0, \infty]$.

### Injective

$\forall_{a_1} \in A, \forall_{a_2} \in A, (f(a_1) = f(a_2) \rightarrow a_1 = a_2)$

This basically means that every input maps to a different output.

### Bijective

Both injective and surjective - one-to-one and every input has an output.

## Summary of Functions 

Here's a photo that summarizes all functions (and non-functions):

![Functions](images/functions.png)



# March 3:

<!-- ## Quiz Review

** This is the entire quiz written out **

Question 1

P: the et of people
L(x, y): the person x likes person y
D(x, y): person x wants to have dinner with person y
A(x): person x is allergic to peanuts
t: the person "Taylor"

GIve a quantified expression to match the english statement, using the symbols above.

Taylor wants to have dinner with everyone who is not allergic to peanuts:

* $\forall_x \in P . \neg A(x) \rightarrow D(t, x)$

There are at least two people who like each other but neither want to have dinner with the other:

* $\exists_{x, y} . L(x, y) \land L(y, x) \land \neg D(x, y) \land \neg D(y, x)$

Everybody likes someone who does not like them

* $\forall_x . \exists_y . \neg L(y, x) \rightarrow$ 

Someone wants to have dinner with everyone who they do not like

* $\exists_x . \forall_y .$

Question 2: Give an english statement for the quantified expression below:

$\forall_x \in P . L(x, x) \rightarrow D(t, x)$

* Taylor wants to have dinner with everyone who likes themselves

$\exists_x \in P . \forall_y \in P . A(x) \land \neg D(x, y)$

* There is someone who is allergic to peanuts and does not want to have dinner with anyone

$\forall_x \in P. (\exists_y \in P . L(y, x)) \rightarrow (\exists_z \in P . D(z, x))$

* if someone likes everyone, then someone wants to have dinner with everyone -->

## A Note on Notation

$\forall_z . (\exists_y . A(y) \lor E(y)) \rightarrow A(z)$

* The period is a replacement for the parenthesis which tells us the _scope_ of the quantifiers. Periods tell us that the scope of the quantifier is starting from it to the end of the statement or a closing parenthesis that came before the quantifier.
* You can rewrite this as:
    * $\forall_z[(\exists_y[A(y) \lor E(y)]) \rightarrow A(z)]$

### Example

Domain: People. Let F = {Apollo, Britomartis, Cupid, Demeter, Bob}. L(x, y) = x loves y

What is $\forall_x \in F . \forall_y \in F . L(x, y)$ -> everyone loves everyone!

#### Negating Quantifiers

If you see this $\not\exists$, rewrite it as $\neg \exists$. Also, swap the quantifier ($\neg \forall$) to $\exists \neg(Stuff)$. 

* $\neg \exists_x (F(x) \lor A(x))$ becomes $\forall_x \neg (F(x) \lor A(x))$
    * which also becomes $\forall_x . (\neg F(x) \land \neg A(x))$

### DeMorgan's Practice

Rewrite: $\neg (\neg \forall_{x, y} \in F . L(x, y))$

* $\neg (\exists_{x, y} \in F . \neg L(x, y))$ -> $\forall_{x, y} \in F . L(x, y)$. Note that this was just a double negation!

Rewrite $\neg (\neg \forall_{x, y} \in F . L(x, y))$ in four different ways!!

<!-- ![DeMorgan's Practice](images/demorgan_practice.png) -->

1. $\neg \exists_x \in F . \neg \forall_y \in F . L(x, y)$
1. $\neg (\exists_x \in F . \exists_y \in F . \neg (L(x, y)))$
1. $\neg \exists_x \in F . \exists_y \in F . \neg (L(x, y))$
1. $\neg (\exists_{x, y} \in F . \neg L(x, y))$
1. $\forall_x \in F . \neg \exists_y \in F . \neg L(x, y)$
1. $\forall_{x, y} \in F \neg \neg L(x, y)$
1. $\forall_{x, y} \in F . L(x, y)$

Note that this is all one big loop - all of these are different ways to say the same thing, $\forall_{x, y} \in F . L(x, y)$.

### One Trick to Avoid

Note that $\not\exists_{x, y} . L(x, y) \equiv \neg \exists_x . \exists_y . L(x, y)$

### Questions to Submit for extra credit

Q1: $\exists_x \in F . \exists_y \in F . \neg L(x, y)$

* There exists someone who doesn't love someone

Q2: $\exists_x \in F . \neg \exists_y \in F . L(x, y)$

* There exists someone who doesn't love anyone

Q3: $\forall_x \in F . \not\exists_y \in F . \neg L(x, y)$

* $\forall_x \in F . \neg \not\exists_y \in F . \neg L(x, y)$

* Everyone doesn't love someone. 

### Entailment

#### Convert this deductive argument into Propositional Logic

1. 6 is an even number (P: 6 is an even number)
1. All real numbers that are even are integers (Q: All real numbers that are even are integers)
1. 6 is an integer (R: 6 is an integer)

#### Predicate Logic

* $s := 6$
* E(x) = x is an even number
* Z(x) = x is an integer
* Domain: real numbers

1. E(S)
2. $\forall_x . E(x) \rightarrow Z(x)$
3. Z(s)


#### Universal Quantifiers and Conjunctions

$\forall_x . E(x) \rightarrow Z(x)$: "All real numbers that are even are integers." Note that you must use $\rightarrow$ rather than $\land$. 

$\exists_x . E(x) \land Z(x)$: "There exists a real number that is even and an integer." Note that you used the $\land$ rather than the $\rightarrow$. Using $\rightarrow$ is vacuously true.

#### Entailment

* Metalanguage:
    * Ex: comments in your code, talking in English about French, analyzing the tone, narrator, and grammar of a passager.







# Feb 27

## Warm-Up
Select all that are equivalent to the situation "Somebody is loved by everybody." If they aren't equivalent, give a counterexample or explain why it's incorrect.

1. $\exists_y . \forall_x (L(x, y))$
    * Correct
2. $\forall_x ( \exists_y (L(x, y)))$
    * Incorrect - this can be phrased as "everybody loves at least one person."
3. $\exists_y . \forall_x L(y, x)$
    * Incorrect - this can be expressed as "there exists at least one person who loves everyone."
    * Consider the situation where someone loves everyone but everyone else doesn't love them back 
4. $\forall_x . \exists_y . L(y, x)$
    * Incorrect - "everyone is receiving love"
5. $\exists_x . \forall_y L(y, x)$
    * Correct - "there exists somebody who's loved by everybody.

Notice how 1 and 5 are similar! They're the same statement just with "flipped" variables. Also, recall how the syntax of using . instead of parenthesis doesn't change it - they're different ways to say the same thing.


![Quantifiers Matching](images/quantifiersmatching.png)

1. Picture A
1. Both
1. Neither
1. Picture B

### Quick Intro to Multiple Quantifiers

Switching order does not always mean logical equivalence!!

$$\exists_y \forall_x L(x, y) \not \equiv \forall_x \exists_y L(x, y)$$

However, notice how even though L(x, y) is _not_ commutative the variables are commutative over the same quantifiers: $\forall_x \forall_y L(x, y) \equiv \forall_y \forall_x L(x, y)$ and if you are using the same quantifiers you can also write it as $\forall_{x, y} . L(x, y)$

_interesting note: see that $\forall_x \exists_y L(x, y) \vDash \exists_y \forall_x L(x, y)$_

### Think about Boolean Logic with Quantifiers!!

Domain: {Ann, Bob, Chris} 

* $\exists_y . \forall_x . L(x, y)$. 
    * $( L(Ann, Ann) \land L(bob, ann) \land L(chris, ann)) \lor (L(ann, bob) \land L(bob, bob) \land L(chris, bob)) \lor (L(Ann, chris) \land L(bob, chris) \land L(Chris, chris))$

### Examples

|Domain|People|
|-|-|
H(x) | x is happy
C(x) | x is in this class
A(x, y) | x appreciates y

1. Everyone is happy
    * $\forall_k . H(k)$
1. Everyone in this class is happy
    * $\forall_x . (C(x) \rightarrow H(x))$
1. Someone is happy
    * $\exists_x . H(x)$
1. Someone in this class is happy
    * $\exists_x . (C(x) \land H(x))$
    * Note that I used the $\land$ rather than the $\rightarrow$!! This is because it is satisfied if anyone is not in the class __or__ anyone is happy.
1. Not everyone is happy
    * $\neg \forall_x H(x)$
1. Only one person is happy
    * $\exists_x . H(x) \land \forall_y . (y \neq x) \rightarrow \neg H(y)$

# Feb 24

Group Activity 1 


# Feb 22

### Universal Quantifier

$\forall$ = "for all" or "given any." It expresses that a propositional function can be satisfied by _every member of the domain_. 

### Ambiguous Question

"Everybody does not love Chris" or "Everybody hates Chris." How cna you rephrase this?

* For all people, each one does not love Chris.
    * $\forall_x . \neg L(x, \text{Chris})$
* There does not exists one person who loves Chris.
    * $\neg (\forall_x . L(x, \text{Chris}))$
    * This can be translated as "It is not the case that across all the people everybody loves Chris."


### $\exists$: Exists - Existential Quantifier

Consider the exists symbol, the complement to $\forall$. This means "there exists" or "there is at least one" or "for some." It expresses that a propositional function _can be satisfied by at least one member of the domain_.

"There does not exist one person who loves Chris."

* $\neg (\exists_x . L(x, \text{Chris})) \text{ or } \neg \exists_x . L(x, \text{Chris})$

You can also use $\not\exists$ instead of $\neg\exists$. You can also do $\exists_x \exists_y$ as $\exists_{x, y}$

### Interesting paradox

Remember that:

* $\neg \exists_x L(x, \text{Chris})$ means "There does not exist one person who loves Chris."
* $\forall_x \neg L(x, \text{Chris})$ means "For all people, each one does not love Chris."

Therefore:

$$\neg \exists_x . L(x, \text{Chris}) \equiv \forall_x . \neg L(x, \text{Chris})$$
$$\not\equiv$$
$$\exists_x . \neg L(x, \text{Chris}) \equiv \neg \forall_x . L(x, \text{Chris})$$

### What does the . mean?

Note that $\exists_x . L(x) \equiv \exists_x (L(x))$. This just specifies scope.

### Importance of Domains Example

Is the logical expression $\forall_x . Q(x)$ true or false with $Q(x) = (x^2 \ge x)$. False!!

* Well, I mean... what is the domain? That's the trick question! We need to specify what _x_ is before we can evaluate this expression.

Now, here's a different question:

$\forall_x \in \mathbb{Z} (Q(x))$ ? 

* $\top$

$\forall_x \in \mathbb{R} . Q(x)$?

* $\bot$

We can evaluate these since they have a specific domain!

### $\exists$ and $\forall$

Associate "for all" with _and's_ since it becomes false if just _one_ truth value is false, and associate "there exists" with _or's_ since it becomes true if just one truth value is true. 

### $\exists$ and $\forall$

What about:

* $\forall_x \in \empty . Q(x)$
    * $\top$ - _vacuously_ true. 

consider it as a for loop:

``` python
def for_all(S)
    Q = True
    for x in S:
        Q = Q and Q(x)
    return Q
```

* $\exists_x \in \empty . Q(x)$
    * $\bot$ - _vacuously_ false


# Feb 20

## Review Mod1Multi2

Question 1: Can you apply simplification $((P \rightarrow Q) \rightarrow R) \lor (P \land Q)$? 

* Yes!! Recall that simplification can go _both_ ways. You could add an $\lor \bot$. 

Question 2: $(P \lor R) \land (Q \lor R) \oplus (P \lor Q)$

* This question was taken off because there are no parenthesis to tell you which order to do things. Thus, it should either be:
    * $((P \lor R) \land (Q \lor R)) \oplus (P \lor Q)$ 
    * $(P \lor R) \land ((Q \lor R) \oplus (P \lor Q))$

### Good to have in your back pocket

|english phrase| DMT phrase|
|-|-|
If p then q | p implies q
if p, q | p only if q
p is sufficient for q | a sufficient condition for q is p
q if p | q whenever p
q when p | q is necessary for p
a necessary condition for p is q | q follows from p
q unless $\neg p$ | q provided that p

### Predicates and First-Order Logic

We can only do so much with atomic propositions. To say more interesting things like "All files that are larger than 1,000 blocks are to be moved to backup provided that they have not been referenced within the last 100 days and that they are not in system files," we need more!

* Atomic propositions: just letters that reference a proposition, e.g. P = "It is sunny today" or Q = "It's Friday"
* A predicate is a proposition that has a(n) argument(s).

### Predicates

Three different definitions of a predicate:

* A function that evaluates to true or false
* A proposition missing the noun(s)
* A proposition template

Determine the predicate and the arguments of the following sentence: "Sam loves Diane." 

* L(x, y) = ___x loves ___y
* "Sam loves Diane" formalizes to L(Sam, Diane)
* "Diane doesn't love Sam" formalizes to $\neg L(\text{Diane}, \text{Sam})$
* "I love lucy" formalizes to $L(i, Lucy)$
* Note that $L(\text{Sam}, \text{Diane}) \not\equiv L(\text{Diane}, \text{Sam})$! It is _not_ commutative. Think of this L(x, y) as a binary function. Love is directional. Diane can loves Sam without Sam loving Diane

What about the statement "Everyone loves Raymond?"

* First you have to specify what your "universe" or "domain" is. Let's say our domain is U = {A, B, C, Raymond}. 
* $\forall_x \in U . L(x, \text{Raymond})$
<!-- * note that this answer doesn't encode Raymond not loving himself. So, if you want to encode that, do something like this:
    * $\forall_x \in U . \exists_y \in U . L(x, \text{Raymond}) \land x \neq y$ -->
* This is a "for all" operator which is synonymous with a repetitive "and" operator, since you could also just write it as L(A, Raymond) $\land$ L(B, Raymond) $\land$ L(C, Raymond) $\land$ L(Raymond, Raymond)
* Also note that you don't have to specify what set the quantifier is in if the domain is specified, as it assumes it is in the domain if not specified







# Feb 17

Practice before Mod1Quiz2:

Review

$\neg (A \land B)$ and $(\neg A \lor \neg B)$ - DeMorgan's

If you were to go from $\neg Q \lor R$ to $\neg (Q \land \neg R)$, make sure to also include the step of double negation in between : $\neg (Q \land \neg \neg R)$

Associativity Rule - when in doubt, you can always do expressions as variables. 



# Feb 15

Did an in-class worksheet. These are the correct answers

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

An alternate solution is:

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


# Feb 13

## Do Now

Make a Truth Table for the expression $\neg p \land \neg q$. Then make a truth table for $\neg (p \land q)$. Are they the same?

* No! I made the truth tables in my iPad but they're not. Recall distributing a $\neg$ across parenthesis reverses or -> and, and -> or.
    * So, $\neg(P \land Q) \neq \neg P \land \neg Q$

![Do Now](images/twotables.jpg)

## Boolean Algebra

__Associative Property__: You can change the order in which you perform operations and not change the outcome. So, for example, (2+3)+5=2+(3+5) is true whereas (2-3)-5 $\neq$ 2-(3-5). 

For our case, we will be dealing with rules that operate over boolean values. 

Which symbols are associative?

* $\neg$ - __NO__: it is a unary operator
* $\lor$ - __YES__: switching the order doesn't matter
    * $(A \lor B) \lor C \equiv A \lor (B \lor C)$
    * Think of this as a Venn Diagram - both sides are equivalent!
* $\land$ - __YES__: switching the order doesn't matter
    * $A \land (B \land C) \equiv A \land (B \land C)$
    * Same - think of it as a Venn Diagram. 
* $\oplus$ - __YES__
* $\leftrightarrow$ - __YES__
* $\rightarrow$ - __NO__
    * Take a look at these two truth tables:
* Be careful when you use the property over different operators!! Note that expressions like $(A \land B) \lor C$ is not equivalent to $A \land (B \lor C)$!!

|A|B|C|$A \rightarrow (B \rightarrow C)$ | $(A \rightarrow B) \rightarrow C$|
|-|-|-|-|-|
0|0|0|__1__ 1|1 __0__
0|0|1|__1__ 1|1 __1__
0|1|0|__1__ 0|1 __0__ 
0|1|1|__1__ 1|1 __1__
1|0|0|__1__ 1|0 __1__
1|0|1|__1__ 1|0 __1__
1|1|0|__0__ 0|1 __0__ 
1|1|1|__1__ 1|1 __1__

Note how we could have stopped on the first row of the $(A \rightarrow B) \rightarrow C)$ since those two rows aren't equal. If you say something is $\equiv$ then it must be true for all possibilities!

### Associativity

![Associativity](images/associative.jpg)

### Communitive Property

Communative property is when you can swap the operands' position.

Which symbols are communative:

* $\neg$ - __NO__
* $\lor$ - __YES__
* $\land$ - __YES__
* $\oplus$ - __YES__
* $\leftrightarrow$ - __YES__
* $\rightarrow$ - __NO__

Here's an example of a proof using associativity and commutativity

![Commutative and Associative Proof](images/assandcomm.jpg)

### DeMorgan's and/or

* Or lends itself to union
* And lends itself to intersection

So, that is, 

* $\neg (P \lor Q) \equiv \neg P \land \neg Q$
* That is to say that $(p \cup q)^{c} \equiv p^{c} \cap q^{c}$
* Same in the opposite direction!

Here's an example of a proof using DeMorgan's Laws:

![DeMorgan Proof 1](images/DMlaw.jpg)

### Distributive Property

Here's an example proof using the Distributive Property:

![Proof Using Distributive Property](images/distributivelaw.jpg)


# Feb 10

## Do Now

Represent the problem with voting we discussed earlier as a venn diagram.    _hint_: Make one set (or variable) to represent __people who are 18+__ and a second intersecting set to represent __people who voted__.

How can i write that with an "if-then" statement? 

* "if you voted, then you _must_ be over 18."
* "if you're under 18, then you can't vote."

### Truth Table Example

![Truth Table 2](images/truthtable2.png)

## Boolean Algebra

Example: Prove 3(x+y) = 3x+3y. Let $x, y \in \mathbb{N}$. 

Try:

* x=0 and y=0. 3(0+0) = 3(0)+3(0).
* x=1 and y=0. 3(1+0) = 3(1)+3(0).
* x=2 and y=0. 3(2+0) = 3(2)+3(0).
* ...

## "Is equivlent to" $\equiv$. 

### Anatomy of an Equivalence Proof

Here's an example of a proof: Prove $(P \lor Q) \lor (R \lor Q) \equiv (P \lor Q) \lor R$

You must start with the left-hand side of the equation and must end with the right-hand side of the equation. You must provide justification for each step, and every expression in between must be equivalent.

|sign|proposition|reasoning|
|-|-|-|
||$(P \lor Q) \lor (R \lor Q)$ | Given
$\equiv$ | $(P \lor Q) \lor (Q \lor R)$|commutativity
$\equiv$ | $((P \lor Q) \lor Q) \lor R$|associativity
$\equiv$ | $(P \lor (Q \lor Q)) \lor R$ | associativity
$\equiv$ | $(P \lor Q) \lor R$ | simplification

## IMPORTANT LOGICAL RULES

__[Logical Rules](https://www.cs.virginia.edu/~emo7bf/cs2120/s2023/axioms.html)__

## Equivalences 

### Simplifications

Simplifications have the property that they make expressions smaller, with fewer operators. The first five important ones are:

|long|simplified|name of rule|
|-|-|-|
$\neg \neg P$ | P | double negation
$\neg \top$ | $\bot$ | definition of $\bot$
$P \land \bot$ | $\bot$ | simplification
$P \land \top$ | P | simplification
$P \lor \bot$ | P | simplification
$P \lor \top$ | $\top$ | simplification

#### Proof using opposite of simplificaiton

Prove: $P \equiv P \land (P \leftrightarrow \top)$. Sneaky tactic is to switch the sides and solve. 

* Start with the parenthesis. How do I simplify $p \leftrightarrow \top$?
    * $\top$ : Simplification!
* Now do $P \land \top$
    * $P$: Simplification!
* Thus, $P \equiv P$

|sign|proposition|rule
|-|-|-|
x|$P \land (P \leftrightarrow \top)$ | given
$\equiv$ | $P \land P$ | simplification
$\equiv$ | P | simplification.

Now you can rewrite the table to "expand" it and properly write the equation:

|sign|proposition|rule|
|-|-|-|
||P|given
$\equiv$|$P \land P$ | simplification
$\equiv$ | $P \land (P \leftrightarrow \top)$ | simplification

### Definition of Implication

Prove: $A \rightarrow (B \oplus A) \equiv \neg A \lor (B \oplus A)$

* think about it: $A \rightarrow B \equiv \neg A \lor B$ where $A = P$ and $B = (Q \oplus P)$

|sign|proposition|rule|
|-|-|-|
||$p \rightarrow (Q \oplus P)$ |given
$\equiv$| $\neg p \lor (Q \oplus P)$ | definition of implication





# Feb 8 

## Reminders from Quizzes

* Any powerset must be a set, i.e. $P(S) = \{\emptyset, ..., S\}$
* Sequences are in params (...)
* Sets are in curly braces {...}
* $\{\emptyset\} \neq \{\}$

## Regrade Requests

Drop by a TA office hours _first_, then if the TA affirms that you got it right, then request points back. 

## Do Now - Thought Experiment

There are four cars below, each with a letter __on one side__, and a __number on the other__ side.I make the unsubstantiated claim that __"if a card has a number less than 18, then there must be a vowel (A) on the other side of that card.__" You are allowed to flip over __only two cards__ to prove or disprove my claim.

![Do Now](images/donow.png)

### Evaluating Propositions

A proposition: __"If a card has a number less than 18, then there must be a vowel on the other side of that card."__

How do we evaluate this proposition with this thought experiment? Use a truth table!

||A |B
|-|-|-|
n < 18 | T | F
$\neg ( n < 18)$ | T | T

Note that: $\neg(n < 18) \equiv (n \ge 18)$

A proposition: __"Either card does _not_ have a number less than 18, or it has a vowel."__ Let's rephrase it as __"either the number the number is $\ge 18$ or it has a vowel, or both."__ Here is the associated truth table:

||A |B
|-|-|-|
n < 18 | T | F
$\neg ( n < 18)$ | T | T


### Same problem, rephrased

We now have a group of 4 people at a polling place. Some people are casting a ballot, others are not. You must be at least 18 years old to vote. Each person has an ID card -- one side their age, the other with a letter. The letter _A_ on the voter's ID card indicates they didn't vote. The letter _B_ indicates that they did vote. Your job is to figure out if anyone voted illegally. You can flip over two cards to decide. 

![Do Now](images/donow.png)

Which one do you flip? 

* not 1, they didn't vote
* yep, flip 2 since you don't know whether or not it's right.
* Nope, not 3, you know they're a legal voter
* yep, flip 4. 

So, $(n \ge 18)$ OR (isVowel) $\equiv$ if ($n < 18$) then (isVowel)

### "Implies" Operator

Truth table for "implies" operator. If it helps, think p = "the person voted" and q = "they're over 18."

|p|q|p$\rightarrow$q|
|-|-|-|
0|0|1
0|1|1
1|0|0
1|1|1

Note that $\neg p \lor q$ is the same as $p \rightarrow q$


### Doin this Truth Table Her Way

Remember that $\neg$ is a unary operator, if there aren't any parenthesis (like in this example) you should be evaluating $\neg p$ first. Each operator has its own column.

Make sure to put a BOX around your answers (my answers are bolded lol)

|p|q|$\neg p \lor q$
|-|-|-|
0|0|1  __1__
0|1|1  __1__ 
1|0|0  __0__
1|1|0  __1__


Another truth table her way. Make sure to put the final answer under the $\land$ symbol. the first one you evaluate is within the parenthesis, second one (final answer) is under the $\land$, in a box/bolded.

|A | B | C | $(A \lor B ) \land C$
|-|-|-|-|
|0|0|0|-|
|0|0|1|-|
|0|1|0|-|
|0|1|1|-|
|1|0|0|-|
|1|0|1|-|
|1|1|0|-|
|1|1|1|-|



### Another way to understand implication

P = My animal is a poodle
Q = it is a dog

|p|q|p$\rightarrow$q|
|-|-|-|
0|0|1
0|1|1
1|0|0
1|1|1

### Venn Diagram of "Implies"

![implies](images/implies.png)


# Feb 6 - Conditionals

## Review

### Quiz Review

$\{\{x\} \times \{y\} \vert x \in \{-1, 0, 1, 2\} y \in \mathbb{N} \ y < x\}$

* {{(1, 0)}, {(2, 0)}, {(2,1)}}

$S = \{x - y \vert (x, y) \in (\{8\} \times \{3, 5\})\}$

* $\{3, 5\} \subset S$ is False.

### Symbols


* $\in$ element of 
* $\subset$ proper subset of
* $\subseteq$ subset of
* P(S) power set of s
* $\vert S \vert$ cardinality
* $S \times T$ S cross T
* $S^{2}$ S cross S

## Propositions

A proposition is a statement that is either true or false.

|Examples of a proposition| Examples of things that aren't a proposition|
|-|-|
Jeremy got the question right| What score did you get on the quiz?
There is only one Jeremy in the class | Is Jeremy the only jeremy in the class?
Taco bell can be used as a laxative | How are you?
Something that is true or false | any imperative statement (i.e. do this, don't do this)

When dealing with propositions, we abstract away difficulties of defining, and we can give them letters (define variables), like P. So, we can say (2+2=5)=P, or ("I am a human") = Q.

### True vs. False

|Concept|Java/C|Python|This class| Bitwise|Name|other
|-------|------|------|----------|--------|----|-----|
true|`true`|`True`|$\top$ or 1| 1|tautology|T
false|`false`|`false`|$\bot$ or 0|0|contradiction|F

The most "mathematically rigorous" way to describe True or False is: $\top$: True; and $\bot$: False. You can also use 1: True; 0: False. 

### Connectives

A proposition is a statement that is either true or false. We can modify, combine, and relate propositions with connectives:

$\land$, (logical and), $\lor$, (logical or), $\neg$, (not), $\leftrightarrow$, (iff), $\rightarrow$, (implication), $\oplus$, exclusive or.

### Propositions

We can modify, combine, and relate propositions with _connectives_:

* $\lor$ is "or"
* $\land$ is "and"
* $\neg$ is "not"

### Truth Table

How to define: make a truth table!

There are two possible inputs to a "not" operator - it is either a $\top$ input or a $\bot$ input. Note that the first column, "P" is the input and $\neg P$ is the output. Notice how "not" only takes in one input, it is a "unary operator."

|P|$\neg P$|
|-|-|
0|1
1|0

Here is an image that contains all the truth tables for the truth table values for "not" 

![Truth Table](images/truthtable.png)

### "And" Operator

Think of this as the "intersection" for example. Note how this is a "binary operator" as there are two inputs. Thus, there are four possible cases - there are _four_ regions in the venn diagram! 

* if you have three intersecting venn diagrams, you have 8 possible inputs.
* if you have n venn diagrams, you have $2^{n}$ inputs

|p|q|$p \land q$
|-|-|-|
1|1|1
1|0|0
0|1|0
0|0|0

### "Or" Operator

Think of this as the "union" sign, for example. 

|p|q|$p \lor q$
|-|-|-|
0|0|0
0|1|0
1|0|1
1|1|1

### "Xor" operator

An example: 
* I want fries __or__ a drink. - you can have both!
* I want it for here __or__ I want it to go. - you can only have one!! Note that this is the use of $\oplus$

![Xor](images/xor.png)

Truth Table:

|p|q|$p \oplus q$|
|-|-|-|
|0|0|0
|0|1|1
|1|0|1
|1|1|0

## "Bi-implies" operator (iff)

This is the negation of $\oplus$.

![bi-implication](images/bi-implication.png)

|p|q|$p \leftrightarrow q$
|-|-|-|
0|0|1
0|1|0
1|0|0
1|1|1

### Putting Conditionals Together

|p|$\neg$|p|$\lor$|p|
|-|-|-|-|-|
0|1|0|1|x
1|0|1|1|x

### How to Do Elizabeth's Truth Tables

This is the order of how to do the truth tables 

|p|q|$\neg(p \land q)$|
|-|-|-|
T|T|-|
T|F|-|
F|T|-|
F|F|-|

First apply the $\land$ rule for the parenthesis

|p|q|$\neg(p \land q)$|
|-|-|-|
T|T|T|
T|F|F|
F|T|F|
F|F|F|

Next apply the $\neg$ operator

|p|q|$\neg(p \land q)$|
|-|-|-|
T|T|__F__ T|
T|F|__T__ F|
F|T|__T__ F|
F|F|__T__ F|

The bolded outcome is the final answer!


# Feb 3 - Quiz 1 In-Class! 

## Review before Quiz

Note that what's on review is _really_ important.

### Cartesian (Cross) Product

If $x = 3,$ then what is $x\in A \times B$? = False
The point is, the cartesian product returns the set of ordered pairs! Think of the cartesian product as a table:

### Power Set

Recall that a power set returns a set of all possible subsets. It is a set of sets!

### Other

What is $\vert \{\{x, y\} \vert x, y \in H\ \vert$ when H = {1, 2, 3}?

Think of it as a table, again! This is cartesian product of H with itself!

* $\vert$ { {1}, {2}, {3}, {1, 2}, {2, 3}, {1, 3} } $\vert$ = 6

What is $\{x + y \vert (x \in \{1, 2\}) \land (y \in \mathbb{N}) \land (y < x)\}$? = {1, 2, 3}

Which of the following contain the empty set as a number when H = {} and K = {}

* $\mathbb{N}$? No.
* P($\mathbb{Z}$)? Yes.
* $\{x \vert x \in (K \backslash H)\}$? 
* $\{x \vert (x \subseteq K ) \land (x \subseteq H)\}$? True
* $\{\{x+y, x-y\} \vert (x \in H) \land (y \in H) \}$

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
    * can have duplicates
    * has order
    * has length
    * lists, arrays, ordered pairs, tuples, etc!
* Both: 
    * Contain anything
    * Can have a sequence of sequences, set of sets, sequence of sets, set of sequences
    * Cannot be modified

### Cartesian Products of Sets

__Ordered Pair:__ An ordered pair is a __sequence with 2 elements.__ It is a pair of objects where one element is designated as first and the other element is designated as second, denoted (a, b)

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




    




















