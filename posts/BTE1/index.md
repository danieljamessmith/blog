---
title: "The Boltzmann Transport Equation - 1. Introduction"
author: "Daniel Smith"
date: "2024-01-29"
categories: [Mathematics, PDEs, Boltzmann Equation]
title-block-banner: false
image: 'preview.png'
draft: false
description:  "I introduce the rigorous theory of the Boltzmann Transport Equation, following my undergraduate research project at Warwick Mathematics Institue: 'The interplay between Information theory and the long-time behaviour of a dilute gas'."
---


# 1 - The Boltzmann Equation

---

## 1.1 - The Evolution Equations

The **Boltzmann equation** (also known as the **Boltzmann transport
equation**) models the behaviour of a gas comprised of a single particle
species, sufficiently dilute so that quantum effects are negligible and
when all inter-particle interactions are assumed to be elastic binary
collisions: 

$$\begin{aligned}
\frac{\partial f}{\partial t} + v\cdot \nabla_{x} f = Q(f,f),\quad x\in X,\: v\in \mathbb{R}^d,\: t\geq0.
\end{aligned}$$

Where $f=f(t,x,v)=f_t(x,v)$ is the particle distribution
function in phase space and $X \subset \mathbb{R}^d$ $(d\geq2)$ is the
spatial domain of the gas. If we instead adopt index notation the
Boltzmann equation reads 

$$\begin{aligned}
    \frac{\partial f}{\partial t} + v_j\frac{\partial f}{\partial x_j} = Q(f,f).
\end{aligned}$$

where summation over the term
$v_j\frac{\partial f}{\partial x_j}$ is left implicit following
Einstein's summation convention. The operator $Q$ appearing in the above
is the **Boltzmann collision operator**, defined by the integral

$$\begin{aligned}
    Q(f,f) = \int_{\mathbb{R}^d\times\mathbb{S}^{d-1}}B(v-v_{*},\sigma)(f'f'_*-ff_*)\,\mathrm{d}\sigma\,\mathrm{d}v_*,
\end{aligned}$$

where the function $B$ is the so-called **collision
kernel**, whose precise form depends on the nature of the inter-particle
interactions being considered, and we have used the standard
abbreviations $f'=f(t,x,v')$, $f_*=f(t,x,v_*)$ and $f'_*=f(t,x,v'_*)$.


Here we denote by $(v',v'_*)$ the precollisional velocities of a pair of
particles who have velocities $(v,v_*)$ post-collision. By applying the
conservation of momentum and energy we can relate the pairs $(v',v'_*)$
and $(v,v_*)$ via

$$\begin{aligned}
    \begin{cases}
    v' +v'_* = v + v_*\\
    |v'|^2+|v'_*|^2 = |v|^2 +|v_*|^2
    \end{cases}
\end{aligned}$$ 

We parameterise the solution space of this system via
the so-called $\mathbf{\sigma}$**-representation**: 

$$\begin{aligned}
 \begin{cases}
 v' = \frac{v+v_*}{2} + \frac{|v-v_*|}{2}\sigma\\
  v_*' = \frac{v+v_*}{2} - \frac{|v-v_*|}{2}\sigma
 \end{cases}   
\end{aligned}$$ 

where $\sigma \in \mathbb{S}^{d-1}$ is precisely the
variable $\sigma$ integrated over in
the above integral expression for $Q(f,f)$. The Boltzmann
operator $Q$ admits a clear decomposition into a gain term $Q^+$ and a
loss term $Q^-$: 

$$\begin{aligned}
Q(f,f) = Q^+(f,f)-Q^-(f,f),
\end{aligned}$$ 

where $Q^+(f,f)$ 'counts' all the collisions which
result in a new particle moving with velocity $v$ and $Q^-(f,f)$
'counts' all the collisions in which a particle of velocity $v$ collides
with another particle resulting in less particles at velocity $v$. It is
frequently convenient to view the Boltzmann operator as the quadratic
form induced by the (non-symmetric) bilinear form 

$$\begin{aligned}
    Q(g,f) = \int_{\mathbb{R}^d\times\mathbb{S}^{d-1}}B(v-v_{*},\sigma)(g'f'_*-gf_*)\,\mathrm{d}\sigma\,\mathrm{d}v_*.
