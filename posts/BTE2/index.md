---
title: "The Boltzmann Transport Equation - 2. Probabilistic Preliminaries"
author: "Daniel Smith"
date: "2024-02-13"
categories: [Mathematics, Probability Theory, Boltzmann Equation]
title-block-banner: false
image: 'preview.png'
draft: false
description:  "Before we can discuss Information Theory and it's consequences for the Boltzmann equation we first need to make some definitions from probability theory."
---


# 2 - Probability Theory

---

## 2.1 - Random Variables and Random Vectors

Throughout we fix a probability space $(\Omega,\mathcal{F},\mathbb{P})$
and consider $\mathbb{R}$ equipped with Lebesgue measure $\lambda$ on
the Borel $\sigma$-algebra $\mathcal{B}(\mathbb{R}).$ The reader is assumed to have taken a first course on measure theory.

Note that a probability space $(\Omega,\mathcal{F},\mathbb{P})$ is a measure space with unit total mass

$$\mathbb{P}(\Omega)=1.$$

---

## Definition 2.1.1

A **random variable** $X$ is a measurable function
$X:\Omega\longrightarrow\mathbb{R}$.

The cumulative distribution function (CDF) $F_X$ of a random variable
$X$ is defined by $F_X(x) = \mathbb{P}(X\leq x).$

A **stochastic process** is an indexed family of random variables
${\{X_t\}_{t\in T}}$, where the indexing set $T$ is not necessarily
countable, and the index $t$ is often interpreted as time.

---

## Definition 2.1.2

$X$ is said to be a **continuous** random variable if its law
$\,\mathbb{P}_X = \mathbb{P}\circ X^{-1}$ is absolutely continuous with
respect to the Lebesgue measure $\lambda$ as a measure on $\mathbb{R}$. That is, if

$$\forall \, N \in \mathcal{B}(\mathbb{R}):$$
$$\lambda(N) = 0 \Rightarrow \mathbb{P}(X \in N) = 0.$$

By the Radon-Nikodym theorem, a random variable $X$ is continuous if
(and only if) there exists a measurable function
$f_X : \mathbb{R} \longrightarrow [0,\infty)$ such that for all
$\, B \in \mathcal{B}(\mathbb{R})$,

$$\mathbb{P}(X\in B) = \int_B f_X\,\text{d}\lambda.$$

The function $f$ is called the probability density function (PDF) of $X$
and is unique up to equality almost everywhere.


---

Unless otherwise stated we now assume that a random variable $X$ is
continuous and has density $f$.

## Definition 2.1.3

A **random vector** $\mathbf{X}$ is an n-tuple of random
variables

$$\mathbf{X}=(X_1,\ldots,X_n) : \Omega \longrightarrow \mathbb{R}^n.$$

The joint CDF $F_{X,Y}$ of a pair of random variables $X,\,Y$ is defined
as

$$F_{X,Y}(x,y) = \mathbb{P}(X\leq x, Y\leq y).$$

From the joint CDF $F_{X,Y}$ we can recover the marginal CDFs $F_X$,
$F_Y$ by sending the other variable to infinity:

$$\begin{aligned}
F_X(x) &= \lim_{y\to\infty}F_{X,Y}(x,y),\\
\\
F_Y(y) &= \lim_{x\to\infty}F_{X,Y}(x,y).
\end{aligned}$$

X and Y are **jointly continuous** if their joint law is absolutely
continuous with respect to the two-dimensional Lebesgue measure
$\lambda_2$ on $(\mathbb{R}^2,\mathcal{B}(\mathbb{R}^2)).$ By the
Radon-Nikodym theorem, X and Y are jointly continuous if (and only if)
there exists a measurable function
$f_{X,Y} : \mathbb{R}^2 \longrightarrow [0,\infty)$ such that for all
$\, B \in \mathcal{B}(\mathbb{R}^2)$,

$$\mathbb{P}((X,Y)\in B) = \int_B f_{X,Y}\,\text{d}\lambda_2,$$ 

where
$f_{X,Y}$ is called the **joint PDF** of X and Y. The marginal PDFs
$f_X$, $f_Y$ can be obtained from $f_{X,Y}$ by integrating out the other
variable:

