---
title: Practice for Quiz 2
author: Charlie Meyer
geometry: margin=0.5cm
date: MoWeFri 1:00 - 1:50
header-includes:
- \usepackage{amsmath}
- \newcommand{\doublearrow}{\leftrightarrow}
---

# Practice for Quiz 4 - Induction 

## Question 1

Prove by induction that $\forall_n \in \mathbb{Z}^+ . \sum_{x=1}^{n} (3x^2-3x+1) = n^3$

We proceed by induction

* __Base Case__: Consider the case when $n=1$. Then, $\sum_{x=1}^{1} (3x^2-3x+1) = 3-3+1 = 1$, and $1^3 = 1$. Thus, the statement is true for $n=1$.
* __Inductive Step__: We proceed by induction on $n$. Assume that the theorem holds for $n$, that is $\sum_{x=1}^{n} (3x^2-3x+1) = n^3$. By adding the $n+1$th term to both sides, we have:

$$\sum_{x=1}^{n} (3x^2+3x+1) + (3(n+1)^2-3(n+1)+1) = n^3 + (3(n+1)^2-3(n+1)+1)$$

Now by simplifying, we can get:

$$\sum_{x=1}^{n+1} (3x^2-3x+1) = n^3 + 3(n^2 +2n+1)-3n-3 + 1$$
$$\sum_{x=1}^{n+1} (3x^2-3x+1) = n^3 + 3n^2 + 6n + 3 - 3n -3 +1$$
$$\sum_{x=1}^{n+1} (3x^2-3x+1) = n^3 + 3n^2 + 3n + 1$$
$$\sum_{x=1}^{n+1} (3x^2-2x+1) =  (n+1)^3$$

By the principle of induction, we have shown that the theorem holds for all $n \in \mathbb{Z}^+$.

## Question 10

Write a proof to prove by induction that $\forall_n in \mathbb{Z}^+ . \sum_{i=1}^{n} 2^{-i} = 1-2^{-n}$. 

We proceed by induction.

* __Base Case__: Consider the case when $n=1$. Then, $\sum_{i=1}^{1} 2^{-i} = 2^{-1} = 1-2^{-1}$, so $\frac{1}{2} = \frac{1}{2}$. Thus, the statement is true for $n=1$.
* __Inductive Step__: We proceed by induction on $n$. Assume the theorem holds for $n-1$, that is $\sum_{i=1}^{n-1} 2^{-1} = 1-2^{-(n-1)}$ for some integer $n >1$. Then:

$$2^{-n} + \sum_{i=1}^{n-1} 2^{-i} = \sum_{i=1}^{n} 2^{-i}$$
$$2^{-n} + 1-2^{-(n-1)} = 1 + \frac{1}{2^n} - \frac{1}{2^{n-1}} = 1+\frac{-1}{2^n} = 1 - \frac{1}{2^n}$$

By the principle of induction, it follows that $\forall_n \in \mathbb{Z}^+ . \sum_{i=1}^{n} 2^{-i} = 1-2^{-n}$.

## Question 16

Prove by induction that $\forall_n \in \mathbb{N} . (\sum_{i=0}^{n} (2i+1)) = (n+1)^2$

We proceed by induction. 

* __Base Case__: Consider the case where $n=0$. Then, $\sum_{i=0}^{0} (2i+1) = 1 = (0+1)^2$. Thus, the statement is true for $n=0$.
* __Inductive Step__: We proceed by induction on $n$. Assume that the theorem holds true for $n$, that is assume $\sum_{i=0}^{n} (2i+1) = (n+1)^2$ for some integer $n > 1$. Then:

$$\sum_{i=0}^{n} (2i+1) + (2(n+1)+1) = (n+1)^2 + 2n + 3$$
$$\sum_{i=0}^{n+1} (2i+1) = n^2 + 4n + 4$$
$$\sum_{i=0}^{n+1} (2i+1) = ((n+1)+1)^2$$

This means that the theorem holds for $n+1$, as well. By the principle of induction, it follows that the theorem holds for all $n \in \mathbb{N}$.

## Question 17

Write a proof by induction that the following function returns $2 \cdot x$ for any non-negative integer $x$:

```pseudocode
let f(x) be computed as
    if x <= 0 then return 0
    else return 2 + f(x-1)
```

We proceed by induction. 

*__Base Case__: Consider the case when x = 0. In this instance, the function returns 0. Thus, the statement is true for $x=0$, since $2 \cdot 0 = 0$.
* __Inductive Step__: We proceed by induction on $x$. Assume that the theorem holds for $x-1$, for some positive integer $x$. Then when the function is called with $x$, it uses the "else" case and returns $2 + f(x-1)$; because the theorem held at $x-1$, $f(x-1)$ is even, which means $2+f(x-1)$ is also even so the theorem holds at $x$ too. 

By the principle of induction, it follows that the theorem holds for all $x \in \mathbb{N}$.


## Question 37

Prove by induction that $\forall_n \in \mathbb{N} . \sum_{i=0}^{n} i = \frac{n(n+1)}{2}$

We proceed by induction. 

* __Base Case__: Consider the case when $n = 0$. That is, consider $\sum_{i=0}^{0} i$, which is equal to 0. Then, $\frac{0(0+1)}{2} = 0$. Thus, the statement is true for $n=0$.
* __Inductive Step__: We proceed by induction on $n$. Assume that the theorem holds for some $n$, that is, assume $\sum_{i=0}^{n} i = \frac{n(n+1)}{2}$ for some integer $n > 0$. Then:

$$\sum_{i=0}^{n} i + (n+1) = \frac{n(n+1)}{2} + (n+1)$$
$$\sum_{i=0}^{n+1} i = \frac{(n+1)((n+1)+1)}{2}$$

This means that the theorem holds for $n+1$, as well. By the principle of induction, it follows that the theorem holds for all $n \in \mathbb{N}$.

## Question 38

Prove by induction that $\forall_n \in \mathbb{N} . \sum_{x=0}^{n} \frac{1}{2^x} = \frac{2^{n+1} - 1}{2^n}$

We proceed by induction.

* __Base Case__: Consider the case when $n=0$. Then, $\sum_{x=0}^{0} \frac{1}{2^x} = \frac{2^1 - 1}{2^0} = \frac{1}{1} = \frac{1}{2^0} = 1$. Thus, the statement is true for $n=0$.
* __Inductive Step__: We proceed by induction on $n$. Assume that the theorem holds for some $n$, that is assume $\sum_{x=0}^{n} \frac{1}{2^x} = \frac{2^{n+1} - 1}{2^n}$ for some arbitrary natural number $n > 0$. Then we will show that the equation must hold for $n+1$ as well.

$$\sum_{x=0}^{n} \frac{1}{2^x} + \frac{1}{2^{n+1}} = \frac{2^{n+1} - 1}{2^n} + \frac{1}{2^{n+1}}$$
$$\sum_{x=0}^{n+1} \frac{1}{2^x} = 2^{-n-1} ( 2^{n+2} - 1)$$
$$\sum_{x=0}^{n+1} \frac{1}{2^x} = \frac{2^{n+2} -1}{2^{n+1}}$$

By induction on $n$, we have proven that $\sum_{x=0}^{n} \frac{1}{2^x} = \frac{2^{n+1} - 1}{2^n}$ for all $n \in \mathbb{N}$.