\end{aligned}$$ 





When the distribution function $f$ is independent of the
spatial variable $x$ the full Boltzmann equation reduces to the **spatially homogeneous Boltzmann
equation**

$$\begin{aligned}
    \frac{\partial f}{\partial t} = Q(f,f).
\end{aligned}$$

If an external force $F = F(x)$ is applied to the
system, we instead consider the more general Boltzmann equation with
force term 

$$\begin{aligned}
    \frac{\partial f}{\partial t} + v\cdot \nabla_{x} f + F\cdot\nabla_{v} f = Q(f,f),
\end{aligned}$$

which in index notation reads as

$$\begin{aligned}
    \frac{\partial f}{\partial t} + v_j\frac{\partial f}{\partial x_j} + F_j\frac{\partial f}{\partial v_j} =  Q(f,f).
\end{aligned}$$ 

Given a solution $f$ of the Boltzmann equation (without
external force) we can define (in adimensional form) the **local
density** $\rho$, the **local macroscopic velocity** $u$ and the **local
temperature** $T$ by 

$$\begin{aligned}
\begin{split}
    \rho &= \int_{\mathbb{R}^d}f(t,x,v)\,\text{d}v,\\
    u &= \frac{1}{\rho}\int_{\mathbb{R}^d}f(t,x,v)v\,\text{d}v,\\
    T &= \frac{1}{\rho d}\int_{\mathbb{R}^d}f(t,x,v)|v-u|^2\,\text{d}v.
\end{split}
\end{aligned}$$

---

## 1.2 - Boundary conditions

For there to be any hope of our problem being well-posed we need to
supplement the Boltzmann equation with boundary conditions, modelling
the interactions between the particles and the boundary $\partial X$ of
the spatial domain $X$.

Of course, the only thing restricting the choice of such boundary
conditions is our imagination. We briefly discuss some of the most
popular and physically relevant choices.


-   **Specular reflection:** 
            $$\begin{aligned}
            f(x,R_xv)& = f(x,v),\quad x\in\partial X,\\
        \end{aligned}$$ 
    where 
    
    $$R_xv = v - 2(v\cdot n(x))n(x)$$

    and $n(x)$ denotes the unit normal at
    $x\in\partial X$. 
    Physically, specular reflection corresponds to the
    particles elastically colliding with a static, hard wall. Although
    not particularly accurate, specular reflection is a natural first
    guess at a boundary condition as it avoids the complex question of
    modelling the interactions of the particles with the fine
    microscopic structure of the wall.

-   **Bounce-back:** 
            $$\begin{aligned}
            f(x,v) = f(x,-v),\quad x\in\partial X.
            \end{aligned}$$ 
    Physically, this condition simply states that
    particles reflect from the boundary with a velocity opposite to
    their incident velocity. Although clearly not particularly
    realistic, it occasionally leads to more physical results than
    specular reflection as it allows for the transfer of some tangential
    momentum to the wall, which is not allowed by specular reflection.

-   **Maxwellian diffusion:** 
        $$\begin{aligned}
        f(x,v) &= \rho_-(x)M_w(v), \quad v\cdot n(x)>0,\\
         \rho_-(x) &= \int_{v\cdot n\lt0}f(x,v)|v\cdot n| \,\mathrm{d}v,\\
        M_w(v) &= \frac{1}{(2\pi)^{\frac{d-1}{2}}T_w^{\frac{d+1}{2}}}\,\mathrm{exp}\left(-\frac{|v|^2}{2T_w}\right).
        \end{aligned}$$
            



---
    




## 1.3 - Collision kernels

The collision kernel $B$ is related to the physical cross section
$\Sigma(v-v_*,\sigma)$ by the identity 

$$\begin{aligned}
    B = |v-v_*|\Sigma
\end{aligned}$$ 

On physical grounds (*Galilean invariance*) it is
assumed that the collision kernel $B$ depends only on the magnitude of
the relative velocity $|v-v_*|$ and the cosine of the deviation angle
$\mathrm{cos}\:\theta = \left\langle \frac{v-v_*}{|v-v_*|},\sigma\right\rangle$.
For this reason it is common to abuse notation by writing

