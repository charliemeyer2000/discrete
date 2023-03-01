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
pandoc -s -o _.pdf _.md 
-->

# First-Order Logic (Mod2Quiz1 Practice)

Define C(a, b) to mean "Can cast value _a_ as type _b_." Define H as the set of values {8, False, "True"}. Define the set K to be the set of types {bool, int}. 

Question 1: Consider $\exists_x \in H . C(x, int)$. Write an equivalent statement that uses the universal quantifier.

* $\neg \forall_x \in H . \neg C(x, int)$

Question 2: Consider $\forall_x \in H . \exists_y \in K . C(x, y)$. Write an equivalent statement that uses boolean operators instead of quantifiers.

* $(C(8, bool) \lor C(8, int)) \land (C(False, bool) \lor C(False, int)) \land (C("True", bool) \lor C("True", int))$

Question 3: Which of the following are propositions? Assume P is a predicate and X and y have not been given set values outside of the individual answers.

* $\forall_{x, y} \in S . P(x, y)$
* $\forall_{x, y, z} \in S . P(x, y)$

Question 4: Select the true entailments

* $P(3) \vDash \exists_x \in \mathbb{Z} . P(x)$
* $\exists_x \in \mathbb{Z} . P(x) \vDash \exists_y \in \mathbb{Z} . P(y)$
* $\exists_x \in \mathbb{N} . P(x) \vDash \exists_x \in \mathbb{Z} . P(x)$


Consider the Symbols:

|Symbol|Means|
|-|-|
S | A set of student submissions to a programming assignment
T | A set of test cases for that assignment
P(s, t) | Submission s passes test case t

Assume that $\vert T \vert = 10$ and that students are given a grade equal to the number of test cases passed (between 0 and 10, with 10 being the perfect score). 

Question 5: Which of the following best expresses the idea that _no student got a 0_?

* $\forall_s \in S . \exists_t \in T . P(s, t)$

Question 6: Which of the following best expresses the idea that some student got a perfect score?

* $\exists_s \in S . \forall_t \in T .  P(s, t)$

Question 7: Which of the following best expresses the idea that one of the tests was easy enough that every submission passed it?

* $\exists_t \in T . \forall_s \in S (s, t)$

Question 8: Which of the following best expresses the idea that none of the tests was impossible to pass?

* $\forall_t \in T . \exists_s \in S . P(s, t)$

Question 9: Which of the following best expresses the idea that every student got a perfect score?

* $\forall_s \in S . \forall_t \in T . P(s, t)$

Question 10: Which of the following best expresses the idea that not every student got a 0?

* $\exists_s \in S . \exists_t \in T . P(s, t)$

Question 11: Which of the following are true comparisons between predicates and propositions?

1. If P(x) is a predicate, then $\forall_x . P(x)$ is a proposition
1. IF $\forall_x P(x)$ is a proposition, then P(x) is a predicate

Question 12: Which of the following are true equivalences?

1. $\forall_x . P(x) \equiv \forall_y . P(y)$
1. $\forall_x . \neg P(x) \equiv \neg \exists_x . P(x)$
1. $\forall_x . \neg P(x) \equiv \not\exists_x . P(x)$
1. $\forall_x . \forall_y . P(x, y) \equiv \forall_y . \forall_x . P(x, y)$

Question 13: Which of the following are true entailments? Assume the domain is "numbers" and that "4" is a member of that domain

1. $\forall_x . P(x) \vDash \exists_x . P(x)$
1. $P(4) \vDash \exists_x . P(x)$
1. $\forall_x . P(x) \vDash P(4)$

Question 14: Which of the following are equivalent to $\neg (\forall_x . (P(x) \land Q(x)))$?

* $\exists_x . \neg (P(x) \land Q(x))$

Question 15: Select true statements - assume P is a predicate meaning "is pleased," _x_ is a variable over the domain of people, and _t_ is the specific person Luther Tychonievich

1. $\forall_x . P(x)$ is a proposition
1. P(t) is a proposition

Question 16:

Let 

* N(x) be untrue no matter which _x_ we pick
* A(x) be true no matter which _x_ we pick
* S(x) be true for some _x_ and not for others

Which of the following are true?

1. $\forall_x . A(x)$
1. $\forall_x . N(x) \rightarrow S(x)$
1. $\exists_x . N(x) \rightarrow S(x)$
1. $\exists_x . S(x) \rightarrow N(x)$
1. $\exists_x . A(x) \land S(x)$

Question 17: Consider 

$$\forall_x . \exists_y . C(x) \rightarrow (H(y) \land L(x, y))$$

and 

$$\exists_y . \forall_x . C(x) \rightarrow (H(y) \land (L(x, y)))$$

Where H(a) means "a is happy" and C(a) means "a is in this class" and L(a, b) means "a likes b."

Select the situations below where these two have identical truth values. Unless otherwise specified below, assume that all combinations of possibility exist. 

1. the class is empty; no one is in it
1. There's only one happy person in this world

Question 18, 19, 20, 21: 

Suppose the domain is single-digit prime numbers; that is, 2, 3, 5, and 7. 

Question 18: The expression $\forall_x . P(x)$ means the same thing as:

* $P(2) \land P(3) \land P(5) \land P(7)$

Question 19: The expression $\exists_x . P(x)$ means the same thing as:

* $P(2) \lor P(3) \lor P(5) \lor P(7)$

Question 20: The expression $\not\exists_x . P(x)$ means the same thing as:

* $\neg P(2) \land \neg P(3) \land \neg P(5) \land \neg P(7)$

Question 21: Provide a counterexample that shows $(A \rightarrow B) \rightarrow C)$ is not equivalent to $A \rightarrow (B \rightarrow C)$

* Consider the situation where a = 0, b = 1, c = 0. 

