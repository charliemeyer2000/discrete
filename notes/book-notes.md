---
title: Discrete Mathematics and Theory (2120)
author: Charlie Meyer
geometry: margin=0.5cm
date: MoWeFri 1:00 - 1:50
header-includes:
- \usepackage{amsmath}
- \newcommand{\doublearrow}{\leftrightarrow}
---

<!-- 
Math for computer science textbook: https://www.cs.virginia.edu/~emo7bf/cs2120/s2023/files/mcs.pdf

Forall x: https://www.cs.virginia.edu/~emo7bf/cs2120/s2023/files/forallx.pdf

forall x solution book: http://forallx.openlogicproject.org/solutions/forallxsol.pdf

cd notes
pandoc -f markdown-implicit_figures -s -o book-notes.pdf book-notes.md


-->

# MCS 3.4.2 and $\forall x$ 14-15 and equivalences and example proof and proof techniques and direct proof

# _Propositions_ and _operators_: MCS 1.1 and $\forall x$ 4.3 and MCS3-3.2.0 and $\forall x$ 5 and about $\rightarrow$ and operators

## MCS 1.1

### Propositions

A _proposition_ is a statement that is either true or false. In the examples below, the first is true and the second is false.

* __Proposition 1.1.1__ $2 + 3 = 5$
* __Proposition 1.1.2__ $1+1=3$

Being true or false excludes statements that are not binary answers, and also excludes questions whose truth varies on circumstance. Unfortunately, not all propositions are easy:

* __Proposition 1.1.3__: For every nonnegative integer, n, the value of $n^{2} + n + 41$ is prime.