$$\begin{aligned}
    B(v-v_*,\sigma) = B(|v-v_*|,\mathrm{cos}\:\theta)
\end{aligned}$$ 

to emphasise the specific forms that collision kernels
can take. Maxwell showed that for a given impact
parameter $p\geq0$ and relative velocity $z\in\mathbb{R}^3$ the
collision kernel is implicitly given by 

$$\begin{aligned}
    B(|z|,\mathrm{cos}\:\theta) = \frac{p}{\mathrm{sin}\theta}\frac{\text{d}p}{\text{d}\theta}|z|.
\end{aligned}$$ 

This can be made explicit in the crucially important
example of a gas of **hard spheres**, where the gas particles are
treated as spheres of fixed radius that interact via elastic collisions
(*'billiard balls'*). For hard spheres in $d = 3$ the cross section is
constant, and thus the collision kernel is given by 

$$\begin{aligned}
    B = |v-v_*|.
\end{aligned}$$ 

In the case of particles interacting by an inverse
$s$-power law force the collision kernel factorises as 

$$\begin{aligned}
\begin{split}
    B(v-v_*,\cos\theta) &= \Psi(|v-v_*|)\,b(\cos\theta)\\
    &= |v-v_*|^{\gamma}\,b(\cos\theta),
\end{split}
\end{aligned}$$ 

where $\Psi(|z|) = |z|^\gamma$ is conventionally called
the **kinetic collision kernel**,\
$\gamma = (s-5)/(s-1)$ in dimension $d = 3$ and $b(\cos\theta)$ is
conventionally called the **angular collision kernel**. The the function
$b$ is typically complicated, smooth away from $0$ and is only known
implicitly.

Such collision kernels are often further classified by the values of
$\gamma$ as follows:

-   $\gamma > 0$ : **hard potentials**

-   $\gamma < 0$ : **soft potentials**

-   $\gamma = 0$ : **Maxwellian potentials**

The edge case of Maxwellian potentials is interesting as in such cases
the collision kernel has no kinetic part and only depends on the cosine
of the deviation angle. This occurs for particles interacting via an
inverse $(2d-1)$-power law force in $\mathbb{R}^d$ (e.g. a force like
$r^{-5}$ in $\mathbb{R}^3$). Such particles are called **Maxwellian
molecules** and should only be considered a theoretical construction.


A crucial assumption frequently made in analytical treatments of the
Boltzmann equation is **Grad's angular cut-off**, which simply assumes
that the angular collision kernel $b$ is integrable:

$$\begin{aligned}
\int_{\mathbb{S}^{d-1}}b(k\cdot\sigma)\,\text{d}\sigma = \left|\mathbb{S}^{d-2}\right|\int_0^{\pi}b(\cos\theta)\sin^{d-2}\theta\,\text{d}\theta<\infty.
\end{aligned}$$


For a spatially inhomogeneous, equilibrium solution of the Boltzmann
equation (i.e. a density $f = f(x,v)$ solving
$v\cdot \nabla_{x} f = Q(f,f)$) we use these quantities to define the
**local Maxwellian distribution** $M_{\text{loc}}^f$ associated to $f$
by

$$\begin{aligned}
    M_{\mathrm{loc}}^f(x,v) = \frac{\rho(x)}{(2\pi T(x))^{d/2}}\,\mathrm{exp}\left[-\frac{1}{2T(x)}|v-u(x)|^2\right].
\end{aligned}$$ 

For a spatially homogeneous, equilibrium solution of the
Boltzmann equation (i.e. a density $f = f(v)$ solving $Q(f,f)=0$)
$\,\rho,\,u$ and $T$ are constant and correspond to the macroscopic
density, velocity and temperature respectively.

Using these quantities
we define the (global) **Maxwellian distribution** $M^f$ associated to
$f$, which physically describes the state of *thermodynamic equilibrium*
in which the gas is maximally diffused, by 

$$\begin{aligned}
    M^f(v) = \frac{\rho}{(2\pi T)^{d/2}}\,\mathrm{exp}\left[-\frac{1}{2T}|v-u|^2\right].
\end{aligned}$$

In the theory of the Boltzmann equation the following question is of central importance:

**Under what conditions, and in what sense, do we have
$f\longrightarrow M^f$ *as* $t \longrightarrow \infty$?**

