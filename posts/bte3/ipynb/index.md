---
title: "The Boltzmann Equation - 3. Information Theory"
author: "Daniel Smith"
date: "2024-03-23"
categories: [Mathematics, Probability Theory, Information Theory, Boltzmann Equation]
title-block-banner: false
image: 'preview.png'
draft: true
description:  "We introduce key notions from information theory such as differential entropy and the Kullback-Liebler (KL) divergence and prove the information inequality."
---


# 3. - Information Theory: Entropy, Mutual Information & KL Divergence

---

# 3.1 - Differential entropy

The physicist's definition of the entropy $S$ of a system with a
continuum of possible states with density $f$ is 

$S = -\int f\log f.$ 

Note that for a probability density $f$ representing particle distribution in phase space the entropy $S$ coincides with Boltzmann's H functional $H(f)$ up to a change of sign:

$H(f) = \int f\log f.$



We can generalise this definition to any probability density $f$ (for
which the integral makes sense) and the resulting quantity is called the
**differential entropy** of $f$.

Intuitively, the entropy measures how
localized a probability density is. A density that concentrates most of
its mass in a small region will have low entropy, while a density that
distributes its mass over a large region will have high entropy. This is
simply a more precise statement of the commonly used heuristic that low
entropy states are and high entropy states are .

Throughout we fix a continuous random variable $X$ with density $f$ and
denote the support set of $f$ by $S$.
i.e. 

$$\begin{aligned}
S &= \text{supp}\,(f)\\
  &= \left\{ x\in\mathbb{R} \,\vert\, f(x)\neq0 \right\}.
\end{aligned}$$

---



### Definition 3.1.1 (Differential Entropy)

The **differential entropy** of the random variable $X$ is denoted by
$h(X)$ or $h(f)$ (as it only depends on the density $f$) and is defined
by 

$$h(f) = -\int_S f(x) \log f(x)\,\text{d} x.$$ 

If $\log = \ln$ then we say
the differential entropy is measured in **nats**.\
If $\log = \log_2$ then we say the differential entropy is measured in
**bits**.

Unless otherwise specified, $\log$ denotes the natural logarithm.

---

### Example 3.1.2 (Entropy of a univariate normal distribution)

Let $X \sim\mathcal{N}(0,\sigma^2)$. That is, suppose $X$ is a random variable with density

$$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{x^2}{2\sigma^2}}.$$

Then we compute 
$$\begin{aligned}
    h(f) &= -\int f\log f\\
    &= -\int_{\mathbb{R}}f(x)\left[-\frac{x^2}{2\sigma^2}-\frac{1}{2}\log 2\pi\sigma^2\right]\,\text{d} x\\
    &= \frac{\mathbb{E}[X^2]}{2\sigma^2}+ \frac{1}{2}\log 2\pi\sigma^2\\
    &= \frac{1}{2}+\frac{1}{2}\log 2\pi\sigma^2\\
    &= \frac{1}{2}\log 2\pi e\sigma^2\;\, \text{nats}\\
     &= \frac{1}{2}\log_2 2\pi e\sigma^2\;\, \text{bits.}\\
\end{aligned}$$

---

### Theorem 3.1.3

For any $c\in\mathbb{R}$ it holds that

$$h(X+c) = h(X).$$


*Proof.*

 $$\begin{aligned}
    h(X) &= -\int f(x)\log f(x)\,\text{d} x\\
    &= - \int f(x-c) \log f(x-c)\,\text{d} x\\
    &= h(X+c)
\end{aligned}$$ 
◻

---



### Theorem 3.1.4

For $a\in\mathbb{R}$ it holds that

$$h(aX) = h(X) + \log|a|.$$


*Proof.*  

Define the random variable $Y = aX$ with density

$$f_Y(y) = \frac{1}{|a|}f_X\left(\frac{y}{a}\right).$$

Then we can directly compute 

$$\begin{aligned}
    h(aX) &= -\int f_Y(y)\log f_Y(y)\,\text{d} y\\
    &= -\int \frac{1}{|a|}f_X\left(\frac{y}{a}\right)\log\left[\frac{1}{|a|}f_X\left(\frac{y}{a}\right)\right]\,\text{d} y\\
    &= -\int f_X(x)\log f_X(x)\,\text{d} x +\log|a|\\
    &= h(X) +\log|a|.
\end{aligned}$$ 

◻

---


### Corollary 3.1.5

$$h(A\mathbf{X}) = h(\mathbf{X})+\log|\det A|$$

---


### Definition 3.1.6 (Joint & Conditional Entropy)