$$\begin{aligned}
f_X(x) &= \int_{-\infty}^{\infty} f_{X,Y}(x,y)\,\text{d} y\\
\\
f_Y(y) &= \int_{-\infty}^{\infty} f_{X,Y}(x,y)\,\text{d} x.
\end{aligned}$$

In particular, jointly continuous random variables are automatically
marginally continuous, although the converse is not true in general.

Analagously, $X_1,\dots,X_n$ are jointly continuous if their joint
    law is absolutely continuous with respect to n-dimensional Lebesgue measure $\lambda_n$, or
    equivalently if there exists a joint PDF for the random vector $(X_1,\dots,X_n)$.


---

## 2.2 - Expectation, Moments and Independence

## Definition 2.2.1

The **expectation** $\mathbb{E}[X]$ of a random variable $X$ is simply
its Lebesgue integral with respect to $\mathbb{P}$ 

$$\begin{aligned}
    \mathbb{E}[X] &= \int_\Omega X \, \text{d}\mathbb{P}\\
    &= \int_\mathbb{R} xf(x) \,\text{d} x.
\end{aligned}$$ 

The $k^{th}$ moment of $f$ around the non-random value
$c\in\mathbb{R}$ is

$$\mathbb{E}\left[(X-c)^k\right] = \int_{-\infty}^{\infty} (x-c)^kf(x)\,\text{d} x.$$

The $k^{th}$ raw moment is the $k^{th}$ moment around the origin, $c=0$,
$$\mathbb{E}[X^k] = \int_{-\infty}^{\infty} x^kf(x)\,\text{d} x.$$

For example, the $1^{st}$ raw moment is the distribution's mean,
$\mu = \mathbb{E}[X]$.

The $k^{th}$ central moment is the $k^{th}$ moment around the mean,
$c = \mu = \mathbb{E}[X]$,

$$\mathbb{E}[(X-\mu)^k] = \int_{-\infty}^{\infty} (x-\mu)^kf(x)\,\text{d} x.$$

For example, the $2^{nd}$ central moment is the distribution's variance,
$\sigma^2 = \mathbb{E}\left[(X-\mu)^2\right]$.

By abuse of language, it is common to refer to integrals of the form
$\int r(x)f(x)\,\text{d} x$ as 'moments' even when the function $r$ is not a
polynomial in $x$.

---

## Definition 2.2.2

Given continuous random variables $X$ and $Y$ with $f_Y(y)>0$ we define:

1.  The conditional CDF $F_{X|Y}$ of $X$ given Y by

    $$F_{X|Y}(x|y) = \frac{\int_{-\infty}^{x}f_{X,Y}(u,y)\,\text{d} u}{f_Y(y)}.$$

2.  The conditional PDF $f_{X|Y}$ of $X$ given $Y$ by

    $$f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}.$$

3.  The conditional probability of the event $\{ X\in A\}$,
    $A\in\mathcal{B}(\mathbb{R)}$, given that $Y = y$ by

    $$\mathbb{P}(X\in A|Y = y) = \int_A f_{X|Y}(x|y)\,\text{d} x.$$

---


## Definition 2.2.3

Random variables $X$ and $Y$ are said to be **independent** if their
joint CDF $F_{X,Y}$ factorises into the tensor product of the
marginals:

$$F_{X,Y}(x,y) = F_X(x)F_Y(y).$$

Equivalently, if X and Y are jointly continuous then we say they are
independent if their joint PDF $f_{X,Y}$ factorises into the tensor
product of the marginals:

$$f_{X,Y}(x,y) = f_X(x)f_Y(y)\quad\text{a.e.}$$

Where for $f,g:E\longrightarrow \mathbb{R}$ the **tensor product**
    $f\otimes g : E^2\longrightarrow \mathbb{R}$ is defined by
    $f\otimes g(x,y) = f(x)g(y).$

---

## Remark 2.2.4

 This is not the most compact and elegant way of defining independence of random variables through the independence of the $\sigma$-algebras they generate. However this definition is equivalent, more intuitive and will suffice for our purposes. 
 

# References:

- [1.] Josephine Evans. *MA359 Measure Theory*, 2022. Warwick Mathematics Institute, University of Warwick.
- [2.] Paul Chleboun. *ST318 Probability Theory*, 2022. Department of Statistics, University of Warwick.