To check this, we can let $p(n) ::= n^{2} + n + 41$ (::= means "equal by definition). However, we see that p(40) = $40^{2} + 40 + 41 = 41*41$ which is not prime. But, the point of this was to show that in general, you can't check a claim about an infinite set by checking a finite set of its elements, no matter how large the finite set. And, __Proposition 1.1.3__ could also be rewritten as: $\forall_{n} \in \mathbb{N}.$ p(n) is prime.

Some other cool theorems: 

* Fermat's Last Theorem: _There are no positive integers x, y, and z such that  $x^{n} + y^{n} = z^{n}$ for some integer $n > 2$. This was eventually proved incorrect.
* Goldbach's Conjecture: _Every even integer greater than 2 is the sum of two primes_. To this day, no one nows whether it's true or false. 

## $\forall_{x}$ 4.3 - Atomic Sentences

Entirely unhelpful? 

## MCS 3 - 3.2.0

While there is a ton of ambiguity in the english language in common speech, in mathematics it is necessary to formulate speech precisely, as we can't make an exact argument if we're not sure what the statements we're even arguing mean!

### Propositions from Propositions

Propositional variables are used in place of specific propositions and can only take on the values of $\top$ or $\bot$. 

#### 3.1.1 - Not, and, and or 

If P is a proposition, then so is not(P). 

| P | not(P) | 
|---|--|
$\top$ | $\bot$
$\bot$ | $\top$

The truth table for the proposition "P and Q" can be seen below: 

| P | Q | P and Q|
|-|-|-|
T | T | T
T | F | F
F | T | F
F | F | F

The truth table for the proposition "P or Q" can be seen below: 

| P | Q | P or Q|
|-|-|-|
T | T | T
T | F | T
F | T | T
F | F | F

If you want to exclude the possibility of having both, then use the "xor," exclusive-or, opeation:

|P|Q|P xor Q|
|-|-|-|
T | T | F 
T | F | T
F | T | T
F | F | F

#### 3.1.2 - Implies

The combinding operation with the least intuitive technical meaning is "implies." This can also be understood as "An implication is true when the if-part is false or the then-part is true." Here is the truth table:

|P | Q | P implies Q| 
|-|-|-|
T | T | T (tt)
T | F | F (tf)
F | T | T (ft)
F | F | F (ff)

The idea of "implies" can allow us to see whether the proposition evaluates to true or not. For example, "If Goldbach's Conjecture is true, then $x^{2} \ge 0$ for every real number x." Now, this sentence is a proposition in the form "P implies Q." The hypothesis, P, is "Goldbach's Conjecture is true" and the conclusion, Q, is "$x^{2} \ge 0$ for every real number x." Since the conclusion is definitely true, we're either on (tt) or (ft) of the truth table - either way, the proposition as a whole is _true_! 

Here's an example of a false implication: "If the moon shines white, then the moon is made of white cheddar." Yes, the moon shines white. But no, the moon is not made of white cheddar cheese. So we're on line (tf) of the truth table, and thus the proposition is _false_.

#### False Hypotheses

An illustrative example of false hypotheses is a system specification which consisted of a series of a dozen rules:

* if $C_{i}$: the system sensors are in condition _i_, then $A_{i}$: the system takes action _i_. Or, more concisely, $C_{i}$ implies $A_{i}$ for $1 \le i \le 12$. Then the fact that the system obeys the specification would be expressed by saying that the :

* [$C_{1}$ implies $A_{1}$] and [$C_{2}$ implies $A_{2}$] and ... and [$C_{12}$ implies $A_{12}$] (3.1)

Suppose conditions $C_{2}$ and $C_{5}$ are true, and the system indeed takes on the specified actions $A_{2}$ and $A_{5}$. This means that in this case the system is behaving according to the specification, and accordingly we want the formula 3.1 to come out to _true_. Now the implications $C_{2}$ implies $A_{2}$ and $C_{5}$ implies $A_{5}$ are both true because their hypotheses and their conclusions are true. But in order for 3.1 to be true, we need all other implications with the false hypotheses $C_{i}$ for $i \neq 2, 5$ to be true. This is exactly what the rule for implications with false hypotheses accomplishes. 

#### If and Only If

Mathematics joins propositions in one additional way: The proposition "P if and only if Q" asserts that P and Q have the same truth value - either both are true or both are false.

|P | Q | P iff Q|
|-|-|-|
T | T | T 
F | T | F
T | F | T
F | F | T

for example, the following _iff_ statement is true for every real number _x_: $x^{2} - 4 \ge 0 \iff \vert x \vert \ge 2$.

* Note that: "iff" is $\iff$. 
* For some values of _x_, _both_ inequalities are true. For other values of _x_, _neither_ inequality is true. In every case, however, the IFF proposition as a whole is true. 

### 3.2 - Propositional Logic in Computer Programs

Consider the code snippet: `if (x > 0) || (x <= 0 && y > 100)`. Let A be the proposition taht `x>0` and let B be the proposition that `y > 100`. Then we can rewrite the condition as: "A or (not(A) and B).

#### 3.2.1 - Truth table calculation

Let's evaluate the truth table of the expression "A or (not(A) and B)":

|A|B| A or (not(A) and B)|A or B|
|-|-|--------------------|------|
T | T| T | T
T | F | T | T
F | T | T | T
F | F | F | F

Note that somehow, the outputs of A or B are the same as "A or (not(A) and B). Expressions whose truth tables always match are called _equivalent_. So, we can simplify the code without changing its behavior to `if (x > 0 || y > 100)`.

#### Notation

|English| Symbolic Notation|
|-|-|
Not(P) | $\neg P$ (alternatively, $\bar{P}$)
P and Q | $P \land Q$
P or Q| $P \lor Q$
P implies Q | $P \to Q$
if P then Q | $P \to Q$
P iff Q | $P \leftrightarrow Q$
P xor Q | $P \oplus Q$

For example, the notation "If P and not(Q), then R" would be written: $(P \land \bar{Q}) \to R$. 

### $\forall_{X}$ 5 - Connections

|symbol|what it is called|rough meaning|
|-|-|-|
$\neg$| negation| "it is not the case that"
$\land$| conjunction|"both...and..."
$\lor$| disjunction | "either...or..."
$\to$ | conditional | "if...then..."
$\leftrightarrow$ | biconditional | "... if and only if ..."

#### 5.1 - Negation

Consider the statement B: "Mary is in Barcelona." Using $\neg$, we can symbolize the sentence "It is not the case that Mary is in Barcelona" using $\neg B$. 

You can also express things like "The wrench is not irreplaceable" by saying $\neg \neg B$. Be careful of tricks like "Jane is unhappy." If we were to say $\neg B$, then we would be saying "It is not the case that Jane is happy," however the phrase "Jane is unhappy" could mean she could be in a state of neither happiness nor unhappiness. 


#### 5.2 - Conjunction

Consider: 

1. Adam is athletic
1. Barbra is athletic
1. Adam is athletic, and Barbara is also athletic.

The third expression can be written as a conjunction of the two - $2. \land 3.$. 

You can then use the previous statements and use parenthesis to express expressions like "it's not the cae that you will get both soup and salad" like $\neg (S_{1} \land S_{2})$ where $S_{1}$ means "you will get soup" and $S_{2}$ means "you will get salad."

#### 5.3 - Disjunction

Consider:

1. Either Fatima will play videogames, or she will watch movies.
1. Either Fatima or Omar will play videogames.
    * F: Fatima will play videogames
    * O: Omar will play videogames
    * M: Fatima will watch movies

To express these expressions, we need to express sentence 1. using $F \lor M$, called _disjunction_. We can express sentence 2 as $F \lor O$. 


#### 5.4 - Conditional

Consider these sentences:

1. If Jean is in paris, then Jean is in France
1. Jean is in France only if Jean is in Paris.
    * P: Jean is in Paris
    * F: Jean is in France

We can symbolize sentence 1. as $P \to F$. This connective is called "the conditional." Here, P is the _antecedent_ and F is the _consequent_. We can symbolize sentence one as $F \to P$. 


#### 5.5 - Biconditional

Consider:

1. Josie is a dog only if she is a mammal
1. Josie is a dog if she is a mammal
1. Josie is a dog if and only if she is a mammal
    * J: Josie is a dog
    * M: Josie is a mammal

Sentence 1 can be symbolized as $J \to M$. Sentence 2 can be symbolized as $M \to J$. Sentence 3 says something stronger than either 1 or 2 - it can be paraphrased as "Josie is a dog if josie is a mammal, and josie is a dog only if josie is a mammal. This can be expressed by $J \leftrightarrow M$. This is called the "biconditional," or "iff" - if and only if. A sentence can be symbolized as $A \leftrightarrow B$ if it can be paraphrased in english as 'A iff B,' as 'A if and only if B.'


#### 5.6 - Unless

We can use all the connectives to express many kinds of sentences with complex structures. For example, the sentence "Unless you wear a jacket, you will catch a cold" where J="You will wear a jacket" and D="You will catch a cold" can be expressed as $\neg J \to D$.

## About $\to$: "If" and Logic

### If

#### If it rains, I'll get wet. 

Logical part is $R \to W$. 

|Raining?|Wet?| Consistent with the phrase?|
|-|-|-|
No|no|yes
No|yes|yes
Yes|no|no
Yes|yes|yes

Beyond Logic - there's a connotation which propositional logic cannot encode that rain starts shortly before wetness and there's a causal connotation that propositional logic cannot encode that rain creates wetness.

#### If you earn a 93% or more, you get an A

Logical part: $E \leftrightarrow A$

|Earned 93?| Get A?|Consistent with phrase?|
|-|-|-|
No|no|yes
no|yes|no
yes|no|no
yes|yes|yes

Beyond logic - there's a temporal condition - you get the 93% before you get the A - which cannot be encoded in propositional logic. Further, the $\leftarrow$ part is "fuzzy." A 92.8% might get you an A, but an 81% won't. The $\to$ part is implicitly "or more": an A+ would not be a problem. 

#### This program crashes if you type Ctrl+Q

Logical part: $C \leftarrow Q$

|it crashes?|Ctrl+Q?| Consistent with phrase?|
|-|-|-|
No|no|yes
no|yes|no
yes|no|yes
yes|yes|yes

Beyond logic - there's a temporal connection that you press Ctrl+Q before it crashes and theres a causal connotation that typing Ctrl+Q triggers the crash that logic cannot encode


### When

#### I love it when it rains

Logical part: $L \leftarrow R$

|I love it?|It rains?| Consistent with the phrase?|
|-|-|-|
no|no|yes
no|yes|no
yes|no|yes
yes|yes|yes

Beyond logic - "when" connotes that the truth of _R_ comes and goes. It also connotes that rain _will_ happen eventually; "if" in this phrase would have some logical meaning, but it would imply doubt that rain would ever occur.

#### I sing when in the shower

Logical part - $\top$

|I sing?|Showering?|consistent with phrase?|
|-|-|-|
no|no|yes
no|yes|yes
yes|no|yes
yes|yes|yes

Beyond logic - This means that there exist some times when i am both in the shower and singing, but does not rule out either singing outside the shower nor that I might have some in-shower time when I'm not singing. We can encode that "there exists some time" idea with first order logic - $\exists t. S(t) \land H(t)$ but not with propositional logic.

### Only

#### It only rains at night

Logical part - $R \to N$

|it rains?|It's night?| consistent with phrase?|
|-|-|-|
no|no|yes
no|yes|yes
yes|no|no
yes|yes|yes

#### I only love my spouse

Logical part - $L \leftrightarrow S$

|I love it?| It's my spouse?| Consistent with phrase?|
|-|-|-|
No|no|yes
no|yes|no
yes|no|no
yes|yes|yes

Beyond logic - the use of "only" implies "love" means something more specific than it would like a phrase "I love cake"and possibly something even more specific than "I love my spouse."

## Operators

Propositions

|Concept|Java/C|Python|This class| Bitwise|Name|other
|-------|------|------|----------|--------|----|-----|
true|`true`|`True`|$\top$ or 1| -1|tautology|T
false|`false`|`false`|$\bot$ or 0|0|contradiction|F
not _P_|`!p`|`not p`|$\neg P$ or $\bar{P}$| ~p|negation
P and Q| `p && q`|`p and q`|$P \land Q$|p & q| conjunction| PQ, $P \cdot Q$
P or Q|p $\vert \vert$ q|p or q| $P \lor Q$| P $\vert$ Q | disjunction | P + Q
P xor Q | `p!=q`| `p!=q`| $P \oplus Q$| p ^ q|parity|$P \veebar Q$
P implies Q | | | $P \to Q$ | | implication | $P \supset Q, P \implies Q$
P iff Q | `p==q` | `p==q` | $P \leftrightarrow Q$ | | bi-implication | $P \iff Q$, P xnor Q

Proofs

|Concept|Symbol|Meaning|
|-|-|-|
equivalent|$\equiv$|"$A \equiv B$" means "$A \leftrightarrow B$ is a tautology"
entails | $\vDash$ | "$A \vDash B$" means "$A \to B$ is a tautology."
provable | $\vdash$| "$A \vdash B$" means "A _proves_ B"; it means both "$A \vdash B$ and "I know _B_ is true because _A_ is true. "$\vdash B$" means "I know _B_ is true."
therefore| $\therefore$ | "$\therefore A$" means "the lines above this $\vdash A$" and also connotes "A is the thing we wanted to show."
proof done | $\blacksquare_{q.e.d}$ | marks the end of a written (prose) proof.
hypothesis | | something we expect is true
theorem || something we've proven is true
corollary || small theorem that builds off of the main theorem
lemma || small theorem that helps set up the proof of the main theorem


Arithmetic

|Concept|Symbol|Meaning|
|-|-|-|
floor | $\lfloor x \rfloor$ | the largest integer not larger than _x_; _x_ rounded down to an integer
ceiling | $\lceil x \rceil$|the smallest integer not smaller than _x_; _x_ rounded up to an integer
exponent| $x^{y}$ | _x_ multiplied by itself _y_ times
sum | $\sum_{x \in \mathbb{S}} f(x)$ | the sum of all members of $\{f(x) \vert x \in \mathbb{S}\}$. By definition, 0 if S = {}.
Product | $\prod_{x \in \mathbb{S}} f(x)$ | The product of all members of $\{f(x) \vert x \in \mathbb{S}\}$. By definition, 1 if S = {}
product | $\prod_{x=a}^{b} f(x)$ | $\prod_{x \in \mathbb{S}} f(x)$ where $\mathbb{S} = \{x \vert (x \in \mathbb{Z}) \land (a \le x \le b)\}$. The product of f(x) applied to integers between _a_ and _b_ inclusive
factorial|x!|$\prod_{i=1}^{x} i$. The product of all positive integers less than or equal to _x_. The number of permutations of a length-_x_ sequence with distinct members. 
choose | $n \choose k$ |$\frac{n!}{(n-k)!k!}$. The number of _k_-member subsets of an _n_-element set. 



# _Sets_: Sets are Values, Sets vs. Sequences, Sets Writeup 

## Sets Writeup

### Defining Sets

1. A set contains numbers. __set__ is thus a term referring to a collection. 
    * Member is the word for something inside a set. 
1. We write a set with curly braces and commas. 
    * {1, 3} is a set. so is {dog, cat, mouse}. Arguably {x?y:z, satisfaction, 2102, :dragon:} is a set but sets whose members do not have some single unifying defined type are so uncommon that many say they're not sets.
1. A member of a set has no other set-related properties besides membership in the set: not order or position in the set, not number of copies in the set. 
    * Thus, {1, 2} and {2, 1} are two ways of writing the same set and {1, 2, 2} is nonsensical. 
1. The only property of a set is its members
1. A set can be empty
1. A set can be infinite. So is the set of positive integers....
1. A set can have sets as members. 
    * {1} is a set, so is {{1}, {}, {84, 5}}, so is the set of all two-element sets of integers.
    * Having sets within sets does not change any other rules - i.e. the set {{1, 2}, {2,1}} is nonsensical.

### Set operations and notation

"_m_ is a member of _S_" is written as $m \in S$. 

* Note that $m \in S$ is a predicate: $1 \in \{1, 2, 3\}$ is $\top$ and $1 \in \{2, 4, 6\}$ is $\bot$. 

"_m_ is not a member of _S_" is written as $m \mathrel{\not\in} S$, that is, $\neg (m \in S)$

* You may also see $\ni$ and $\mathrel{\not\in}$ which means the same thing as $\in$ and $\mathrel{\not\in}$ but with the set on the left and the member on the right instead of the other way around.

### Sub- and super-sets

$A \subseteq B$ is defined to mean "every member of _A_ is also a member of _B_," that is, $\forall x.((x \in A) \rightarrow (x \in B))$

* The $\subseteq$ symbol is pronounced "is a subset of." It intentionally looks somewhat like the $\leq$ symbol because if $A \subseteq B$ then _A_ is "less than or equal to _B_ in the sense that everything _A_ has, _B_ has too, and _B_ may have more. 

| $\top$: True | $\bot$: False |
|--------|---------------|
$\{\}\subseteq \{1, 2\}$ | $\{1, 2\} \subseteq \{2, 3\}$
$\{1\} \subseteq \{1, 2\}$ | $\{1, 2\} \subseteq \{1\}$
$\{1, 2\} \subseteq \{1, 2\}$
$\{1,2\} \subseteq$ the integers | $\{1, 2.3\} \subseteq$ the integers

$A \subset B$ is defined to mean both "$A \subseteq B$" and "$A \neq B$"; that is, $(A \subseteq B) \land (A \neq B).$ The symbol $\subseteq$ is pronounced "is a proper subset of." 

| $\top$: True | $\bot$: False |
|--------|---------------|
$\{\}\subset \{1, 2\}$ | $\{1\} \subset \{2, 3\}$
$\{1\} \subset \{1, 2\}$ | $\{1, 2\} \subset \{1\}$
|| $\{1, 2\} \subseteq \{1, 2\}$
$\{1,2\} \subset$ the integers | $\{1, 2.3\} \subset$ the integers

$A \supseteq B$ means $B \subseteq A$; $A \supset B$ means $B \subset A$

* the symbol "$\supseteq$" is pronounced "is a superset of". The "$\supset$" synbol is pronounced "is a proper superset of." 

### Sets from other sets

$A \cup B$ is defined to mean "A set containing every member of _A_ every member of _B_ and no other members. That is, "a set S such that $\forall x.(x \in S \leftrightarrow ((x \in A) \lor (x \in B)))$"

* The $\cup$ symbol is pronounced "union" and $A \cup B$ is called the union of _A_ and _B_." Note that $(A \subseteq) \leftrightarrow ((A \cup B) = B)$

| A | B | $A \cup B$ |
|------------|----------|--------------|
{1, 2} | {1, 2} | {1, 2}
{1, 2} | {0} | {1, 2}
{1, 2} | {5, 6} | {1, 2, 5, 6}
{1, 2, 4, 8} | {2, 4, 6, 8} | {1, 2, 4, 6, 8}
the positive numbers | {0} | the non-negative numbers
the even numbers | the odd numbers | the integers 

$A \cap B$ is defined to mean "a set containing every member shared both by _A_ and _B_, and no other members"; that is; "a set _S_ such that $\forall x. (x \in S \leftrightarrow ((x \in A) \land (x \in B)))$

* the $\cap$ symbol is pronounced "intersection" and $A \cap B$ is called the "intersection of _A_ and _B_". It intentionally looks similar to $\land$ to suggest a similar value to the member of intersection of _A_ and _B_ if it is a member of _A_ and a member of _B_. 
* Note that $(A \subseteq B) \leftrightarrow ((A \cap B) = A)$

| A | B | $A \cap B$ |
|----|----|-----|
{1, 2} | {1, 2} | {1, 2}
{1, 2} | {} | {}
{1, 2} | {5, 6} | {}
{1, 2, 4, 8} | {2, 4, 6, 8} | {2, 4, 8}
the positive numbers | the integers | the positive integers 

If we say that $A \cap B = \{\}$, then we say that _A_ and _B_ are disjoint. Less commonly, __overlap__ is used to mean "are not disjoint."

A \ B is defined to mean "a set containing every member of _A_ that is not a member of _B_, and no other members"; that is, "a set _S_ such that $\forall x. (x \in S \leftrightarrow ((x \in A) \lor (x \notin B)))$"

* the \ symbol is pronounced either "Minus" or "set minus." A \ B has everything _A_ has provided _B_ does not have it. It is rarely used in computing. Note that $(A \subseteq B) \leftrightarrow ((A \backslash B )) = \emptyset$

| A | B | $A \backslash B$ |
|-|-|-|
{1, 2} | {1, 2} | {}
{1, 2} | {} | {1, 2}
{1, 2} | {5, 6} |{1, 2}
{1, 2, 4, 8} | {2, 4, 6, 8} | {1}
the integers | the positive numbers | the negative integers

pow(A) or P(A) is defined to mean "the set of all subsets of A"; that is, "a set S such that $\forall x. (x \in S \leftrightarrow (x \subseteq A))$". pow(A) or P(A) is called the power set of _A_ and is the set of all subsets of _A_. Note that every set, even {}, has one subset: {}; thus, a power set is never empty, $\emptyset \in P(A)$ is a tautology, and $\emptyset = P(A)$ is a contradiction regardless of what set _A_ is.

|A|P(A)|
|-|-|
{} | {{}}
{1} | {{}, {1}}
{1, 2} | {{}, {1}, {2}, {1, 2}}
{{1, 2}, {3}} | {{}, {{1, 2}, {3}, {{1, 2}, 3}}
{{}}|{{}, {{}}}

| Concept | Set Notation | Actuality
|-----|------|-------|
"add" x to S | $S \cup \{x\}$ | a set like S except it also has _x_ in it
"remove" _x_ to S | $S \backslash \{x\}$ | a set like S except it does not have _x_ in it.
_A_ "xor" _B_ | $(A \cup B) \backslash (A \cap B)$ | a set with elements in _A_ or _B_ but not both

### Counting Members

$|A|$ means "the number of distinct values that are members of _A_." We call this notion the __cardinality__ and read $|A|$ as "the cardinality of _A_."

|A| $\vert A \vert$ |
|----|-----|
{} | 0
{1, 2} | 2
{{1, 2}} | 2
{1, {2, 3}} | 2
P({1, 3, 5, 7}) | 16
P(A) | $2^{\vert A\vert}$

### Set-builder notation

Set-builder notation $\{x \in \mathbb{Z} \vert x^3 - 30x + 1 > 0\}$ would be written: "x for x in Z if $x^3 - 30x +1 > 0$ ", although you'd have to define a sensible, finite Z range. 

### Common sets

There are some common sets that have their own symbols. Many of them are listed in MCS 4.1.1

| Symbol | Set | Elements |
|-|-|-|
$\empty$ | the empty set | none
$\mathbb{N}$ | nonnegative integers | {0, 1, 2, 3, ...}
$\mathbb{Z}$ | integers | {..., -3, 2, -1, 0, 1, 2, 3, ...}
$\mathbb{Q}$ | rational numbers | {$\frac{1}{2}$, $-\frac{5}{3}$, 16, etc.}
$\mathbb{R}$ | real numbers | $\{\pi, e, -9, \sqrt{2}, etc\}$
$\mathbb{C}$ | complex numbers | $\{i, \frac{19}{2}, \sqrt{2}-2i, etc\}$

### Quantifiers and Sets

Quantifiers are often used with sets. Set-notation quantifiers and domain-bound quantifiers can be each defined in terms of the other.

### Core Notation

The notation $\forall x \in S . P(x)$ means "the predicate P(x) is true for every x in the set _S_." It does not say anything about the true or falsehood of P(x) for _x_ not in _S_, nor does it assert that there are any members of _S_. 

The notation "$\exists x \in S . P(x)$" means "there is at least one element of _S_, and at least one element of _S_ makes the predicate P(x) true. It does not say anything about the truth or falsehood of P(x) for _x_ not in _S_, nor if there are more (or even at all) members of _S_ that also make P(x) true.

* "$\forall x, y \in S$" is shorthand for "$\forall x \in S . \forall y \in S$".
* "$\exists x, y \in S$" is shorthand for "$\exists x, y \in S . \exists y \in S$".

### Converting "$\forall x \in S...$" to "$\forall x...$"

If a domain is not specifed and all quantifiers are given with sets, the implicit domain is union of all such sets or any superset containing that union.

### Converting "$\forall x . ...$" to "$\forall x \in S...$"

Define a set _U_ representing the entire domain. The symbol _U_ is not required, but is often used with the intent that it suggest the "universal set" or the "universe of discourse." 


## Sets vs Sequences

Sets ands sequences are "composite" values because they are made up of other values - true, false, and numbers. Both sets and sequences:

* May contain any other value, including other sets and sequences
* Are values, not entities
* are used to define other structures of interest in discrete math
* are commonly written with their contained values separated by commas

### Set:

* Written with curly braces, like {1, 2}
* Cannot contain the same value more than once
* Members have no order, i.e. {2, 3} = {3, 2}
* The empty set (the only set with cardinality 0) is written {} or $\emptyset$
* Has many operators and special notations like $\{1, 2\} \cup \{ x^2 | x \in \mathbb{N}^+\}$
* A singleton set is always distinct from its member; {2} $\neq$ 2
* always called a "set"
* contained values are called "members"; "element" is also sometimes used

### Sequence

* Written with parenthesis, like (1, 2)
* Can contain the same value any number of times; (1, 1) is a sequence and is distinct from (1) and (1, 1, 1)
* Items have an order, i.e. (2, 3) $\neq$ (3, 2)
* the empty sequence (the only sequence with length 0) is written () or $\epsilon$
* has no operators that are commonly used in computing
* A singleton sequence is often considered equal to its item: i.e. (2) = 2
* Called a "sequence" or a "tuple", with special words for some lengths (i.e. "pair" or "triple") and some element types (i.e. "string")
* contained values are called "items"; "elements" is also sometimes used

### Sets are Values

#### By example

7 is a value. Charlie is an entity. If we let _x_ and _y_ both refer to 7 and make _x_ bigger, x is no longer 7. This gets to the idea that 7 is a value: an unchanging Platonic ideal. It is impossible, by definition, to make 7 itself bigger. Similarly, if Charlie eats a ton and grows, he's still Charlie. 

Because _x_ and _y_ both refer to a value, changing the value of _x_ has no impact on _y_ whereas "Charles" and "Charlie" both refer to an entity, so making "Charlie" richer means "Charles" is richer.

#### Entities and Values

##### A value can be written in multiple ways

"3+4" and "7" represent the same _integer_ but "3+4" and "7" represent different _arithmetic expressions_.

##### Variables name just one value within a given context

Within a single problem, if one assigns _x=2_, then x=2 and this cannot change. 

##### Discrete math values have related programming entitites

Sets are values in discrete mathematics, just like numbers are: unchangeable Platonic ideals. Everything in discrete mathematics is a mathematical construct and thus a value, not an entity.

# Good Proofs in Practice

The purpose of a proof is to establish the truth of an assertion with absolute certainty. To be understanding and helpful, a proof should not only worry about correctness, but also be clear. here are some helpful tactics to achieve this: 

* State your game plan: a proof begins by explaining the general line of reasoning, for example "we use case analysis" or "we argue by contradiction."
* Keep a linear flow: proofs are written like mathematical mosaics.. the steps of an argument should follow one another in an intelligible order.
* A proof is an essay: a proof looks like an essay with some equations thrown in.
* Avoid symbolism: use words when you can!
* Introduce notation thoughtfully: An argument can be easily simplified with a variable or defining a new term, but do this sparingly becuase the reader then has to remember all of that! 
* Structure long proofs: Use preliminary lemmas to cite repeatedly.
* Be wary of the obvious: what is obvious to one reader might not be to another - you don't have to prove every single claim you say, but don't use phrases like "clearly" or "obviously" to bully your reader into thinking they're dumb or accept it as true just because

# Skills from Mathematics

1. Discussing definitions
    
    1. Mathematicians begin with thinking hard about definitions early in their undergraduate career and fluency in discussing definitions is something that can benefit everyone.

1. Coming up with counterexamples

    1. When coming up with a new definition, one has as et of examples and counterexamples that one wants the definition to adhere to. So examples and counterexamples help build good definitions.
    1. When encountering an existing definition, the first thing a mathematician does is write down examples/counterexamples.

1. Being wrong and often admitting it

    1. Fostering doubt, being wrong, admitting it, and starting over distinguishes mathematical discourse even from much praised scientific discourse. There's no fame or money behind it, just the personal insight for truth.
    1. The mathematical habit is putting your personal pride or embarrassment aside for the sake of insight.

1. Evaluating many possible consequences of a claim

    1. The limits of an argument result in an even better and more elegant theorem that includes the original claim. More often, you realize you were wrong. So this habit is a less formal variation of being wrong often and coming up with counterexamples.

1. Teasing apart the assumptions underlying an argument

    1. Treating claims mathematically rather than through emotion allows us to tease apart claims without bias.

1. Scaling the ladder of abstraction

    1. Mathematicians "scale the ladder" of abstraction - i.e. they start at the lowest rung where they understand some examples of a paper, jump to the main theorem of the paper, and then synthesize that information to the real world.

