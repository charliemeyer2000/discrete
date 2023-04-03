---
title: Mod3Quiz1
author: Charlie Meyer
geometry: margin=0.5cm
date: MoWeFri 1:00 - 1:50
header-includes:
- \usepackage{amsmath}
- \newcommand{\doublearrow}{\leftrightarrow}
---

<!-- 
pandoc -s -o quiz3-1.pdf quiz3-1.md
-->
# Proof by contradiction

## Problem Statement

Prove by contradiction that $(\vert A \cup B \vert = \vert A \vert) \rightarrow (B \subseteq A)$.

You must use the following definition: $\vert A \cup B \vert = \vert A \vert + \vert B \vert - \vert A \cap B \vert$.

## Solution


1. We proceed by contradiction.
1. Assume that $\neg((\vert A \cup B \vert = \vert A \vert) \rightarrow (B \subseteq A))$.
1. We can then simplify this to $(\vert A \cup B \vert = \vert A \vert) \rightarrow (B \not\subseteq A)$, or in english, that the size of the union of sets $A$ and $B$ is equal to the size of set $A$, but set $B$ is not a subset of set $A$.
1. With this assumption, then there exists an element $b \in B$ such that $b \not\in A$.
1. We know that by definition $\vert A \cup B \vert = \vert A \vert + \vert B \vert - \vert A \cap B \vert$. Since $b \in B$ and $b \not\in A$, then we know that $\vert A \cup B \vert = \vert A \vert + \vert B \vert - \vert A \cap B \vert - 1$.
1. Therefore, we know that $\vert A \cup B \vert > \vert A \vert$. 
1. Therein lies the contradiction, as we found that $\vert A \cup B \vert > \vert A \vert$ when we assumed that $\vert A \cup B \vert = \vert A \vert$. 
1. Because our assumption that $\neg((\vert A \cup B \vert = \vert A \vert) \rightarrow (B \subseteq A))$ led to a contradiction, we know that $(\vert A \cup B \vert = \vert A \vert) \rightarrow (B \subseteq A)$ must be true. 