---

## 1.4 - The H Theorem

For a probability density $f$ on $X \times \mathbb{R}^d$ define
Boltzmann's **H functional** by 
$$\begin{aligned}
    H(f) 
= \int_{X\times\mathbb{R}^d}f\log f\,\text{d} x\,\text{d} v.
\end{aligned}$$

$H(f)$ is well-defined in $\mathbb{R}\cup\{\infty\}$
provided that $$\int f(x,v)|v|^2\,\text{d} x\,\text{d} v < \infty,$$ i.e. if $f$
has finite energy. We note that up to a change of sign the $H$
functional is just the differential entropy of $f$, to be defined in a future post.

Boltzmann's **H theorem** loosely states that $H(f)$ is a quantity
monotonically decreasing (non-increasing) in time, and is stationary if
and only if $f$ is a Maxwellian. Making this precise is a task more
technical that it might first appear. 


---

### Theorem 1.4.1 (Boltzmann's H Theorem)

Let $(f_t)_{t\geq0}$ be a well-behaved (smooth) solution of the
Boltzmann equation (in particular with finite entropy), with either
periodic, bounce-back or specular boundary conditions. In the latter
case assume further that $d = 2 \text{ or } 3$ and the spatial domain
$X$ has no axis of symmetry. Then:

1.  $$\frac{\text{d}}{\text{d} t} H(f_t) \leq 0.$$
    Moreover, one can define another functional $D$ on
    $L^1\left(\mathbb{R}^d\right)$ called the such that
    $$\frac{\text{d}}{\text{d} t} H(f_t) = -\int_X D(f_t(x,\cdot\,)\,\text{d} x.$$


2.  Assume that $B(v-v_*,\sigma)>0$ for a.e.
    $(v,v_*,\sigma)\in\mathbb{R}^d\times\mathbb{R}^d\times\mathbb{S}^{d-1}$
    (this is always true in cases of physical interest).
    
    Let $f(x,v)$ be a probability density on $X\times\mathbb{R}^d$ with
    finite energy, $\int f(x,v)|v|^2\,\text{d} x\,\text{d} v <\infty.$ Then:
    
    $$\int_X D(f(x,\cdot\,)\text{d} x = 0\,\, \Longleftrightarrow\,\, f\; \text{is a local Maxwellian}, \text{ i.e. } f = M_{\mathrm{loc}}^f.$$


3.  
$$\begin{aligned}
            (f_t)_{t\geq0} \text{ is stationary }\,\,&\Longleftrightarrow\,\, D(f_t(x,\cdot\,) = 0\quad\forall\, t\geq 0\\
            &\Longleftrightarrow\,\, f_t \text{ is a global Maxwellian, i.e. } f_t(x,v) = M^f(v) \quad\forall\, t\geq 0.
    \end{aligned}$$


*Proof.*

See Theorem 1, section 1.1.2 in Rezakhanlou, Villani & Golse [3.].


---

## 1.5 - Collision Invariants and conservation laws

The entropy dissipation functional $D$ introduced in
Theorem 1 can be
expressed as 

$$\begin{aligned}
   D(f) = \frac{1}{4}\int_{\mathbb{R}^d\times\mathbb{R}^d\times\mathbb{S}^{d-1}}B(v-v_{*},\sigma)(f'f'_*-ff_*)\mathrm{log}\,\frac{f'f'_*}{ff_*}\,\text{d}\sigma\,\text{d} v_*\,\text{d} v.
\end{aligned}$$

And formally satisfies

$$\frac{\text{d}}{\text{d} t} H(f_t) = - \int D(f_t(x,\cdot\,)\,\text{d} x$$ 

in the spatially inhomogeneous case and

$$\frac{\text{d}}{\text{d} t} H(f_t) = D(f_t),$$ 

in the spatially homogeneous case.

The derivation of the above formula for $D$ relies on the following lemma used
to symmetrize the Boltzmann operator $Q$:

---

### Lemma 1.5.1

The change of variables interchanging the
primed and unprimed velocities 

$$\begin{aligned}
    (v,v_*,\sigma) \longmapsto (v',v'_*,k)\\
\end{aligned}$$ 

where 

$$\begin{aligned}
k &= \frac{v-v_*}{|v-v_*|}\\
\\
\sigma &= \frac{v'-v'_*}{|v'-v'_*|} 
\end{aligned}$$


is involutive (self-inverse) and has unit Jacobian
determinant.

Similarly, the change of variables interchanging the starred and
unstarred velocities $(v,v_*,v',v'_*)\longmapsto(v_*,v,v'_*,v')$ is also
involutive with unit Jacobian.

---


Morally, this lemma simply states than under an integral sign one can
interchange primed and unprimed velocities
$(v,v_*) \longmapsto (v',v'_*)$ and starred and unstarred velocities
$(v,v_*) \longmapsto (v_*,v)$ at will. Physically, this property relies
on the time- and space-reversal symmetry of the microscopic dynamics.\
Repeated application of Lemma 1 to an integral of the form $\int Q(f,f)\phi$ for an
arbitrary continuous function $\phi$ of velocity gives 

$$\begin{aligned}
\int_{\mathbb{R}^d} Q(f,f)\phi\,dv &= \int_{\mathbb{R}^d\times\mathbb{R}^d\times\mathbb{S}^{d-1}}B(v-v_{*},\sigma)(f'f'_*-ff_*)\phi\;\text{d}\sigma\,\text{d}v_*\text{d}v\\
&=\int_{\mathbb{R}^d\times\mathbb{R}^d\times\mathbb{S}^{d-1}}B(v-v_{*},\sigma)(ff_*)(\phi'-\phi)\;\text{d}\sigma\,\text{d}v_*\text{d}v\\
&=\frac{1}{2}\int_{\mathbb{R}^d\times\mathbb{R}^d\times\mathbb{S}^{d-1}}B(v-v_{*},\sigma)(ff_*)(\phi'+\phi'_*-\phi-\phi_*)\;\text{d}\sigma\,\text{d}v_*\text{d}v\\
&=-\frac{1}{4}\int_{\mathbb{R}^d\times\mathbb{R}^d\times\mathbb{S}^{d-1}}B(v-v_{*},\sigma)(f'f'_*-ff_*)(\phi'+\phi'_*-\phi-\phi_*)\;\text{d}\sigma\,\text{d}v_*\text{d}v\\
\end{aligned}$$ 

Taking $\phi = \mathrm{log}\,f$ yields the above integral formula for $D$. Moreover,
we see from the last line of the above that for $\phi$ satisfying the
functional equation 

$$\begin{aligned}
    \phi + \phi_* = \phi' + \phi'_*
\end{aligned}$$ 

we have, at least formally, the conservation law:

$$\begin{aligned}
        \frac{\text{d}}{\text{d} t}\int f(t,x,v)\phi(v)\,\text{d} x\,\text{d} v = 0.
\end{aligned}$$

Such functions $\phi$ are called **collision invariants** as they
correspond to quantities conserved by the microscopic dynamics.

The functional equation $\phi + \phi_* = \phi' + \phi'_*$ has been solved under progressively weaker and weaker
assumptions on $\phi$, each time concluding that the most general
solution is

$$\phi(v) = A + B\cdot v + C|v|^2$$ 

for some $A,\,C\in\mathbb{R}$, $B\in\mathbb{R}^d.$ 

Thus, all collision invariants
can be written as a linear combination of the so-called **elementary
collision invariants** 

$$\begin{aligned}
    \phi(v) = 1, v_1,\dots,v_d,\frac{v^2}{2},
\end{aligned}$$

which correspond to the conservation of mass, the
conservation of each of the $d$ components of momentum and the
conservation of energy respectively.

---

# References:

- [1.] Carlo Cercignani et al. *Mathematical methods in kinetic theory*, volume 1. Springer, 1969.
- [2.] Cédric Villani. *A review of mathematical topics in collisional kinetic theory*. Handbook of mathematical fluid dynamics, 1(71-305):3–8, 2002.
- [3.] Fraydoun Rezakhanlou, Cedric Villani, and Fraņcois Golse. Entropy methods for the Boltzmann
        equation: lectures from a special semester at the Centre Emile Borel, Institut H. Poincar ́e, Paris,
        2001. Number 1916. Springer Science & Business Media, 2008.

