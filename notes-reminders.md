---
author: Charlie Meyer
date: Wednesday, November 9th
title: notes
output: md_document
variant: markdown+simple_tables
geometry: margin=2cm
---

<!-- copy and paste stuff

pandoc -s -o class-notes.pdf class-notes.md

-->

# Discrete Math Variables Shortcuts

[Latex Variables](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)

Common latex variables:

$ \Z$: set of integers

$ \exists$: exists

$ \forall$: for all

$ \neg $: logical not

$ \lor$: logical or

$ \land $: logical and

$ \oplus $ xor

$ \rightarrow $: implies

$ \Rightarrow $: right arrow

$ \leftrightarrow $: iff, biconditional

$  \equiv $: equivalent

$ \vdash $: provable

$ \vDash $: entails

$ \therefore $ - therefore

$ 


$ \{ \} $: braces




<!-- Headings -->
# Section
Information about this main section
## Subsection
General Notes. *This text* is in italics. **this text** is bolded or storng, basically. 
I don't like ~~this text~~ so i'm gonna strike through it
to separate things, i'm gonna use 
___
Fuck, i wanna show those stars on an italic statement! I'm gonna do \**bruh** to do that.

I need to quote things 
> "this is a quote"

oh shit it popped out look at that fucking sick af.



to link something you do [Some link](https://google.com)

i need a fuckin list. Here ya go bitch. leave a space bitch cunt

* Item 1 
* Item 2
* Item 3
    * nested item bitch

Ok, fuck it, ordered list. Just make sure you leave a space. 

1. fuck yuo
1. fuck you
    1. oh look at that it's indented text.

code blocks - the shit you actually need here lol

``some fuckin code here jsut copy and pate it``

ok fuck i want an image




oooo shit wait here we go, let's do some github fuckin code blocks. shit gives you auto text editing and stuff wow omg so swag much cool ^_^

``` java
    public class fuckYou(){
        public static void main(String[] args){
            System.out.println("yeah boy");
        }
    }
```

```javascript
    function()
```

    

alright im gonna test something here just wait
$$e=mc^2$$
aw yeah

shit 

we good in this bitch

$$\int_{0}^{1} {x}\ dx = \frac{1}{2} $$
$$V_{sphere} = \frac{4}{3} \pi  r ^2 $$






using fuckin latex in your markdown shit here ya go bitch


\begin{align}
    \tag{1.1}
    V_{sphere} = \frac{4}{3}\pi r^3
\end{align}



$$
\int_{a}^{b} x^2 \,dx = \frac{x^2}{2x}
$$

get ready for this alignment so wow much cool

\begin{align*}
e^{i\pi} &= \sum_{n=1}^\infty\frac{(i\pi)^n}{n!}
&& \text{(Taylor series for $e^x$)} \\
&= \sum_{n=1}^\infty \frac{\pi^{2n}}{(2n)!}
+ i\sum_{n=1}^\infty\frac{\pi^{2n+1}}{(2n+1)!}
&& \text{(rearrangement of terms)} \\
&= \cos(\pi) + i \sin(\pi)
&& \text{(Taylor series for $\cos(x)$ and $\sin(x)$)} \\
&= -1. && \text{(simplifying the previous expression)}
\end{align*}







$$\int_0^1 x^2 \,dx= \frac13$$
$$\int_0^1 \int_0^{2\pi} r \,d\varphi\,dr$$
$$\iint_{x^2+y^2\le 1} x+y \,dx\,dy$$

ok so like you can do lists very easily in markdown but watch this imma do it in latex. unfortunately live viewer doesn't work with this this latex so imma just have to trust that it works and use pandoc.

\begin{enumerate}
\item here's an item
\item oh shit here's another one
\begin{enumerate}
\item watch this! nested list cunt im fucking sick af
\item oh yeah? wanna see me do it again?
\begin{enumerate}
\item fuck yeah dude
\end{enumerate}
\end{enumerate}
\end{enumerate}


ok so here's some common expressions in latex

$a + b$

\begin{math}
a\dot b
\end{math}


$a^{e^{2^{\pi}}}$

yeah ok here we go some more shit
ready for some calc 3 notation?
$$ f \colon \mathbb{R} \to \mathbb{R^2} \\ cum $$
lit 
ok
so like 

im gonna cum

idk i think that's basically it i mean like i've done some latex and put it into a markdown file so fuck yeah

A potential function for a vector field is a scalar-valued function that satisfies a certain condition. Given a vector field $\mathbf{F}(x,y,z) = (F_1(x,y,z), F_2(x,y,z), F_3(x,y,z))$, a potential function $\phi(x,y,z)$ must satisfy the condition

$$\frac{\partial \phi}{\partial x} = F_1(x,y,z), \quad \frac{\partial \phi}{\partial y} = F_2(x,y,z), \quad \frac{\partial \phi}{\partial z} = F_3(x,y,z).$$

It can be difficult to find a potential function for a given vector field, as it requires solving a system of partial differential equations. In general, there may not be a potential function for a given vector field, or there may be multiple potential functions.

In the case of the vector field $\mathbf{F}(x,y,z) = (\ln(8y), (x/y) + \ln(2z), y/z)$, one potential function is given by

$$\phi(x,y,z) = \frac{x^2}{2} + \frac{8y^2}{2} + \frac{2z^2}{2} - \ln(y) - 2\ln(z).$$

To show that this is a potential function, we can verify that

$$\frac{\partial \phi}{\partial x} = F_1(x,y,z), \quad \frac{\partial \phi}{\partial y} = F_2(x,y,z), \quad \frac{\partial \phi}{\partial z} = F_3(x,y,z).$$

For example,

$$\frac{\partial \phi}{\partial x} = \frac{\partial}{\partial x} \left( \frac{x^2}{2} + \frac{8y^2}{2} + \frac{2z^2}{2} - \ln(y) - 2\ln(z) \right) = x = F_1(x,y,z) = \ln(8y).$$

Note that this is not the only potential function for the given vector field. In general, there may be multiple potential functions for a given vector field.