Questions 22-31

The domain is _people_. Use the following symbols:

|Symbol|Meaning|
|-|-|
D(x) | x is a doctor 
N(x) | x is a nurse 
P(x) | x is a prescriber 
S(x) | x supervises y

Question 22: Convert the following from English to logic - no one is a doctor

* $\not\exists_x . D(x)$

Question 23: Convert the following from English to logic - no doctor is a nurse

* $\forall_x . D(x) \rightarrow \neg N(x)$
* $\not\exists_x . D(x) \land N(x)$

Question 24: Convert the following from English to lofic - some doctors are prescribers

$\exists_x . D(x) \land P(x)$

Question 25: Convert the following from English to logic - All doctors are prescribers

* $\forall_x . D(x) \rightarrow P(x)$

Question 26: All doctors supervise someone.

* $\forall_x . \exists_y . D(x) \rightarrow S(x, y)$

Question 27: There are no mutual supervisions: that is, no one supervises their supervisor.

* $\forall_x . \forall_y . \neg( S(x, y) \land S(y, x))$

Question 28: Convert $\exists_x . N(x)$ to english.

* There exists at least one nurse OR nurses exist OR there is a nurse

Question 29: Convert $\exists_x . N(x) \land \neg P(x)$ to english.

* Not all nurses are prescribers

Question 30: Convert $\not\exists_x . \forall_y . S(x, y)$ to english.

* No one supervises everyone

Question 31: Convert $\forall_x . (N(x) \land P(x)) \rightarrow (\not\exists_y . D(y) \land S(x, y))$ to english.

* If a nurse is a prescriber, then there is no doctor that supervises to them OR Doctor's don't supervise prescribing nurses.

Questions 32-36:

Assume the symbols

|Symbol|Meaning|
|-|-|
H | the set of hospital staff
F | the set of patient medical files
D(h) | h is a doctor
N(h) | h is a nurse 
P(h) | h is a prescriber
W(h, f) | h can write to file f
R(h, f) | h can read file f
S(x, y) | x supervises y

Pick the logic that best encodes the provided english

Question 32: Some doctors can write to all files

* $\exists_x \in H . D(x) \land \forall_y \in F . W(x, y)$

Question 33: Prescribers can write some files

* $\forall_x \in H . P(x) \rightarrow (\exists_y \in F . W(x, y))$

Question 34: Everyone can read anything they write

$\forall_x \in H . \forall_y \in F . W(x, y) \rightarrow R(x, y)$

Question 35: If a doctor or nurse cannot read a file, they cannot write to that file either

* $\forall_x \in H . \forall_y \in F . (\neg R(x, y) \land (D(x) \lor N(x))) \rightarrow \neg W(x, y)$

Question 36: Some doctors supervise some nurses who can read all files.

$\exists_x \in H \exists_y \in H . D(x) \land N(y) \forall_z \in F . D(x) \land N(y) \land S(x, y) \land R(y, z)$

Questions 37-41:

Assume the symbols

|Symbol|Meaning|
|-|-|
H | the set of hospital staff
F | the set of patient medical files
D(h) | h is a doctor
N(h) | h is a nurse
P(h) | h is a prescriber
W(h, f) | h can write to file f
R(h, f) | h can read file f
S(x, y) | x supervises y

Pick the english that best encodes the provided logic

Question 37: $\forall_x \in H . \neg (D(x) \land N(x))$

* it is not the case that every staff member is a doctor and a nurse. OR no doctor is also a nurse

Question 38: $\forall_x \in H . \forall_f \in F . W(x, f) \rightarrow P(x)$

* Someone can't write to a file unless they're a prescriber OR everyone either can't write to a file or they're a prescriber

Question 39: $\forall_n \in H . \exists_f \in F . N(n) \rightarrow R(n, f)$

* Every nurse can read a file

Question 40: $\forall_{x, y} \in H . \forall_z \in F . (S(x, y) \land W(y, z)) \rightarrow R(x, z)$

* Supervisors can read what files their subordinates write to OR supervisors can read what those they supervise write

Question 41: $\exists_x \in H . \forall_y \in F . R(x, y) \land W(x, y)$

* There's someone who can read and write every file

Questions 42-49: 

The domain is __students in a class__.

Use the following symbols. Keep in minds students can double major.

|Symbol|Meaning|
|-|-|
C(x) | x is a computer science major
M(x) | x is a math major
E(x) | x is an electrical engineering major
S(x) | x is a cognitive science major
W(x, y) | x works with y

Question 42: Convert the following from English to logic - everyone is a computer science major

* $\forall_x . C(x)$

Question 43: There are some cognitive science majors who work with some math majors

* $\exists_{x, y} . C(x) \land M(y) \land W(x, y)$

Question 44: No one is both an electrical engineer major and a cognitive science major.

* $\not\exists_x . E(x) \land S(x)$

Question 45: All math majors are also majoring in either computer science or cognitive science. 

* $\forall_x . M(x) \rightarrow (C(x) \lor S(x))$

Question 46: Only cognitive science majors work with both math majors and electrical engineering majors

* $\forall_x . ((\exists_y . M(y) \land W(x, y)) \land (\exists_z . E(z) \land W(x, z))) \rightarrow S(x)$

Question 47: $\exists_{x, y} . (x \neq y) \land M(x) \land C(y) \land W(x, y)$

* There are two students who are not the same person, one is a math major and the other is a computer science major, and they work together OR there's a math major and a computer science major who work together

Question 48: $\exists_x . \forall_y . E(x) \land ((x \neq y) \rightarrow \neg E(y))$

* There's only one electrical engineering major.

Question 49: $\forall_x . \exists_y . M(x) \rightarrow (C(y) \land W(x, y))$

* Every math major works with at least one computer science major