The **joint differential entropy** of a set $X_1,\dots,X_n$ of (jointly
continuous) random variables with joint density $f = f(x_1,\dots,x_n)$
is defined as

$$h(X_1,\dots,X_n) = -\int f(x_1,\dots,x_n) \log f(x_1,\dots,x_n)\,\text{d}^{n}x.$$

If $X$ and $Y$ have joint density $f_{X,Y}(x,y)$ then we define the
**conditional differential entropy** as

$$h(X|Y) = -\int f_{X,Y}(x,y) \log f_{X|Y}(x|y)\,\text{d} x\,\text{d} y.$$

Since in general $f_{X|Y}(x|y) = f_{X,Y}(x,y)/f_Y(y)$ we immediately
obtain the **chain rule**:

$$h(X|Y) = h(X,Y) - h(Y),$$

which may fail to hold if any of the concerned entropies are infinite or
do not exist.

---


### Example 3.1.7  (Entropy of a multivariate normal distribution)

Let $X_1,\dots,X_n$ have a multivariate Gaussian distribution with mean
$\mu$ and covariance matrix $K$. Then

$$h(X_1,\dots, X_n) = \frac{1}{2}\log\left[(2\pi e)^n\det K\right].$$

## 3.2 - Relative Entropy & Mutual Information

### Definition 3.2.1 (KL divergence)

The **relative entropy** (also known as the **Kullback-Liebler
divergence**) $D(f\,||\,g)$ between two densities $f$ and $g$ is defined
as

$$D(f\,||\,g) = \int f(x)\log\frac{f(x)}{g(x)}\,\text{d}x.$$

---

*Note:*
$$D(f\,||\,g) < \infty \Longleftrightarrow \text{supp}\,f\subseteq\text{supp}\,g.$$


### Definition 3.2.2 (Mutual information)

Given two random variables $X$ and $Y$ with joint density $f_{X,Y}$
define the **mutual information** $I(X;Y)$ between $X$ and $Y$ by

$$I(X;Y) = \int f_{X,Y}(x,y)\log\left[\frac{f_{X,Y}(x,y)}{f_X(x)f_Y(y)}\right]\,\text{d}x\,\text{d}y.$$

---

From the definition it is clear that we have the formulas

$$\begin{aligned}
    I(X;Y) &= h(X) - h(X|Y)\\
    &= h(Y) - h(Y|X)\\
    &= h(X) + h(Y) - h(X,Y).
\end{aligned}$$

Along with

$$I(X;Y) = D(f_{X,Y}\,||\,f_X\otimes f_Y).$$

Note the special cases 

$$\begin{aligned}
I(X;Y) &= I(Y;X),\\
I(X;X) &= h(X).
\end{aligned}$$

### Theorem 3.2.3 (Information inequality)

For any pair of densities $f,\,g$:

$$D(f\,||\,g) \geq 0,$$

with equality if and only if $f = g$ a.e.


*Proof.*  

Without loss of generality assume $f/g\geq1$.
Use the fact that $\int f = \int g = 1$ to rewrite 

$$\begin{aligned}
    D(f\,||\,g) &= \int f\log\frac{f}{g}\\
    &= \int f\left(\frac{g}{f}-1-\log\frac{g}{f}\right).
\end{aligned}$$

Now note that for $t\geq1$ we have the inequality:

$$t - 1 -\log t \geq 0,$$

in which equality holds iff $t=1.$ This can be easily established
graphically or by means of elementary calculus. Applying this inequality
to $f/g$ and integrating yields

$$\int \frac{g}{f}-1-\log\frac{g}{f}\;\geq\; 0$$

with equality iff $f = g$ a.e. ◻

---


### Corollary 3.2.4

For any pair of random variables $X,\,Y$: $$I(X;Y)\geq 0,$$ with
equality if and only if $X$ and $Y$ are independent.


*Proof.*  

$$I(X;Y) = D(f_{X,Y}\,||\,f_X\otimes f_Y) \geq 0$$ 

with equality iff
$f_{X,Y} = f_X\otimes f_Y$ a.e. i.e. iff $X$ and $Y$ are independent. ◻

---

### Corollary 3.2.5

For any pair of random variables $X,\,Y$:

$$h(X|Y) \leq h(X),$$

with equality if and only if $X$ and $Y$ are independent.


*Proof.* 

$$h(X) - h(X|Y) = I(X;Y)\,\geq\,0,$$ 

with equality iff $X$ and
$Y$ are independent by Corollary 3.2.4. ◻

---

# References:

- [1] Thomas M Cover. Elements of information theory. John Wiley & Sons, 1999
