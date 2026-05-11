# Candidate Evidence Eval Inspection

> Exploratory diagnostic report only. Do not treat these counts as regression metrics.

- Eval file: `eval/candidate_evidence_questions.yaml`
- Index dir: `.math_rag_index`
- Mode: `hybrid`
- Top-k: `10`
- Candidate questions: 140
- Negative questions: 20

## Diagnostic Counts

- Expected source appeared in top-k: 96/140
- Expected chunk type appeared in top-k: 114/140
- Expected terms appeared in top-k: 131/140
- Negative questions with strong-looking evidence requiring manual review: 1

## Questions

### conic_poincare_001 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss conical approximation of Poincare type cscK metrics?

**Expected sources:** `2210.11862`
**Expected chunk types:** `theorem`, `proposition`, `proof`, `text`
**Expected terms:** `Poincare type`, `conical approximation`, `cscK`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.647 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | yes | yes | cscK | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 2 | 0.573 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 22-35 | no | yes | cscK | ...tion} \begingroup \raggedright Let $X$ be a compact K\"ahler manifold endowed with a constant scalar curvature K\"ahler(cscK) metric $\omega_X$, and assume it admits no non-trivial holomorphic vector field. In this article, we aim at constructing complete cscK metrics on the complement of finitely many points in $X$, which exhibit Poincar\'e type singularity... |
| 3 | 0.571 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | no | no | cscK | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |
| 4 | 0.556 | `corpus/arxiv/1803.09506/source/source.tex` | `definition` | Singular constant scalar curvature K\"ahler metrics > Construct approximate cscK cone metrics for big classes | lines 2313-2315 | no | no | cscK | \begin{defn} We say a big class $\Om$ has the cscK approximation property, if there exists a family of class $\Om_t\rightarrow \Om$ such that $\Om_t$ admits cscK metrics. \end{defn} |
| 5 | 0.369 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Introduction | lines 221-230 | no | yes | cscK | A lot of progress has been made in this case. Auvray proved in \cite[Theorem 1]{A} the existence of Poincar\'e type geodesic. He also discovered a topological constraint for the Poincar\'e type cscK metrics in \cite{A2}, asymptotic properties of Poincar\'e type extremal K\"ahler metrics in \cite{A3} and the Poincar\'e type Futaki characters in \cite{A4}. See... |
| 6 | 0.439 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 220-223 | no | yes | cscK | In Section \ref{a priori estimates}, we establish a priori estimates for \eqref{2nd pde} in both the cscK cone problem and the degenerate cases. The a priori estimates of Chen-Cheng rely on fixed smooth K\"ahler metric. In the conical setting, their a priori estimates can not be applied directly, since the a priori estimates are required to be obtained with... |
| 7 | 0.351 | `corpus/my_notes/project_paper_index.md` | `text` | Project Paper Index > Poincare, Cusp, And Cone Metrics | lines 199-255 | no | yes | conical approximation, cscK | ## Poincare, Cusp, And Cone Metrics - Hugues Auvray, "Asymptotic properties of extremal Kähler metrics of Poincaré type". arXiv: https://arxiv.org/abs/1401.0123 Local: `corpus/arxiv/1401.0123` Role: asymptotic analysis for Poincare-type extremal metrics. - Hugues Auvray, "Note on Poincaré type Kähler metrics and Futaki characters". arXiv: https://arxiv.org/a... |
| 8 | 0.436 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 81-91 | no | yes | cscK | ...$[E_i]$ denotes the Poincar\'e dual of the $E_i$. Our main theorem adds new examples to the existing list of Poincar\'e type metrics. We recall here some important examples: (a) the K\"ahler-Einstein metrics of Poincar\'e type, whose existence were shown by Tian-Yau \cite{TY87}, Kobayashi \cite{Kob84} and Cheng-Yau \cite{CY80}; (b) the toric extremal K\"ahle... |
| 9 | 0.430 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 128-143 | no | yes | cscK | ...seen from \cite{Auv14} Theorem 4, is a necessary condition for the existence of extremal K\"ahler metric of Poincar\'e type in the given K\"ahler class (\ref{Kahler class with ai}). \paragraph{Strategy of the proof and Outline of the article} \begin{itemize} \item To prepare ourselves with the construction, we recap the momentum construction of Hwang-Singer... |
| 10 | 0.332 | `corpus/arxiv/1205.0056/source/cone_metrics.tex` | `text` | The space of K\"ahler cone metrics > CscK cone metrics | lines 1190-1192 | no | yes | cscK | %\subsection{CscK cone metrics} |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_002 - conic/cusp/Poincare metrics

**Question:** Where does the corpus state or prove uniqueness for Poincare type cscK metrics?

**Expected sources:** `2410.14130`
**Expected chunk types:** `theorem`, `proposition`, `proof`
**Expected terms:** `uniqueness`, `Poincare type`, `constant scalar curvature`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.734 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | no | no | constant scalar curvature | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 2 | 0.580 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | no | no | - | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |
| 3 | 0.544 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Introduction | lines 185-188 | yes | no | uniqueness | ...e{CLP} another way to prove the convexity of the $K$-energy. Chen-Paun-Zeng used PDEs method in \cite{CPZ} to prove the uniqueness of the cscK metric and extremal K\"ahler metric. A natural question is: could we prove the uniqueness of cscK metric on more general K\"ahler manifolds? Note that the methods we mentioned above depend on the compactness of the ma... |
| 4 | 0.619 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 145-159 | no | no | - | This paper is organized as follows. In Section 2, we recall the definitions of {\kah} metrics of Poincar\'{e}/cone singularities. In addition, we define a background {\kah} metric with cone singularities, which converges to a cscK metric of Poincar\'{e} type. Finally, we consider a fixed point formula on the weighted {\hol} space, which characterizing a cscK... |
| 5 | 0.416 | `corpus/arxiv/1205.0056/source/cone_metrics.tex` | `text` | Introduction | lines 617-642 | no | no | uniqueness | ...als, as observed by Berndtsson, the convexity of the Ding functional along the bounded geodesic is applied to prove the uniqueness of K\"ahler-Einstein cone metrics (generalizing the Bando-Mabuchi uniqueness theorem \cite{MR946233}). However the cone geodesic {we construct} here has more {regularity} across the divisor in a subspace $\mathcal{H}_C$ which sti... |
| 6 | 0.406 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | no | - | ...phic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelia... |
| 7 | 0.384 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 155-163 | no | no | constant scalar curvature | ...ralize our previous results in \cite{cc2} , where we assume the automorphism group is discrete. For simplicity, we only state and prove the results on constant scalar curvature K\"ahler metrics in this paper. Analogous results for extremal K\"ahler metrics can be proved in a similar way without additional estimates. \\ Throughout this paper, we denote $ G=Au... |
| 8 | 0.378 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2847-2852 | no | no | - | ...finity section in $X$. This is already treated in Corollary~\ref{Hirzebruch} where we know that there exists Poincar\'e type extremal metrics. The above computations then confirm that the condition of equation~\eqref{hyperbolicity-condition} holds, which we also know by general theory regarding extremal Poincar\'e type metrics. To prove Corollary~\ref{Hirzeb... |
| 9 | 0.376 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | ...anifolds? %\item In Corollary 1.7, can we extend it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic topology, how far is the class of Calabi dream manifolds from the class of all smooth minimal models of general type? %\item Motived by Conjecture 1 in \cite{LeSz13}, we may ask whe... |
| 10 | 0.362 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 419-430 | no | no | - | ...next section, we recall the non-Archimedean and Archimedean functionals, and explain they are related to each other. We state the basic correspondence between finite energy non-Archimedean metrics and maximal geodesic rays as established by Berman-Boucksom-Jonsson. We discuss the twist of non-Archimedean metrics that was introduced in \cite{His16b} for smoot... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_003 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss toric extremal metrics with Poincare type singularities?

**Expected sources:** `1711.08424`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `toric`, `extremal`, `Poincare type`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.787 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2786-2791 | yes | yes | toric, extremal | \subsection{The proof of Corollary~\ref{Hirzebruch-non-poincare}} The missing component in the proof is to show that the extremal metrics obtained cannot be of Poincar\'e type. For this we will show that in the above situation, the necessary condition in equation~\eqref{hyperbolicity-condition} for the existence of a toric extremal metric of Poincar\'e type... |
| 2 | 0.599 | `corpus/arxiv/1510.02226/source/source.tex` | `text` | unsectioned | lines 274-280 | no | yes | toric, extremal | \begin{document} {\Huge \sc \bf\maketitle} \begin{abstract} We construct new explicit toric scalar-flat \Ka ALE metrics with orbifold singularities, which we use to obtain smooth extremal K\"ahler metrics on appropriate resolutions of orbifolds. \end{abstract} |
| 3 | 0.629 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | The relative K-stability of a pair > Test configurations and $K$-stability of a pair | lines 513-522 | yes | yes | toric, extremal | We shall next turn to the toric case as a model example for the above theory, and where specific computations are manageable. We shall show (see in particular Corollary \ref{Hirzebruch-non-poincare}) that there are examples of relatively $K$-stable triples $(X,Z,L)$ satisfying $F_{\chi}''(0) > 0,$ which cannot be of Poincar\'e type. We note, however, that th... |
| 4 | 0.472 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | no | yes | extremal | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 5 | 0.458 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | toric | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 6 | 0.454 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 81-91 | no | yes | toric, extremal | ...$[E_i]$ denotes the Poincar\'e dual of the $E_i$. Our main theorem adds new examples to the existing list of Poincar\'e type metrics. We recall here some important examples: (a) the K\"ahler-Einstein metrics of Poincar\'e type, whose existence were shown by Tian-Yau \cite{TY87}, Kobayashi \cite{Kob84} and Cheng-Yau \cite{CY80}; (b) the toric extremal K\"ahle... |
| 7 | 0.410 | `corpus/arxiv/1401.0123/source/ExtPK.tex` | `text` | Introduction | lines 290-336 | no | yes | extremal | ~ Theorem \ref{thm_mainthm1} states that extremal K�hler metrics of Poincar� type are \textit{asymptotically products} near the divisor. Similar results for K�hler-Einstein metrics were already known \cite{sch,wu}; these previous approaches differ fundamentally to ours though. Indeed, in that case, the K�hler-Einstein analogue of Theorem \ref{thm_mainthm2} f... |
| 8 | 0.390 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `text` | Introduction | lines 211-217 | no | yes | toric, extremal | Lejmi studied the notion of extremal toric almost K\"ahler metrics in~\cite{lejmi} and showed that a large and interesting part of them (the involutive type ones) is in one-to-one correspondence with $\mathcal{AK}(P,\sigma)$. %In the integral case $H$ coincides with the inverse of the symplectic potential Hessian. Chen--Li--Sheng proved that existence of a t... |
| 9 | 0.380 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Conjectural picture | lines 666-667 | no | yes | - | \section{Conjectural picture} In this final section we discuss what one might expect about the existence problem for metrics with cone singularities on a Fano manifold. It is natural to think of such a metric as a solution of a distributional equation |
| 10 | 0.371 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 645-648 | no | yes | toric, extremal | ...\emph{$T$-invariant finite-energy potentials}. Our contribution is twofold: we simultaneously incorporate \emph{Lahdili-type weights} and a \emph{twist by a positive $(1,1)$-current} satisfying a natural decomposition condition, and we carry out the analysis in the finite-energy setting $\cE^T(X,\omega)$ (rather than restricting to smooth or Poincar\'e-type... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_004 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss the space of Poincare type Kahler metrics on a divisor complement?

**Expected sources:** `1205.0056`
**Expected chunk types:** `definition`, `proposition`, `text`
**Expected terms:** `space`, `Poincare type Kahler metrics`, `divisor`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.734 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | no | yes | divisor | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 2 | 0.608 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Appendix > Curvature decomposition of Poincar\'e type metrics | lines 2321-2324 | no | yes | divisor | \subsection{Curvature decomposition of Poincar\'e type metrics}\label{sec:poincare-curvature} In this appendix, we establish the curvature decomposition formula for Poincar\'e type metrics that is used throughout the paper. The main result (Corollary~\ref{decomp}) shows that the Ricci curvature of a Poincar\'e type metric decomposes into a smooth part, a log... |
| 3 | 0.550 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 22-35 | no | yes | - | ...X$, and assume it admits no non-trivial holomorphic vector field. In this article, we aim at constructing complete cscK metrics on the complement of finitely many points in $X$, which exhibit Poincar\'e type singularity at each point. The motivation for studying Poincar\'e type metrics stems from the standard Poincar\'e cusp metric $$\omega_{\Delta^*}=\displ... |
| 4 | 0.410 | `corpus/arxiv/1401.0123/source/ExtPK.tex` | `text` | Introduction | lines 290-336 | no | yes | divisor | ~ Theorem \ref{thm_mainthm1} states that extremal K�hler metrics of Poincar� type are \textit{asymptotically products} near the divisor. Similar results for K�hler-Einstein metrics were already known \cite{sch,wu}; these previous approaches differ fundamentally to ours though. Indeed, in that case, the K�hler-Einstein analogue of Theorem \ref{thm_mainthm2} f... |
| 5 | 0.397 | `corpus/arxiv/1401.0128/source/Note_PKFutaki.tex` | `text` | Introduction | lines 359-410 | no | yes | divisor | An extremal metrics is a K�hler metrics such that the Riemannian gradient of its scalar curvature is holomorphic. Constraint \eqref{eqn_constraint} is a reformulation of that of \cite[Prop.4.5]{auv3}, and as such, extends that on the existence of constant scalar curvature metrics in $\mathscr{M}^{D}_{[\omega_X]}$ of \cite{auv2}, which states as: $\sbar^D< \s... |
| 6 | 0.394 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted cscK problem on semisimple principal fibration | lines 2104-2110 | no | yes | - | Also, from \cite[Section 5]{AJL}, any Kähler metric \(\omega\) on \(X\) induces a Kähler metric \(\tilde{\omega}\) on \(Y\) such that the restriction \((Y_b, \tilde{\omega}_b)\) of \((Y, \tilde{\omega})\) to a fiber over a point \(b \in B\) is \(\T\)-equivariantly Kähler isomorphic to \((X, \omega)\). Such a metric \(\tilde{\omega}\) on \(Y\) is the \emph{co... |
| 7 | 0.375 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | unsectioned | lines 149-167 | no | yes | divisor | ...tre-ville \\ Montr{\'e}al (Qu{\'e}bec) \\ H3C 3P8 \\ Canada} \email{lars.sektnan@cirget.ca} \keywords{Extremal K\"ahler metrics, toric geometry, complete Poincar\'e metrics on a complement of divisor.} \subjclass{53C55, 53C25} \thanks{V.A. was supported in part by an NSERC discovery grant. He is grateful to l'\'Ecole Normale Sup\'erieure and l'\'Ecole polyte... |
| 8 | 0.348 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Uniqueness of the Poincar\'e type cscK metrics > Proof Theorem \ref{unique csck}, Theorem \ref{main theorem 2} and Theorem \ref{fixed point} | lines 2245-2359 | no | yes | space, divisor | \begin{thebibliography}{9} \bibitem{Ao} T. Aoi. \newblock A conical approximation of constant scalar curvature K\"ahler metrics of Poincar\'e type. \newblock arXiv preprint arXiv:2210.11862 (2022). \bibitem{A} H. Auvray. \newblock The space of Poincar\'e type K\"ahler metrics on the complement of a divisor. \newblock Journal f\"ur die reine und angewandte Ma... |
| 9 | 0.340 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Introduction | lines 247-288 | no | yes | divisor | \section{Introduction} Let $\D\subset M$ be a smooth divisor in a compact \K manifold. A \K edge metric on $M$ with angle $2\pi \be$ along $\D$ is a \K metric on $\MsmD$ that is asymptotically equivalent at $\D$ to the model edge metric $$ g_\be:=\|z_1\|^{2\be-2}\|dz_1\|^2 + \sum_{j=2}^n \|dz_j\|^2; $$ here $z_1,z_2,\ldots,z_n$ are holomorphic coordinates such tha... |
| 10 | 0.334 | `corpus/my_notes/project_paper_index.md` | `text` | Project Paper Index > Poincare, Cusp, And Cone Metrics | lines 199-255 | no | yes | space, divisor | ## Poincare, Cusp, And Cone Metrics - Hugues Auvray, "Asymptotic properties of extremal Kähler metrics of Poincaré type". arXiv: https://arxiv.org/abs/1401.0123 Local: `corpus/arxiv/1401.0123` Role: asymptotic analysis for Poincare-type extremal metrics. - Hugues Auvray, "Note on Poincaré type Kähler metrics and Futaki characters". arXiv: https://arxiv.org/a... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_005 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss extremal Poincare type metrics and Futaki invariants?

**Expected sources:** `1401.0123`, `1401.0128`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `extremal`, `Poincare type`, `Futaki`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.658 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2786-2791 | no | yes | extremal | \subsection{The proof of Corollary~\ref{Hirzebruch-non-poincare}} The missing component in the proof is to show that the extremal metrics obtained cannot be of Poincar\'e type. For this we will show that in the above situation, the necessary condition in equation~\eqref{hyperbolicity-condition} for the existence of a toric extremal metric of Poincar\'e type... |
| 2 | 0.537 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | no | yes | extremal | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 3 | 0.590 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2847-2852 | no | yes | extremal | ...finity section in $X$. This is already treated in Corollary~\ref{Hirzebruch} where we know that there exists Poincar\'e type extremal metrics. The above computations then confirm that the condition of equation~\eqref{hyperbolicity-condition} holds, which we also know by general theory regarding extremal Poincar\'e type metrics. To prove Corollary~\ref{Hirzeb... |
| 4 | 0.441 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 113-119 | no | yes | extremal, Futaki | The \textbf{\textit{extremal vector field}} for the Poincar\'e type K\"ahler metric setting is defined using the Futaki character introduced in \cite{Auv13-2}, and we will discuss in more detail in Section~\ref{subsection 9.3}. Here, we just mention that it is a holomorphic vector field depending only on the K\"ahler class and maximal compact subgroup $K$. F... |
| 5 | 0.429 | `corpus/arxiv/1401.0128/source/Note_PKFutaki.tex` | `text` | Introduction | lines 359-410 | yes | yes | extremal, Futaki | An extremal metrics is a K�hler metrics such that the Riemannian gradient of its scalar curvature is holomorphic. Constraint \eqref{eqn_constraint} is a reformulation of that of \cite[Prop.4.5]{auv3}, and as such, extends that on the existence of constant scalar curvature metrics in $\mathscr{M}^{D}_{[\omega_X]}$ of \cite{auv2}, which states as: $\sbar^D< \s... |
| 6 | 0.403 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Proofs of Lemmas \ref{s1is2}, \ref{s1is1} and \ref{s1is2overk} | lines 1659-1726 | no | yes | extremal, Futaki | ....~M.~J. Calderbank, P. Gauduchon and C. T{\o}nnesen-Friedman, {\it Hamiltonian $2$-forms in K\"ahler geometry} III {\it Extremal metrics and stability}, arXiv:math.DG/??????? \bibitem{Bando-Mabuchi} S. Bando and T. Mabuchi, {\it Uniqueness of Einstein--K\"ahler metrics modulo connected group actions}, in `Algebraic Geometry' (Sendai 1985), Adv. Stud. Pure Ma... |
| 7 | 0.375 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | Lower bound on the Calabi functional | lines 2270-2278 | no | yes | extremal, Futaki | The constant $4\cdot (2\pi)^n$ arises from the difference between the differential-geometric and algebro-geometric Futaki invariants and inner products. This is analgous to the finite dimensional result, Theorem~\ref{thm:destablwrbound}. In the same way as we did there, we can extend the result to the case of extremal metrics. We simply need to modify the te... |
| 8 | 0.344 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `text` | Introduction and the statement of the results > Log Futaki invariant computed with respect to the conically singular metrics | lines 369-370 | no | yes | Futaki | \subsection{Log Futaki invariant computed with respect to the conically singular metrics} \label{intscmsfi} Although the log Futaki invariant is conjectured to be related to the existence of conically singular cscK metrics, the log Futaki invariant itself is computed with respect to a \textit{smooth} \kah metric in $c_1 (L)$. We now consider the following qu... |
| 9 | 0.338 | `corpus/arxiv/1401.0123/source/ExtPK.tex` | `text` | Introduction | lines 263-266 | yes | yes | extremal | ...hat this definition allows a rather loose behaviour near the divisor, in the sense that one can easily produce Poincar� type metrics such that their restrictions to directions parallel to the divisor \textit{does not} converge near the divisor. Our first main result states nonetheless that such a convergence does occur for extremal Poincar� type K�hler metri... |
| 10 | 0.332 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Convex Preliminaries > Polarized toric manifolds | lines 1349-1350 | no | yes | - | and $D_{j} \coloneqq \mu_{P}^{-1}(F_{j})$. By setting $c_{j}$ the Poincare dual of $D_{j}$, we have |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_006 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss relative or modified Futaki invariants for Poincare type metrics?

**Expected sources:** `1401.0128`
**Expected chunk types:** `definition`, `proposition`, `text`
**Expected terms:** `Futaki`, `Poincare`, `relative`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.587 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2786-2791 | no | yes | Poincare | \subsection{The proof of Corollary~\ref{Hirzebruch-non-poincare}} The missing component in the proof is to show that the extremal metrics obtained cannot be of Poincar\'e type. For this we will show that in the above situation, the necessary condition in equation~\eqref{hyperbolicity-condition} for the existence of a toric extremal metric of Poincar\'e type... |
| 2 | 0.463 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | K-stability > K-stability of a pair $(V,D)$ | lines 2016-2064 | no | yes | Futaki, relative | Let us briefly explain the last condition. In Section~\ref{sec:extremalruled} we will construct complete extremal metrics on the complement of a divisor on a ruled surface, and we will find that for a range of polarisations $m<k_2$ (where $m$ parametrises the polarisation and $k_2$ is a constant - see Section~\ref{sec:extremalruled} for details) we obtain me... |
| 3 | 0.545 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2847-2852 | no | yes | Poincare | ...finity section in $X$. This is already treated in Corollary~\ref{Hirzebruch} where we know that there exists Poincar\'e type extremal metrics. The above computations then confirm that the condition of equation~\eqref{hyperbolicity-condition} holds, which we also know by general theory regarding extremal Poincar\'e type metrics. To prove Corollary~\ref{Hirzeb... |
| 4 | 0.407 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 113-119 | no | yes | Futaki | The \textbf{\textit{extremal vector field}} for the Poincar\'e type K\"ahler metric setting is defined using the Futaki character introduced in \cite{Auv13-2}, and we will discuss in more detail in Section~\ref{subsection 9.3}. Here, we just mention that it is a holomorphic vector field depending only on the K\"ahler class and maximal compact subgroup $K$. F... |
| 5 | 0.391 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | ...anifolds? %\item In Corollary 1.7, can we extend it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic topology, how far is the class of Calabi dream manifolds from the class of all smooth minimal models of general type? %\item Motived by Conjecture 1 in \cite{LeSz13}, we may ask whe... |
| 6 | 0.385 | `corpus/arxiv/1401.0128/source/Note_PKFutaki.tex` | `text` | Introduction | lines 315-332 | yes | yes | Futaki | Metrics of $\mathscr{M}_{[\omega_X]}^D$ are complete, with finite volume (equal to that of $X$ for smooth K�hler metrics of class $[\omega_X]$); they also share a common mean scalar curvature, which differs from that attached to smooth K�hler metrics of class $[\omega_X]$. Restricting our attention to the set $\hD$ of holomorphic vector fields with their nor... |
| 7 | 0.385 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `text` | Introduction and the statement of the results > Log Futaki invariant computed with respect to the conically singular metrics | lines 369-370 | no | yes | Futaki | \subsection{Log Futaki invariant computed with respect to the conically singular metrics} \label{intscmsfi} Although the log Futaki invariant is conjectured to be related to the existence of conically singular cscK metrics, the log Futaki invariant itself is computed with respect to a \textit{smooth} \kah metric in $c_1 (L)$. We now consider the following qu... |
| 8 | 0.380 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `text` | Introduction | lines 251-260 | no | yes | relative | We discuss in~\S\ref{sectFORMALsol} consequences of this last result and open problems in relation with the relative toric version of the Yau--Tian--Donaldson conjecture. In the next section we gather facts, definition, key results and recall brief explanations on the topic of toric extremal (almost) K\"ahler metrics. Section~\ref{sectMAIN} contains the proo... |
| 9 | 0.364 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | It is an interesting question to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except i... |
| 10 | 0.353 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Relative K-polystability of weighted extremal manifolds > Expansions of weighted invariants | lines 655-657 | no | yes | Futaki, relative | Since we wish to compute relative stability, we must also compute how the inner products \(\langle-,-\rangle_{(\X,\A_T)}\) and the weighted Futaki invariants \(F_{v,w}\) change on the blowup. First, we state the following analogue of \cite[Proposition 37]{Sze15} in the weighted setting: |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_007 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss deforming the cone angle in a cscK cone path?

**Expected sources:** `1803.09506`
**Expected chunk types:** `theorem`, `proof`, `text`
**Expected terms:** `cone angle`, `cscK`, `path`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.913 | `corpus/arxiv/1803.09506/source/source.tex` | `definition` | CscK cone path | lines 4524-4526 | yes | no | cone angle, cscK, path | \begin{defn}\label{cscK cone path defn} We say the path $\{\om_{\varphi^\beta}=\om_0+i\p\bar \p\varphi^\beta ;0< \beta\leq 1\} $ is a cscK cone path, if $\om_{\varphi^\beta}$ is a cscK cone metric with cone angle $\beta$ along the smooth divisor $D$. \end{defn} |
| 2 | 0.811 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `conjecture` | Log Futaki invariant and log $K$-stability > Log $K$-stability | lines 725-727 | no | no | cone angle, cscK | \begin{conjecture} \label{logdtyconj} $((X,D);L)$ is log $K$-polystable with cone angle $2 \pi \beta$ if and only if $X$ admits a cscK metric in $c_1(L)$ with cone singularities along $D$ with cone angle $2 \pi \beta$. \end{conjecture} |
| 3 | 0.736 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction > Openness of coercivity | lines 698-700 | no | yes | cone angle, cscK | \begin{cor}[Openness of existence of conic cscK metrics]\label{cor:openness-conic-cscK} Let $D$ be a smooth divisor and assume that $X$ admits no nonzero holomorphic vector field preserving $D$. If $[\om]$ admits a cscK cone metric with cone angle $\alpha_0 \in (0,1)$, then there exists a neighborhood $\mathcal{U}$ of $\alpha_0$ in $(0,1)$ such that $[\om]$... |
| 4 | 0.900 | `corpus/arxiv/1803.09506/source/source.tex` | `theorem` | Introduction | lines 312-315 | yes | yes | cone angle, cscK, path | \begin{thm}[Openness theorem]\label{openess main} Assume that $Aut(X;D)$ is discrete and $C_1(L_D)> 0$. The cscK cone path is open when the cone angle $\beta>0$. \end{thm} |
| 5 | 0.716 | `corpus/arxiv/2210.11862/source/source.tex` | `remark` | Preliminaries > {\kah} cone metrics approximating a cscK metric of Poincar\'{e} type and fixed point formula | lines 477-485 | no | no | cone angle, cscK | ...u}, Guenancia uses the function $\log \left( (1 - e^{- t\beta})/\beta \right) $ in order to define a {\kah} metric with cone singularities. So, the function $G_\beta (t)$ is equal to the function in \cite{Gu} up to the coefficient $a_\beta$ (and additive constants). The reason why we put coefficient $a_\beta$ is that we consider the construction of a cscK co... |
| 6 | 0.849 | `corpus/arxiv/1803.09506/source/source.tex` | `theorem` | CscK cone path > Deform cone angle of the cscK cone path | lines 4555-4558 | yes | yes | cone angle, cscK, path | \begin{thm}\label{openess} Assume that $Aut(X;D)$ is discrete and $C_1(L_D)> 0$. The cscK cone path is open when $\beta>0$. Precisely, if $\om_{\varphi^{\beta_0}}$ is a cscK cone metric with cone angle $\beta_0\in (0,1)$ along the smooth divisor $D$, then there is a $\delta>0$ such that for all $\beta\in (\beta_0-\delta,\beta_0+\delta)$, there exists a cscK... |
| 7 | 0.602 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Introduction | lines 32-41 | no | yes | cone angle | ...} Let $D$ be a smooth divisor in a complex manifold $X$. In this paper we study K\"ahler metrics on $X\setminus D$ with cone singularities of cone angle $2\pi \beta$ transverse to $D$, where $0<\beta<1$. The case we have primarily in mind is when $X$ is a Fano manifold, $D$ is an anticanonical divisor and the metrics are K\"ahler-Einstein; the motivation bei... |
| 8 | 0.752 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 316-326 | yes | yes | cone angle, cscK, path | The precise statement is given in \thmref{openess}. This result should be compared with Donaldson's continuity path of K\"ahler-Einstein cone metrics in the resolution of YTD conjecture for Fano K\"ahler-Einstein metrics \cite{MR3264766,MR3472831}. Donaldson's continuity path deforms the cone angles of K\"ahler-Einstein cone metrics \cite{MR2975584}. The par... |
| 9 | 0.748 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `remark` | Momentum-constructed cscK metrics with cone singularities along a divisor > Background and overview | lines 978-980 | no | no | cone angle, cscK | %\begin{remark} %Theorem \ref{mainthmmc} shows, in particular, that it is not possible to deform the cone angle along $D$ of a conically singular cscK metric, \textit{as long as we use the momentum construction}; it is uniquely determined by the \kah class. %\end{remark} |
| 10 | 0.690 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | cscK cone metrics and convergence > Proof of Theorem \ref{cone to cusp} | lines 854-856 | no | yes | cscK | has a fixed point, i.e., there exists a cscK cone metric of angle $2\pi\beta$. In order to show this, we prove that the map $\mathcal{N}_\beta : C^{4, \alpha}_{\eta} \to C^{4, \alpha}_{\eta}$ is a contraction map. |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_008 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss log K-stability for cscK cone metrics?

**Expected sources:** `1508.02640`, `1803.09506`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `log K-stability`, `cone angle`, `cscK cone`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.804 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 179-182 | yes | yes | cscK cone | We will prove that the existence of cscK cone metrics in terms of the properness of the log $K$-energy. |
| 2 | 0.802 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Preliminaries > {\kah} metrics with cone singularities | lines 320-325 | no | yes | cscK cone | The existence of cscK cone metrics is related to algebro-geometric stability which is called log $K$-polystability. |
| 3 | 0.588 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `remark` | Introduction and the statement of the results > Momentum-constructed metrics and log Futaki invariant | lines 350-355 | yes | no | cone angle | ...each rational \kah class (or polarisation) of $\mathbb{X} = \prj(\mathcal{F} \oplus \cx)$ admits a momentum-constructed cscK metric with cone singularities along $D$ with cone angle $2 \pi \beta$ if and only if it is log $K$-polystable with cone angle $2 \pi \beta$ with respect to the product log test configuration generated by the fibrewise $\cx^*$-action o... |
| 4 | 0.693 | `corpus/arxiv/1803.09506/source/source.tex` | `lemma` | Properness implies existence > Twisted cscK cone metric | lines 858-861 | yes | no | cscK cone | \begin{lem}\label{globalminimiser} Assume $\chi\geq 0$ is smooth closed $(1,1)$-form. The $\chi$-twisted cscK cone metrics are the global minimiser of the log $\chi$-twisted $K$-energy in $\mathcal H_\beta$. \end{lem} |
| 5 | 0.548 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction > K-stability and K\"ahler-Einstein metrics | lines 195-198 | no | yes | log K-stability, cone angle | \subsection{K-stability and K\"ahler-Einstein metrics} There has been much recent work on the study of K\"ahler-Einstein metrics with cone angles along a divisor \cite{D3}. Indeed, in the solution of the Yau-Tian-Donaldson conjecture when $L=-K_X$, an important feature was the use of the \emph{Donaldson continuity method} \begin{equation}\label{doncont}\Ric... |
| 6 | 0.485 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 635-663 | no | yes | - | \section*{Introduction} The constant scalar curvature K\"ahler (cscK) metric problem has become one of the central focus in K\"ahler geometry during the last decades. The Yau--Tian--Donaldson conjecture asserts that given a compact K\"ahler manifold with a fixed K\"ahler class, the existence of cscK metrics in the K\"ahler class is equivalent to an algebro-g... |
| 7 | 0.464 | `corpus/arxiv/math_0412518/source/slopeobs_archive.tex` | `text` | Slope stability as a necessary condition for K-stability > Slope stability as an obstruction to K-stability | lines 673-684 | no | yes | - | \subsection{Slope stability as an obstruction to K-stability}\label{sec:slopestabilityasanobstruction}\ \nopagebreak \vskip 5pt Slope stability with respect to $Z$ is precisely K-stability restricted to test configurations arising from the degeneration to the normal cone of $Z$. In (\cite{RT} Theorem 4.18) it is shown that K-semistability implies slope semis... |
| 8 | 0.452 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | ...phic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelia... |
| 9 | 0.565 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 316-326 | yes | yes | cone angle, cscK cone | ...ment is given in \thmref{openess}. This result should be compared with Donaldson's continuity path of K\"ahler-Einstein cone metrics in the resolution of YTD conjecture for Fano K\"ahler-Einstein metrics \cite{MR3264766,MR3472831}. Donaldson's continuity path deforms the cone angles of K\"ahler-Einstein cone metrics \cite{MR2975584}. The paralleling idea is... |
| 10 | 0.447 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Conjectural picture | lines 666-667 | no | yes | - | \section{Conjectural picture} In this final section we discuss what one might expect about the existence problem for metrics with cone singularities on a Fano manifold. It is natural to think of such a metric as a solution of a distributional equation |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_009 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss Jeffres-Mazzeo-Rubinstein edge singularities?

**Expected sources:** `1105.5216`
**Expected chunk types:** `theorem`, `definition`, `text`
**Expected terms:** `edge singularities`, `Kahler-Einstein`, `polyhomogeneous`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.845 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Conjectural picture | lines 666-667 | no | yes | - | \section{Conjectural picture} In this final section we discuss what one might expect about the existence problem for metrics with cone singularities on a Fano manifold. It is natural to think of such a metric as a solution of a distributional equation |
| 2 | 0.788 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `remark` | Log Futaki invariant and log $K$-stability > Log $K$-stability | lines 714-716 | no | no | - | \begin{remark} We need some restriction on the singularities of $\mathcal{X}$ and $\mathcal{D}$ to define log $K$-stability (cf.~Remark \ref{pathsingkstble}), when the log test configuration is not product or trivial (cf.~\cite{os}), but we do not discuss this issue since only the product log test configurations will be important for us later. \end{remark} |
| 3 | 0.684 | `corpus/arxiv/1008.2607/source/source.tex` | `definition` | K\"{a}hler geometry on toric surfaces > The Abreu equation on $\Delta$ | lines 577-582 | no | yes | - | \begin{defn}\label{definition_1} Let $K$ be a smooth function on $\bar\Delta$. It is called {\em edge-nonvanishing} if it does not vanish on any edge of $\Delta$. That is to say, for any edge $\ell$ there exists a point $\xi^{(\ell)}$ on the edge such that $K(\xi^{(\ell)})\not=0$. \end{defn} |
| 4 | 0.611 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Linear analysis | lines 1203-1232 | yes | yes | polyhomogeneous | ...facts about the linear elliptic theory needed to handle the existence, deformation and regularity theory for canonical edge metrics. We discuss this from two points of view, reviewing the estimates obtained by Donaldson in the wedge H\"older spaces, and also describing how to obtain analogous estimates in the edge H\"older spaces. These latter estimates are... |
| 5 | 0.545 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | ...o all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelian} \end{document} |
| 6 | 0.543 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | no | yes | - | ...rk) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail in our next paper and refer interested readers to the following works and references therein: |
| 7 | 0.531 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | It is an interesting question to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except i... |
| 8 | 0.574 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Introduction | lines 247-288 | yes | yes | edge singularities | \section{Introduction} Let $\D\subset M$ be a smooth divisor in a compact \K manifold. A \K edge metric on $M$ with angle $2\pi \be$ along $\D$ is a \K metric on $\MsmD$ that is asymptotically equivalent at $\D$ to the model edge metric $$ g_\be:=\|z_1\|^{2\be-2}\|dz_1\|^2 + \sum_{j=2}^n \|dz_j\|^2; $$ here $z_1,z_2,\ldots,z_n$ are holomorphic coordinates such tha... |
| 9 | 0.455 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Introduction > Coercivity and Ding-stability | lines 516-542 | no | yes | - | ...ray~\cite{PS,Berm16}, giving rise to a one-to-one correspondence between $\cHNA$ and geodesic rays with \emph{algebraic singularities} (emanating from $0$). It further follows from~\cite{BHJ2,Berm16} that to each functional $\opF$ among $\opE,\opL_\theta,\opD_\theta,\opJ$ corresponds a non-Archimedean version\footnote{For notational simplicity, we denote a f... |
| 10 | 0.443 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | - | \def\Rico{\Ric\,\!\o} \def\Q{{\bf ????????????}} \def\a{\alpha} \def\be{\beta} \def\o{\omega} \def\O{\Omega} \def\th{\theta} \def\Th{\Theta} \def\vp{\varphi} \def\eps{\epsilon} \def\vps{\varphi_s} \def\ovp{{\o_{\vp}}} \def\on{\omega^n} \def\ovpn{\omega_{\vp}^n} \def\ovps{\omega_{\vp_s}} \def\ovpsn{\omega_{\vp_s}^n} \def\intM{\int_M} \def\Ric{\hbox{\rm Ric}\,... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_010 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss conic Kahler-Einstein metrics and divisor cone angles?

**Expected sources:** `1105.5216`, `1205.0056`, `1508.02640`
**Expected chunk types:** `theorem`, `definition`, `text`
**Expected terms:** `conic`, `Kahler-Einstein`, `cone angle`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.760 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Openness of coercivity > Coercivity > Applications to conic and cusp singularities | lines 1829-1834 | no | yes | conic, cone angle | \subsubsection*{Applications to conic and cusp singularities} Having established the general openness result for coercivity under perturbations (Proposition \ref{prop:coercivity-weighted-twisted} and Proposition \ref{prop:cusp-to-conic}), we now apply it to two important geometric settings: perturbations from cusp singularities to conic singularities, and pe... |
| 2 | 0.712 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Singular constant scalar curvature K\"ahler metrics > Examples | lines 2548-2550 | no | yes | cone angle | \subsection{Examples} In this Section, we construct singular cscK metrics on log Fano pairs. We set $\tri$ to be an effective $Q$-divisor. The divisor $D$ has two parts. One part is with coefficients in $(-1,0]$. Then by definition, the cone angle $\beta_i$ is equal to $1+\alpha_i$. So we have $\beta\in (0,1]$. The other part is the $\pi$-exceptional divisor... |
| 3 | 0.667 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Fundamentals of $\cC^{4,\a,\b}$ space > From local to global | lines 1588-1591 | no | yes | conic, cone angle | ...will give an equivalent global definition of the space $\cC^{4,\a,\b}$ here. Recall that Donaldson metric $\Omega$ is a conic K\"ahler metric on $X$ with cone angle $2\pi\b$ along the divisor $D$. And it is quasi-isometric to $\Omega_0$ near any point $p$ on the divisor. Therefore, we can introduce the following definition. |
| 4 | 0.596 | `corpus/arxiv/1612.01866/source/BoundedRicci.tex` | `text` | unsectioned | lines 1-61 | no | yes | Kahler-Einstein, cone angle | ...\numberwithin{equation}{section} \bibliographystyle{plain} %--------Meta Data: Fill in your info------ \title{K\"ahler metrics with cone singularities along a divisor of bounded Ricci curvature} \author{Martin de Borbon} \date{DECEMBER, 2016} \begin{document} \begin{abstract} Let $D$ be a smooth divisor in a compact complex manifold $X$ and let $\beta \in (... |
| 5 | 0.726 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Openness of coercivity > Convexity of K-energy with mixed cusp and conic singularities | lines 1501-1506 | no | yes | conic, cone angle | \subsection{Convexity of K-energy with mixed cusp and conic singularities} Consider the case where $\chi$ is the current of integration along a simple normal crossing divisor $D=\sum_{i=1}^k D_i + \sum_{j=k+1}^N (1-\alpha_j)D_j$ where the first $k$ components $D_1,\ldots,D_k$ have coefficient $1$ (corresponding to cusp singularities with cone angle $0$), and... |
| 6 | 0.708 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction > Openness of coercivity | lines 698-700 | no | yes | conic, cone angle | \begin{cor}[Openness of existence of conic cscK metrics]\label{cor:openness-conic-cscK} Let $D$ be a smooth divisor and assume that $X$ admits no nonzero holomorphic vector field preserving $D$. If $[\om]$ admits a cscK cone metric with cone angle $\alpha_0 \in (0,1)$, then there exists a neighborhood $\mathcal{U}$ of $\alpha_0$ in $(0,1)$ such that $[\om]$... |
| 7 | 0.559 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Conjectural picture | lines 679-684 | no | yes | cone angle | Note that if $\beta=\nu^{-1}$ for an integer $\nu$, our metrics with cone singularities are {\it orbifold} metrics, so a great deal of standard theory can be brought to bear. See the recent work \cite{kn:RT} of Ross and Thomas, for example. \ Suppose that we are in a case when solutions exist for small cone angles but not for cone angles close to $1$. We wou... |
| 8 | 0.551 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction > K-stability and K\"ahler-Einstein metrics | lines 195-198 | no | yes | cone angle | \subsection{K-stability and K\"ahler-Einstein metrics} There has been much recent work on the study of K\"ahler-Einstein metrics with cone angles along a divisor \cite{D3}. Indeed, in the solution of the Yau-Tian-Donaldson conjecture when $L=-K_X$, an important feature was the use of the \emph{Donaldson continuity method} \begin{equation}\label{doncont}\Ric... |
| 9 | 0.531 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Introduction | lines 247-288 | yes | yes | conic, cone angle | \section{Introduction} Let $\D\subset M$ be a smooth divisor in a compact \K manifold. A \K edge metric on $M$ with angle $2\pi \be$ along $\D$ is a \K metric on $\MsmD$ that is asymptotically equivalent at $\D$ to the model edge metric $$ g_\be:=\|z_1\|^{2\be-2}\|dz_1\|^2 + \sum_{j=2}^n \|dz_j\|^2; $$ here $z_1,z_2,\ldots,z_n$ are holomorphic coordinates such tha... |
| 10 | 0.486 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `remark` | Introduction and the statement of the results > K\"ahler metrics with cone singularities along a divisor and log $K$-stability | lines 279-287 | yes | no | conic | \begin{remark} There are several important points when we consider cscK metrics with cone singularities in $c_1(L)$, which we list as follows. \begin{enumerate} \item Unlike in the Fano case where $D \in \|- \lambda K_X\|$ for some $\lambda \in \mathbb{N}$ is natural, $D$ and $L$ can be chosen completely independently; $D$ can be any smooth effective divisor i... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_011 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss gluing constructions for cscK metrics of Poincare type?

**Expected sources:** `2405.11952`
**Expected chunk types:** `theorem`, `proposition`, `proof`, `text`
**Expected terms:** `gluing`, `cscK`, `Poincare type`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.688 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | no | yes | cscK | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 2 | 0.613 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 22-35 | yes | yes | cscK | ...tion} \begingroup \raggedright Let $X$ be a compact K\"ahler manifold endowed with a constant scalar curvature K\"ahler(cscK) metric $\omega_X$, and assume it admits no non-trivial holomorphic vector field. In this article, we aim at constructing complete cscK metrics on the complement of finitely many points in $X$, which exhibit Poincar\'e type singularity... |
| 3 | 0.591 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | no | no | cscK | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |
| 4 | 0.582 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 145-159 | no | yes | cscK | This paper is organized as follows. In Section 2, we recall the definitions of {\kah} metrics of Poincar\'{e}/cone singularities. In addition, we define a background {\kah} metric with cone singularities, which converges to a cscK metric of Poincar\'{e} type. Finally, we consider a fixed point formula on the weighted {\hol} space, which characterizing a cscK... |
| 5 | 0.365 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | cscK | ...phic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelia... |
| 6 | 0.360 | `corpus/arxiv/math_0511118/source/source.tex` | `text` | unsectioned | lines 119-165 | no | yes | - | ...rfaces, every K\"ahler class is admissible. In particular, our results complete the classification of extremal K\"ahler metrics on geometrically ruled surfaces, answering several long-standing questions. We also find that our characterization agrees with a notion of K-stability for admissible K\"ahler classes. Our examples and nonexistence results therefore... |
| 7 | 0.353 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | unsectioned | lines 162-212 | no | yes | cscK | ...equence has a subsequence that converges in a weak sense. In~\cite{Don05_1} Donaldson proved interior estimates for the cscK equation for toric surfaces. Unfortunately recent examples in~\cite{ACGT3} show that positivity of the Futaki invariant for algebraic test-configurations may not be enough to ensure the existence of a cscK metric. One approach suggeste... |
| 8 | 0.351 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction > Applications and examples of twisted cscK metrics | line 162 | no | yes | cscK | The twisted cscK equation $$S(\omega) - \Lambda_{\omega} \alpha = C_{\alpha}$$ appears in many constructions of cscK metrics. The original, and perhaps most important, use of twisted cscK case is in the construction of K\"ahler-Einstein metrics. Here one takes $L$ to be the anti-canonical bundle of $X$ and looks for solutions to the \emph{twisted K\"ahler-Ei... |
| 9 | 0.346 | `corpus/my_notes/project_paper_index.md` | `text` | Project Paper Index > Poincare, Cusp, And Cone Metrics | lines 199-255 | no | yes | gluing, cscK | ## Poincare, Cusp, And Cone Metrics - Hugues Auvray, "Asymptotic properties of extremal Kähler metrics of Poincaré type". arXiv: https://arxiv.org/abs/1401.0123 Local: `corpus/arxiv/1401.0123` Role: asymptotic analysis for Poincare-type extremal metrics. - Hugues Auvray, "Note on Poincaré type Kähler metrics and Futaki characters". arXiv: https://arxiv.org/a... |
| 10 | 0.344 | `corpus/arxiv/1401.0123/source/ExtPK.tex` | `text` | Introduction | lines 290-336 | no | yes | - | ~ Theorem \ref{thm_mainthm1} states that extremal K�hler metrics of Poincar� type are \textit{asymptotically products} near the divisor. Similar results for K�hler-Einstein metrics were already known \cite{sch,wu}; these previous approaches differ fundamentally to ours though. Indeed, in that case, the K�hler-Einstein analogue of Theorem \ref{thm_mainthm2} f... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_012 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss asymptotics of scalar curvature for Poincare type metrics?

**Expected sources:** `1711.08424`, `1205.0056`, `1401.0123`
**Expected chunk types:** `proposition`, `lemma`, `proof`, `text`
**Expected terms:** `scalar curvature`, `asymptotics`, `Poincare`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.699 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | no | yes | scalar curvature | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 2 | 0.624 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Appendix > Curvature decomposition of Poincar\'e type metrics | lines 2321-2324 | no | yes | Poincare | \subsection{Curvature decomposition of Poincar\'e type metrics}\label{sec:poincare-curvature} In this appendix, we establish the curvature decomposition formula for Poincar\'e type metrics that is used throughout the paper. The main result (Corollary~\ref{decomp}) shows that the Ricci curvature of a Poincar\'e type metric decomposes into a smooth part, a log... |
| 3 | 0.622 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 22-35 | no | yes | scalar curvature | \section{Introduction} \begingroup \raggedright Let $X$ be a compact K\"ahler manifold endowed with a constant scalar curvature K\"ahler(cscK) metric $\omega_X$, and assume it admits no non-trivial holomorphic vector field. In this article, we aim at constructing complete cscK metrics on the complement of finitely many points in $X$, which exhibit Poincar\'e... |
| 4 | 0.591 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2786-2791 | yes | yes | Poincare | \subsection{The proof of Corollary~\ref{Hirzebruch-non-poincare}} The missing component in the proof is to show that the extremal metrics obtained cannot be of Poincar\'e type. For this we will show that in the above situation, the necessary condition in equation~\eqref{hyperbolicity-condition} for the existence of a toric extremal metric of Poincar\'e type... |
| 5 | 0.476 | `corpus/arxiv/1401.0123/source/ExtPK.tex` | `text` | Introduction | lines 290-336 | yes | yes | scalar curvature, asymptotics | ~ Theorem \ref{thm_mainthm1} states that extremal K�hler metrics of Poincar� type are \textit{asymptotically products} near the divisor. Similar results for K�hler-Einstein metrics were already known \cite{sch,wu}; these previous approaches differ fundamentally to ours though. Indeed, in that case, the K�hler-Einstein analogue of Theorem \ref{thm_mainthm2} f... |
| 6 | 0.569 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Momentum construction of scalar-flat K\"ahler metric | lines 157-160 | no | yes | - | \section{Momentum construction of scalar-flat K\"ahler metric}\label{section 2} In this section, we discuss how the momentum construction in \cite{HS02} gives rise to the cuspidal SFK metric on the punctured line bundle $\mathcal{O}(-1)^*$ appeared in the introduction. Let $p: (L, h)\rightarrow (M^m,\omega_M)$ be an Hermitian holomorphic line bundle with cur... |
| 7 | 0.397 | `corpus/arxiv/1401.0128/source/Note_PKFutaki.tex` | `text` | Introduction | lines 359-410 | no | yes | scalar curvature | An extremal metrics is a K�hler metrics such that the Riemannian gradient of its scalar curvature is holomorphic. Constraint \eqref{eqn_constraint} is a reformulation of that of \cite[Prop.4.5]{auv3}, and as such, extends that on the existence of constant scalar curvature metrics in $\mathscr{M}^{D}_{[\omega_X]}$ of \cite{auv2}, which states as: $\sbar^D< \s... |
| 8 | 0.392 | `corpus/arxiv/1512.06391/source/source.tex` | `text` | A Futaki invariant > The Futaki invariant for a K\"ahler class | lines 351-355 | no | yes | scalar curvature | ...tric ${\tilde g}_{\omega}(X,Y) = \frac{1}{f_{K, \omega, a}^2} \omega(X, JY)$ is Einstein--Maxwell? \end{problem} By the discussion in the previous section, we are looking for metrics $\omega \in \mathcal{K}_{\Omega}^G$ such that the corresponding scalar curvature of $\tilde g$ |
| 9 | 0.371 | `corpus/arxiv/1712.06697/source/source.tex` | `text` | unsectioned | lines 111-155 | no | yes | scalar curvature | ...xtra space built in, we don't call it with argument %% 2 for doublespacing, but instead by the following chart: %% 10pt type \spacing{1.67} %% 11pt type \spacing{1.62} %% 12pt type \spacing{1.66} %% To return to normal spacing, use \spacing{1} \begin{document} % PLUS THE \end COMMAND AT THE END. \newcommand{\avint}{{- \hspace{-3.5mm} \int}} \spacing{1} %----... |
| 10 | 0.367 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | scalar curvature | ...ef\cs{$\clubsuit$} % Tamas' comments \title{Tian's properness conjectures and Finsler geometry of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{document} \maketitle \begin{abstract} Well-known conjectures of Tian predict t... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_013 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss Poincare type metrics near a smooth divisor?

**Expected sources:** `1205.0056`, `1401.0123`
**Expected chunk types:** `definition`, `lemma`, `text`
**Expected terms:** `smooth divisor`, `Poincare type`, `Kahler metric`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.921 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Appendix > Curvature decomposition of Poincar\'e type metrics | lines 2321-2324 | no | yes | - | \subsection{Curvature decomposition of Poincar\'e type metrics}\label{sec:poincare-curvature} In this appendix, we establish the curvature decomposition formula for Poincar\'e type metrics that is used throughout the paper. The main result (Corollary~\ref{decomp}) shows that the Ricci curvature of a Poincar\'e type metric decomposes into a smooth part, a log... |
| 2 | 0.712 | `corpus/arxiv/1401.0123/source/ExtPK.tex` | `text` | Introduction | lines 263-266 | yes | yes | - | Notice that this definition allows a rather loose behaviour near the divisor, in the sense that one can easily produce Poincar� type metrics such that their restrictions to directions parallel to the divisor \textit{does not} converge near the divisor. Our first main result states nonetheless that such a convergence does occur for extremal Poincar� type K�hl... |
| 3 | 0.628 | `corpus/arxiv/math_0611002/source/thesis.tex` | `definition` | K-stability > K-stability of a pair $(V,D)$ | lines 1938-1950 | no | yes | - | \begin{defn}\label{defn:cuspsing} A complete K\"ahler metric $g$ on $V\setminus D$ is \emph{asymptotically hyperbolic near $D$} if near $D$ it is asymptotic to a metric of the form \[ g_0 = K\cdot\frac{\|dz\|^2}{(\|z\|\log \|z\|)^2}+h,\] where $K$ is a smooth positive function on $V$, the symmetric 2-tensor $h$ is a smooth extension of a metric on $D$, and $z$ is... |
| 4 | 0.626 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Theorem~\ref{thm:criterion} and Proposition~\ref{complete-first-order} > Proof of Theorem~\ref{thm:criterion} | lines 2253-2262 | no | yes | - | for $w(x)$ defined in \eqref{w}. Thus, $W(\zeta)$ is a smooth function near $0$. A similar (and well-established) argument using $u_0$ instead of $u$ shows that $\varphi_{u_0}$ can be viewed as a smooth function $\psi_0(z)$ on $\C^n_v$, so that the relative potential $\varphi(z)$ in \eqref{phi} is written as $$\varphi(z) = - \alpha \log\big(-\log\|z_1\|\big) +... |
| 5 | 0.499 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 128-143 | no | yes | - | ...seen from \cite{Auv14} Theorem 4, is a necessary condition for the existence of extremal K\"ahler metric of Poincar\'e type in the given K\"ahler class (\ref{Kahler class with ai}). \paragraph{Strategy of the proof and Outline of the article} \begin{itemize} \item To prepare ourselves with the construction, we recap the momentum construction of Hwang-Singer... |
| 6 | 0.611 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `definition` | Introduction | lines 193-205 | no | yes | - | \begin{defn}\label{d:Poincare-type} Let $Z \subset X$ be a simple normal crossing divisor in a compact complex $n$-dimensional K\"ahler manifold $(X, \omega_0)$. A K\"ahler metric $\omega$ on $X\setminus Z$ is said to be of {\it Poincar\'e type of class $[\omega_0]$} if \begin{enumerate} \item[$\bullet$] On any open subset $U\subset X$ with holomorphic coord... |
| 7 | 0.583 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `proof` | Appendix > The Log-Mabuchi energy of Poincar\'e type K\"ahler metrics > Potential space of Poincar\'e type K\"ahler metrics | lines 2011-2028 | no | no | - | ...lume follows from an elementary calculation in local coordinates. Without loss of generality, we may assume that $D$ is smooth and is defined by $\{z_1=0\}$ in a local chart $(z_1,\ldots,z_n)$. By the asymptotic behavior of Poincar\'e type metrics (Definition~\ref{def: poincaretypemetdefn}), the volume form satisfies \begin{equation}\label{eq:MA-asymptotic}... |
| 8 | 0.460 | `corpus/arxiv/1401.0128/source/Note_PKFutaki.tex` | `text` | Introduction | lines 359-410 | no | yes | smooth divisor | An extremal metrics is a K�hler metrics such that the Riemannian gradient of its scalar curvature is holomorphic. Constraint \eqref{eqn_constraint} is a reformulation of that of \cite[Prop.4.5]{auv3}, and as such, extends that on the existence of constant scalar curvature metrics in $\mathscr{M}^{D}_{[\omega_X]}$ of \cite{auv2}, which states as: $\sbar^D< \s... |
| 9 | 0.565 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `proposition` | Appendix > Curvature decomposition of Poincar\'e type metrics | lines 2356-2372 | no | no | - | \begin{prop}[A Variant of the Poincar\'e-Lelong Formula]\label{PoincareLelong} Let \((X, \omega)\) be a K\"ahler manifold. Let \(g\) be a smooth function on \(X \setminus D\). For any holomorphic chart \(U\) near the divisor \(D\) where \(D_{\text{smooth}} \cap U = \{z_1 = 0\}\), assume the following conditions hold: \[ \lim_{z_1 \to 0} \left\|z_1 \frac{\part... |
| 10 | 0.446 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | no | yes | - | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_014 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss complete Kahler metrics on divisor complements?

**Expected sources:** `1205.0056`, `1711.08424`
**Expected chunk types:** `definition`, `theorem`, `text`
**Expected terms:** `complete Kahler`, `divisor complement`, `Poincare`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.558 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | no | yes | - | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 2 | 0.515 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted cscK problem on semisimple principal fibration | lines 2104-2110 | no | yes | - | Also, from \cite[Section 5]{AJL}, any Kähler metric \(\omega\) on \(X\) induces a Kähler metric \(\tilde{\omega}\) on \(Y\) such that the restriction \((Y_b, \tilde{\omega}_b)\) of \((Y, \tilde{\omega})\) to a fiber over a point \(b \in B\) is \(\T\)-equivariantly Kähler isomorphic to \((X, \omega)\). Such a metric \(\tilde{\omega}\) on \(Y\) is the \emph{co... |
| 3 | 0.417 | `corpus/my_notes/requested_non_arxiv_sources.md` | `text` | Requested non-arXiv and correction pointers > Journal-only or correction pointers | lines 7-23 | no | yes | complete Kahler | ...- Sebastien Boucksom, Tomoyuki Hisamoto, Mattias Jonsson, "Uniform K-stability and asymptotics of energy functionals in Kahler geometry", JEMS 21 (2019), 2905-2944. ArXiv source in corpus: `corpus/arxiv/1603.01026`. EMS page with correction pointer: https://ems.press/journals/jems/articles/16240 Local status: arXiv paper downloaded; correction pointer record... |
| 4 | 0.411 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Introduction | lines 168-192 | yes | yes | - | \section{Introduction} In this article, we are interested in the study of (non-compact) complete extremal K\"ahler metrics, defined on the complement of a simple normal crossing divisor $Z$ in an $n$-dimensional K\"ahler manifold $X$. Such metrics naturally appear (see e.g. \cite{Do2}) in attempts to apply continuity methods, or to study global properties of... |
| 5 | 0.400 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | ...veral questions : \begin{enumerate} \item Do all crystallographic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enume... |
| 6 | 0.390 | `corpus/arxiv/1401.0123/source/ExtPK.tex` | `text` | Introduction | lines 263-266 | no | yes | - | Notice that this definition allows a rather loose behaviour near the divisor, in the sense that one can easily produce Poincar� type metrics such that their restrictions to directions parallel to the divisor \textit{does not} converge near the divisor. Our first main result states nonetheless that such a convergence does occur for extremal Poincar� type K�hl... |
| 7 | 0.376 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | K-stability > K-stability of a pair $(V,D)$ | lines 1921-1937 | no | yes | - | ...we propose a definition of K-stability for a pair $(V,D)$ consisting of a smooth polarised variety $(V,L)$ and a smooth divisor $D\subset V$. The aim is to find a stability condition for the existence of a complete extremal metric on $V\setminus D$ which is asymptotically hyperbolic near $D$. A well-known case is the polarisation $K_V+D$, where $K_V$ is the... |
| 8 | 0.372 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | - | ...ef\cs{$\clubsuit$} % Tamas' comments \title{Tian's properness conjectures and Finsler geometry of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{document} \maketitle \begin{abstract} Well-known conjectures of Tian predict t... |
| 9 | 0.363 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Introduction | lines 247-288 | no | yes | - | \section{Introduction} Let $\D\subset M$ be a smooth divisor in a compact \K manifold. A \K edge metric on $M$ with angle $2\pi \be$ along $\D$ is a \K metric on $\MsmD$ that is asymptotically equivalent at $\D$ to the model edge metric $$ g_\be:=\|z_1\|^{2\be-2}\|dz_1\|^2 + \sum_{j=2}^n \|dz_j\|^2; $$ here $z_1,z_2,\ldots,z_n$ are holomorphic coordinates such tha... |
| 10 | 0.361 | `corpus/arxiv/0805.0128/source/extremal2a.tex` | `text` | Introduction | lines 219-255 | no | yes | - | ...h an understanding of what goes wrong when the positivity hypothesis is violated. Section 6 is a supplement in which we discuss an explicit family of complete zero scalar curvature metrics, generalising the Taub-NUT metric, and explain that these can be expected to arise as blow-up limits of solutions. We also discuss briefly the connection with \lq\lq colla... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_015 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss cusp limits of conic cscK metrics?

**Expected sources:** `2210.11862`, `1803.09506`, `2410.14130`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `cusp limit`, `conic`, `cscK`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.525 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 128-143 | no | yes | conic, cscK | ...begin{itemize} \item To prepare ourselves with the construction, we recap the momentum construction of Hwang-Singer and discuss the derivation of the desired complete cuspidal SFK metric $\omega_{HS}$ in Section \ref{section 2}. Besides, we introduce the conical family of scalar-flat K\"ahler metrics connecting the Burns-Simanca metric and the cuspidal metri... |
| 2 | 0.513 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Introduction | lines 106-118 | no | yes | conic, cscK | ...s unique up to holomorphic automorphisms in 1980s. Recently, Berndtsson \cite{Bo} generalized this uniqueness result to conic K\"ahler-Einstein metrics on Fano manifolds, by his observation on the convexity of certain energy functional (the $Ding$-functional) along geodesics in the space of all K\"ahler potentials. And Berndtsson's method is further generali... |
| 3 | 0.502 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction > Openness of coercivity | lines 701-703 | no | yes | conic | More significantly, our framework allows us to deduce existence of small-angle conic metrics from coercivity at the cusp (Poincar\'e) limit. |
| 4 | 0.473 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | cscK | ...phic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelia... |
| 5 | 0.468 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `text` | Introduction and the statement of the results > Log Futaki invariant computed with respect to the conically singular metrics | lines 369-370 | no | yes | conic, cscK | \subsection{Log Futaki invariant computed with respect to the conically singular metrics} \label{intscmsfi} Although the log Futaki invariant is conjectured to be related to the existence of conically singular cscK metrics, the log Futaki invariant itself is computed with respect to a \textit{smooth} \kah metric in $c_1 (L)$. We now consider the following qu... |
| 6 | 0.467 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | yes | yes | cscK | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 7 | 0.464 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | yes | no | cscK | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |
| 8 | 0.450 | `corpus/arxiv/0805.0128/source/extremal2a.tex` | `text` | Introduction | lines 219-255 | no | yes | - | ...s on the results, are related to our lack of understanding of this basic local question---what are the possible $C^{0}$ limits of solutions to the equation (1)? \ The main work of this paper finishes in Section 5. However, it is interesting to complement the existence proofs with an understanding of what goes wrong when the positivity hypothesis is violated.... |
| 9 | 0.429 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | yes | cscK | ...ction defined on the sphere of infinity ${\mathcal S}_\infty.$ One important technical ingredient to prove existence of cscK from geodesic stability is the following properness theorem, which says that if $K$-energy is ``proper" with respect to a suitably defined distance (defined precisely in Definition \ref{d1.1} below), then cscK exists. To extend the pro... |
| 10 | 0.425 | `corpus/arxiv/1712.06697/source/source.tex` | `remark` | Introduction | lines 266-269 | no | no | cscK | \begin{rem} In Theorem \ref{t1.1} and the first part of Theorem \ref{t1.2}, it is sufficient to assume that $\varphi$ remains bounded under $L^1$ geodesic distance, due to the fact that cscK metrics are minimizers of $K$-energy. We will discuss this matter in more detail in our next paper of the series. \end{rem} |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_016 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss Poincare type K-energy or Mabuchi functional on noncompact complements?

**Expected sources:** `1205.0056`, `1401.0123`, `2410.14130`
**Expected chunk types:** `definition`, `proposition`, `text`
**Expected terms:** `K-energy`, `Mabuchi`, `Poincare`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.837 | `corpus/arxiv/1603.01026/source/source.tex` | `text` | Test configurations as non-Archimedean metrics > Functionals on non-Archimedean metrics | lines 1232-1233 | no | yes | K-energy, Mabuchi | \item[(v)] The \emph{non-Archimedean Mabuchi functional} (or K-energy) is |
| 2 | 0.815 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction | lines 649-651 | no | no | K-energy, Mabuchi | \begin{cor}[Weighted K-energy convexity for mixed cusp and conic singularities, see Corollary \ref{prop:extention-K-energy-divisor}]\label{cor:mixed-singularities} The weighted twisted Mabuchi functional $\cM_{v,\mathrm{w}}^{2\pi[D]}$ for mixed cusp/conic divisors admits a unique greatest lower semicontinuous extension to $\cET(X, \omega)$, that is moreover... |
| 3 | 0.797 | `corpus/arxiv/1610.07998/source/source.tex` | `theorem` | Introduction | lines 303-305 | no | no | K-energy | \begin{thmC} If K-energy functional is G-coercive, then the polarized manifold is uniformly K-stable for $G$. \end{thmC} |
| 4 | 0.743 | `corpus/arxiv/1509.04561/source/source.tex` | `example` | Twisted K\"ahler--Einstein currents and coercivity > The coercivity criterion | lines 1059-1060 | no | no | K-energy, Mabuchi | \begin{exam} The dichotomy (a)--(b) applies in particular to the Mabuchi K-energy functional of any compact K\"ahler manifold, which is geodesically convex by~\cite{BB17,CLP,BDL}, and has entropy growth by Example~\ref{exam:Mab}. \end{exam} |
| 5 | 0.740 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Background materials > $d_{1}$-distances, reduced $d_{1}$-distances and the reduced J-functionals | line 644 | no | yes | K-energy | We say that the relative K-energy is $T$-coercive if $M_{V}$ satisfies the condition (2) and (or) (3) in Theorem \ref{ext_coer_equiv}. |
| 6 | 0.727 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | The uniform estimate in the positive case > Mabuchi's K-energy and Tian's invariants | lines 2854-2858 | no | yes | K-energy, Mabuchi | \subsection{Mabuchi's K-energy and Tian's invariants} \label{TianMabuchiSubSec} Define the twisted Mabuchi K-energy functional by integration over paths $\{\o_{\vp_t}\}\subset \calH_{\o_0}$ smooth in $t$, |
| 7 | 0.723 | `corpus/arxiv/1801.05907/source/source.tex` | `theorem` | Introduction | lines 303-304 | no | no | - | \begin{thm}\label{t1.1}(Theorem \ref{t3.1}) There exists a constant scalar curvature K\"ahler metric if and only if the K energy functional is proper with respect to the $L^1$ distance modulo $G$. \end{thm} |
| 8 | 0.797 | `corpus/arxiv/1610.07998/source/source.tex` | `theorem` | Remarks about stability and coercivity in the general setting | lines 1238-1240 | no | no | K-energy | \begin{thm} If K-energy functional is G-coercive, then the polarized manifold is uniformly K-stable for $G$. \end{thm} |
| 9 | 0.617 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | K-energy, Mabuchi | ...s of Tian predict that existence of canonical K\"ahler metrics should be equivalent to various notions of properness of Mabuchi's K-energy functional. In some instances this has been verified, especially under restrictive assumptions on the automorphism group. We provide counterexamples to the original conjecture in the presence of continuous automorphisms.... |
| 10 | 0.724 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Background materials > Energy functionals | lines 465-466 | no | yes | K-energy | In other word, the K-energy functional is the integration of the Futaki invariant. \item For a smooth geodesic $\{\varphi^{t}\}$ in $\mathcal{H}_{0}^{S}$ we have |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_017 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss extremal vector fields for Poincare type metrics?

**Expected sources:** `1401.0123`, `1711.08424`
**Expected chunk types:** `definition`, `proposition`, `text`
**Expected terms:** `extremal vector field`, `Poincare`, `Futaki`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.778 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2786-2791 | yes | yes | Poincare | \subsection{The proof of Corollary~\ref{Hirzebruch-non-poincare}} The missing component in the proof is to show that the extremal metrics obtained cannot be of Poincar\'e type. For this we will show that in the above situation, the necessary condition in equation~\eqref{hyperbolicity-condition} for the existence of a toric extremal metric of Poincar\'e type... |
| 2 | 0.617 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | no | yes | - | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 3 | 0.553 | `corpus/arxiv/1401.0128/source/Note_PKFutaki.tex` | `text` | Introduction | lines 359-410 | no | yes | Futaki | An extremal metrics is a K�hler metrics such that the Riemannian gradient of its scalar curvature is holomorphic. Constraint \eqref{eqn_constraint} is a reformulation of that of \cite[Prop.4.5]{auv3}, and as such, extends that on the existence of constant scalar curvature metrics in $\mathscr{M}^{D}_{[\omega_X]}$ of \cite{auv2}, which states as: $\sbar^D< \s... |
| 4 | 0.526 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 113-119 | no | yes | extremal vector field, Futaki | The \textbf{\textit{extremal vector field}} for the Poincar\'e type K\"ahler metric setting is defined using the Futaki character introduced in \cite{Auv13-2}, and we will discuss in more detail in Section~\ref{subsection 9.3}. Here, we just mention that it is a holomorphic vector field depending only on the K\"ahler class and maximal compact subgroup $K$. F... |
| 5 | 0.647 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2847-2852 | yes | yes | Poincare | ...finity section in $X$. This is already treated in Corollary~\ref{Hirzebruch} where we know that there exists Poincar\'e type extremal metrics. The above computations then confirm that the condition of equation~\eqref{hyperbolicity-condition} holds, which we also know by general theory regarding extremal Poincar\'e type metrics. To prove Corollary~\ref{Hirzeb... |
| 6 | 0.446 | `corpus/arxiv/1401.0123/source/ExtPK.tex` | `text` | Introduction | lines 263-266 | yes | yes | - | ...hat this definition allows a rather loose behaviour near the divisor, in the sense that one can easily produce Poincar� type metrics such that their restrictions to directions parallel to the divisor \textit{does not} converge near the divisor. Our first main result states nonetheless that such a convergence does occur for extremal Poincar� type K�hler metri... |
| 7 | 0.433 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Proofs of Lemmas \ref{s1is2}, \ref{s1is1} and \ref{s1is2overk} | lines 1659-1726 | no | yes | Futaki | ....~M.~J. Calderbank, P. Gauduchon and C. T{\o}nnesen-Friedman, {\it Hamiltonian $2$-forms in K\"ahler geometry} III {\it Extremal metrics and stability}, arXiv:math.DG/??????? \bibitem{Bando-Mabuchi} S. Bando and T. Mabuchi, {\it Uniqueness of Einstein--K\"ahler metrics modulo connected group actions}, in `Algebraic Geometry' (Sendai 1985), Adv. Stud. Pure Ma... |
| 8 | 0.418 | `corpus/arxiv/1302.6979/source/ambitoric2.tex` | `text` | Link with CR and sasakian $5$-manifolds | lines 2178-2194 | no | yes | - | .... In particular, quasiregular Sasaki--Einstein $5$-manifolds have K\"ahler--Einstein orbifolds as quotients by the Reeb vector field, and this provides one way of constructing them. As observed by D.~Martelli and J.~Sparks~\cite{Martelli-Sparks,Sparks}, the Sasaki--Einstein manifolds of J.~Gauntlett, D.~Martelli, J.~Sparks, D.~Waldram~\cite{GMSW} and M.~Cvet... |
| 9 | 0.413 | `corpus/arxiv/1302.6975/source/ambitoric1.tex` | `text` | Introduction | lines 153-216 | no | yes | - | ...s with general relativity and complex surface geometry. In relativity, analytic continuations of families of lorentzian metrics and/or their parameters yield riemannian ones~\cite{Berard-Bergery,Page}, while concepts and techniques in one area have analogues in the other. In complex geometry, E.~Calabi's extremal K\"ahler metrics~\cite{Cal1} have become a fo... |
| 10 | 0.405 | `corpus/arxiv/math_0202280/source/source.tex` | `text` | unsectioned | lines 164-214 | no | yes | - | ...K\"ahler metric has a hamiltonian $2$-form. From this we deduce a local classification of weakly Bochner-flat K\"ahler metrics, rederiving in particular Bryant's classification of Bochner-flat K\"ahler metrics. We also obtain a new proof of the Derdzi\'nski--Maschler classification of conformally Einstein K\"ahler metrics in higher dimensions, and an Ansatz... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_018 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss cscK metrics with edge or cone singularities along a divisor?

**Expected sources:** `1105.5216`, `1508.02640`, `1803.09506`
**Expected chunk types:** `theorem`, `definition`, `text`
**Expected terms:** `edge`, `cone singularities`, `divisor`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.836 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Preliminaries > {\kah} metrics with cone singularities | lines 241-248 | no | yes | cone singularities | \subsection{{\kah} metrics with cone singularities} In this subsection, we recall the definition of {\kah} metrics with cone singularities along $D$. In addition, we recall the definition of cscK metric with cone singularities along $D$. We take a real parameter $\beta \in (0,1]$. |
| 2 | 0.787 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction > Twisted and log K-stability | lines 199-200 | no | yes | cone singularities, divisor | ...wisting $T$ is precisely the log Donaldson-Futaki invariant for a general $D \in \|2T\|$. That the existence of a twisted cscK metric depends on an arbitrary choice of twisting $\alpha$ is analogous to the arbitrary choice of $D$ in the study of cscK metrics with cone singularities along a divisor. We relate the two notions of stability in Theorem \ref{logimpl... |
| 3 | 0.724 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `conjecture` | Log Futaki invariant and log $K$-stability > Log $K$-stability | lines 725-727 | yes | no | cone singularities | \begin{conjecture} \label{logdtyconj} $((X,D);L)$ is log $K$-polystable with cone angle $2 \pi \beta$ if and only if $X$ admits a cscK metric in $c_1(L)$ with cone singularities along $D$ with cone angle $2 \pi \beta$. \end{conjecture} |
| 4 | 0.723 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | A priori estimates | lines 2694-2698 | yes | yes | cone singularities | \section{A priori estimates}\label{a priori estimates} In this section, we derive the a priori estimates of the cscK metrics with both cone singularities and degeneration. |
| 5 | 0.568 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Introduction | lines 32-41 | no | yes | edge, cone singularities, divisor | \section{Introduction} Let $D$ be a smooth divisor in a complex manifold $X$. In this paper we study K\"ahler metrics on $X\setminus D$ with cone singularities of cone angle $2\pi \beta$ transverse to $D$, where $0<\beta<1$. The case we have primarily in mind is when $X$ is a Fano manifold, $D$ is an anticanonical divisor and the metrics are K\"ahler-Einstei... |
| 6 | 0.705 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `definition` | Introduction and the statement of the results > K\"ahler metrics with cone singularities along a divisor and log $K$-stability | lines 273-275 | yes | yes | cone singularities | \begin{definition} \label{defofcsckncpt} A \kah metric $\omega_{sing}$ with cone singularities along $D$ with cone angle $2 \pi \beta$ is said to be of \textbf{constant scalar curvature K\"ahler} or $\textbf{cscK}$ if its scalar curvature $S(\omega_{sing})$, which is a well-defined smooth function on $X \setminus D$, satisfies $S(\omega_{sing}) = \cst$ on $X... |
| 7 | 0.562 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Introduction | lines 247-288 | yes | yes | edge, divisor | \section{Introduction} Let $\D\subset M$ be a smooth divisor in a compact \K manifold. A \K edge metric on $M$ with angle $2\pi \be$ along $\D$ is a \K metric on $\MsmD$ that is asymptotically equivalent at $\D$ to the model edge metric $$ g_\be:=\|z_1\|^{2\be-2}\|dz_1\|^2 + \sum_{j=2}^n \|dz_j\|^2; $$ here $z_1,z_2,\ldots,z_n$ are holomorphic coordinates such tha... |
| 8 | 0.688 | `corpus/arxiv/1803.09506/source/source.tex` | `definition` | CscK cone path | lines 4524-4526 | yes | yes | divisor | \begin{defn}\label{cscK cone path defn} We say the path $\{\om_{\varphi^\beta}=\om_0+i\p\bar \p\varphi^\beta ;0< \beta\leq 1\} $ is a cscK cone path, if $\om_{\varphi^\beta}$ is a cscK cone metric with cone angle $\beta$ along the smooth divisor $D$. \end{defn} |
| 9 | 0.659 | `corpus/arxiv/1803.09506/source/source.tex` | `theorem` | CscK cone path > Deform cone angle of the cscK cone path | lines 4555-4558 | yes | yes | divisor | \begin{thm}\label{openess} Assume that $Aut(X;D)$ is discrete and $C_1(L_D)> 0$. The cscK cone path is open when $\beta>0$. Precisely, if $\om_{\varphi^{\beta_0}}$ is a cscK cone metric with cone angle $\beta_0\in (0,1)$ along the smooth divisor $D$, then there is a $\delta>0$ such that for all $\beta\in (\beta_0-\delta,\beta_0+\delta)$, there exists a cscK... |
| 10 | 0.460 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | K-stability > K-stability of a pair $(V,D)$ | lines 2016-2064 | no | yes | edge, divisor | Let us briefly explain the last condition. In Section~\ref{sec:extremalruled} we will construct complete extremal metrics on the complement of a divisor on a ruled surface, and we will find that for a range of polarisations $m<k_2$ (where $m$ parametrises the polarisation and $k_2$ is a constant - see Section~\ref{sec:extremalruled} for details) we obtain me... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_019 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss analytic estimates for conic or Poincare type cscK metrics?

**Expected sources:** `1803.09506`, `2210.11862`, `2410.14130`
**Expected chunk types:** `theorem`, `lemma`, `proof`
**Expected terms:** `estimates`, `conic`, `Poincare type`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.668 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | yes | no | - | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 2 | 0.647 | `corpus/arxiv/1803.09506/source/source.tex` | `remark` | Introduction | lines 245-247 | yes | no | estimates, conic | \begin{rem} These estimates are also obtained for cscK cone metric by directly making use of the conical background metric as shown in \cite{arXiv:1805.04944}, which are considered to be the limit of \thmref{A priori estimates}. \end{rem} |
| 3 | 0.632 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 81-91 | no | no | conic | ...$[E_i]$ denotes the Poincar\'e dual of the $E_i$. Our main theorem adds new examples to the existing list of Poincar\'e type metrics. We recall here some important examples: (a) the K\"ahler-Einstein metrics of Poincar\'e type, whose existence were shown by Tian-Yau \cite{TY87}, Kobayashi \cite{Kob84} and Cheng-Yau \cite{CY80}; (b) the toric extremal K\"ahle... |
| 4 | 0.600 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction > Openness of coercivity | lines 701-703 | no | no | conic | More significantly, our framework allows us to deduce existence of small-angle conic metrics from coercivity at the cusp (Poincar\'e) limit. |
| 5 | 0.463 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | no | - | In the intriguing paper \cite{Ross11}, the authors defined a notion of analytic test configurations which is an one-parameter family of K\"ahler potentials, concave with respect to this parameter. They proved that each analytic test configuration defines a unique geodesic ray (up to parallelism), thus defines a point at ${\mathcal S}_\infty.$ It is important... |
| 6 | 0.427 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `text` | Introduction and the statement of the results > Log Futaki invariant computed with respect to the conically singular metrics | lines 369-370 | no | no | conic | \subsection{Log Futaki invariant computed with respect to the conically singular metrics} \label{intscmsfi} Although the log Futaki invariant is conjectured to be related to the existence of conically singular cscK metrics, the log Futaki invariant itself is computed with respect to a \textit{smooth} \kah metric in $c_1 (L)$. We now consider the following qu... |
| 7 | 0.424 | `corpus/arxiv/1712.06697/source/source.tex` | `text` | Introduction | lines 156-166 | no | no | estimates, conic | ...ction{Introduction} This is the first of a series of three papers in the study of of constant scalar curvature K\"ahler metrics (cscK metrics), following a program outlined in \cite{chen15}. In this paper, we focus on establishing a priori estimates for cscK metrics in compact K\"ahler manifold without boundary. Our estimates can be easily adapted to extrema... |
| 8 | 0.411 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Preliminaries > More functionals | lines 1285-1287 | no | no | - | %By proving Theorem \ref{thm-Echislope}, we will show that this is well-defined and does not depend on the choice of the decreasing sequence $\Phi_m$. The constant scalar curvature K\"{a}hler metrics are global minimizers of Mabuchi functional $\bfM(\vphi)$. We now have the following important analytic criterion for the existence of cscK metrics: |
| 9 | 0.398 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Introduction | lines 106-118 | no | no | conic | ...s unique up to holomorphic automorphisms in 1980s. Recently, Berndtsson \cite{Bo} generalized this uniqueness result to conic K\"ahler-Einstein metrics on Fano manifolds, by his observation on the convexity of certain energy functional (the $Ding$-functional) along geodesics in the space of all K\"ahler potentials. And Berndtsson's method is further generali... |
| 10 | 0.396 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Linear analysis | lines 1203-1232 | no | no | estimates | ...s about the linear elliptic theory needed to handle the existence, deformation and regularity theory for canonical edge metrics. We discuss this from two points of view, reviewing the estimates obtained by Donaldson in the wedge H\"older spaces, and also describing how to obtain analogous estimates in the edge H\"older spaces. These latter estimates are obta... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_020 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss the logarithmic or cusp boundary behavior of potentials?

**Expected sources:** `1205.0056`, `1711.08424`, `2210.11862`
**Expected chunk types:** `definition`, `lemma`, `text`
**Expected terms:** `logarithmic`, `cusp`, `potential`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.974 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Appendix > Curvature decomposition of Poincar\'e type metrics | lines 2321-2324 | no | yes | logarithmic | ...lt (Corollary~\ref{decomp}) shows that the Ricci curvature of a Poincar\'e type metric decomposes into a smooth part, a logarithmic part, and the divisor $[D]$. The key technical tool is a variant of the Poincar\'e-Lelong formula (Proposition~\ref{PoincareLelong}) adapted to functions with specific asymptotic behavior near the divisor, which we establish usi... |
| 2 | 0.818 | `corpus/my_notes/toric_manifolds_mixed_conic_cusp/notes/one_conic_point.tex` | `text` | \(\mathbb{CP}^1\) with one conic point: symplectic picture > Conic Guillemin condition | lines 16-23 | no | yes | logarithmic, potential | \subsection*{Conic Guillemin condition} A symplectic potential has the form \[ u(x)=\frac{1}{2\beta}(1+x)\log(1+x)+\frac12(1-x)\log(1-x)+h(x), \qquad h\in C^\infty. \] The logarithmic terms describe the boundary behavior, and the coefficient \(\beta^{-1}\) encodes the cone angle \(2\pi\beta\). |
| 3 | 0.781 | `corpus/arxiv/1008.2607/source/source.tex` | `text` | K\"{a}hler geometry on toric surfaces > The Legendre transformation, moment maps and potential functions | lines 505-507 | no | yes | - | Note that the first map is induced from \eqref{eqn_1.1a}. It is known that $u$ must satisfy certain behavior near boundary of $\Delta$. |
| 4 | 0.682 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Further study on the cuspidal scalar-flat K\"ahler metric | lines 354-362 | no | yes | cusp | for some $\varphi_2=O(\|z\|_h^{-2})$; near $E$, $$\omega_{HS}=\ddb\left(\log\|z\|_h^2-\log(\log2-\log\|z\|_h^2)+O\left(\frac{1}{\log\|z\|_h^2}\right)\right).$$ \paragraph{$\mathcal{O}(-k)$ case} We have studied the cuspidal metric on $\mathcal{O}(-1)^*$; in fact, similar behavior of the metric can be seen in $\mathcal{O}(-k)^*$ for $k>1$. Note |
| 5 | 0.618 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | It is an interesting question to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except i... |
| 6 | 0.695 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `lemma` | Appendix > The Log-Mabuchi energy of Poincar\'e type K\"ahler metrics > Potential space of Poincar\'e type K\"ahler metrics | lines 2091-2093 | no | yes | potential | \begin{lemma}\label{lem:poincare-E1} The space $\tmom$ of Poincar\'e type potentials is contained in the finite energy space $\mathcal{E}^1(X, \omega)$. \end{lemma} |
| 7 | 0.674 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Momentum construction of scalar-flat K\"ahler metric | lines 157-160 | no | yes | cusp | \section{Momentum construction of scalar-flat K\"ahler metric}\label{section 2} In this section, we discuss how the momentum construction in \cite{HS02} gives rise to the cuspidal SFK metric on the punctured line bundle $\mathcal{O}(-1)^*$ appeared in the introduction. Let $p: (L, h)\rightarrow (M^m,\omega_M)$ be an Hermitian holomorphic line bundle with cur... |
| 8 | 0.519 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | %\begin{q} There is a few open questions for the Calabi dream manifolds: %\begin{enumerate} %\item What linear combinations of Chern numbers are nonnegative for all Calabi dream manifolds? %\item In Corollary 1.7, can we extend it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic to... |
| 9 | 0.636 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Appendix > The Log-Mabuchi energy of Poincar\'e type K\"ahler metrics > Potential space of Poincar\'e type K\"ahler metrics | lines 1992-2006 | no | yes | potential | \noindent By Lemma \ref{lem:poincare-E1}, the space $\tmom$ of Poincar\'e type potentials is contained in the finite energy space $\mathcal{E}^1$. We denote $\tmom^T:= \tmom \cap \cET(X, \omega)$ the space of $T$-invariant Poincar\'e type K\"ahler potentials. Without loss of generality, we can assume that the K\"ahler metric $\om$ and the potential $\mathfra... |
| 10 | 0.508 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | A metric degeneration | lines 3218-3234 | no | yes | cusp, potential | ...etric degeneration}\label{sec:metricdegen} We will first construct a family of metrics on $\mathbf{P}^1$ using K\"ahler potentials, and then use their momentum profiles to define a sequence of metrics on a ruled manifold and we compute the asymptotic rate of change of the Mabuchi functional. We define the sequence using K\"ahler potentials on $\mathbf{C}\set... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_021 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss Poincare type cscK metrics in relation to automorphisms?

**Expected sources:** `2410.14130`, `1401.0123`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `automorphism`, `Poincare type`, `cscK`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.747 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | no | yes | cscK | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 2 | 0.701 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | no | no | cscK | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |
| 3 | 0.686 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 22-35 | no | yes | cscK | ...tion} \begingroup \raggedright Let $X$ be a compact K\"ahler manifold endowed with a constant scalar curvature K\"ahler(cscK) metric $\omega_X$, and assume it admits no non-trivial holomorphic vector field. In this article, we aim at constructing complete cscK metrics on the complement of finitely many points in $X$, which exhibit Poincar\'e type singularity... |
| 4 | 0.658 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 145-159 | no | yes | cscK | This paper is organized as follows. In Section 2, we recall the definitions of {\kah} metrics of Poincar\'{e}/cone singularities. In addition, we define a background {\kah} metric with cone singularities, which converges to a cscK metric of Poincar\'{e} type. Finally, we consider a fixed point formula on the weighted {\hol} space, which characterizing a cscK... |
| 5 | 0.518 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | automorphism | ...ef\cs{$\clubsuit$} % Tamas' comments \title{Tian's properness conjectures and Finsler geometry of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{document} \maketitle \begin{abstract} Well-known conjectures of Tian predict t... |
| 6 | 0.458 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | automorphism, cscK | ...phic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelia... |
| 7 | 0.451 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Introduction | lines 106-118 | no | yes | automorphism, cscK | ...ntroduction} Bando-Mabuchi \cite{BM} proved that K\"ahler-Einstein metric on Fano manifolds is unique up to holomorphic automorphisms in 1980s. Recently, Berndtsson \cite{Bo} generalized this uniqueness result to conic K\"ahler-Einstein metrics on Fano manifolds, by his observation on the convexity of certain energy functional (the $Ding$-functional) along g... |
| 8 | 0.425 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `text` | Introduction and the statement of the results > Log Futaki invariant computed with respect to the conically singular metrics | lines 369-370 | no | yes | cscK | \subsection{Log Futaki invariant computed with respect to the conically singular metrics} \label{intscmsfi} Although the log Futaki invariant is conjectured to be related to the existence of conically singular cscK metrics, the log Futaki invariant itself is computed with respect to a \textit{smooth} \kah metric in $c_1 (L)$. We now consider the following qu... |
| 9 | 0.423 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Introduction | lines 185-188 | yes | yes | cscK | ...to prove the convexity of the $K$-energy. Chen-Paun-Zeng used PDEs method in \cite{CPZ} to prove the uniqueness of the cscK metric and extremal K\"ahler metric. A natural question is: could we prove the uniqueness of cscK metric on more general K\"ahler manifolds? Note that the methods we mentioned above depend on the compactness of the manifold. As a resul... |
| 10 | 0.420 | `corpus/arxiv/1712.06697/source/source.tex` | `remark` | Introduction | lines 266-269 | no | no | cscK | \begin{rem} In Theorem \ref{t1.1} and the first part of Theorem \ref{t1.2}, it is sufficient to assume that $\varphi$ remains bounded under $L^1$ geodesic distance, due to the fact that cscK metrics are minimizers of $K$-energy. We will discuss this matter in more detail in our next paper of the series. \end{rem} |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_022 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss the modified scalar curvature equation for Poincare type extremal metrics?

**Expected sources:** `1711.08424`, `1401.0123`
**Expected chunk types:** `definition`, `proposition`, `text`
**Expected terms:** `modified scalar curvature`, `extremal`, `Poincare`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.785 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2786-2791 | yes | yes | extremal, Poincare | \subsection{The proof of Corollary~\ref{Hirzebruch-non-poincare}} The missing component in the proof is to show that the extremal metrics obtained cannot be of Poincar\'e type. For this we will show that in the above situation, the necessary condition in equation~\eqref{hyperbolicity-condition} for the existence of a toric extremal metric of Poincar\'e type... |
| 2 | 0.749 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | no | yes | extremal | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 3 | 0.607 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 652-659 | no | yes | extremal, Poincare | ...crossing divisors. More specifically, Xu \cite{Xu25} and Xu--Zheng \cite{Xu_Zheng25} established uniqueness results for extremal and cscK Poincar\'e-type metrics along smooth divisors, employing the convexity framework of Berman--Berndtsson \cite{BB} where applying a partition of unity involves subtleties near the divisor. In contrast, our approach leverages... |
| 4 | 0.647 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2847-2852 | yes | yes | extremal, Poincare | ...finity section in $X$. This is already treated in Corollary~\ref{Hirzebruch} where we know that there exists Poincar\'e type extremal metrics. The above computations then confirm that the condition of equation~\eqref{hyperbolicity-condition} holds, which we also know by general theory regarding extremal Poincar\'e type metrics. To prove Corollary~\ref{Hirzeb... |
| 5 | 0.610 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Preliminaries > {\kah} cone metrics approximating a cscK metric of Poincar\'{e} type and fixed point formula | lines 396-399 | no | yes | extremal | The reason why we put the coefficient $a_0$ is that the scalar curvature $S(\tilde{\omega}_{0})$ is asymptotic to the average value of the scalar curvature $\underline{S}$ (see Lemma \ref{estimate at infinity}). The properties of cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type is well studied by Auvray as follows. |
| 6 | 0.602 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Appendix > Curvature decomposition of Poincar\'e type metrics | lines 2321-2324 | no | yes | Poincare | \subsection{Curvature decomposition of Poincar\'e type metrics}\label{sec:poincare-curvature} In this appendix, we establish the curvature decomposition formula for Poincar\'e type metrics that is used throughout the paper. The main result (Corollary~\ref{decomp}) shows that the Ricci curvature of a Poincar\'e type metric decomposes into a smooth part, a log... |
| 7 | 0.473 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Applications and Discussions > Extremal K\"ahler metric | lines 1475-1478 | no | yes | extremal | \subsection{Extremal K\"ahler metric}\label{subsection 9.3} We discuss the situation of extremal K\"ahler(extK) metrics in Theorem~\ref{thm application 2}. To solve the extK equation, we need to choose $T$-invariant coordinates when defining weighted H\"older spaces, and we want to solve for $T$-invariant potential functions. Comparing the expansion of $\ome... |
| 8 | 0.467 | `corpus/arxiv/1401.0123/source/ExtPK.tex` | `text` | Introduction | lines 290-336 | yes | yes | extremal | ~ Theorem \ref{thm_mainthm1} states that extremal K�hler metrics of Poincar� type are \textit{asymptotically products} near the divisor. Similar results for K�hler-Einstein metrics were already known \cite{sch,wu}; these previous approaches differ fundamentally to ours though. Indeed, in that case, the K�hler-Einstein analogue of Theorem \ref{thm_mainthm2} f... |
| 9 | 0.465 | `corpus/arxiv/1008.2607/source/source.tex` | `text` | Introduction | lines 99-167 | no | yes | extremal | \section{Introduction} \v\n Extremal metrics, introduced by E. Calabi, have been studied intensively in the past 20 years. There are three aspects of the topic: sufficient conditions for existence, necessary conditions for existence and the uniqueness of extremal metric. The necessary conditions for the existence are conjectured to be related to certain stab... |
| 10 | 0.434 | `corpus/arxiv/1401.0128/source/Note_PKFutaki.tex` | `text` | Introduction | lines 359-410 | no | yes | extremal | An extremal metrics is a K�hler metrics such that the Riemannian gradient of its scalar curvature is holomorphic. Constraint \eqref{eqn_constraint} is a reformulation of that of \cite[Prop.4.5]{auv3}, and as such, extends that on the existence of constant scalar curvature metrics in $\mathscr{M}^{D}_{[\omega_X]}$ of \cite{auv2}, which states as: $\sbar^D< \s... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_023 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss existence obstructions for Poincare type extremal metrics?

**Expected sources:** `1401.0123`, `1401.0128`, `1711.08424`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `obstruction`, `Futaki`, `Poincare type extremal`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.871 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2786-2791 | yes | yes | - | \subsection{The proof of Corollary~\ref{Hirzebruch-non-poincare}} The missing component in the proof is to show that the extremal metrics obtained cannot be of Poincar\'e type. For this we will show that in the above situation, the necessary condition in equation~\eqref{hyperbolicity-condition} for the existence of a toric extremal metric of Poincar\'e type... |
| 2 | 0.720 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | no | yes | - | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 3 | 0.555 | `corpus/arxiv/1401.0123/source/ExtPK.tex` | `text` | Introduction | lines 290-336 | yes | yes | obstruction | ~ Theorem \ref{thm_mainthm1} states that extremal K�hler metrics of Poincar� type are \textit{asymptotically products} near the divisor. Similar results for K�hler-Einstein metrics were already known \cite{sch,wu}; these previous approaches differ fundamentally to ours though. Indeed, in that case, the K�hler-Einstein analogue of Theorem \ref{thm_mainthm2} f... |
| 4 | 0.502 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 113-119 | no | yes | Futaki | The \textbf{\textit{extremal vector field}} for the Poincar\'e type K\"ahler metric setting is defined using the Futaki character introduced in \cite{Auv13-2}, and we will discuss in more detail in Section~\ref{subsection 9.3}. Here, we just mention that it is a holomorphic vector field depending only on the K\"ahler class and maximal compact subgroup $K$. F... |
| 5 | 0.622 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2847-2852 | yes | yes | - | ...finity section in $X$. This is already treated in Corollary~\ref{Hirzebruch} where we know that there exists Poincar\'e type extremal metrics. The above computations then confirm that the condition of equation~\eqref{hyperbolicity-condition} holds, which we also know by general theory regarding extremal Poincar\'e type metrics. To prove Corollary~\ref{Hirzeb... |
| 6 | 0.419 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Introduction | lines 247-288 | no | yes | obstruction | ...coordinates such that $\D = \{z_1 = 0\}$ locally. We always assume that $0 < \be \le 1$. Of particular interest is the existence and geometry of metrics of this type which are also Einstein. The existence of \KE (KE) edge metrics was first conjectured by Tian in the mid '90's \cite{T}. In fact, Tian conjectured the existence of KE metrics with `crossing' ed... |
| 7 | 0.415 | `corpus/arxiv/1808.02813/source/source.tex` | `text` | unsectioned | lines 130-137 | no | yes | - | \begin{abstract} We study the existence of weighted extremal K\"ahler metrics in the sense of \cite{aclg17,lahdili} on the total space of an admissible projective bundle over a Hodge K\"ahler manifold of constant scalar curvature. Admissible projective bundles have been defined in \cite{acgt}, and they include the projective line bundles~\cite{hwang-singer}... |
| 8 | 0.409 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | ...bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except in the Fano manifold where the authors proved it indirectly in route of CDS's theorem.\\ We have the following theorem which is useful to our characteri... |
| 9 | 0.404 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 150-166 | no | yes | obstruction | \section{Introduction} This is the second of a series of papers discussing constant scalar curvature K\"ahler metrics. In this paper, for simplicity, we will only consider the case $Aut_0(M, J) = 0.\;$ Here $Aut_0(M,J)$ denotes the identity component of the automorphism group and $Aut_0(M,J)=0$ means the group is discrete. Under this assumption, we prove Don... |
| 10 | 0.396 | `corpus/arxiv/0905.0498/source/source.tex` | `text` | unsectioned | lines 115-134 | no | yes | - | ...dmits a K\"ahler metric of constant scalar curvature if and only if $E$ is polystable. We also address the more general existence problem of extremal K\"ahler metrics on such bundles and prove that the splitting of $E$ as a direct sum of stable subbundles is necessary and sufficient condition for the existence of extremal K\"ahler metrics in sufficiently sma... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_024 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss regularity of conic cscK metrics along a divisor?

**Expected sources:** `1508.02640`, `1803.09506`, `1105.5216`
**Expected chunk types:** `theorem`, `lemma`, `proof`, `text`
**Expected terms:** `regularity`, `conic cscK`, `divisor`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.682 | `corpus/arxiv/1803.09506/source/source.tex` | `definition` | CscK cone path | lines 4524-4526 | yes | no | divisor | \begin{defn}\label{cscK cone path defn} We say the path $\{\om_{\varphi^\beta}=\om_0+i\p\bar \p\varphi^\beta ;0< \beta\leq 1\} $ is a cscK cone path, if $\om_{\varphi^\beta}$ is a cscK cone metric with cone angle $\beta$ along the smooth divisor $D$. \end{defn} |
| 2 | 0.643 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction > Openness of coercivity | lines 698-700 | no | yes | conic cscK, divisor | \begin{cor}[Openness of existence of conic cscK metrics]\label{cor:openness-conic-cscK} Let $D$ be a smooth divisor and assume that $X$ admits no nonzero holomorphic vector field preserving $D$. If $[\om]$ admits a cscK cone metric with cone angle $\alpha_0 \in (0,1)$, then there exists a neighborhood $\mathcal{U}$ of $\alpha_0$ in $(0,1)$ such that $[\om]$... |
| 3 | 0.552 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `remark` | Introduction and the statement of the results > K\"ahler metrics with cone singularities along a divisor and log $K$-stability | lines 279-287 | yes | no | regularity, divisor | \begin{remark} There are several important points when we consider cscK metrics with cone singularities in $c_1(L)$, which we list as follows. \begin{enumerate} \item Unlike in the Fano case where $D \in \|- \lambda K_X\|$ for some $\lambda \in \mathbb{N}$ is natural, $D$ and $L$ can be chosen completely independently; $D$ can be any smooth effective divisor i... |
| 4 | 0.493 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Introduction | lines 106-118 | no | yes | conic cscK | ...s unique up to holomorphic automorphisms in 1980s. Recently, Berndtsson \cite{Bo} generalized this uniqueness result to conic K\"ahler-Einstein metrics on Fano manifolds, by his observation on the convexity of certain energy functional (the $Ding$-functional) along geodesics in the space of all K\"ahler potentials. And Berndtsson's method is further generali... |
| 5 | 0.486 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Linear analysis | lines 1203-1232 | yes | yes | regularity, divisor | ...rSection} We now present the key facts about the linear elliptic theory needed to handle the existence, deformation and regularity theory for canonical edge metrics. We discuss this from two points of view, reviewing the estimates obtained by Donaldson in the wedge H\"older spaces, and also describing how to obtain analogous estimates in the edge H\"older sp... |
| 6 | 0.456 | `corpus/arxiv/1205.0056/source/cone_metrics.tex` | `text` | Introduction | lines 617-642 | no | yes | regularity, divisor | Concerning geodesics with weak regularity, we should compare the construction in Berndtsson's remarkable paper \cite{MR2480611} with our result. It is easy to compute that the volume of the K\"ahler cone metric belongs to $L^p$ with $p(\b_i-1)+1>0$ for any $1\leq i\leq k$. According to Kolodziej's theorem in \cite{MR1618325}, there exists a unique H\"older c... |
| 7 | 0.423 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | no | yes | divisor | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 8 | 0.412 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction > K-stability and K\"ahler-Einstein metrics | lines 195-198 | no | yes | divisor | \subsection{K-stability and K\"ahler-Einstein metrics} There has been much recent work on the study of K\"ahler-Einstein metrics with cone angles along a divisor \cite{D3}. Indeed, in the solution of the Yau-Tian-Donaldson conjecture when $L=-K_X$, an important feature was the use of the \emph{Donaldson continuity method} \begin{equation}\label{doncont}\Ric... |
| 9 | 0.403 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Introduction | lines 166-184 | no | yes | regularity | ...rogram \cite{C2} \cite{C3} is to understand the existence and uniqueness problem of constant scalar curvature K\"ahler (cscK) metrics. As shown by Mabuchi \cite{M2}, the cscK metrics are the critical points of a functional called $K$-energy or the Mabuchi functional. By definition, a cscK metric satisfies the following equation: \[ R_\varphi = \underline{R}... |
| 10 | 0.387 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | ...phic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelia... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_025 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss scalar curvature for metrics with cusp singularities?

**Expected sources:** `1711.08424`, `2210.11862`, `2410.14130`
**Expected chunk types:** `proposition`, `lemma`, `text`
**Expected terms:** `scalar curvature`, `cusp singularities`, `Poincare`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.841 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | yes | yes | scalar curvature, cusp singularities | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 2 | 0.601 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 22-35 | no | yes | scalar curvature | \section{Introduction} \begingroup \raggedright Let $X$ be a compact K\"ahler manifold endowed with a constant scalar curvature K\"ahler(cscK) metric $\omega_X$, and assume it admits no non-trivial holomorphic vector field. In this article, we aim at constructing complete cscK metrics on the complement of finitely many points in $X$, which exhibit Poincar\'e... |
| 3 | 0.663 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Preliminaries | lines 160-169 | yes | yes | scalar curvature | \section{Preliminaries} In this section, we consider the following. Firstly, we recall the definitions of {\kah} metrics of Poincar\'{e} type and the weighted {\hol} space by following \cite{Au2}. Secondly, we recall the definition of {\kah} metrics with cone singularities along a divisor by following \cite{Zhe1}. Finally, we define a {\kah} metric with cone... |
| 4 | 0.457 | `corpus/arxiv/1401.0123/source/ExtPK.tex` | `text` | Introduction | lines 229-251 | no | yes | scalar curvature, cusp singularities | This conjecture, first designed for K�hler-Einstein metrics on Fano manifolds \cite{yau,tia}, was reformulated \cite{don} for constant scalar curvature K�hler metrics (an important special case of extremal metrics), and finally adapted to extremal K�hler metrics \cite{mab,sze2}. This problem is still widely open in the ``if'' direction, except for the notabl... |
| 5 | 0.447 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `text` | Introduction and the statement of the results > K\"ahler metrics with cone singularities along a divisor and log $K$-stability | lines 267-272 | no | yes | scalar curvature | ...assical) Futaki invariant, $\text{Fut}_{D,\beta}$ is expected to vanish on \kah classes which contain a \ke or constant scalar curvature \kah metric with cone singularities along $D$ with cone angle $2 \pi \beta$.\footnote{This certainly holds for \ke metrics on Fano manifolds; see \cite[Theorem 2.1]{sw} and also \cite[Theorem 7]{cds3}.}%\footnote{In fact, f... |
| 6 | 0.419 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 652-659 | no | yes | scalar curvature, Poincare | Regarding Corollary \ref{cor:mixed-singularities}, we emphasize that while \cite{Xu_Zheng25} and \cite{Xu25} restrict their attention to smooth divisors, our framework handles general twisted positive $(1,1)$-currents $\chi$, thereby covering simple normal crossing divisors. More specifically, Xu \cite{Xu25} and Xu--Zheng \cite{Xu_Zheng25} established unique... |
| 7 | 0.410 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Conjectural picture | lines 666-667 | no | yes | - | \section{Conjectural picture} In this final section we discuss what one might expect about the existence problem for metrics with cone singularities on a Fano manifold. It is natural to think of such a metric as a solution of a distributional equation |
| 8 | 0.408 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | unsectioned | lines 114-137 | no | yes | scalar curvature | \title[Existence, Properness and Geodesic stability]{Existence of constant scalar curvature K\"ahler cone metrics, properness and geodesic stability} \author{Kai Zheng} % \address{University of Warwick} \curraddr{Tongji University, Shanghai 200092, P.R. CHINA} \email[Kai Zheng]{kaizheng@amss.ac.cn} %\date{\today} \begin{document} \maketitle \begin{abstract}... |
| 9 | 0.397 | `corpus/arxiv/1512.06391/source/source.tex` | `text` | A Futaki invariant > The Futaki invariant for a K\"ahler class | lines 351-355 | no | yes | scalar curvature | ...tric ${\tilde g}_{\omega}(X,Y) = \frac{1}{f_{K, \omega, a}^2} \omega(X, JY)$ is Einstein--Maxwell? \end{problem} By the discussion in the previous section, we are looking for metrics $\omega \in \mathcal{K}_{\Omega}^G$ such that the corresponding scalar curvature of $\tilde g$ |
| 10 | 0.395 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | scalar curvature | ...ef\cs{$\clubsuit$} % Tamas' comments \title{Tian's properness conjectures and Finsler geometry of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{document} \maketitle \begin{abstract} Well-known conjectures of Tian predict t... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_026 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss cscK metrics on quasi-projective or punctured manifolds?

**Expected sources:** `1205.0056`, `2405.11952`, `2410.14130`
**Expected chunk types:** `theorem`, `text`
**Expected terms:** `quasi-projective`, `punctured`, `cscK`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.717 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | no | no | cscK | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |
| 2 | 0.533 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | %\begin{q} There is a few open questions for the Calabi dream manifolds: %\begin{enumerate} %\item What linear combinations of Chern numbers are nonnegative for all Calabi dream manifolds? %\item In Corollary 1.7, can we extend it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic to... |
| 3 | 0.508 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | - | ...ef\cs{$\clubsuit$} % Tamas' comments \title{Tian's properness conjectures and Finsler geometry of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{document} \maketitle \begin{abstract} Well-known conjectures of Tian predict t... |
| 4 | 0.503 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Introduction | lines 106-118 | no | yes | cscK | \section{Introduction} Bando-Mabuchi \cite{BM} proved that K\"ahler-Einstein metric on Fano manifolds is unique up to holomorphic automorphisms in 1980s. Recently, Berndtsson \cite{Bo} generalized this uniqueness result to conic K\"ahler-Einstein metrics on Fano manifolds, by his observation on the convexity of certain energy functional (the $Ding$-functiona... |
| 5 | 0.472 | `corpus/arxiv/0912.4095/source/source.tex` | `text` | Introduction | lines 36-60 | no | yes | cscK | \section{Introduction} Calabi~\cite{Cal82} introduced the notion of extremal metrics as candidates for canonical representatives of K\"ahler classes on compact K\"ahler manifolds. Unfortunately not all K\"ahler manifolds admit extremal metrics (eg. Levine~\cite{Lev}) and even if they do, they may not admit them in all K\"ahler classes (see eg. Apostolov, Cal... |
| 6 | 0.471 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Introduction | lines 185-188 | yes | yes | cscK | ...to prove the convexity of the $K$-energy. Chen-Paun-Zeng used PDEs method in \cite{CPZ} to prove the uniqueness of the cscK metric and extremal K\"ahler metric. A natural question is: could we prove the uniqueness of cscK metric on more general K\"ahler manifolds? Note that the methods we mentioned above depend on the compactness of the manifold. As a resul... |
| 7 | 0.470 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Introduction | lines 295-300 | no | yes | cscK | The paper is organised as follows. In Section \ref{sec:background}, we settle the necessary background material on cscK manifolds. Then, Section \ref{sec:foldable toric surfaces} is devoted to the classification of foldable surfaces and the proofs of Proposition \ref{prop:intro fans} and Proposition \ref{prop:intro}. In Section \ref{sec:local moduli construc... |
| 8 | 0.468 | `corpus/arxiv/math_0412518/source/slopeobs_archive.tex` | `remark` | Examples > Unstable rational manifolds | lines 2116-2127 | no | no | cscK | ...cture}. The case of $\PP^2$ blown up at $\ge4$ points gives smooth polarised del Pezzo surfaces with $\aut(X)=0$ but no cscK metric in certain classes. This is in contrast to the case of the anticanonical polarisation for which Tian \cite{Ti1} proved the ``folklore conjecture", that smooth Fano surfaces have a K\"ahler-Einstein metric if and only if their ho... |
| 9 | 0.464 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | It is an interesting question to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except i... |
| 10 | 0.455 | `corpus/arxiv/2110.08491/source/source.tex` | `text` | \bf Introduction | lines 160-167 | no | yes | cscK | This conjecture were generalized to extremal metrics. Recently, there have been many progresses towards this conjecture (see \cite{BDL2}, \cite{CC1}, \cite{CC2}, \cite{DL}, \cite{Li}). \v In a sequence of papers, Donaldson initiated a program to study the extremal metrics on toric manifolds: Donaldson formulated $K$-stability for polytopes and conjectured th... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_027 - conic/cusp/Poincare metrics

**Question:** Where does the corpus compare cone metrics and Poincare type metrics?

**Expected sources:** `2210.11862`, `1803.09506`, `1205.0056`
**Expected chunk types:** `remark`, `example`, `text`
**Expected terms:** `cone metrics`, `Poincare type`, `comparison`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.639 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 81-91 | no | yes | - | ...$[E_i]$ denotes the Poincar\'e dual of the $E_i$. Our main theorem adds new examples to the existing list of Poincar\'e type metrics. We recall here some important examples: (a) the K\"ahler-Einstein metrics of Poincar\'e type, whose existence were shown by Tian-Yau \cite{TY87}, Kobayashi \cite{Kob84} and Cheng-Yau \cite{CY80}; (b) the toric extremal K\"ahle... |
| 2 | 0.629 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | yes | yes | - | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 3 | 0.576 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 145-159 | yes | yes | - | This paper is organized as follows. In Section 2, we recall the definitions of {\kah} metrics of Poincar\'{e}/cone singularities. In addition, we define a background {\kah} metric with cone singularities, which converges to a cscK metric of Poincar\'{e} type. Finally, we consider a fixed point formula on the weighted {\hol} space, which characterizing a cscK... |
| 4 | 0.376 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Introduction | lines 247-288 | no | yes | cone metrics | ...= \{z_1 = 0\}$ locally. We always assume that $0 < \be \le 1$. Of particular interest is the existence and geometry of metrics of this type which are also Einstein. The existence of \KE (KE) edge metrics was first conjectured by Tian in the mid '90's \cite{T}. In fact, Tian conjectured the existence of KE metrics with `crossing' edge singularities when $\D$... |
| 5 | 0.357 | `corpus/arxiv/1401.0128/source/Note_PKFutaki.tex` | `text` | Introduction | lines 359-410 | no | yes | - | An extremal metrics is a K�hler metrics such that the Riemannian gradient of its scalar curvature is holomorphic. Constraint \eqref{eqn_constraint} is a reformulation of that of \cite[Prop.4.5]{auv3}, and as such, extends that on the existence of constant scalar curvature metrics in $\mathscr{M}^{D}_{[\omega_X]}$ of \cite{auv2}, which states as: $\sbar^D< \s... |
| 6 | 0.352 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | - | ...ef\cs{$\clubsuit$} % Tamas' comments \title{Tian's properness conjectures and Finsler geometry of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{document} \maketitle \begin{abstract} Well-known conjectures of Tian predict t... |
| 7 | 0.352 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `remark` | Introduction and the statement of the results > K\"ahler metrics with cone singularities along a divisor and log $K$-stability | lines 279-287 | no | yes | - | \begin{remark} There are several important points when we consider cscK metrics with cone singularities in $c_1(L)$, which we list as follows. \begin{enumerate} \item Unlike in the Fano case where $D \in \|- \lambda K_X\|$ for some $\lambda \in \mathbb{N}$ is natural, $D$ and $L$ can be chosen completely independently; $D$ can be any smooth effective divisor i... |
| 8 | 0.350 | `corpus/arxiv/1205.0056/source/cone_metrics.tex` | `text` | Introduction | lines 617-642 | yes | yes | cone metrics | Concerning geodesics with weak regularity, we should compare the construction in Berndtsson's remarkable paper \cite{MR2480611} with our result. It is easy to compute that the volume of the K\"ahler cone metric belongs to $L^p$ with $p(\b_i-1)+1>0$ for any $1\leq i\leq k$. According to Kolodziej's theorem in \cite{MR1618325}, there exists a unique H\"older c... |
| 9 | 0.346 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2847-2852 | no | yes | - | ...finity section in $X$. This is already treated in Corollary~\ref{Hirzebruch} where we know that there exists Poincar\'e type extremal metrics. The above computations then confirm that the condition of equation~\eqref{hyperbolicity-condition} holds, which we also know by general theory regarding extremal Poincar\'e type metrics. To prove Corollary~\ref{Hirzeb... |
| 10 | 0.345 | `corpus/arxiv/1401.0123/source/ExtPK.tex` | `text` | Introduction | lines 263-266 | no | yes | - | ...hat this definition allows a rather loose behaviour near the divisor, in the sense that one can easily produce Poincar� type metrics such that their restrictions to directions parallel to the divisor \textit{does not} converge near the divisor. Our first main result states nonetheless that such a convergence does occur for extremal Poincar� type K�hler metri... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_028 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss Poincare type extremal metrics on toric varieties with labeled polytopes?

**Expected sources:** `1711.08424`
**Expected chunk types:** `theorem`, `example`, `text`
**Expected terms:** `labeled polytope`, `toric variety`, `Poincare type extremal`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.773 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2786-2791 | yes | yes | - | \subsection{The proof of Corollary~\ref{Hirzebruch-non-poincare}} The missing component in the proof is to show that the extremal metrics obtained cannot be of Poincar\'e type. For this we will show that in the above situation, the necessary condition in equation~\eqref{hyperbolicity-condition} for the existence of a toric extremal metric of Poincar\'e type... |
| 2 | 0.547 | `corpus/arxiv/2110.08491/source/source.tex` | `remark` | \bf Introduction | lines 200-204 | no | no | - | \begin{remark} In \cite{Del}, Delcroix expressed $K$-stability of polarized spherical varieties in terms of combinatorial data and provided a combinatorial sufficient condition of $G$-uniform $K$-stability. The appendix of \cite{Del} by Yuji Odaka showed that for non-singular spherical varieties, $G$-uniform $K$-stability is equivalent to existence of cscK m... |
| 3 | 0.533 | `corpus/arxiv/0909.4512/source/source.tex` | `text` | Introduction | lines 132-142 | no | yes | - | Note that explicit Sasaki--Einstein metrics of this type have been found in~\cite{exMS,other2} and toric Sasaki--Einstein metrics have been systematically studied in~\cite{futakiChoOno,futakiOnoWang}.\\ In order to prove Theorem~\ref{mainTHEOparall}, we consider the cases of \defin{generic} labeled quadrilaterals (that is, quadrilaterals which have no parall... |
| 4 | 0.512 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | toric variety | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 5 | 0.635 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | The relative K-stability of a pair > Test configurations and $K$-stability of a pair | lines 513-522 | yes | yes | - | We shall next turn to the toric case as a model example for the above theory, and where specific computations are manageable. We shall show (see in particular Corollary \ref{Hirzebruch-non-poincare}) that there are examples of relatively $K$-stable triples $(X,Z,L)$ satisfying $F_{\chi}''(0) > 0,$ which cannot be of Poincar\'e type. We note, however, that th... |
| 6 | 0.431 | `corpus/arxiv/1008.2607/source/source.tex` | `text` | Introduction | lines 99-167 | no | yes | - | \section{Introduction} \v\n Extremal metrics, introduced by E. Calabi, have been studied intensively in the past 20 years. There are three aspects of the topic: sufficient conditions for existence, necessary conditions for existence and the uniqueness of extremal metric. The necessary conditions for the existence are conjectured to be related to certain stab... |
| 7 | 0.405 | `corpus/arxiv/2208.12493/source/toric-lecture-notes.tex` | `text` | Existence: an overview > The canonical solution | lines 1874-1920 | no | yes | - | \bibitem{Do-08} S.K. Donaldson, {\it Extremal metrics on toric surfaces: a continuity method}, J. Differential Geom. {\bf 79} (2008), 389--432. \bibitem{Do-09} S.K. Donaldson, {\it Constant scalar curvature metrics on toric surfaces}, Geom. Funct. Anal. {\bf 19} (2009), 83--136. \bibitem{gauduchon-book} P. Gauduchon, Calabi's extremal K\"ahler metrics: An el... |
| 8 | 0.400 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 113-119 | no | yes | - | The \textbf{\textit{extremal vector field}} for the Poincar\'e type K\"ahler metric setting is defined using the Futaki character introduced in \cite{Auv13-2}, and we will discuss in more detail in Section~\ref{subsection 9.3}. Here, we just mention that it is a holomorphic vector field depending only on the K\"ahler class and maximal compact subgroup $K$. F... |
| 9 | 0.388 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `text` | Introduction | lines 251-260 | no | yes | - | We discuss in~\S\ref{sectFORMALsol} consequences of this last result and open problems in relation with the relative toric version of the Yau--Tian--Donaldson conjecture. In the next section we gather facts, definition, key results and recall brief explanations on the topic of toric extremal (almost) K\"ahler metrics. Section~\ref{sectMAIN} contains the proo... |
| 10 | 0.383 | `corpus/arxiv/1808.07811/source/source.tex` | `text` | unsectioned | lines 250-256 | no | yes | - | We illustrate our theory with specific computations on smooth toric varieties and on the toric fibre bundles introduced in \cite{ACGT}. As an application, we obtain a Yau--Tian--Donaldson type correspondence for $(\uu,\vv)$-extremal K\"ahler classes on ${\mathbb P}^1$-bundles over products of compact Hodge cscK manifolds, thus extending some of the results i... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_029 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss boundedness or coercivity of energy functionals for singular cscK metrics?

**Expected sources:** `2210.11862`, `1508.02640`, `1803.09506`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `coercivity`, `energy functional`, `singular cscK`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.873 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | yes | no | singular cscK | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |
| 2 | 0.808 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Existence of singular weighted cscK metrics | lines 1668-1670 | no | yes | coercivity | \section{Existence of singular weighted cscK metrics} \label{sect_existence} We shall combine the a priori estimates obtained in the previous section and the uniform coercivity established in \cite{Boucksom_Jonsson_Trusiani_2024} to construct singular weighted cscK metrics. |
| 3 | 0.557 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | ...obstructed (see \cite{IltenTuro}). Finally, the toric MMP (that produces the classification of toric surfaces) produces singular varieties in general. So our main ingredients to prove Theorem \ref{theo:intro} do not generalise, a priori, in higher dimension. Nevertheless, it would be interesting to study what goes through the new difficulties. We expect the... |
| 4 | 0.543 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | ...uestion to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except in the Fano manifold wh... |
| 5 | 0.535 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 419-430 | no | yes | - | In the next section, we recall the non-Archimedean and Archimedean functionals, and explain they are related to each other. We state the basic correspondence between finite energy non-Archimedean metrics and maximal geodesic rays as established by Berman-Boucksom-Jonsson. We discuss the twist of non-Archimedean metrics that was introduced in \cite{His16b} fo... |
| 6 | 0.523 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `remark` | Introduction and the statement of the results > K\"ahler metrics with cone singularities along a divisor and log $K$-stability | lines 279-287 | yes | no | singular cscK | \begin{remark} There are several important points when we consider cscK metrics with cone singularities in $c_1(L)$, which we list as follows. \begin{enumerate} \item Unlike in the Fano case where $D \in \|- \lambda K_X\|$ for some $\lambda \in \mathbb{N}$ is natural, $D$ and $L$ can be chosen completely independently; $D$ can be any smooth effective divisor i... |
| 7 | 0.521 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | Introduction | lines 269-271 | no | yes | - | Similarly to the case of cscK metrics, using the sub-slope property of convex functions, we obtain the following corollary giving an obstruction to the existence of $(\uu,\vv)$-cscK metrics in a K\"ahler class $\alpha$, in terms of the boundedness of the corresponding $(\uu,\vv)$-Mabuchi energy. |
| 8 | 0.650 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 635-663 | no | yes | coercivity, singular cscK | \section*{Introduction} The constant scalar curvature K\"ahler (cscK) metric problem has become one of the central focus in K\"ahler geometry during the last decades. The Yau--Tian--Donaldson conjecture asserts that given a compact K\"ahler manifold with a fixed K\"ahler class, the existence of cscK metrics in the K\"ahler class is equivalent to an algebro-g... |
| 9 | 0.507 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 595-604 | no | yes | coercivity, energy functional | \section{Introduction} Finding canonical Kähler metrics is a central theme in complex geometry. In higher dimensions, constant scalar curvature Kähler (cscK) metrics provide an analogue of Poincar\'e’s uniformization theorem; see the surveys \cite{Boucksom_2018, Donaldson_2018_2} for background and further references. Kähler--Einstein metrics form an especia... |
| 10 | 0.506 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Introduction | lines 106-118 | no | yes | energy functional | ...ic automorphisms in 1980s. Recently, Berndtsson \cite{Bo} generalized this uniqueness result to conic K\"ahler-Einstein metrics on Fano manifolds, by his observation on the convexity of certain energy functional (the $Ding$-functional) along geodesics in the space of all K\"ahler potentials. And Berndtsson's method is further generalized to prove the uniquen... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### conic_poincare_030 - conic/cusp/Poincare metrics

**Question:** Where does the corpus discuss Poincare type cscK metrics as limits of conic approximations?

**Expected sources:** `2210.11862`, `2410.14130`
**Expected chunk types:** `theorem`, `proof`, `text`
**Expected terms:** `limit`, `conic approximation`, `Poincare type cscK`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.719 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | yes | yes | limit | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 2 | 0.700 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 81-91 | no | yes | limit | ...$[E_i]$ denotes the Poincar\'e dual of the $E_i$. Our main theorem adds new examples to the existing list of Poincar\'e type metrics. We recall here some important examples: (a) the K\"ahler-Einstein metrics of Poincar\'e type, whose existence were shown by Tian-Yau \cite{TY87}, Kobayashi \cite{Kob84} and Cheng-Yau \cite{CY80}; (b) the toric extremal K\"ahle... |
| 3 | 0.622 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction > Openness of coercivity | lines 701-703 | no | yes | limit | More significantly, our framework allows us to deduce existence of small-angle conic metrics from coercivity at the cusp (Poincar\'e) limit. |
| 4 | 0.632 | `corpus/arxiv/2210.11862/source/source.tex` | `theorem` | Introduction | lines 94-100 | yes | yes | - | ...is no nontrivial holomorphic vector field on $D$ and ${\rm Aut}_0 ((X,L_X); D)$ is trivial. If $X \setminus D$ admits a cscK metric $\omega_{0}^{cscK} \in c_1 (L_X)$ of Poincar\'{e} type, then there exists a cscK cone metric $\omega_{\beta}^{cscK} \in c_1(L_X)$ of cone angle $2 \pi \beta$ along $D$ for any $0<\beta \ll 1$. Moreover, $\omega_{\beta}^{cscK}$ c... |
| 5 | 0.602 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 145-159 | yes | yes | - | This paper is organized as follows. In Section 2, we recall the definitions of {\kah} metrics of Poincar\'{e}/cone singularities. In addition, we define a background {\kah} metric with cone singularities, which converges to a cscK metric of Poincar\'{e} type. Finally, we consider a fixed point formula on the weighted {\hol} space, which characterizing a cscK... |
| 6 | 0.471 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `text` | Introduction and the statement of the results > Log Futaki invariant computed with respect to the conically singular metrics | lines 369-370 | no | yes | - | \subsection{Log Futaki invariant computed with respect to the conically singular metrics} \label{intscmsfi} Although the log Futaki invariant is conjectured to be related to the existence of conically singular cscK metrics, the log Futaki invariant itself is computed with respect to a \textit{smooth} \kah metric in $c_1 (L)$. We now consider the following qu... |
| 7 | 0.403 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Introduction | lines 106-118 | no | yes | - | ...s unique up to holomorphic automorphisms in 1980s. Recently, Berndtsson \cite{Bo} generalized this uniqueness result to conic K\"ahler-Einstein metrics on Fano manifolds, by his observation on the convexity of certain energy functional (the $Ding$-functional) along geodesics in the space of all K\"ahler potentials. And Berndtsson's method is further generali... |
| 8 | 0.400 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | ...phic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelia... |
| 9 | 0.375 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Introduction | lines 185-188 | yes | yes | - | ...to prove the convexity of the $K$-energy. Chen-Paun-Zeng used PDEs method in \cite{CPZ} to prove the uniqueness of the cscK metric and extremal K\"ahler metric. A natural question is: could we prove the uniqueness of cscK metric on more general K\"ahler manifolds? Note that the methods we mentioned above depend on the compactness of the manifold. As a resul... |
| 10 | 0.369 | `corpus/arxiv/0805.0128/source/extremal2a.tex` | `text` | Introduction | lines 219-255 | no | yes | limit | ...s on the results, are related to our lack of understanding of this basic local question---what are the possible $C^{0}$ limits of solutions to the equation (1)? \ The main work of this paper finishes in Section 5. However, it is interesting to complement the existence proofs with an understanding of what goes wrong when the positivity hypothesis is violated.... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_001 - toric Abreu equation

**Question:** Where does the corpus discuss the Abreu equation in toric Kahler geometry?

**Expected sources:** `dg-ga_9711014`, `math_0407486`, `0805.0128`
**Expected chunk types:** `definition`, `theorem`, `text`
**Expected terms:** `Abreu equation`, `toric`, `scalar curvature`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.632 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Background > The $v$-scalar curvature | lines 541-545 | no | yes | Abreu equation, toric | In particular, toric solutions to the $(v,\,w)$-cscK equation \eqref{vwcscK} give rise to solutions $u \in C^\infty(P)$ to the \emph{generalized Abreu equation}: |
| 2 | 0.629 | `corpus/arxiv/2108.12297/source/source.tex` | `text` | Weighted toric K-stability > Generalized Abreu's equation | lines 1330-1333 | no | yes | Abreu equation | This formula generalizes the expression $(\ref{abreu})$ and is referred to as \textit{the generalized Abreu equation}. This equation has been studied for example in \cite{VA3, LLS, LLS2, LLS3}. |
| 3 | 0.621 | `corpus/arxiv/1008.2607/source/source.tex` | `conjecture` | K\"{a}hler geometry on toric surfaces > $K$-stability and existence of extremal metrics | lines 696-699 | no | no | Abreu equation | \begin{conjecture}\label{conjecture_2.1.3} Let $\Delta$ be a Delzant polytope. If $(\Delta, K)$ is uniformly stable, the Abreu equation $ \mc S(u)=K $ admits a solution in $\mc C^\infty(\Delta,v)$, \end{conjecture} |
| 4 | 0.618 | `corpus/arxiv/2110.08491/source/source.tex` | `text` | \bf Scalar curvatures on homogeneous toric bundles | lines 759-762 | no | yes | Abreu equation, toric, scalar curvature | \section{\bf Scalar curvatures on homogeneous toric bundles}\label{Sec-5} In this section, we generalize our results to homogeneous toric bundles. First, we briefly review homogeneous toric bundles and the generalized Abreu equation, For the details, see \cite{D5} and \cite{CHLLS}. Then we sketch the proof of Theorem \ref{theorem_1.1}. |
| 5 | 0.582 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Labelled polytopes and the Abreu--Guillemin theory for K\"ahler metrics of Poincar\'e type > Donaldson metrics on a labelled polytope | line 738 | no | yes | Abreu equation, toric | The extremality of the K\"ahler metric \eqref{toric-g} with $u\in \cS(\Delta, {\bf L})$ reduces to solving the {\it Abreu equation}~\cite{Abreu0} |
| 6 | 0.599 | `corpus/arxiv/1008.2607/source/source.tex` | `conjecture` | K\"{a}hler geometry on toric surfaces > $K$-stability and existence of extremal metrics | lines 683-689 | no | no | Abreu equation | \begin{conjecture}\label{conjecture_2.1.2} If $(\Delta, K)$ is polystable, the Abreu equation $ \mc S(u)=K $ admits a solution in $\mc C_\infty(\Delta)$, where $\mc C_\infty(\Delta)$ consists of smooth convex functions on $\Delta$ that are continuous on $\bar\Delta$. \end{conjecture} |
| 7 | 0.415 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted cscK problem on semisimple principal fibration | lines 2104-2110 | no | yes | scalar curvature | Also, from \cite[Section 5]{AJL}, any Kähler metric \(\omega\) on \(X\) induces a Kähler metric \(\tilde{\omega}\) on \(Y\) such that the restriction \((Y_b, \tilde{\omega}_b)\) of \((Y, \tilde{\omega})\) to a fiber over a point \(b \in B\) is \(\T\)-equivariantly Kähler isomorphic to \((X, \omega)\). Such a metric \(\tilde{\omega}\) on \(Y\) is the \emph{co... |
| 8 | 0.411 | `corpus/my_notes/requested_non_arxiv_sources.md` | `text` | Requested non-arXiv and correction pointers > Journal-only or correction pointers | lines 7-23 | no | yes | toric, scalar curvature | ## Journal-only or correction pointers - Simon K. Donaldson, "Scalar curvature and stability of toric varieties", Journal of Differential Geometry 62 (2002), 289-349. Source: https://projecteuclid.org/euclid.jdg/1090950195 DOI: 10.4310/jdg/1090950195 Local status: bibliographic pointer only. No arXiv identifier was identified in this update. - Sebastien Bouc... |
| 9 | 0.411 | `corpus/arxiv/math_0407486/source/intest2.tex` | `text` | Estimates for higher derivatives > Rescaling sections | lines 854-914 | yes | yes | toric, scalar curvature | \begin{thebibliography}{99} \bibitem{kn:Abr} M. Abreu {\em Kahler geometry of toric varieties and extremal metrics} Int. J. Math. {\bf 9} 641-651 1998 \bibitem{kn:An} M. T. Anderson {\em Orbifold compactness for spaces of Riemannian metrics and applications} Math. Annalen {\bf 331} 739-778 2005 \bibitem{kn:Caf} L.A. Caffarelli {\em Interior $W^{2}_{p}$ estim... |
| 10 | 0.378 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Proof of Theorem \ref{suff} | lines 2778-2847 | no | yes | toric | ...icts to \eqref{convDF}. %\begin{acknowledgements} %\end{acknowledgements} \begin{thebibliography}{99} \bibitem{Ab03} M.~Abreu, K\"ahler geometry of toric manifolds in symplectic coordinates. \emph{Symplectic and contact topology: interactions and perspectives (Toronto, ON/Montreal, QC, 2001)}, 1--24, Fields Inst. Commun., \textbf{35}, \emph{Amer. Math. Soc.,... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_002 - toric Abreu equation

**Question:** Where does the corpus discuss Donaldson interior estimates for solutions of Abreu's equation?

**Expected sources:** `math_0407486`
**Expected chunk types:** `theorem`, `proposition`, `proof`
**Expected terms:** `interior estimates`, `Abreu equation`, `Donaldson`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.707 | `corpus/arxiv/math_0407486/source/intest2.tex` | `text` | Estimates for higher derivatives > Rescaling sections | lines 854-914 | yes | no | interior estimates, Donaldson | ...aces of Riemannian metrics and applications} Math. Annalen {\bf 331} 739-778 2005 \bibitem{kn:Caf} L.A. Caffarelli {\em Interior $W^{2}_{p}$ estimates for solutions to the Monge-Amp\'ere equation} Annals of Math. {\bf 131} 135-150 1990 \bibitem{kn:CafGut} L.A. Caffarelli and C.E. Guti\'errez {\em Properties of the solutions of the linearised Monge-Amp\`ere e... |
| 2 | 0.605 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `text` | Labelled polytope and toric (almost) K\"ahler geometry > Extremal K\"ahler metrics unicity and an open condition | lines 393-395 | no | no | Donaldson | Donaldson proved in~\cite{don:extMcond} that the set of labelling $\lab\in \mN(P)$ for which the Abreu's equation has a solution is open in $\mN(P)$, the $d$--dimensional open cone of labellings of $P$ in $\kt^d$. |
| 3 | 0.633 | `corpus/arxiv/math_0407486/source/intest.tex` | `text` | Introduction | lines 134-145 | yes | no | - | ...mega,\sigma}$. As explained in \cite{kn:don}, simple examples show that for some data $\Omega, A, d\sigma$ there are no solutions of Abreu's equation with the given boundary behaviour. By the same token, one needs further assumptions before {\it a priori} estimates of a solution can be obtained. The condition which we expect to be appropriate involves the li... |
| 4 | 0.498 | `corpus/arxiv/2208.12493/source/toric-lecture-notes.tex` | `text` | Existence: an overview > The canonical solution | lines 1819-1873 | no | no | interior estimates, Donaldson | ...Chen, A.-M. Li and L. Sheng, {\it Uniform K-stability for extremal metrics on toric varieties}, Journal of Differential Equations {\bf 257} (2014), 1487--1500. \bibitem{CLS} B. Chen, A.-M. Li and L. Sheng, {\it Extremal metrics on toric surfaces}, preprint arXiv:1008.2607. \bibitem{CC1} X. Chen, J. Cheng, {\it On the constant scalar curvature K\"ahler metric... |
| 5 | 0.472 | `corpus/arxiv/0805.0128/source/extremal2b.tex` | `text` | Blow-up limits > Discussion | lines 1422-1481 | no | no | interior estimates, Donaldson | ...at more complicated situations in which we have several \lq\lq creases'', dividing the polygon into more parts. This is discussed in \cite{kn:D1}, and taken much further by Szelyhidi in \cite{kn:Sz}. Szekelyhidi's work also suggests very strongly that a similar picture holds for the limiting behaviour of the Calabi flow. Notice also that this (conjectural) p... |
| 6 | 0.556 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `proposition` | Introduction | lines 248-250 | no | yes | - | ...MALintro} For any simple labelled polytope $(P,\sigma)$, there exists an infinite dimensional family of formal extremal solutions $H :P \ra \mbox{Sym}^2(\kt^*)$ of equation~\eqref{eqABREUintroH} satisfying the boundary condition associated to $\sigma$. Whenever one of these solutions is positive definite on the interior of $P$, $(P,\sigma)$ is uniformly $K$-... |
| 7 | 0.421 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Linear analysis | lines 1203-1232 | no | no | Donaldson | ...linear elliptic theory needed to handle the existence, deformation and regularity theory for canonical edge metrics. We discuss this from two points of view, reviewing the estimates obtained by Donaldson in the wedge H\"older spaces, and also describing how to obtain analogous estimates in the edge H\"older spaces. These latter estimates are obtained through... |
| 8 | 0.415 | `corpus/arxiv/1008.2607/source/source.tex` | `text` | Proof of Theorem \ref{theorem_1.1} > The continuity method | lines 2190-2212 | no | no | interior estimates, Abreu equation, Donaldson | ...ha}$-converges to a function $\phi\in C^{6,\alpha}_{\mathbb T^2}(M)$ with $\mathcal S(g+\phi)=K\circ\nabla^f$. } \v The estimates for $\psi\indexm$ will be established by the following steps: \v\n {\em Interior estimates: } Donaldson proved the interior regularity for the Abreu equation when $n=2$. In \cite{CLS2}, we proved the interior regularity for the Ab... |
| 9 | 0.409 | `corpus/arxiv/1205.0056/source/cone_metrics.tex` | `text` | Introduction | lines 660-697 | no | no | Donaldson | ...ibe the structure of our paper. In Section {\ref{space}}, we recall the notations and the function spaces introduced by Donaldson. In particular, we {define} the boundary case. {Then}, we generalize the Riemannian structure to the space of K\"ahler cone metrics. The delicate part here is the growth rate near the divisor. In {the Donaldson} space, we derive t... |
| 10 | 0.503 | `corpus/arxiv/math_0407486/source/intest.tex` | `text` | Introduction | lines 67-131 | yes | no | - | the Hessian matrix $u_{ij}= \frac{\partial^{2} u}{\partial x^{i}\partial x^{j}}$. We call this PDE {\it Abreu's equation} since the expression $S(u)$ appears in \cite{kn:Abr}, in the study of the differential geometry of toric varieties. In this paper we will be primarily interested in the case when $A$ is a constant. Solutions to Equation~\ref{eq:Abreu} the... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_003 - toric Abreu equation

**Question:** Where does the corpus discuss extremal metrics on toric surfaces?

**Expected sources:** `0805.0128`, `1008.2607`, `2402.01159`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `toric surfaces`, `extremal metrics`, `Abreu`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.583 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | yes | yes | toric surfaces | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 2 | 0.515 | `corpus/arxiv/2110.08491/source/source.tex` | `text` | \bf Introduction | lines 160-167 | no | yes | toric surfaces, extremal metrics | This conjecture were generalized to extremal metrics. Recently, there have been many progresses towards this conjecture (see \cite{BDL2}, \cite{CC1}, \cite{CC2}, \cite{DL}, \cite{Li}). \v In a sequence of papers, Donaldson initiated a program to study the extremal metrics on toric manifolds: Donaldson formulated $K$-stability for polytopes and conjectured th... |
| 3 | 0.480 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | unsectioned | lines 162-212 | no | yes | toric surfaces, extremal metrics | An interesting testing ground for these ideas is the case of toric varieties, which was developed by Donaldson. In~\cite{Don02} he showed that in the case of toric surfaces K-stability implies that the Mabuchi functional is bounded from below (this was later extended by Zhou-Zhu~\cite{ZZ06} to show properness of the Mabuchi functional) and a minimising seque... |
| 4 | 0.461 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `text` | Introduction | lines 251-260 | no | yes | - | We discuss in~\S\ref{sectFORMALsol} consequences of this last result and open problems in relation with the relative toric version of the Yau--Tian--Donaldson conjecture. In the next section we gather facts, definition, key results and recall brief explanations on the topic of toric extremal (almost) K\"ahler metrics. Section~\ref{sectMAIN} contains the proo... |
| 5 | 0.457 | `corpus/arxiv/0706.0505/source/source.tex` | `text` | unsectioned | lines 408-448 | no | yes | toric surfaces, extremal metrics | \title {A note on the $K-$stability on toric manifolds} \author {Bin $\text{Zhou}^*$} %\author{Haozhao Li\\School of Mathematical Sciences\\ Peking %University, Beijing, 100871, P.R. China\\ %lnsinx@math.pku.edu.cn\\ } \address{ * Department of Mathematics, Peking University, Beijing, 100871, China} \author { Xiaohua $\text{Zhu}^{*,**}$} \thanks { ** Partial... |
| 6 | 0.445 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Proofs of Lemmas \ref{s1is2}, \ref{s1is1} and \ref{s1is2overk} | lines 1659-1726 | no | yes | extremal metrics | ...--15. \bibitem{ACG1} V. Apostolov, D.~M.~J. Calderbank and P. Gauduchon, {\it The geometry of weakly self-dual K\"ahler surfaces}, Compositio Math. {\bf 135} (2003), 279--322. \bibitem{ACG2} V. Apostolov, D.~M.~J. Calderbank and P. Gauduchon, {\it Hamiltonian $2$-forms in K\"ahler geometry} I {\it General Theory}, J. Diff. Geom., to appear, arXiv:math.DG/020... |
| 7 | 0.442 | `corpus/arxiv/0905.0498/source/source.tex` | `text` | unsectioned | lines 115-134 | no | yes | - | ...ic of constant scalar curvature if and only if $E$ is polystable. We also address the more general existence problem of extremal K\"ahler metrics on such bundles and prove that the splitting of $E$ as a direct sum of stable subbundles is necessary and sufficient condition for the existence of extremal K\"ahler metrics in sufficiently small K\"ahler classes.... |
| 8 | 0.437 | `corpus/arxiv/math_0511118/source/source.tex` | `text` | unsectioned | lines 119-165 | no | yes | - | ...sible' K\"ahler classes (i.e., the ones compatible with the bundle structure in a way we make precise) which contain an extremal K\"ahler metric. In many cases, such as on geometrically ruled surfaces, every K\"ahler class is admissible. In particular, our results complete the classification of extremal K\"ahler metrics on geometrically ruled surfaces, answe... |
| 9 | 0.436 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Introduction | lines 168-192 | no | yes | - | \section{Introduction} In this article, we are interested in the study of (non-compact) complete extremal K\"ahler metrics, defined on the complement of a simple normal crossing divisor $Z$ in an $n$-dimensional K\"ahler manifold $X$. Such metrics naturally appear (see e.g. \cite{Do2}) in attempts to apply continuity methods, or to study global properties of... |
| 10 | 0.434 | `corpus/arxiv/1302.6979/source/ambitoric2.tex` | `text` | Introduction | lines 228-276 | no | yes | toric surfaces | In dimension four, examples and theory come together to provide a moderately complete picture. Extremal K\"ahler surfaces of Calabi type are locally toric (as the base is a constant curvature Riemann surface) and there are specific results for toric surfaces: for example, K-polystability implies uniform K-polystability~\cite{Donaldson1,Sz2} and for constant... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_004 - toric Abreu equation

**Question:** Where does the corpus discuss symplectic potentials and scalar curvature on toric manifolds?

**Expected sources:** `dg-ga_9711014`, `2208.12493`, `0805.0128`
**Expected chunk types:** `definition`, `example`, `text`
**Expected terms:** `symplectic potential`, `scalar curvature`, `toric`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.770 | `corpus/arxiv/2108.12297/source/source.tex` | `text` | Weighted toric K-stability > Existence of $(\v,\w)$-cscK is equivalent to $(\v,\w)$-uniform K-stability | lines 1527-1530 | no | yes | symplectic potential | We now focus on the converse. We consider the space of normalized K\"ahler potentials $(\ref{normalized-compatible-potential})$ and normalized symplectic potentials |
| 2 | 0.615 | `corpus/arxiv/0905.0498/source/source.tex` | `text` | unsectioned | lines 115-134 | no | yes | scalar curvature, toric | ...ma$ of genus $\ge 2$. Building on ideas of Fujiki~\cite{fujiki}, we prove that $M$ admits a K\"ahler metric of constant scalar curvature if and only if $E$ is polystable. We also address the more general existence problem of extremal K\"ahler metrics on such bundles and prove that the splitting of $E$ as a direct sum of stable subbundles is necessary and suf... |
| 3 | 0.560 | `corpus/arxiv/1708.05253/source/source.tex` | `text` | Introduction | lines 324-376 | no | yes | scalar curvature, toric | In Section~\ref{s:lkr-sph}, we study the construction of toric K\"ahler metrics as Levi--K\"ahler quotients of products of spheres. Building on Theorem~\ref{t:toric}, we characterize such quotients in Theorem~\ref{t:product-spheres} as those associated to a polytope with the combinatorial type of a product of simplicies. In turn, Theorem~\ref{t:symplectic-po... |
| 4 | 0.525 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | %\begin{q} There is a few open questions for the Calabi dream manifolds: %\begin{enumerate} %\item What linear combinations of Chern numbers are nonnegative for all Calabi dream manifolds? %\item In Corollary 1.7, can we extend it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic to... |
| 5 | 0.520 | `corpus/arxiv/2208.12493/source/toric-lecture-notes.tex` | `text` | Existence: an overview > The canonical solution | lines 1819-1873 | yes | yes | scalar curvature, toric | \begin{thebibliography}{10} \bibitem{abreu0} M.~Abreu, {\it K{\"a}hler geometry of toric varieties and extremal metrics}, Internat. J. Math {\bf 9} (1998), 641--651. \bibitem{abreu} M.~Abreu, {\it K{\"a}hler metrics on toric orbifolds}, J. Differential Geom. {\bf 58} (2001), 151--187. \bibitem{ACGT2} V.~Apostolov, D.~M.~J. Calderbank, P.~Gauduchon and C.~T{\... |
| 6 | 0.517 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Appendix | lines 2405-2515 | no | yes | scalar curvature, toric | \bibitem{cc2} X.-X. Chen, J. Cheng. \newblock On the constant scalar curvature K\"ahler metrics(II): Existence results \newblock preprint. \bibitem{chenhe12} X.X. Chen and W-Y. He. \newblock The complex Monge-Amp\'{e}re equation on compact K\"{a}hler manifolds. \newblock Math. Ann. 354 (2012), no. 4, 1583--1600. \bibitem{CPZ} X.X. Chen, M. Paun and Yu Zeng.... |
| 7 | 0.509 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Introduction | lines 106-118 | no | yes | scalar curvature | \section{Introduction} Bando-Mabuchi \cite{BM} proved that K\"ahler-Einstein metric on Fano manifolds is unique up to holomorphic automorphisms in 1980s. Recently, Berndtsson \cite{Bo} generalized this uniqueness result to conic K\"ahler-Einstein metrics on Fano manifolds, by his observation on the convexity of certain energy functional (the $Ding$-functiona... |
| 8 | 0.509 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | Uniqueness of weighted cscK metrics | lines 1005-1042 | no | yes | scalar curvature, toric | \bibitem{Do-02} S.~K.~Donaldson, {\it Scalar curvature and stability of toric varieties}, J. Differential Geom. {\bf 62} (2002), 289--349. \bibitem{donaldson1} S.~K.~Donaldson, {\it Scalar curvature and projective embeddings {\rm II}.}, Q. J. Math. {\bf 56} (2005), no.3, 345--356. \bibitem{Gauduchon} P.~Gauduchon, {\rm Calabi's extremal metrics: An elementar... |
| 9 | 0.498 | `corpus/arxiv/dg-ga_9711014/paper.pdf` | `text` | unsectioned | p. 2 | yes | yes | scalar curvature, toric | ...n-torus T n such that the image of the cor- responding moment map φ is precisely ∆. The triple ( X∆,ω,φ ) is called a (symplectic) toric variety. It follows from the constructi on, due to Delzant [4], that X∆ comes also equipped with an intrinsic T n-invariant complex structure compatible with the intrinsic symplectic form. In other wor ds, X∆ has an in- tr... |
| 10 | 0.494 | `corpus/arxiv/math_0401320/source/hfkg2.tex` | `text` | Hamiltonian actions and toric geometry | lines 338-357 | no | yes | toric | \section{Hamiltonian actions and toric geometry}\label{s:hamtoric} We begin by reviewing hamiltonian torus actions, paying particular attention to the theory of toric K\"ahler manifolds. Toric K\"ahler geometry can be studied either from the complex or symplectic viewpoint, and we adopt, primarily, the latter. Furthermore, with a view to applications, we do... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_005 - toric Abreu equation

**Question:** Where does the corpus discuss labeled polytopes and extremal affine functions?

**Expected sources:** `1711.08424`, `2208.12493`, `0909.4512`
**Expected chunk types:** `definition`, `proposition`, `text`
**Expected terms:** `labeled polytope`, `extremal affine function`, `toric`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.990 | `corpus/arxiv/0909.4512/source/source.tex` | `definition` | Toric orbifolds and extremal metrics -- a quick survey. > Toric orbifolds and labeled polytopes. | line 171 | yes | yes | labeled polytope | \begin{definition}\label{defnPolytEquiv}The polytopes $\Delta\subset \mathfrak{t}^*$ and $\Delta' \subset \mathfrak{s}^*$ are \defin{equivalent} if there exists an affine isomorphism $\phi$ between the respective affine spaces so that $\phi(\Delta)=\Delta'$. Two labeled polytopes are \defin{equivalent} if the underlying polytopes are equivalent via an affine... |
| 2 | 0.711 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | Introduction | lines 320-321 | no | yes | - | where $\ell$ runs through all the affine functions. This interprets the non-Archimedean J-functional. |
| 3 | 0.700 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Applications and Discussions > Extremal K\"ahler metric | lines 1475-1478 | no | yes | - | \subsection{Extremal K\"ahler metric}\label{subsection 9.3} We discuss the situation of extremal K\"ahler(extK) metrics in Theorem~\ref{thm application 2}. To solve the extK equation, we need to choose $T$-invariant coordinates when defining weighted H\"older spaces, and we want to solve for $T$-invariant potential functions. Comparing the expansion of $\ome... |
| 4 | 0.875 | `corpus/arxiv/0909.4512/source/source.tex` | `text` | Introduction | lines 111-115 | yes | yes | labeled polytope, extremal affine function, toric | Note that our result provides a computable condition of relative $K$--stability for the labeled polytopes we consider and gives an explicit solution for the constant scalar curvature equation on labeled quadrilaterals. Indeed, constant functions are equipoised on any quadrilateral. Another natural class of examples is given by toric weakly Bocher-flat K\"ahl... |
| 5 | 0.679 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted toric Yau-Tian-Dolnaldson correspondence | lines 1932-1936 | no | yes | toric | ...Yau-Tian-Dolnaldson correspondence}{\label{s:ytd}} We consider a toric K\"ahler manifold $(X,\omega_0,\mathbb{T})$ with labeled Delzant polytope $(P, \textbf{L})$ \cite{VA4, TD}, where $\textbf{L} =(L_j)_{j=1}^k$ is the collection of non-negative affine linear functions defining $P$, with $dL_j$ being primitive elements of the lattice of circle subgroups of... |
| 6 | 0.656 | `corpus/arxiv/1008.2607/source/source.tex` | `text` | Some results via affine techniques > Calabi geometry | lines 801-806 | no | yes | - | \v In \cite{CLS}, we used the affine blow-up analysis to prove the following estimates. We only state the results for the Delzant polytopes. |
| 7 | 0.631 | `corpus/arxiv/2309.02279/source/document.tex` | `theorem` | Introduction | lines 86-88 | no | no | - | \begin{theorem}\label{thm:main} Let \((X,\alpha_T)\) be a \((v,w)\)-extremal manifold, where \(T\) is maximal in the hamiltonian isometry group of the weighted extremal metric, and the weight functions \(v,w\) satisfy Assumption \ref{ass:weights}. Then \((X,\alpha_T)\) is relatively weighted K-polystable. \end{theorem} |
| 8 | 0.523 | `corpus/arxiv/2110.08491/source/source.tex` | `text` | \bf Introduction | lines 205-208 | no | yes | toric | ...iew the notion of relative $\widehat K$-polystability and uniform $K$-polystability. In Section \ref{Sec-Estimates}, we discuss some properties of convex functions on polytopes. In Section \ref{Sec-4}, we prove the Theorem \ref{theorem_1.3}. In Section \ref{Sec-5}, after briefly reviewing homogeneous toric bundles and the generalized Abreu equation, we sketc... |
| 9 | 0.456 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Explicit Donaldson metrics on quadrilaterals > Toric Calabi type metrics | lines 1564-1581 | yes | yes | extremal affine function, toric | ...arbitrary real numbers. It thus follows that if $(\Delta,{\bf L})$ is a labelled trapezoid for which the corresponding extremal affine function $s_{(\Delta,{\bf L})}$ is parallel to the pair of parallel facets, then, by taking $F$ to be either one or two of the parallel facets of $\Delta$, the extremal affine function $s_{(\Delta,{\bf L},F)}$ must also be p... |
| 10 | 0.562 | `corpus/arxiv/0909.4512/source/source.tex` | `text` | Introduction | lines 117-124 | yes | yes | labeled polytope, extremal affine function, toric | The above theorem implies that for convex labeled quadrilaterals, the condition that $\zeta_{(\Delta,u)}$ is constant implies the $K$-stability of $(\Delta,u)$. It also provides an effective parametrization of the K\"ahler--Einstein solutions found in~\cite{exMS,other2,H2FII} in terms of classes of affine-equivalent convex quadrilaterals.\\ One geometric app... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_006 - toric Abreu equation

**Question:** Where does the corpus discuss Guillemin boundary conditions for toric Kahler metrics?

**Expected sources:** `dg-ga_9711014`, `2208.12493`, `0805.0128`
**Expected chunk types:** `definition`, `example`, `text`
**Expected terms:** `Guillemin`, `boundary conditions`, `symplectic potential`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.761 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Convex Preliminaries > Symplectic potentials | lines 1424-1433 | no | yes | Guillemin, symplectic potential | By the theory of Guillemin \cite{G94b} and Abreu \cite{Ab03}, there is the following correspondence for $S$-invariant K\"ahler metrics in $c_{1}(L_{P})$ and symplectic potentials. Let $u$ be a strictly convex function on $P^{\circ}$. The function $u$ is said to satisfy the {\it Guillemin's boundary condition} if it satisfies the following conditions: \begin{... |
| 2 | 0.725 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Labelled polytopes and the Abreu--Guillemin theory for K\"ahler metrics of Poincar\'e type > A class of Poincar\'e type toric K\"ahler metrics | lines 1003-1010 | no | yes | Guillemin, boundary conditions, symplectic potential | \subsection{A class of Poincar\'e type toric K\"ahler metrics} To link Conjectures~\ref{conjecture2} and \ref{conjecture1}, one needs a criterion ensuring that the Donaldson metric is of Poincar\'e type. We address this question in this section. We start by introducing a class of toric metrics in the form \eqref{toric-g} on $(\Delta^0 \times \T)$ via a certa... |
| 3 | 0.721 | `corpus/arxiv/0805.0128/source/extremal2a.tex` | `text` | Introduction | lines 81-102 | yes | yes | Guillemin, boundary conditions | ...(We often use the notation $u^{ij}_{ij}$ for the left-hand side of (1).) A solution of this equation, with appropriate boundary behaviour, is a critical point, in fact the minimiser, of ${\cal M}$. More precisely, we require $u$ to satisfy {\it Guillemin boundary conditions}, which depend on the measure $\sigma$. We refer to the previous papers cited for th... |
| 4 | 0.681 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | Coercivity for the toric case > Torus-invariant metrics | lines 907-909 | no | yes | Guillemin | is called toric potential. By the standard Delzant construction, one can prove that $u$ defines a convex function on $P^\circ$. Moreover, $u$ is characterized by the Guillemin boundary condition. That is, if $P$ is written in the form |
| 5 | 0.670 | `corpus/arxiv/0909.4512/source/source.tex` | `text` | Introduction | lines 68-70 | no | yes | boundary conditions, symplectic potential | ...d{equation} These expressions use the standard identifications $(\bR^n)^* \simeq \bR^n$, $T_{x}\bR^n \simeq \bR^n$. The boundary conditions (\ref{condCOMPACTIFonH}) are elaborated in~\cite{H2FII} and are equivalent to the boundary conditions in~\cite{don:estimate} and~\cite{abreuOrbifold}. When $(\Delta,u)$ is a rational labeled polytope corresponding to a s... |
| 6 | 0.640 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted toric Yau-Tian-Dolnaldson correspondence > Existence via estimates | lines 1980-1988 | no | yes | Guillemin, boundary conditions, symplectic potential | ...ectic potentials, i.e. the space of continuous convex functions on \(P\), smooth in the interior \(P^0\), which satisfy Guillemin's boundary conditions defined in \cite{Gui}. It is well known that each Kähler potential defines a Kähler structure on \(X\) \cite{SKD, Gui}. We denote by \(\mathrm{Scal}_\v(u) : P \longrightarrow \mathbb{R}\) the weighted scalar... |
| 7 | 0.558 | `corpus/arxiv/math_0401320/source/hfkg2.tex` | `text` | Hamiltonian actions and toric geometry > Compatible K\"ahler metrics: compactification | lines 676-699 | no | yes | boundary conditions | ...o compatible uniformizing charts. On the other hand we learn nothing about the dependence of the angular coordinates on metrics which induce different $S^2\mathfrak{t}$-valued functions on the interior of the Delzant polytope. Thus the above lemma does not suffice to clarify Abreu's proof. The issue of the compactification of toric K\"ahler metrics is an imp... |
| 8 | 0.503 | `corpus/arxiv/dg-ga_9711014/paper.pdf` | `text` | unsectioned | p. 1 | yes | yes | Guillemin | arXiv:dg-ga/9711014v1 19 Nov 1997 K¨ ahler Geometry of Toric Varieties and Extremal Metrics Miguel Abreu ∗ Institute for Advanced Study revised version November 26, 2024 1991 Mathematics Subject Classiﬁcation: Primary 53C55, Se condary 14M25 53C25 58F05. Abstract A (symplectic) toric variety X, of real dimension 2 n, is completely determined by its moment po... |
| 9 | 0.480 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 10 | 0.462 | `corpus/arxiv/1008.2607/source/source.tex` | `text` | Introduction | lines 99-167 | no | yes | Guillemin | \section{Introduction} \v\n Extremal metrics, introduced by E. Calabi, have been studied intensively in the past 20 years. There are three aspects of the topic: sufficient conditions for existence, necessary conditions for existence and the uniqueness of extremal metric. The necessary conditions for the existence are conjectured to be related to certain stab... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_007 - toric Abreu equation

**Question:** Where does the corpus discuss K-stability or uniform K-stability for toric varieties?

**Expected sources:** `1610.07998`, `2110.10386`, `2110.08491`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `toric`, `uniform K-stability`, `K-energy`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.839 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | Coercivity for the toric case > Toric test configurations | lines 1041-1044 | yes | yes | toric, uniform K-stability | defined for any normalized convex function $f$, continuous up to the boundary. The definition is valid only for the toric situation, however, it is powerful to simplify the arguments. We introduce the equivalent definitions of toric uniform K-stability by the following proposition. |
| 2 | 0.684 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction | lines 123-127 | no | yes | uniform K-stability | This strengthens results of Odaka \cite{O2} and Odaka-Sano \cite{OS}, who proved K-stability under the same hypotheses. We remark that it is known that the above varieties admit K\"ahler-Einstein metrics. However we also prove uniform K-stability in \emph{explicit neighbourhoods} of the (anti)-canonical classes on varieties of general type and also Fano vari... |
| 3 | 0.620 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | unsectioned | lines 162-212 | no | yes | toric, uniform K-stability | An interesting testing ground for these ideas is the case of toric varieties, which was developed by Donaldson. In~\cite{Don02} he showed that in the case of toric surfaces K-stability implies that the Mabuchi functional is bounded from below (this was later extended by Zhou-Zhu~\cite{ZZ06} to show properness of the Mabuchi functional) and a minimising seque... |
| 4 | 0.588 | `corpus/arxiv/2208.12493/source/toric-lecture-notes.tex` | `text` | Uniform K-stability | lines 1516-1519 | no | yes | toric, uniform K-stability | Using that convex PL functions are dense in $\cC(\Delta)$ (see Remark~\ref{r:density}), uniform K-stability can be equivalently introduced by requiring that the condition (i) of Proposition~\ref{p:uniform-K-stability} is satisfied on convex PL functions. Thus, uniform K-stability (with respect to any tamed norm) is a stronger condition on $(\Delta, {\bf L})$... |
| 5 | 0.585 | `corpus/arxiv/1603.01026/source/source.tex` | `text` | Test configurations as non-Archimedean metrics > Uniform K-stability | lines 1349-1364 | no | yes | uniform K-stability | ...sible. See~\cite[Proposition~8.2]{BHJ1} for details. The fact that $J^\NA(\phi)=0$ iff $\phi=\phi_\triv+c$ implies that uniform K-stability is stronger than K-stability as introduced by \cite{Tian97,Don2}. Our notion of uniform K-stability is equivalent to uniform K-stability defined either with respect to the $L^1$-norm or the minimum norm in the sense of~\... |
| 6 | 0.572 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 635-663 | no | yes | uniform K-stability | ...\"ahler class, the existence of cscK metrics in the K\"ahler class is equivalent to an algebro-geometric notion called "K-stability". \smallskip Several progresses in the literature \cite{Darvas_Rubinstein_2017, Berman_Darvas_Lu_2020, Chen_Cheng_2021_1, Chen_Cheng_2021_2} have shown that the existence of a unique cscK metric in a K\"ahler class is equivalent... |
| 7 | 0.564 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | toric | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 8 | 0.542 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Proof of Theorem \ref{suff} | lines 2778-2847 | yes | yes | toric, uniform K-stability, K-energy | ...gin{acknowledgements} %\end{acknowledgements} \begin{thebibliography}{99} \bibitem{Ab03} M.~Abreu, K\"ahler geometry of toric manifolds in symplectic coordinates. \emph{Symplectic and contact topology: interactions and perspectives (Toronto, ON/Montreal, QC, 2001)}, 1--24, Fields Inst. Commun., \textbf{35}, \emph{Amer. Math. Soc., Providence, RI}, 2003. \bib... |
| 9 | 0.533 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | ...in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except in the Fano manifold where the authors proved it indirectly in route of CDS's theorem.\\ We have the following theorem which is useful to our characterization of borderline case. |
| 10 | 0.518 | `corpus/arxiv/1602.03114/source/source.tex` | `text` | Introduction and main results | lines 182-199 | no | yes | toric, uniform K-stability | \paragraph*{Further relations to previous results.} We end the introduction with a brief (but by no means complete) discussion about further relations to previous results. Much work has been done on Tian's properness conjectures in the case when the K\"ahler class is anti-canonical and we refer to \cite{DR17} for a detailed historical account. To our knowled... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_008 - toric Abreu equation

**Question:** Where does the corpus discuss Donaldson scalar curvature and stability of toric varieties?

**Expected sources:** `dg-ga_9711014`, `corpus/my_notes/requested_non_arxiv_sources.md`
**Expected chunk types:** `theorem`, `text`
**Expected terms:** `scalar curvature`, `stability`, `toric varieties`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.787 | `corpus/arxiv/2110.08491/source/source.tex` | `remark` | \bf Introduction | lines 200-204 | no | no | scalar curvature, stability | \begin{remark} In \cite{Del}, Delcroix expressed $K$-stability of polarized spherical varieties in terms of combinatorial data and provided a combinatorial sufficient condition of $G$-uniform $K$-stability. The appendix of \cite{Del} by Yuji Odaka showed that for non-singular spherical varieties, $G$-uniform $K$-stability is equivalent to existence of cscK m... |
| 2 | 0.546 | `corpus/arxiv/1008.2607/source/source.tex` | `text` | Introduction | lines 99-167 | no | yes | scalar curvature, stability, toric varieties | ...On the other hand, there has been no much progress on the existence of extremal metrics or K\"ahler metrics of constant scalar curvature. One reason is that the equation is highly nonlinear and of fourth order. The problem is to solve the equation under certain necessary stability conditions. It was Tian who first gave an analytic ``stability" condition and... |
| 3 | 0.490 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Appendix | lines 2405-2515 | no | yes | scalar curvature, stability, toric varieties | \bibitem{cc2} X.-X. Chen, J. Cheng. \newblock On the constant scalar curvature K\"ahler metrics(II): Existence results \newblock preprint. \bibitem{chenhe12} X.X. Chen and W-Y. He. \newblock The complex Monge-Amp\'{e}re equation on compact K\"{a}hler manifolds. \newblock Math. Ann. 354 (2012), no. 4, 1583--1600. \bibitem{CPZ} X.X. Chen, M. Paun and Yu Zeng.... |
| 4 | 0.487 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | toric varieties | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 5 | 0.476 | `corpus/arxiv/0706.0505/source/source.tex` | `text` | unsectioned | lines 815-886 | no | yes | scalar curvature, stability, toric varieties | \begin{thebibliography}{Gua} \bibitem[Ab]{Ab} Abreu, M., K\"ahler geometry of toric varieties and extremal metrics, Inter. J. Math. Vol 9 (1998), 641-651. %\bibitem[Ca] {Ca} Calabi, E., Extremal K\"ahler metrics. %Seminar on differential geometry, Ann. of Math Stud., Princeton %Univ. Press, Princeton, N.J., Vol 102 (1982), 259-290. \bibitem [D1] {Do} Donalds... |
| 6 | 0.476 | `corpus/arxiv/0905.0498/source/source.tex` | `text` | Compatible extremal almost K\"ahler metrics | lines 2826-2899 | no | yes | scalar curvature, stability, toric varieties | \bibitem{Do0} S.~K.~Donaldson, {\it Infinite determinants, stable bundles and curvature}, Duke Math. J. {\bf 54} (1987), 231--247. \bibitem{Do} S.~K.~Donaldson, {\it Remarks on gauge theory, complex geometry and $4$-dimensional topology}, Fields Medalists' Lectures, 384--403, World Sci. Ser. 20th Century Math. {\bf 5}, World. Sci. Publishing, River Edge, NJ,... |
| 7 | 0.468 | `corpus/arxiv/math_0412518/source/slopeobs_archive.tex` | `text` | Introduction > Acknowledgments | lines 213-225 | no | yes | stability | \subsection*{Acknowledgments}\ \vskip 5pt We would most like to thank Simon Donaldson, who suggested looking at stability of projective bundles $\PP(E)$ via the degeneration mentioned in (\ref{ext1}). As we discuss there, the deformation to the normal cone collapses to this degeneration in one special case, and it was this case that motivated our study of th... |
| 8 | 0.458 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | unsectioned | lines 162-212 | no | yes | scalar curvature, stability, toric varieties | An interesting testing ground for these ideas is the case of toric varieties, which was developed by Donaldson. In~\cite{Don02} he showed that in the case of toric surfaces K-stability implies that the Mabuchi functional is bounded from below (this was later extended by Zhou-Zhu~\cite{ZZ06} to show properness of the Mabuchi functional) and a minimising seque... |
| 9 | 0.450 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | Uniqueness of weighted cscK metrics | lines 1005-1042 | no | yes | scalar curvature, stability, toric varieties | \bibitem{Do-02} S.~K.~Donaldson, {\it Scalar curvature and stability of toric varieties}, J. Differential Geom. {\bf 62} (2002), 289--349. \bibitem{donaldson1} S.~K.~Donaldson, {\it Scalar curvature and projective embeddings {\rm II}.}, Q. J. Math. {\bf 56} (2005), no.3, 345--356. \bibitem{Gauduchon} P.~Gauduchon, {\rm Calabi's extremal metrics: An elementar... |
| 10 | 0.446 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Proof of Theorem \ref{suff} | lines 2848-2920 | no | yes | scalar curvature, stability, toric varieties | \bibitem{CLS18} B.~Chen, A.~M.~Li and L.~Sheng, Extremal metrics on toric surfaces. \emph{Adv. Math.} \textbf{340} (2018), 363--405. \bibitem{Ch00a} X.~X.~Chen, The space of K\"ahler metrics. \emph{J. Differential Geom.} \textbf{56} (2000) no.2, 189--234. \bibitem{Ch00b} X.~X.~Chen, On the lower bound of the Mabuchi energy and its application. \emph{Internat... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_009 - toric Abreu equation

**Question:** Where does the corpus discuss toric Yau-Tian-Donaldson results for extremal metrics?

**Expected sources:** `2110.10386`, `2110.08491`, `1610.07998`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `Yau-Tian-Donaldson`, `toric`, `extremal metrics`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.750 | `corpus/arxiv/1302.6979/source/ambitoric2.tex` | `text` | Extremal ambitoric $4$-orbifolds and convex quadrilaterals > Extremal ambitoric orbifolds and K-polystability | lines 1540-1544 | no | yes | toric | We now generalize these results to arbitrary quadrilaterals, on which we relate the existence of ambitoric extremal K\"ahler metrics to the toric K-polystability criteria. |
| 2 | 0.720 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Introduction > Stability properties w.r.t. weights > Yau-Tian-Donaldson correspondence in the toric case | lines 317-318 | no | yes | Yau-Tian-Donaldson, toric | \subsubsection*{Yau-Tian-Donaldson correspondence in the toric case} We address the existence problem in the toric setting: |
| 3 | 0.594 | `corpus/arxiv/2110.08491/source/source.tex` | `text` | \bf Introduction | lines 160-167 | yes | yes | Yau-Tian-Donaldson, toric, extremal metrics | This conjecture were generalized to extremal metrics. Recently, there have been many progresses towards this conjecture (see \cite{BDL2}, \cite{CC1}, \cite{CC2}, \cite{DL}, \cite{Li}). \v In a sequence of papers, Donaldson initiated a program to study the extremal metrics on toric manifolds: Donaldson formulated $K$-stability for polytopes and conjectured th... |
| 4 | 0.527 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `text` | Introduction | lines 251-260 | no | yes | toric | We discuss in~\S\ref{sectFORMALsol} consequences of this last result and open problems in relation with the relative toric version of the Yau--Tian--Donaldson conjecture. In the next section we gather facts, definition, key results and recall brief explanations on the topic of toric extremal (almost) K\"ahler metrics. Section~\ref{sectMAIN} contains the proo... |
| 5 | 0.525 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Introduction | lines 82-96 | yes | yes | Yau-Tian-Donaldson, toric | ...quivalent to that $\operatorname{grad}_{\omega}^{(1, 0)}(s(\omega)-\overline{s})$ is a holomorphic vector field on $X$. Extremal K\"ahler metrics have been widely studied as canonical K\"ahler metrics containing constant scalar curvature K\"ahler metrics and in particular K\"ahler-Einstein metrics. Especially, the existence problem of extremal K\"ahler metri... |
| 6 | 0.509 | `corpus/arxiv/1401.0123/source/ExtPK.tex` | `text` | Introduction | lines 205-223 | no | yes | Yau-Tian-Donaldson, extremal metrics | ...s of K�hler classes on compact K�hler manifolds, generalising the K�hler-Einstein problem, E. Calabi introduced \textit{extremal K�hler metrics}, defined as the minimisers of the $L^2$-norm of the Ricci tensor among a fixed class \cite{cal}. Extremal metrics turn out to satisfy rich geometric properties, e.g. maximality of the group of isometric automorphism... |
| 7 | 0.493 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | unsectioned | lines 114-137 | no | yes | Yau-Tian-Donaldson | \title[Existence, Properness and Geodesic stability]{Existence of constant scalar curvature K\"ahler cone metrics, properness and geodesic stability} \author{Kai Zheng} % \address{University of Warwick} \curraddr{Tongji University, Shanghai 200092, P.R. CHINA} \email[Kai Zheng]{kaizheng@amss.ac.cn} %\date{\today} \begin{document} \maketitle \begin{abstract}... |
| 8 | 0.485 | `corpus/arxiv/0905.0498/source/source.tex` | `text` | unsectioned | lines 115-134 | no | yes | toric | ...ic of constant scalar curvature if and only if $E$ is polystable. We also address the more general existence problem of extremal K\"ahler metrics on such bundles and prove that the splitting of $E$ as a direct sum of stable subbundles is necessary and sufficient condition for the existence of extremal K\"ahler metrics in sufficiently small K\"ahler classes.... |
| 9 | 0.476 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Introduction > The weighted constant scalar curvature problem | lines 241-248 | no | yes | Yau-Tian-Donaldson, toric | ...t as for the usual Calabi Ansatz, one can attempt to study the existence problem for weighted constant scalar curvature metrics on $Y$ indirectly by studying a different existence problem on the fiber $M$. The perspective that we take in this paper is to restrict attention to the situation where $M$ is toric and our torus $\T$ satisfies $\dim_\R \T = \dim_\C... |
| 10 | 0.449 | `corpus/arxiv/1004.2012/source/Kempf_Ness_uniqueness_12272011.tex` | `text` | Further Discussions | lines 1921-1968 | no | yes | Yau-Tian-Donaldson, extremal metrics | \section{Further Discussions} There are also some further interesting questions. \begin{prob} A general notion of optimal degenerations and its relation to the Calabi flow. Generalize the theorem to the uniqueness of some ``canonical" objects in the closure, allowing the occurrence of singularities. On the other hand, by the Yau-Tian-Donaldson conjecture, on... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_010 - toric Abreu equation

**Question:** Where does the corpus discuss Hamiltonian 2-forms and extremal toric metrics?

**Expected sources:** `math_0202280`, `math_0401320`, `math_0511118`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `Hamiltonian 2-forms`, `extremal`, `toric`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.830 | `corpus/arxiv/0909.4512/source/source.tex` | `text` | Calabi toric structures and trapezoids. > K\"ahler toric $4$-orbifolds with non-trivial Hamiltonian $2$--forms. | lines 562-563 | no | yes | toric | The classification of Hamiltonian $2$--forms on symplectic toric $4$--orbifolds claimed in the introduction follows from the following proposition together with Proposition~\ref{lemCALABItoricFunc} and the fact that orthotoric metrics characterize the ones admitting Hamiltonian $2$-forms of order two~\cite{H2FI}. |
| 2 | 0.536 | `corpus/arxiv/math_0401320/source/hfkg2.tex` | `text` | unsectioned | lines 215-250 | yes | yes | extremal, toric | The main goal of this paper is to show that a compact K\"ahler manifold with a hamiltonian $2$-form of order $\ell$ is necessarily biholomorphic to a projective bundle $M$ of the form described above, and conversely to show precisely how to construct K\"ahler metrics with hamiltonian $2$-forms of order $\ell$ on such bundles. We hope however, that with the v... |
| 3 | 0.525 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Proofs of Lemmas \ref{s1is2}, \ref{s1is1} and \ref{s1is2overk} | lines 1659-1726 | no | yes | extremal | \begin{thebibliography}{99} %\bibitem{atiyah} M.~F.~Atiyah, {\it Convexity and commuting hamiltonians}, %Bull. London Math. Soc. {\bf 14} (1982), 1--15. \bibitem{ACG1} V. Apostolov, D.~M.~J. Calderbank and P. Gauduchon, {\it The geometry of weakly self-dual K\"ahler surfaces}, Compositio Math. {\bf 135} (2003), 279--322. \bibitem{ACG2} V. Apostolov, D.~M.~J.... |
| 4 | 0.501 | `corpus/arxiv/math_0202280/source/source.tex` | `text` | unsectioned | lines 164-214 | yes | yes | extremal, toric | Our main result shows that any K\"ahler manifold with a hamiltonian $2$-form induces a (local) semisimple rigid $\ell$-torus action $(\ell\leq m)$ with orthotoric fibres, and that conversely, such an explicit K\"ahler metric has a hamiltonian $2$-form. From this we deduce a local classification of weakly Bochner-flat K\"ahler metrics, rederiving in particula... |
| 5 | 0.568 | `corpus/arxiv/0909.4512/source/source.tex` | `text` | Introduction | lines 132-142 | no | yes | extremal, toric | Note that explicit Sasaki--Einstein metrics of this type have been found in~\cite{exMS,other2} and toric Sasaki--Einstein metrics have been systematically studied in~\cite{futakiChoOno,futakiOnoWang}.\\ In order to prove Theorem~\ref{mainTHEOparall}, we consider the cases of \defin{generic} labeled quadrilaterals (that is, quadrilaterals which have no parall... |
| 6 | 0.431 | `corpus/arxiv/1302.6979/source/ambitoric2.tex` | `text` | Introduction | lines 228-276 | no | yes | extremal, toric | In dimension four, examples and theory come together to provide a moderately complete picture. Extremal K\"ahler surfaces of Calabi type are locally toric (as the base is a constant curvature Riemann surface) and there are specific results for toric surfaces: for example, K-polystability implies uniform K-polystability~\cite{Donaldson1,Sz2} and for constant... |
| 7 | 0.418 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Proof of Theorem \ref{suff} | lines 2778-2847 | no | yes | Hamiltonian 2-forms, extremal, toric | ...gin{acknowledgements} %\end{acknowledgements} \begin{thebibliography}{99} \bibitem{Ab03} M.~Abreu, K\"ahler geometry of toric manifolds in symplectic coordinates. \emph{Symplectic and contact topology: interactions and perspectives (Toronto, ON/Montreal, QC, 2001)}, 1--24, Fields Inst. Commun., \textbf{35}, \emph{Amer. Math. Soc., Providence, RI}, 2003. \bib... |
| 8 | 0.403 | `corpus/arxiv/0905.0498/source/source.tex` | `text` | Compatible extremal almost K\"ahler metrics | lines 2754-2825 | no | yes | Hamiltonian 2-forms, extremal, toric | \begin{thebibliography}{99} \bibitem{Abreu0} M.~Abreu, {\it K{\"a}hler geometry of toric varieties and extremal metrics}, Internat. J. Math {\bf 9} (1998), 641--651. \bibitem{Abreu1} M.~Abreu, {\it K{\"a}hler metrics on toric orbifolds}, J. Differential Geom. {\bf 58} (2001), 151--187. \bibitem{hfkg1} V.~Apostolov, D.~M.~J. Calderbank and P.~Gauduchon, {\it... |
| 9 | 0.395 | `corpus/arxiv/1510.02226/source/source.tex` | `text` | Resolution of singularities of type $\TI$ > Resolution of extremal K\"ahler metrics | lines 1542-1596 | no | yes | extremal, toric | Theorem~\ref{theo:extremal} is just a consequence of the above corollary. \begin{thebibliography}{10} \bibitem{abreu0} M. Abreu, {\it K\"ahler geometry of toric manifolds in symplectic coordinates}, in ``Symplectic and contact topology: Interactions and Perspectives'', Eliashberg, Khesin, Lalonde (eds.), Fields Institute Communications, {\bf 35} (2003), 1--2... |
| 10 | 0.490 | `corpus/arxiv/math_0401320/source/hfkg2.tex` | `text` | unsectioned | lines 119-149 | yes | yes | extremal, toric | The first is the notion of a rigid hamiltonian torus action. This natural condition, for torus actions on a K\"ahler manifold, was introduced locally in part I, but such actions turn out to be remarkably well behaved globally, leading to a fairly explicit classification: up to a blow-up, compact K\"ahler manifolds with a rigid hamiltonian torus action are bu... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_011 - toric Abreu equation

**Question:** Where does the corpus discuss ambitoric geometry and extremal toric surfaces?

**Expected sources:** `1302.6979`, `1302.6975`
**Expected chunk types:** `theorem`, `definition`, `text`
**Expected terms:** `ambitoric`, `extremal toric surfaces`, `Einstein`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.677 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Explicit Donaldson metrics on quadrilaterals > Ambitoric structures | line 1356 | no | yes | ambitoric | \subsection{Ambitoric structures} Here we briefly review the explicit construction of extremal toric metrics for $n=2$ via the ambitoric ansatz of \cite{ACG1}. |
| 2 | 0.657 | `corpus/arxiv/1302.6975/source/ambitoric1.tex` | `text` | Ambitoric geometry | lines 692-697 | yes | yes | ambitoric | \section{Ambitoric geometry} Ambitoric geometry concerns ambik\"ahler structures for which both K\"ahler metrics are toric with respect to a common $T^2$-action; the pointwise geometry is the following. |
| 3 | 0.612 | `corpus/arxiv/1302.6979/source/ambitoric2.tex` | `text` | Extremal ambitoric $4$-orbifolds and convex quadrilaterals > Extremal ambitoric metrics and adapted factorizations | lines 1427-1434 | yes | yes | ambitoric | \subsection{Extremal ambitoric metrics and adapted factorizations} \label{s:extremal} A toric K\"ahler metric is extremal if and only if its scalar curvature is equal to the extremal affine function. For regular ambitoric structures, a straightforward computation of the scalar curvatures of the two K\"ahler metrics yields the following result~\cite{ACG1}. |
| 4 | 0.454 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 5 | 0.445 | `corpus/arxiv/1510.02226/source/source.tex` | `text` | Resolution of singularities of type $\TI$ > Resolution of extremal K\"ahler metrics | lines 1542-1596 | no | yes | ambitoric, extremal toric surfaces, Einstein | Theorem~\ref{theo:extremal} is just a consequence of the above corollary. \begin{thebibliography}{10} \bibitem{abreu0} M. Abreu, {\it K\"ahler geometry of toric manifolds in symplectic coordinates}, in ``Symplectic and contact topology: Interactions and Perspectives'', Eliashberg, Khesin, Lalonde (eds.), Fields Institute Communications, {\bf 35} (2003), 1--2... |
| 6 | 0.429 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Proofs of Lemmas \ref{s1is2}, \ref{s1is1} and \ref{s1is2overk} | lines 1659-1726 | no | yes | Einstein | .... London Math. Soc. {\bf 14} (1982), 1--15. \bibitem{ACG1} V. Apostolov, D.~M.~J. Calderbank and P. Gauduchon, {\it The geometry of weakly self-dual K\"ahler surfaces}, Compositio Math. {\bf 135} (2003), 279--322. \bibitem{ACG2} V. Apostolov, D.~M.~J. Calderbank and P. Gauduchon, {\it Hamiltonian $2$-forms in K\"ahler geometry} I {\it General Theory}, J. Dif... |
| 7 | 0.522 | `corpus/arxiv/1302.6979/source/ambitoric2.tex` | `text` | Introduction | lines 277-335 | yes | yes | ambitoric, Einstein | ...hm:stability}, which establishes, for quadrilaterals, Donaldson's conjecture~\cite{Donaldson1} that the existence of an extremal K\"ahler metric is equivalent to relative K-polystability with respect to toric degenerations. Indeed, we show that temperate quadrilaterals admit a factorization structure which relates the polystability condition directly to the... |
| 8 | 0.410 | `corpus/arxiv/1512.06391/source/source.tex` | `text` | Further observations > Computing the Futaki invariant > The Futaki invariant of $\C P^1 \times \C P^1$ and the classification of toric Einstein--Maxwell metrics | lines 1288-1332 | no | yes | ambitoric, extremal toric surfaces, Einstein | \begin{thebibliography}{10} \bibitem{abreu0} M.~Abreu, {\it K{\"a}hler geometry of toric varieties and extremal metrics}, Internat. J. Math {\bf 9} (1998), 641--651. \bibitem{abreu} M.~Abreu, {\it K{\"a}hler metrics on toric orbifolds}, J. Differential Geom. {\bf 58} (2001), 151--187. \bibitem{AG} V. Apostolov and P. Gauduchon, {\it The Riemannian Goldberg--... |
| 9 | 0.395 | `corpus/arxiv/1808.07811/source/source.tex` | `text` | The structure of the automorphism group and stability of the $(\uu,\vv)$-cscK metrics under deformations | lines 2136-2186 | no | yes | ambitoric, Einstein | ...ility theorem in \cite{LS} (see also \cite{FS}). \begin{thebibliography}{99} \bibitem{abreu0} M.~Abreu, {\it K{\"a}hler geometry of toric varieties and extremal metrics}, Internat. J. Math {\bf 9} (1998), 641--651. \bibitem{abreu} M.~Abreu, {\it K{\"a}hler metrics on toric orbifolds}, J. Differential Geom. {\bf 58} (2001), 151--187. \bibitem{AC} V. Apostolov... |
| 10 | 0.391 | `corpus/arxiv/1708.05253/source/source.tex` | `text` | Curvature of Levi--K\"ahler quotients of products of spheres > Extremal Levi--K\"ahler quotients > CSC Levi--K\"ahler quotients of $\Sph^5\times \Sph^3$ | lines 2984-3048 | no | yes | ambitoric, extremal toric surfaces, Einstein | ...ic and $F(x)=-c(x^2-1)(x-\beta)(x -\eta) (x-\gamma)$ (resp. $F(x)=-c(x^2-1)(x-\beta)(x -\eta)$), one gets an ansatz for extremal (resp. constant scalar curvature) toric orbifolds, which are also Levi--K\"ahler quotients of $\Sph^5 \times \Sph^3$. We further specialize to the constant scalar curvature case, i.e. $F(x)=-c(x^2-1)(x-\beta)(x -\eta)$ for a non-ze... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_012 - toric Abreu equation

**Question:** Where does the corpus discuss toric projective bundles and extremal Kahler metrics?

**Expected sources:** `0905.0498`, `0909.4512`
**Expected chunk types:** `theorem`, `example`, `text`
**Expected terms:** `projective bundles`, `extremal Kahler`, `toric`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.635 | `corpus/arxiv/0905.0498/source/source.tex` | `remark` | Rigid toric bundles and the generalized Calabi construction > Proof of Theorem \ref{th:small-classes} | lines 2063-2066 | yes | no | toric | \begin{rem}\label{trivial-corollary} As any invariant K\"ahler metric on a toric manifold is compatible, Theorem~\ref{th:small-classes} implies the existence of (compatible) extremal metrics on a rigid semisimple toric bundles $M$ over a CSC locally product K\"ahler manifold, in the case when there are no blow-downs and $W=V$ is a toric extremal K\"ahler man... |
| 2 | 0.425 | `corpus/arxiv/math_0401320/source/hfkg2.tex` | `text` | unsectioned | lines 215-250 | no | yes | projective bundles, toric | ...to show that a compact K\"ahler manifold with a hamiltonian $2$-form of order $\ell$ is necessarily biholomorphic to a projective bundle $M$ of the form described above, and conversely to show precisely how to construct K\"ahler metrics with hamiltonian $2$-forms of order $\ell$ on such bundles. We hope however, that with the various motivations discussed a... |
| 3 | 0.420 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Proofs of Lemmas \ref{s1is2}, \ref{s1is1} and \ref{s1is2overk} | lines 1659-1726 | no | yes | projective bundles | ....~M.~J. Calderbank, P. Gauduchon and C. T{\o}nnesen-Friedman, {\it Hamiltonian $2$-forms in K\"ahler geometry} III {\it Extremal metrics and stability}, arXiv:math.DG/??????? \bibitem{Bando-Mabuchi} S. Bando and T. Mabuchi, {\it Uniqueness of Einstein--K\"ahler metrics modulo connected group actions}, in `Algebraic Geometry' (Sendai 1985), Adv. Stud. Pure Ma... |
| 4 | 0.419 | `corpus/arxiv/math_0511118/source/source.tex` | `text` | unsectioned | lines 119-165 | no | yes | projective bundles | We obtain a characterization, on a large family of projective bundles, of those `admissible' K\"ahler classes (i.e., the ones compatible with the bundle structure in a way we make precise) which contain an extremal K\"ahler metric. In many cases, such as on geometrically ruled surfaces, every K\"ahler class is admissible. In particular, our results complete... |
| 5 | 0.418 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | unsectioned | lines 146-172 | no | yes | toric | ...zza, Simon Jubert and Abdellah Lahdili} \begin{document} \begin{abstract} In this paper we investigate the existence of metrics with weighted constant scalar curvature (wcscK for short) on a compact Kähler manifold $X$: this notion include constant scalar curvature K\"ahler metrics, weighted solitons, Calabi’s extremal Kähler metrics and extremal metric on s... |
| 6 | 0.414 | `corpus/arxiv/1808.02813/source/source.tex` | `text` | unsectioned | lines 130-137 | no | yes | projective bundles, toric | \begin{abstract} We study the existence of weighted extremal K\"ahler metrics in the sense of \cite{aclg17,lahdili} on the total space of an admissible projective bundle over a Hodge K\"ahler manifold of constant scalar curvature. Admissible projective bundles have been defined in \cite{acgt}, and they include the projective line bundles~\cite{hwang-singer}... |
| 7 | 0.391 | `corpus/arxiv/1808.07811/source/source.tex` | `text` | The structure of the automorphism group and stability of the $(\uu,\vv)$-cscK metrics under deformations | lines 2136-2186 | no | yes | projective bundles, toric | ...m in \cite{LS} (see also \cite{FS}). \begin{thebibliography}{99} \bibitem{abreu0} M.~Abreu, {\it K{\"a}hler geometry of toric varieties and extremal metrics}, Internat. J. Math {\bf 9} (1998), 641--651. \bibitem{abreu} M.~Abreu, {\it K{\"a}hler metrics on toric orbifolds}, J. Differential Geom. {\bf 58} (2001), 151--187. \bibitem{AC} V. Apostolov and D.~M.~J... |
| 8 | 0.376 | `corpus/arxiv/1302.6979/source/ambitoric2.tex` | `text` | Introduction | lines 277-335 | no | yes | toric | ...hm:stability}, which establishes, for quadrilaterals, Donaldson's conjecture~\cite{Donaldson1} that the existence of an extremal K\"ahler metric is equivalent to relative K-polystability with respect to toric degenerations. Indeed, we show that temperate quadrilaterals admit a factorization structure which relates the polystability condition directly to the... |
| 9 | 0.368 | `corpus/arxiv/0909.4512/source/source.tex` | `text` | Introduction | lines 132-142 | yes | yes | toric | Note that explicit Sasaki--Einstein metrics of this type have been found in~\cite{exMS,other2} and toric Sasaki--Einstein metrics have been systematically studied in~\cite{futakiChoOno,futakiOnoWang}.\\ In order to prove Theorem~\ref{mainTHEOparall}, we consider the cases of \defin{generic} labeled quadrilaterals (that is, quadrilaterals which have no parall... |
| 10 | 0.364 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Introduction | lines 168-192 | no | yes | toric | \section{Introduction} In this article, we are interested in the study of (non-compact) complete extremal K\"ahler metrics, defined on the complement of a simple normal crossing divisor $Z$ in an $n$-dimensional K\"ahler manifold $X$. Such metrics naturally appear (see e.g. \cite{Do2}) in attempts to apply continuity methods, or to study global properties of... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_013 - toric Abreu equation

**Question:** Where does the corpus discuss relative K-stability and extremal metrics in the toric setting?

**Expected sources:** `math_0611002`, `0912.4095`, `2110.10386`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `relative K-stability`, `extremal metrics`, `toric`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.584 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Relative weighted K-stability > Relative weighted K-(semi/poly)stability | lines 474-483 | no | yes | relative K-stability | \subsection{Relative weighted K-(semi/poly)stability} In this section we introduce notions of relative weighted K-(semi/poly)stability. In the non-weighted setting, relative K-stability was initially introduced by Sz{\'e}kelyhidi \cite{Sze07} for algebraic varieties, and later extended to the K{\"a}hler setting by Dervan \cite{Der18}. Although relative weigh... |
| 2 | 0.562 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `text` | Introduction | lines 251-260 | no | yes | toric | We discuss in~\S\ref{sectFORMALsol} consequences of this last result and open problems in relation with the relative toric version of the Yau--Tian--Donaldson conjecture. In the next section we gather facts, definition, key results and recall brief explanations on the topic of toric extremal (almost) K\"ahler metrics. Section~\ref{sectMAIN} contains the proo... |
| 3 | 0.524 | `corpus/arxiv/1808.02813/source/source.tex` | `text` | Introduction > Structure of the paper | lines 218-219 | no | yes | extremal metrics, toric | ...f the paper} Section~\ref{review} contains the main technical body of the paper. After a brief review of the admissible setting of \cite{acgt}, we summarize in Proposition~\ref{emsolution} the main tools allowing us to extend the theory of \cite{acgt} from extremal to weighted extremal metrics. With this in place, we compute in Proposition~\ref{futaki} the w... |
| 4 | 0.511 | `corpus/arxiv/1302.6979/source/ambitoric2.tex` | `text` | Introduction | lines 277-335 | no | yes | toric | ...hm:stability}, which establishes, for quadrilaterals, Donaldson's conjecture~\cite{Donaldson1} that the existence of an extremal K\"ahler metric is equivalent to relative K-polystability with respect to toric degenerations. Indeed, we show that temperate quadrilaterals admit a factorization structure which relates the polystability condition directly to the... |
| 5 | 0.508 | `corpus/arxiv/0905.0498/source/source.tex` | `text` | Further observations > Relative K-energy and the main conjecture | lines 2222-2233 | no | yes | toric | \subsection{Relative K-energy and the main conjecture} Leaving aside the specific motivation of this paper to study projective bundles over a curve, the theory of rigid semisimple toric bundles which we reviewed in Sect.~\ref{calabi-type} extends the theory of extremal K\"ahler metrics on toric manifolds~\cite{Do2,Do3,Do5,Sz,ZZ,ZZ2} to this more general cont... |
| 6 | 0.497 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | unsectioned | lines 162-212 | yes | yes | extremal metrics, toric | An interesting testing ground for these ideas is the case of toric varieties, which was developed by Donaldson. In~\cite{Don02} he showed that in the case of toric surfaces K-stability implies that the Mabuchi functional is bounded from below (this was later extended by Zhou-Zhu~\cite{ZZ06} to show properness of the Mabuchi functional) and a minimising seque... |
| 7 | 0.496 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Introduction | lines 311-335 | no | yes | toric | Similar existence results hold for the toric surfaces $X= \C P^2$ and $\C P^1 \times \C P^1$, see Corollary~\ref{c:product} and Theorem~\ref{thm:triangle} below. We end this introduction by noticing that part (b) of Theorem~\ref{main-example} above implies that while for the $X,Z$ and $[\omega_0]$ considered here, the relative stability of $(X,Z,[\omega_0])$... |
| 8 | 0.489 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 635-663 | no | yes | - | ...-Donaldson conjecture asserts that given a compact K\"ahler manifold with a fixed K\"ahler class, the existence of cscK metrics in the K\"ahler class is equivalent to an algebro-geometric notion called "K-stability". \smallskip Several progresses in the literature \cite{Darvas_Rubinstein_2017, Berman_Darvas_Lu_2020, Chen_Cheng_2021_1, Chen_Cheng_2021_2} have... |
| 9 | 0.476 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 113-119 | no | yes | - | The \textbf{\textit{extremal vector field}} for the Poincar\'e type K\"ahler metric setting is defined using the Futaki character introduced in \cite{Auv13-2}, and we will discuss in more detail in Section~\ref{subsection 9.3}. Here, we just mention that it is a holomorphic vector field depending only on the K\"ahler class and maximal compact subgroup $K$. F... |
| 10 | 0.473 | `corpus/arxiv/1602.03114/source/source.tex` | `text` | Introduction and main results | lines 182-199 | no | yes | toric | \paragraph*{Further relations to previous results.} We end the introduction with a brief (but by no means complete) discussion about further relations to previous results. Much work has been done on Tian's properness conjectures in the case when the K\"ahler class is anti-canonical and we refer to \cite{DR17} for a detailed historical account. To our knowled... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_014 - toric Abreu equation

**Question:** Where does the corpus discuss affine functions and the extremal vector field on a polytope?

**Expected sources:** `2208.12493`, `0805.0128`, `1711.08424`
**Expected chunk types:** `definition`, `proposition`, `text`
**Expected terms:** `affine function`, `extremal vector field`, `polytope`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.900 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | K-stability of toric varieties > Test-configurations for toric bundles | lines 2549-2606 | no | yes | extremal vector field, polytope | Let us assume now that $M$ is just a point, so that $(X,L)$ is a polarised toric variety with corresponding polytope $\Delta$. In this case $Q_1=1$ and $Q_2=0$, so we get back Donaldson's result in~\cite{Don02}: A rational piecewise linear convex function $f$ on $\Delta$ defines a test-configuration for $X$ whose Futaki invariant is given by $\frac{1}{2}\mat... |
| 2 | 0.880 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Applications and Discussions > Extremal K\"ahler metric | lines 1557-1559 | no | yes | extremal vector field | We use \cite{APS11} Lemma 7.0.2 to match the metrics on the two pieces and obtain a metric $\omega_{sol}$ on $Bl_pX\backslash E$. To show the $\mathcal D^*\mathcal D(\psi_{f_{\ep}})$ term vanishes, we use the condition (\ref{theorem condition}). To make sense of the condition, we first discuss the definition of the extremal vector field. |
| 3 | 0.859 | `corpus/arxiv/0909.4512/source/source.tex` | `text` | Introduction | lines 74-79 | no | yes | affine function, extremal vector field, polytope | The \defin{extremal affine function} $\zeta_{(\Delta,u)}$ is the $L^2$--projection (with respect to the euclidian measure) of $S(G)$ to the finite dimensional space of affine-linear functions on $\Delta$. It turns out that $\zeta_{(\Delta,u)}$ is independent of the symplectic potential $G\in S(\Delta,u)$ and may also be defined as the solution of a linear sy... |
| 4 | 0.818 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `text` | Constant scalar curvature case and interpretation in term of metric with cone angle singularity > The constant scalar curvature case | lines 625-632 | no | yes | affine function, polytope | ...looking more specifically for constant scalar curvature metrics, it would have to restrict attention to those labelled polytope with a constant extremal affine function $\exv_{(P,\sigma)}$, which in the toric setting coincides with the vanishing Futaki invariant on the Lie algebra $\kt\oplus J\kt$. % % % % In case $(P,\lab,\Lambda)$ is rational and associat... |
| 5 | 0.779 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Background > Weighted extremal metrics | lines 111-121 | no | yes | polytope | \subsection{Weighted extremal metrics}\label{subsec:weighted_extremal_metrics} Here we very briefly review the definitions and our conventions on weighted cscK metrics; a more thorough treatment was already given in \cite{Hal23}. Let \((X,\omega)\) be a compact \(n\)-dimensional K{\"a}hler manifold. The Ricci curvature of \(\omega\) is \[\Ric(\omega):=-\frac... |
| 6 | 0.736 | `corpus/arxiv/dg-ga_9711014/paper.pdf` | `text` | unsectioned | p. 7 | no | yes | affine function, polytope | ...∂y i (∂G ij ∂y a GjbGab) = − ∂ ∂y i (∂G ij ∂y a δ a j ) = − ∂ 2Gij ∂y i∂y j . The Euler-Lagrange equation deﬁning an extremal K¨ ahler metric is given by (grad R)(1,0) = (F ij ∂R ∂x j ) ∂ ∂z i ≡ holomorphic vector ﬁeld . Because the coeﬃcients of the ∂/∂z i are real, the only way the above vector ﬁeld is holomorphic is if F ij∂R ∂x j = ∂R ∂y i ≡ constant, i... |
| 7 | 0.665 | `corpus/arxiv/0905.0498/source/source.tex` | `text` | Rigid toric bundles and the generalized Calabi construction > The extremal vector field | lines 1471-1509 | no | yes | affine function, extremal vector field | where $\sum_{j=1}^N d_j=d=m-\ell$. It follows that integrals over $M$ of functions of $z$ (pullbacks from $\Delta$) are given by integrals on $\Delta$ with respect to the volume form $p(z)\,dv$, where $dv$ is the (constant) euclidean volume form on $\mathfrak t^*$, obtained by wedging any generators of the lattice $\Lambda$. \smallskip We now recall the defi... |
| 8 | 0.642 | `corpus/arxiv/1302.6979/source/ambitoric2.tex` | `text` | Introduction | lines 277-335 | no | yes | extremal vector field | ...hm:stability}, which establishes, for quadrilaterals, Donaldson's conjecture~\cite{Donaldson1} that the existence of an extremal K\"ahler metric is equivalent to relative K-polystability with respect to toric degenerations. Indeed, we show that temperate quadrilaterals admit a factorization structure which relates the polystability condition directly to the... |
| 9 | 0.595 | `corpus/arxiv/0706.0505/source/source.tex` | `text` | unsectioned | lines 515-597 | no | yes | extremal vector field, polytope | ...the test-configuration is trivial. \end{defi} An n-dimensional polarized toric manifold $M$ corresponds to an integral polytope $P$ in $\mathbb {R}^n$ which is described by a common set of some half-spaces, \beq\langle l_i, x\rangle < \lambda_i, ~i=1,...,d. \eeq Here $l_i$ are $d-$vectors in $\mathbb {R}^n$ with all components in $\mathbb {Z}$, which satisf... |
| 10 | 0.592 | `corpus/arxiv/1008.2607/source/source.tex` | `text` | Introduction | lines 99-167 | no | yes | polytope | \section{Introduction} \v\n Extremal metrics, introduced by E. Calabi, have been studied intensively in the past 20 years. There are three aspects of the topic: sufficient conditions for existence, necessary conditions for existence and the uniqueness of extremal metric. The necessary conditions for the existence are conjectured to be related to certain stab... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_015 - toric Abreu equation

**Question:** Where does the corpus discuss convexity of functionals on the space of toric symplectic potentials?

**Expected sources:** `1610.07998`, `2208.12493`, `0805.0128`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `convexity`, `symplectic potentials`, `K-energy`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.047 | `corpus/arxiv/2108.12297/source/source.tex` | `text` | Weighted toric K-stability > Existence of $(\v,\w)$-cscK is equivalent to $(\v,\w)$-uniform K-stability | lines 1527-1530 | no | yes | symplectic potentials | We now focus on the converse. We consider the space of normalized K\"ahler potentials $(\ref{normalized-compatible-potential})$ and normalized symplectic potentials |
| 2 | 0.888 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Explicit Donaldson metrics on quadrilaterals > Regular ambitoric structures | line 1706 | no | yes | symplectic potentials | whose inverses are the Hessians in momenta of the symplectic potentials |
| 3 | 0.844 | `corpus/arxiv/2208.12493/source/toric-lecture-notes.tex` | `text` | Existence: an overview > The Chen--Cheng and He results | line 1632 | yes | yes | symplectic potentials | where, we recall, $u_0^* = \pi(u_0)$ is the $\cC_{\infty}^*(\Delta)$ normalization of the canonical symplectic potential. Letting $\cS^0(\Delta, {\bf L})= \cS(\Delta, {\bf L})\cap \cC^0_{\infty}(\Delta)$ be the corresponding slice in the space of symplectic potentials, we have |
| 4 | 0.842 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `theorem` | Constant scalar curvature case and interpretation in term of metric with cone angle singularity > Log K--stability of labelled polytopes and cscK metric with cone angle singularity | lines 699-700 | no | yes | - | % \begin{corollary} The space of cscK toric metrics on a symplectic toric surface is connected. % \end{corollary} |
| 5 | 0.759 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Convex Preliminaries > Energy functionals on polarized toric manifolds | lines 1791-1794 | no | yes | symplectic potentials | As shown by Guan in \cite{Gua00}, any pair of K\"ahler potentials in $\mathcal{H}_{0}^{S}$ can be joined by a unique geodesic segment, which are obtained as a line segment of symplectic potentials. Thus, we have the following; |
| 6 | 0.752 | `corpus/arxiv/0909.4512/source/source.tex` | `text` | Toric orbifolds and extremal metrics -- a quick survey. > Compatible K\"ahler metrics and the extremal equation > Uniqueness | lines 225-230 | no | yes | convexity, symplectic potentials | ...queness}\label{uniqueness} Guan~\cite{guan} showed the uniqueness, up to automorphisms, of compatible extremal K\"ahler toric metrics on a smooth compact symplectic toric manifold. In fact, he proved that a geodesic in the space of compatible $T$--invariant K\"ahler metrics corresponds, via the Moser Lemma, to a straight line in the space of symplectic poten... |
| 7 | 0.676 | `corpus/arxiv/math_0511118/source/source.tex` | `lemma` | Admissible extremal K\"ahler metrics > K-energy and the extremal polynomial | lines 1171-1181 | no | no | symplectic potentials, K-energy | \begin{lemma} \label{symplectic-setting} The K-energy ${E}_{\omega}^G$, restricted to the space of admissible K\"ahler metrics in $\Omega$ and viewed as a function on the space of symplectic potentials, is determined uniquely up to an additive constant by the formula \begin{equation*} (d {E}_{\omega}^G)_{g}[\dot u] = \int_M (\pr_g^\perp \Scal_g) \dot u \, \m... |
| 8 | 0.670 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Introduction | lines 106-118 | no | yes | convexity | ...{Bo} generalized this uniqueness result to conic K\"ahler-Einstein metrics on Fano manifolds, by his observation on the convexity of certain energy functional (the $Ding$-functional) along geodesics in the space of all K\"ahler potentials. And Berndtsson's method is further generalized to prove the uniqueness of singular K\"ahler-Einstein metrics on \emph{kl... |
| 9 | 0.639 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 645-648 | no | yes | convexity, K-energy | Building on the literature on extensions and convexity of energy functionals, notably \cite{BB,BDL,Lah,AJL,BJT}, we prove convexity of \emph{weighted, twisted K-energy} along weak geodesics in the space of \emph{$T$-invariant finite-energy potentials}. Our contribution is twofold: we simultaneously incorporate \emph{Lahdili-type weights} and a \emph{twist by... |
| 10 | 0.618 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_016 - toric Abreu equation

**Question:** Where does the corpus discuss the fourth-order nature of Abreu's equation?

**Expected sources:** `dg-ga_9711014`, `math_0407486`, `0805.0128`
**Expected chunk types:** `definition`, `theorem`, `text`
**Expected terms:** `fourth-order`, `Abreu equation`, `Hessian`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.833 | `corpus/arxiv/math_0407486/source/intest.tex` | `text` | Preliminaries > Miscellaneous formulae | line 280 | yes | yes | - | So our second form of Abreu's equation is |
| 2 | 0.620 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Conjectural picture | lines 666-667 | no | yes | - | \section{Conjectural picture} In this final section we discuss what one might expect about the existence problem for metrics with cone singularities on a Fano manifold. It is natural to think of such a metric as a solution of a distributional equation |
| 3 | 0.615 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `text` | Labelled polytope and toric (almost) K\"ahler geometry > Extremal K\"ahler metrics unicity and an open condition | lines 393-395 | no | yes | - | Donaldson proved in~\cite{don:extMcond} that the set of labelling $\lab\in \mN(P)$ for which the Abreu's equation has a solution is open in $\mN(P)$, the $d$--dimensional open cone of labellings of $P$ in $\kt^d$. |
| 4 | 0.604 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | Coercivity for the toric case > Torus-invariant metrics | lines 929-932 | no | yes | fourth-order | We say $u$ is normalized at this end. The scalar curvature is given by a fourth-order differential of $u$. |
| 5 | 0.713 | `corpus/arxiv/math_0407486/source/intest.tex` | `text` | Preliminaries > Miscellaneous formulae | lines 273-278 | yes | yes | - | Now the first form of Abreu's equation, as in the Introduction is $$ u^{ij}_{ij}= -A. $$ We define a vector field $v= (v^{j})$ by |
| 6 | 0.684 | `corpus/arxiv/math_0407486/source/intest.tex` | `text` | Applications of the maximum principle > An upper bound on the determinant | lines 1153-1158 | yes | yes | - | where we have used the fact that $u^{ij}u_{ij}= n$. The crucial step now is to observe that $$u^{ij} g^{pq} u_{pi} u_{qj} = g^{pq}u_{pq}, $$ the ordinary Euclidean Laplacian of $u$, in the metric $g$. We next use the form Equation~\ref{eq:Ab4} of Abreu's equation to see that |
| 7 | 0.668 | `corpus/arxiv/math_0407486/source/intest.tex` | `text` | Preliminaries > Miscellaneous formulae | lines 282-286 | yes | yes | - | (Of course, the left hand side of this expression is the ordinary divergence of the vector field $v$.) On the other hand, by Equation~\ref{eq:id3}, the vector field can also be expressed as $$ v^{j}= u^{ij}L_{j}, $$ so we have our third form of Abreu's equation |
| 8 | 0.527 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | It is an interesting question to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except i... |
| 9 | 0.656 | `corpus/arxiv/math_0407486/source/intest.tex` | `theorem` | The two dimensional case. > The conjugate function | lines 745-750 | yes | yes | - | \begin{thm} Suppose $u\in \cS_{\Omega,\sigma}$ is a solution of Abreu's equation where $A$ is a constant and the dimension $n$ is $2$. Then there is a constant $K$, depending tamely on $\Omega, \sigma$, such that $\vert v\vert \leq K$ throughout $\Omega$. \end{thm} |
| 10 | 0.496 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | no | yes | - | ...rk) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail in our next paper and refer interested readers to the following works and references therein: |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_017 - toric Abreu equation

**Question:** Where does the corpus discuss boundary behavior of solutions to Abreu's equation?

**Expected sources:** `math_0407486`, `0805.0128`, `2208.12493`
**Expected chunk types:** `theorem`, `lemma`, `proof`, `text`
**Expected terms:** `boundary`, `Abreu equation`, `solution`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.848 | `corpus/arxiv/math_0407486/source/intest.tex` | `text` | Introduction | lines 134-145 | yes | yes | boundary, solution | over the set of smooth convex functions on $\Omega$ with $L^{1}$ boundary values. It is likely (although this requires proof) that any extrema of this functional lies in our space $\cS_{\Omega,\sigma}$. As explained in \cite{kn:don}, simple examples show that for some data $\Omega, A, d\sigma$ there are no solutions of Abreu's equation with the given boundar... |
| 2 | 0.699 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `proposition` | Introduction | lines 248-250 | no | no | boundary, solution | ...MALintro} For any simple labelled polytope $(P,\sigma)$, there exists an infinite dimensional family of formal extremal solutions $H :P \ra \mbox{Sym}^2(\kt^*)$ of equation~\eqref{eqABREUintroH} satisfying the boundary condition associated to $\sigma$. Whenever one of these solutions is positive definite on the interior of $P$, $(P,\sigma)$ is uniformly $K$-... |
| 3 | 0.668 | `corpus/arxiv/1205.0056/source/cone_metrics.tex` | `text` | Linearized equation > The maximum principle and the weak solution | lines 3214-3217 | no | yes | solution | Now we use the maximum principle to deduce the uniqueness of solutions of the elliptic equation \eqref{linear equ ge}. |
| 4 | 0.657 | `corpus/arxiv/2208.12493/source/toric-lecture-notes.tex` | `text` | Toric K\"ahler metrics: compactification | lines 1054-1055 | yes | yes | boundary | {\tiny \begin{exercise}[\bf Abreu's boundary conditions~\cite{abreu}]\label{abreu2} Show that \eqref{a1} and \eqref{a2} are equivalent to |
| 5 | 0.640 | `corpus/arxiv/1008.2607/source/source.tex` | `text` | K\"{a}hler geometry on toric surfaces > The Legendre transformation, moment maps and potential functions | lines 505-507 | no | yes | boundary | Note that the first map is induced from \eqref{eqn_1.1a}. It is known that $u$ must satisfy certain behavior near boundary of $\Delta$. |
| 6 | 0.772 | `corpus/arxiv/math_0407486/source/intest.tex` | `text` | Preliminaries > Miscellaneous formulae | line 280 | yes | yes | - | So our second form of Abreu's equation is |
| 7 | 0.752 | `corpus/arxiv/math_0407486/source/intest.tex` | `text` | Introduction | lines 67-131 | yes | yes | boundary, solution | the Hessian matrix $u_{ij}= \frac{\partial^{2} u}{\partial x^{i}\partial x^{j}}$. We call this PDE {\it Abreu's equation} since the expression $S(u)$ appears in \cite{kn:Abr}, in the study of the differential geometry of toric varieties. In this paper we will be primarily interested in the case when $A$ is a constant. Solutions to Equation~\ref{eq:Abreu} the... |
| 8 | 0.691 | `corpus/arxiv/math_0407486/source/intest.tex` | `theorem` | The two dimensional case. > Integrating bounds on $v$ | lines 908-917 | yes | yes | boundary, solution | \begin{thm} Let $\Omega\subset \bR^{2}$ and $u\in \cS_{\Omega,\sigma}$ be a normalised solution of Abreu's equation with $A$ constant. Suppose Condition 1 holds. Then $$ L \leq C_{0}+ C_{1} \vert \nabla u \vert \leq C_{2} d^{-2}, $$ where $d$ is the distance to the boundary of $\Omega$ and $C_{0},C_{1}, C_{2}$ depends tamely on $\Omega, \sigma, \lambda$. \en... |
| 9 | 0.683 | `corpus/arxiv/math_0407486/source/intest.tex` | `proposition` | Applications of the maximum principle > Lower bound for the determinant | lines 1050-1056 | yes | no | boundary, solution | \begin{prop} In either Case 1 or Case 2, a solution $u\in \cS_{\Omega,\sigma}$ of Abreu's equation with boundary data satisfies $$ \det u_{ij} \geq \rho_{\Omega}^{-1} \left( \frac{\sup_{\Omega} A}{n}\right)^{n}. $$ in $\Omega$. \end{prop} |
| 10 | 0.536 | `corpus/arxiv/0805.0128/source/extremal2a.tex` | `text` | Introduction | lines 219-255 | yes | yes | solution | ...esults, are related to our lack of understanding of this basic local question---what are the possible $C^{0}$ limits of solutions to the equation (1)? \ The main work of this paper finishes in Section 5. However, it is interesting to complement the existence proofs with an understanding of what goes wrong when the positivity hypothesis is violated. Section 6... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_018 - toric Abreu equation

**Question:** Where does the corpus discuss Calabi flow or Calabi functional in toric geometry?

**Expected sources:** `math_0412518`, `1008.2607`, `0805.0128`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `Calabi functional`, `toric`, `extremal`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.836 | `corpus/arxiv/0909.4512/source/source.tex` | `proposition` | Calabi toric structures and trapezoids. > K\"ahler toric $4$-orbifolds with non-trivial Hamiltonian $2$--forms. | lines 521-522 | no | yes | toric | \begin{proposition} \label{propHam2fOrder1polytope} The moment polytope of a symplectic toric orbifold admitting a compatible Calabi toric metric is a trapezoid or a triangle.\end{proposition} |
| 2 | 0.723 | `corpus/arxiv/1302.6979/source/ambitoric2.tex` | `theorem` | Orbifold compactifications of ambitoric structures > Ambitoric structures and their local classification | lines 954-959 | no | yes | toric | \begin{result} \cite{ACG1} Let $(M,g_\pm,J_\pm,\omega_\pm,\tor)$ be an ambitoric $4$-manifold or orbifold. Then any point in an open dense subset of $M$ has a neighbourhood on which $(g_\pm,J_\pm,\omega_\pm,\tor)$ is either a toric K\"ahler product, a toric Calabi geometry, or a regular ambitoric structure. \end{result} |
| 3 | 0.691 | `corpus/arxiv/1004.2012/source/Kempf_Ness_uniqueness_12272011.tex` | `text` | Introduction | lines 217-272 | no | yes | - | ...redient in the proof of the above theorems is to obtain some $C^0$ bound. We shall study the asymptotic behavior of the Calabi flow near a cscK metric. The global existence and convergence are established by using the Lojasiewicz inequality which controls the gradient of a real analytic function near a critical point. Suppose now we have two cscK metrics adj... |
| 4 | 0.676 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | %\begin{q} There is a few open questions for the Calabi dream manifolds: %\begin{enumerate} %\item What linear combinations of Chern numbers are nonnegative for all Calabi dream manifolds? %\item In Corollary 1.7, can we extend it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic to... |
| 5 | 0.582 | `corpus/arxiv/1510.01260/source/source.tex` | `text` | Introduction | lines 168-177 | no | yes | - | \paragraph{Convergence and large time behaviour of the weak twisted Calabi flow.} As advertised above, using Theorem \ref{ExtKEnergyThmIntr}, we can run the weak twisted Calabi flow $[0,\infty) \ni t \to c_t \in \mathcal E^2$ for any starting point $c_0 \in \mathcal E^2$. Indeed, $(\mathcal E^2,d_2)$ is a CAT(0)-space and the extended functional $\mathcal K_... |
| 6 | 0.556 | `corpus/arxiv/2108.12297/source/source.tex` | `text` | Introduction > Motivation | lines 168-180 | no | yes | toric, extremal | \subsection{Motivation} A central problem in K\"ahler geometry, proposed by Calabi \cite{EC2} in the 1980's, is to find a canonical K\"ahler metric in a given cohomology class of a compact K\"ahler manifold. Calabi suggested looking for \textit{extremal K\"ahler metrics}, characterized by the property that the flow of the gradient of the scalar curvature pre... |
| 7 | 0.535 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | Introduction | lines 509-611 | no | yes | toric | ...metrics representing a fixed cohomology class on a compact \K manifold $(M,\JJJ,\o)$ Motivated by results in conformal geometry and the direct method in the calculus of variations, in the 90's Tian introduced the notion of ``properness on $\calH$" \cite[Definition 5.1]{T1994} in terms of the Aubin nonlinear energy functional $J$ \cite{Aubin84} and the Mabuc... |
| 8 | 0.527 | `corpus/arxiv/2208.12493/source/toric-lecture-notes.tex` | `text` | The Calabi problem on a toric manifold | lines 1115-1117 | no | yes | toric, extremal | ...scalar curvature (CSC) K\"ahler metrics are examples, and, motivated by the Uniformization Theorem for complex curves, Calabi proposed the problem of finding an extremal K\"ahler metric $(g, \omega)$ in a given deRham class $[\omega]\in H^2(M, \R)$. This is known as the {\it Calabi Problem}, and is of greatest interest in current research in K\"ahler geomet... |
| 9 | 0.525 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | \label{sec:Introduction}Introduction > Statement of the main results > Further extensions and applications | lines 372-401 | no | yes | - | ...is that it also has bearings on the uniqueness and regularity problem for very weak minimizers of the (twisted) Mabuchi functional. The point is that, extending the results in \cite{bbegz} concerning the case when $[\omega]=c_{1}(X)$, the Mabuchi functional, as defined by formula \ref{eq:formula for mab intro}, can be extended to the ``finite energy'' comple... |
| 10 | 0.508 | `corpus/arxiv/1302.6975/source/ambitoric1.tex` | `text` | Introduction | lines 245-262 | no | yes | toric, extremal | Thus motivated, we study ambitoric structures in general and show that in a neighbourhood of any point, they are either of Calabi type (hence classified by well-known results), or ``regular''. Our explicit local classification in the regular case (Theorem~\ref{thm:ambitoric}) relies on subtle underlying geometry which we attempt to elucidate, although some f... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_019 - toric Abreu equation

**Question:** Where does the corpus discuss slope stability and lower bounds for the Calabi functional?

**Expected sources:** `math_0412518`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `slope stability`, `Calabi functional`, `lower bounds`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.900 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | Lower bound on the Calabi functional | lines 2255-2259 | no | yes | Calabi functional | \section{Lower bound on the Calabi functional}\label{sec:lwrcalabi} In~\cite{Don05} Donaldson showed that a destabilising test-configuration gives a lower bound for the Calabi functional. The precise statement is the following. |
| 2 | 0.862 | `corpus/arxiv/1004.2012/source/Kempf_Ness_uniqueness_12272011.tex` | `theorem` | Stability of the Calabi flow | lines 1418-1422 | no | yes | - | \begin{thm}(\cite{Ch4}) For any $J\in\U$, the Mabuchi functional $E$ on the space of K\"ahler metrics compatible with $J$ is bounded below, and the lower bound is achieved by the infimum along the Calabi flow initiating from $J$. \end{thm} |
| 3 | 0.830 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | K-stability of twisted cscK metrics > Lower bounds on the twisted Calabi functional | lines 292-294 | no | yes | Calabi functional | Our strategy to prove Theorem \ref{stabilityofcscK} is to first prove the following lower bound on the twisted Calabi functional, which is the twisted analogue of \cite[Theorem 2]{D2}. |
| 4 | 0.809 | `corpus/arxiv/1803.09506/source/source.tex` | `remark` | Singular constant scalar curvature K\"ahler metrics > Twisted $J$-metrics and properness | lines 1996-1998 | no | no | - | \begin{rem} As shown in \cite{MR3412393}, the lower bound of the twisted $J$-functional $J^\gamma_{-\chi}(\vphi)$ is related to the geodesic stability. \end{rem} |
| 5 | 0.752 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | ...elow? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except in the Fano manifold where the authors proved it indirectly in route of CDS's theorem.\\ We have the following theorem which is useful to our characterization of borde... |
| 6 | 0.648 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | no | yes | - | An intriguing question motivated from above remark is whether geodesic stability in $\mathcal{E}_0^{\infty}$ (in the sense defined in the above remark) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail i... |
| 7 | 0.591 | `corpus/arxiv/math_0511118/source/source.tex` | `text` | K-stability and admissible extremal K\"ahler metrics > Introduction to stability | lines 1969-1994 | no | yes | - | \subsection{Introduction to stability}\label{intro} For a Hodge manifold $(M,\Omega$), the existence of a CSC K\"ahler metric in $\Omega$ is conjectured to be equivalent to a notion of {\it stability}~\cite{CT,Do1,Do2,luo,PT,tian,zhang} for the polarized projective variety $(M,L)$, where $L$ is a line bundle on $M$ with $c_1(L)= \Omega/2\pi$. This conjecture... |
| 8 | 0.727 | `corpus/arxiv/1412.0648/source/twisted.tex` | `remark` | Norms on test configurations | line 743 | no | no | Calabi functional | \begin{remark} This norm on test configurations was introduced by Donaldson \cite{D2}, in order to normalise the Donaldson-Futaki invariant to obtain a lower bound on the Calabi functional, as we did in Proposition \ref{calabifunctional}. The $L^2$-norm is also expected to have direct analytic relevance, see \cite[Section 3.1.1]{GS5}. \end{remark} |
| 9 | 0.567 | `corpus/arxiv/math_0412518/source/slopeobs_archive.tex` | `text` | Slope stability as a necessary condition for K-stability > Extension to K\"ahler manifolds | lines 948-1007 | yes | yes | slope stability | \subsection{Extension to K\"ahler manifolds}\label{extensionkahler}\ \vskip 5pt The definition of K-(poly/semi)stability given in \eqref{defkstab} cannot be defined when the K\"ahler class is not rational, but slope (poly/semi)\-stability can. The same issue arises for bundles; GIT cannot construct moduli for bundles over non-projective manifolds, but the sl... |
| 10 | 0.557 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | unsectioned | lines 161-222 | no | yes | - | ...em*{dfn1}{\bf{Definition 1}} \newtheorem*{dfn2}{\bf{Definition 2}} \newtheorem*{dfn3}{\bf{Definition 3}} \title[Uniform stability for equivariant polarizations]{Uniform stability and coercivity for equivariant polarizations} \date{\today} \author{Tomoyuki Hisamoto} \address{Graduate School of Mathematics\\ Nagoya University\\ Furocho\\ Chikusa\\ Nagoya\\ Jap... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_020 - toric Abreu equation

**Question:** Where does the corpus discuss test configurations or filtrations for toric manifolds?

**Expected sources:** `2110.08491`, `1610.07998`, `1603.01026`
**Expected chunk types:** `definition`, `theorem`, `text`
**Expected terms:** `filtration`, `test configuration`, `toric`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.047 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 403-405 | no | yes | filtration, test configuration, toric | ...f YTD conjecture for any polarized manifold (see Definition \ref{def-Kst} and Conjecture \ref{conj-YTD}). For polarized toric manifolds, using the fact that toric model filtrations are the same as filtrations from toric test configurations, we see that Conjecture \ref{conj-reg} is true for toric model filtrations. As a consequence, we get another proof of th... |
| 2 | 0.745 | `corpus/arxiv/2110.08491/source/source.tex` | `text` | \bf Preliminaries > (Relative) $K$-polystability | lines 283-285 | yes | yes | test configuration, toric | \subsection{(Relative) $K$-polystability} In \cite{D1}, Donaldson introduced the (relative) $K$-polystability by test configurations. For toric case, the definition is |
| 3 | 0.610 | `corpus/arxiv/1801.05907/source/source.tex` | `question` | Introduction | lines 282-283 | no | no | test configuration | \begin{q} Is the set of points defined by test configurations dense in the sphere of infinity ${\mathcal S}_\infty.\;$ More importantly, does the uniform stability or filtrated stability in the sense of G. Sz$\acute{\text{e}}$kelyhidi\cite{Sz06} imply geodesic stability? \end{q} |
| 4 | 0.553 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `remark` | Log Futaki invariant and log $K$-stability > Log $K$-stability | lines 714-716 | no | no | test configuration | \begin{remark} We need some restriction on the singularities of $\mathcal{X}$ and $\mathcal{D}$ to define log $K$-stability (cf.~Remark \ref{pathsingkstble}), when the log test configuration is not product or trivial (cf.~\cite{os}), but we do not discuss this issue since only the product log test configurations will be important for us later. \end{remark} |
| 5 | 0.486 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | %\begin{q} There is a few open questions for the Calabi dream manifolds: %\begin{enumerate} %\item What linear combinations of Chern numbers are nonnegative for all Calabi dream manifolds? %\item In Corollary 1.7, can we extend it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic to... |
| 6 | 0.446 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Extremal Poincar\'e type K\"ahler metrics on toric varieties > Stability of pairs and toric test configurations | lines 597-608 | no | yes | test configuration, toric | ...onvex piecewise affine linear functions $f_{\alpha}$ with integer coefficients. He associates to such an $f_{\alpha}$ a test configuration $({\mathcal X}, \cL)$, called {\it toric}, and identifies the Donaldson--Futaki invariant of the central fibre $(X_0,L_0)$ with \eqref{toric-futaki}. Sz\'ekelyhidi~\cite[\S~4.1]{Sz} shows that \eqref{toric-relative-futaki... |
| 7 | 0.431 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Relative weighted K-stability > Twisting test configurations | lines 390-393 | no | yes | test configuration | \subsection{Twisting test configurations} Since we are dealing with non-projective K{\"a}hler manifolds, we will need a mild generalisation of test configurations that allows one to incorporate irrational elements of the Lie algebra \(\mathfrak{t}\); such test configurations were used in \cite{Der18}. We first describe how integral elements of \(\mathfrak{t}... |
| 8 | 0.419 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Introduction | lines 82-96 | no | yes | test configuration, toric | ...K-polystability requires the positivity of the \emph{relative Donaldson-Futaki invariant} $DF_{V}>0$ for any nontrivial test object. Here $V$ is the extremal K\"ahler vector field of $(X, L)$ (\cite{FM95}), and test object is a special kind of degeneration of $(X, L)$, which is called a \emph{test configuration}. On the other hand, calculations by Apostolov-... |
| 9 | 0.407 | `corpus/arxiv/2506.02360/source/2025_06_03_extremal.tex` | `text` | Preliminaries > Relative $K$-stability | lines 311-316 | no | yes | filtration, test configuration | ...each of this paper. The reader is referred to \cite{BJ18,BBJ,Li20} for more details. There is another generalisation of test configurations, called models \cite{Li20}. The definition of models is similar to that of test configurations, but we are allowed to consider non-semiample polarisations for models \cite[Definition 2.1]{Li20}. Models define filtrations... |
| 10 | 0.403 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction | lines 123-127 | no | yes | test configuration | ...d} K-stability in analogous situations. The third theme of the present work is to characterise the \emph{triviality} of test configurations. It was noticed by Li-Xu that \emph{every} polarised variety $(X,L)$ admits test configurations with zero Donaldson-Futaki invariant \cite{LX}, which are not the trivial test configuration. Stoppa showed that these test... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_021 - toric Abreu equation

**Question:** Where does the corpus discuss toric contact geometry in relation to moment cones?

**Expected sources:** `1708.04942`, `1708.05253`
**Expected chunk types:** `definition`, `theorem`, `text`
**Expected terms:** `toric contact`, `moment cone`, `CR`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.752 | `corpus/arxiv/0909.4512/source/source.tex` | `text` | Toric orbifolds and extremal metrics -- a quick survey. > Sasaki toric geometry. > Contact toric manifolds. | lines 261-264 | no | yes | moment cone | Lerman established \cite{L:contactCONVEX,L:contactToric} a correspondence between contact toric manifolds and good polyhedral cones. The image, $\im \hat{\mu}$, of the contact moment map of a compact contact toric manifold $(N, \mD, \hat{T})$ does not contain $0$ and $\mC= \im \hat{\mu} \cup \{0\}$ is a convex, polyhedral cone which is good with respect to t... |
| 2 | 0.477 | `corpus/arxiv/1708.04942/source/source.tex` | `text` | Introduction | lines 196-246 | yes | yes | toric contact, CR | \section*{Introduction} Toric contact geometry lies at the interface of of two important themes in contemporary geometry. The first is the use of toric methods, beginning with toric varieties and toric symplectic manifolds, to provide large classes of geometric objects which can be understood in an essentially combinatorial way. The second is a growing inter... |
| 3 | 0.446 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `text` | Introduction | lines 251-260 | no | yes | - | We discuss in~\S\ref{sectFORMALsol} consequences of this last result and open problems in relation with the relative toric version of the Yau--Tian--Donaldson conjecture. In the next section we gather facts, definition, key results and recall brief explanations on the topic of toric extremal (almost) K\"ahler metrics. Section~\ref{sectMAIN} contains the proo... |
| 4 | 0.428 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | CR | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 5 | 0.424 | `corpus/arxiv/1302.6979/source/ambitoric2.tex` | `text` | Introduction | lines 277-335 | no | yes | CR | ...Donaldson1} that the existence of an extremal K\"ahler metric is equivalent to relative K-polystability with respect to toric degenerations. Indeed, we show that temperate quadrilaterals admit a factorization structure which relates the polystability condition directly to the positivity of the quartics $A$ and $B$ appearing in the expression for the extremal... |
| 6 | 0.406 | `corpus/arxiv/1008.2607/source/source.tex` | `text` | K\"{a}hler geometry on toric surfaces | lines 219-248 | no | yes | - | \section{K\"{a}hler geometry on toric surfaces }\label{sect_1} %%%%%%%%%%%%%%%%%%%%%%%%sect_2 In this section, we review the K\"{a}hler geometry {of} toric surface and introduce the notations to be used in this paper. We assume that the readers are familiar with some basic knowledge of toric varieties. A toric manifold is a 2$n$-dimensional K\"{a}hler manifo... |
| 7 | 0.397 | `corpus/arxiv/1708.05253/source/source.tex` | `text` | Curvature of Levi--K\"ahler quotients of products of spheres > Extremal Levi--K\"ahler quotients > CSC Levi--K\"ahler quotients of $\Sph^5\times \Sph^3$ | lines 3120-3165 | yes | yes | CR | ...remal metrics: An elementary introduction}, Lecture Notes. \bibitem{GGK} V.~Ginzburg, V.~Guillemin and Y.~Karshon, {\it Moment maps, cobordisms, and Hamiltonian group actions}, Mathematical Surveys and Monographs \textbf{98}, Amer. Math. Soc., Providence, 2002. \bibitem{Guillemin} V.~Guillemin, {\it K{\"a}hler structures on toric varieties}, J. Differential... |
| 8 | 0.393 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | Remarks about stability and coercivity in the general setting | lines 1215-1219 | no | yes | - | \section{Remarks about stability and coercivity in the general setting} In relation with Theorem B, we discuss the definition of stability proposed in the introduction, which would work for general polarizations and automorphism groups. %The results support our torus formulation given in the previous sections. |
| 9 | 0.391 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | no | yes | - | ...rk) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail in our next paper and refer interested readers to the following works and references therein: |
| 10 | 0.389 | `corpus/arxiv/dg-ga_9711014/paper.pdf` | `text` | unsectioned | p. 1 | no | yes | - | arXiv:dg-ga/9711014v1 19 Nov 1997 K¨ ahler Geometry of Toric Varieties and Extremal Metrics Miguel Abreu ∗ Institute for Advanced Study revised version November 26, 2024 1991 Mathematics Subject Classiﬁcation: Primary 53C55, Se condary 14M25 53C25 58F05. Abstract A (symplectic) toric variety X, of real dimension 2 n, is completely determined by its moment po... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_022 - toric Abreu equation

**Question:** Where does the corpus discuss ALE scalar-flat Kahler metrics on weighted projective spaces?

**Expected sources:** `1510.02226`
**Expected chunk types:** `theorem`, `example`, `text`
**Expected terms:** `ALE`, `scalar-flat Kahler`, `weighted projective`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.702 | `corpus/arxiv/1510.02226/source/source.tex` | `text` | Introduction | lines 281-297 | yes | yes | ALE, weighted projective | ...tion{Introduction} In this paper we apply the formalism from \cite{ACG,ACGT} in order to generalize the construction of scalar-flat K\"ahler {\it asymptotically locally euclidean} (ALE) metrics, defined on the total space of the vector bundle $\mathcal{O}(-r) \to \CP^n$ (see e.g. \cite{LeBrun,simanca,pedersen-poon,rollin-singer,HS}) to a family of scalar-fla... |
| 2 | 0.484 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Applications and Discussions > Extremal K\"ahler metric | lines 1475-1478 | no | yes | - | \subsection{Extremal K\"ahler metric}\label{subsection 9.3} We discuss the situation of extremal K\"ahler(extK) metrics in Theorem~\ref{thm application 2}. To solve the extK equation, we need to choose $T$-invariant coordinates when defining weighted H\"older spaces, and we want to solve for $T$-invariant potential functions. Comparing the expansion of $\ome... |
| 3 | 0.361 | `corpus/my_notes/project_paper_index.md` | `text` | Project Paper Index > Other Related Local Papers | lines 372-383 | no | yes | ALE, weighted projective | ## Other Related Local Papers - Vestislav Apostolov and Gideon Maschler, "Conformally Kähler, Einstein-Maxwell Geometry". arXiv: https://arxiv.org/abs/1512.06391 Local: `corpus/arxiv/1512.06391` Role: conformally Kähler Einstein-Maxwell geometry related to weighted/extremal constructions. - Vestislav Apostolov and Yann Rollin, "ALE scalar-flat Kähler metrics... |
| 4 | 0.443 | `corpus/arxiv/1510.02226/source/source.tex` | `theorem` | The general case: Proof of Theorem~\ref{thm:main} > Orbifold extension of the metric over boundary points. | lines 1117-1119 | yes | yes | weighted projective | \begin{cor}\label{c:compactification} The K\"ahler metric \eqref{order-ell} gives rise to a scalar-flat K\"ahler metric $(g_{\bf a}, J_{\bf a}, \omega_{\bf a})$ on the non-compact weighted projective space $M_{\bf a}=\mathbb{C}P^m_{-a_0, a_1, \ldots, a_1, \ldots, a_{\ell}, \ldots, a_{\ell}}$, where each positive integer $a_j$ is counted $(1+n_j)$-times. \end... |
| 5 | 0.388 | `corpus/arxiv/1510.02226/source/source.tex` | `proof` | Resolution of singularities of type $\TI$ > Resolution of extremal K\"ahler metrics | lines 1511-1527 | yes | no | ALE, weighted projective | ...only singularities of type $\TI$. In particular they are isolated. The complex orbifold $\cX_1$ is obtained by gluing a weighted projective spaces of non-compact type. This space carries a scalar-flat K\"ahler ALE metric by Theorem~\ref{thm:main}. Furthermore, the ALE metric has a good decay at infinity, in the sense that it satisfies Proposition~\ref{p:asym... |
| 6 | 0.307 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Introduction | lines 42-49 | no | yes | ALE | ...We begin by considering a \lq\lq flat model'' for a cone singularity and in Section 2 we obtain an estimate in H\"older spaces for the Laplace operator, as in the usual Schauder theory. This depends on certain properties of the Green's function which are derived in Section 3, using Bessel functions and classical methods. In Section 4 we introduce complex str... |
| 7 | 0.368 | `corpus/arxiv/1510.02226/source/source.tex` | `text` | Introduction > Remarks and Applications > Toward smooth scalar-flat ALE metrics | lines 527-548 | yes | yes | ALE | \subsubsection{Toward smooth scalar-flat ALE metrics} It seems reasonable to expects a version of Theorem~\ref{theo:extremal} adapted to ALE spaces endowed with scalar-flat K\"ahler metrics. This should be straightforward when the work in progress of Arezzo--Lena \cite{AL} is completed. Their idea is to generalize the Arezzo--Pacard gluing theory to the case... |
| 8 | 0.288 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted cscK problem on semisimple principal fibration | lines 2104-2110 | no | yes | - | Also, from \cite[Section 5]{AJL}, any Kähler metric \(\omega\) on \(X\) induces a Kähler metric \(\tilde{\omega}\) on \(Y\) such that the restriction \((Y_b, \tilde{\omega}_b)\) of \((Y, \tilde{\omega})\) to a fiber over a point \(b \in B\) is \(\T\)-equivariantly Kähler isomorphic to \((X, \omega)\). Such a metric \(\tilde{\omega}\) on \(Y\) is the \emph{co... |
| 9 | 0.280 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Existence of singular weighted cscK metrics > Proof of Theorem~\ref{bigthm_existence_0} | lines 1721-1723 | no | yes | - | \subsection{Proof of Theorem~\ref{bigthm_existence_0}} We now prove the following result on the existence of singular weighted cscK metrics. |
| 10 | 0.335 | `corpus/arxiv/1510.02226/source/source.tex` | `text` | unsectioned | lines 185-273 | yes | yes | ALE, weighted projective | ...lph{theointro}} \newtheorem{defintro}{Definition} \renewcommand{\thedefintro}{\Alph{defintro}} \date{\today} \title[ALE metrics on non-compact weighted projective spaces]{ALE scalar-flat K\"ahler metrics on non-compact weighted projective spaces} \author{Vestislav Apostolov} \address{Vestislav Apostolov \\ D{\'e}partement de Math{\'e}matiques\\ UQAM\\ C.P. 8... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_023 - toric Abreu equation

**Question:** Where does the corpus discuss conformally Kahler Einstein-Maxwell geometry in toric examples?

**Expected sources:** `1512.06391`
**Expected chunk types:** `theorem`, `example`, `text`
**Expected terms:** `conformally Kahler`, `Einstein-Maxwell`, `toric`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.481 | `corpus/arxiv/1512.06391/source/source.tex` | `text` | Einstein--Maxwell toric 4-orbifolds with $b_2 \le 2$ > Toric orbifolds with $b_2=2$ > Ambitoric structures | lines 678-681 | yes | yes | toric | Thus $M$ has a pair of conformally equivalent but oppositely oriented K\"ahler metrics, invariant under a local $2$-torus action, and both locally toric with respect to that action. There are three classes of examples of ambitoric structures. |
| 2 | 0.481 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Explicit Donaldson metrics on quadrilaterals > Ambitoric structures | lines 1375-1379 | no | yes | toric | Thus $M$ has a pair of conformally equivalent but oppositely oriented K\"ahler metrics, invariant under a local $2$-torus action, and both locally toric with respect to that action. There are three classes of examples of ambitoric structures. |
| 3 | 0.383 | `corpus/arxiv/1302.6979/source/ambitoric2.tex` | `text` | Introduction | lines 277-335 | no | yes | toric | ...Donaldson1} that the existence of an extremal K\"ahler metric is equivalent to relative K-polystability with respect to toric degenerations. Indeed, we show that temperate quadrilaterals admit a factorization structure which relates the polystability condition directly to the positivity of the quartics $A$ and $B$ appearing in the expression for the extremal... |
| 4 | 0.361 | `corpus/my_notes/project_paper_index.md` | `text` | Project Paper Index > Other Related Local Papers | lines 372-383 | no | yes | Einstein-Maxwell, toric | ## Other Related Local Papers - Vestislav Apostolov and Gideon Maschler, "Conformally Kähler, Einstein-Maxwell Geometry". arXiv: https://arxiv.org/abs/1512.06391 Local: `corpus/arxiv/1512.06391` Role: conformally Kähler Einstein-Maxwell geometry related to weighted/extremal constructions. - Vestislav Apostolov and Yann Rollin, "ALE scalar-flat Kähler metrics... |
| 5 | 0.334 | `corpus/arxiv/1808.07811/source/source.tex` | `text` | The structure of the automorphism group and stability of the $(\uu,\vv)$-cscK metrics under deformations | lines 2136-2186 | no | yes | Einstein-Maxwell, toric | ...ility theorem in \cite{LS} (see also \cite{FS}). \begin{thebibliography}{99} \bibitem{abreu0} M.~Abreu, {\it K{\"a}hler geometry of toric varieties and extremal metrics}, Internat. J. Math {\bf 9} (1998), 641--651. \bibitem{abreu} M.~Abreu, {\it K{\"a}hler metrics on toric orbifolds}, J. Differential Geom. {\bf 58} (2001), 151--187. \bibitem{AC} V. Apostolov... |
| 6 | 0.314 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | Coercivity for the toric case > Torus-invariant metrics | line 924 | no | yes | toric | one obtains the toric potential $u$ satisfying |
| 7 | 0.313 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | Uniqueness of weighted cscK metrics | lines 940-1004 | no | yes | Einstein-Maxwell | \begin{thebibliography}{99} \bibitem{AC} V. Apostolov and D.~M.~J. Calderbank, {\it The CR geometry of weighted extremal K\"ahler and Sasaki metrics}, arXiv:1810.10618. \bibitem{ACGT} V.~Apostolov, D.~M.~J. Calderbank, P.~Gauduchon and C.~T{\o}nnesen-Friedman, {\it Extremal K\"ahler metrics on projective bundles over a curve}. Adv. Math. {\bf 227} (2011), 23... |
| 8 | 0.298 | `corpus/arxiv/0909.4512/source/source.tex` | `proposition` | Calabi toric structures and trapezoids. > K\"ahler toric $4$-orbifolds with non-trivial Hamiltonian $2$--forms. | lines 521-522 | no | no | toric | \begin{proposition} \label{propHam2fOrder1polytope} The moment polytope of a symplectic toric orbifold admitting a compatible Calabi toric metric is a trapezoid or a triangle.\end{proposition} |
| 9 | 0.295 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted cscK problem on semisimple principal fibration | lines 2104-2110 | no | yes | - | Also, from \cite[Section 5]{AJL}, any Kähler metric \(\omega\) on \(X\) induces a Kähler metric \(\tilde{\omega}\) on \(Y\) such that the restriction \((Y_b, \tilde{\omega}_b)\) of \((Y, \tilde{\omega})\) to a fiber over a point \(b \in B\) is \(\T\)-equivariantly Kähler isomorphic to \((X, \omega)\). Such a metric \(\tilde{\omega}\) on \(Y\) is the \emph{co... |
| 10 | 0.295 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `theorem` | Constant scalar curvature case and interpretation in term of metric with cone angle singularity > Log K--stability of labelled polytopes and cscK metric with cone angle singularity | lines 699-700 | no | yes | toric | % \begin{corollary} The space of cscK toric metrics on a symplectic toric surface is connected. % \end{corollary} |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_024 - toric Abreu equation

**Question:** Where does the corpus discuss homogeneous toric bundles and YTD-type statements?

**Expected sources:** `2110.08491`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `homogeneous toric bundles`, `YTD`, `filtration`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.856 | `corpus/arxiv/2110.08491/source/source.tex` | `text` | \bf Introduction | lines 171-172 | yes | yes | homogeneous toric bundles | In this paper, we consider toric manifolds and homogeneous toric bundles. The equation for toric manifolds is (\ref{eqn-1.3}). We prove the following theorem. |
| 2 | 0.818 | `corpus/arxiv/2110.08491/source/source.tex` | `text` | \bf Scalar curvatures on homogeneous toric bundles | lines 759-762 | yes | yes | homogeneous toric bundles | \section{\bf Scalar curvatures on homogeneous toric bundles}\label{Sec-5} In this section, we generalize our results to homogeneous toric bundles. First, we briefly review homogeneous toric bundles and the generalized Abreu equation, For the details, see \cite{D5} and \cite{CHLLS}. Then we sketch the proof of Theorem \ref{theorem_1.1}. |
| 3 | 0.773 | `corpus/arxiv/2110.08491/source/source.tex` | `text` | \bf Scalar curvatures on homogeneous toric bundles > \bf Proof of Theorem \ref{theorem_1.1} | lines 870-872 | yes | yes | homogeneous toric bundles | By Theorem \ref{theorem_stab-1}, we have the equivalence of relative $\widehat{K}$-stability and uniformly relative $K$-stability for homogeneous toric bundles. The proof is the same as in Theorem \ref{theorem_5.2}. |
| 4 | 0.753 | `corpus/arxiv/2110.08491/source/source.tex` | `text` | \bf Scalar curvatures on homogeneous toric bundles > $K$-stabilities for homogeneous toric bundles | lines 856-859 | yes | yes | homogeneous toric bundles | When $A+h_G$ is a constant function, the Definition \ref{defn_toric_hat_k-1} is the same as the definition for the homogeneous toric bundles in \cite{Sz1}. \v\v |
| 5 | 0.639 | `corpus/arxiv/2110.08491/source/source.tex` | `text` | \bf Scalar curvatures on homogeneous toric bundles > \bf Proof of Theorem \ref{theorem_1.1} | lines 876-880 | yes | yes | homogeneous toric bundles | ...ty is a necessary condition. So we only need to prove the sufficiency of uniformly relatively $K$-polystability. \v For homogeneous toric bundles, using the bound of $\mathbb D$, by the same argument as in Section \ref{Sec-4}, we have the following theorem |
| 6 | 0.610 | `corpus/arxiv/2110.08491/source/source.tex` | `text` | \bf Introduction | lines 205-208 | yes | yes | homogeneous toric bundles, filtration | ...iew the notion of relative $\widehat K$-polystability and uniform $K$-polystability. In Section \ref{Sec-Estimates}, we discuss some properties of convex functions on polytopes. In Section \ref{Sec-4}, we prove the Theorem \ref{theorem_1.3}. In Section \ref{Sec-5}, after briefly reviewing homogeneous toric bundles and the generalized Abreu equation, we sketc... |
| 7 | 0.411 | `corpus/arxiv/0905.0498/source/source.tex` | `text` | unsectioned | lines 115-134 | no | yes | - | ...and only if $E$ is polystable. We also address the more general existence problem of extremal K\"ahler metrics on such bundles and prove that the splitting of $E$ as a direct sum of stable subbundles is necessary and sufficient condition for the existence of extremal K\"ahler metrics in sufficiently small K\"ahler classes. The methods used to prove the abov... |
| 8 | 0.393 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 9 | 0.387 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | no | yes | - | ...rk) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail in our next paper and refer interested readers to the following works and references therein: |
| 10 | 0.361 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Semisimple principal fibrations > K\"ahler-Ricci solitons > K\"ahler-Ricci solitons on line bundles | lines 1707-1711 | no | yes | - | \subsubsection{K\"ahler-Ricci solitons on line bundles}\label{section-chili} In this section we discuss the examples of non-compact complete shrinking K\"ahler-Ricci solitons which are built out of certain negative line bundles $L \to B$ over a compact Fano manifold $B$. Starting with Cao \cite{Caosoliton} and Feldman-Ilmanen-Knopf \cite{FIK} in the case of... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### toric_abreu_025 - toric Abreu equation

**Question:** Where does the corpus discuss Apostolov's lecture notes on the Kahler geometry of toric manifolds?

**Expected sources:** `2208.12493`
**Expected chunk types:** `definition`, `example`, `text`
**Expected terms:** `Kahler geometry of toric manifolds`, `moment polytope`, `symplectic potential`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: no
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.514 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Proofs of Lemmas \ref{s1is2}, \ref{s1is1} and \ref{s1is2overk} | lines 1659-1726 | no | yes | - | .... London Math. Soc. {\bf 14} (1982), 1--15. \bibitem{ACG1} V. Apostolov, D.~M.~J. Calderbank and P. Gauduchon, {\it The geometry of weakly self-dual K\"ahler surfaces}, Compositio Math. {\bf 135} (2003), 279--322. \bibitem{ACG2} V. Apostolov, D.~M.~J. Calderbank and P. Gauduchon, {\it Hamiltonian $2$-forms in K\"ahler geometry} I {\it General Theory}, J. Dif... |
| 2 | 0.487 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Proof of Theorem \ref{suff} | lines 2778-2847 | no | yes | - | ...onvDF}. %\begin{acknowledgements} %\end{acknowledgements} \begin{thebibliography}{99} \bibitem{Ab03} M.~Abreu, K\"ahler geometry of toric manifolds in symplectic coordinates. \emph{Symplectic and contact topology: interactions and perspectives (Toronto, ON/Montreal, QC, 2001)}, 1--24, Fields Inst. Commun., \textbf{35}, \emph{Amer. Math. Soc., Providence, RI}... |
| 3 | 0.472 | `corpus/arxiv/2108.12297/source/source.tex` | `text` | Applications > Proof of Corollary \ref{prop-ex} | lines 1777-1834 | no | yes | - | \bibitem{PG} P. Gauduchon, \textit{Calabi’s extremal K\"ahler metrics: An elementary introduction}, Lecture Notes. \bibitem{DG2} D. Guan, \textit{Existence of extremal metrics on compact almost homogeneous Kähler manifolds with two ends}, Trans. Am. Math. Soc. \textbf{347} (1995), 2255–2262. \bibitem{DG}D. Guan, \textit{On Modified Mabuchi Functional and Mab... |
| 4 | 0.461 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted cscK problem on semisimple principal fibration | lines 2104-2110 | no | yes | - | Also, from \cite[Section 5]{AJL}, any Kähler metric \(\omega\) on \(X\) induces a Kähler metric \(\tilde{\omega}\) on \(Y\) such that the restriction \((Y_b, \tilde{\omega}_b)\) of \((Y, \tilde{\omega})\) to a fiber over a point \(b \in B\) is \(\T\)-equivariantly Kähler isomorphic to \((X, \omega)\). Such a metric \(\tilde{\omega}\) on \(Y\) is the \emph{co... |
| 5 | 0.450 | `corpus/arxiv/math_0511118/source/source.tex` | `text` | Proof of Lemma \ref{asymptotics} | lines 2993-3059 | no | yes | - | \bibitem{fujita} T.~Fujita, {\it On polarized manifolds whose adjoint bundles are not semipositive}, in `Algebraic Geometry' (Sendai, 1985), 167--178, Adv. Stud. in Pure Math. {\bf 10}, North Holland, 1987. \bibitem{gauduchon} P.~Gauduchon, {\rm Calabi's extremal metrics: An elementary introduction}, in preparation. \bibitem{guan0} D.~Guan, {\it Existence of... |
| 6 | 0.446 | `corpus/arxiv/1808.07811/source/source.tex` | `text` | The structure of the automorphism group and stability of the $(\uu,\vv)$-cscK metrics under deformations | lines 2237-2280 | no | yes | - | ...lar curvature K\"ahler metrics}, arXiv:1412.0648. \bibitem{Dyr1} Z. Sj\"ostr\"om Dyrefelt, {\it K-semistability of cscK manifolds with transcendental cohomology class}, J. Geom. Anal., 28(4), 2927-2960.. \bibitem{Dyr2} Z. Sj\"ostr\"om Dyrefelt, {\it On K-polystability of cscK manifolds with transcendental cohomology class}, arXiv:1711.11482, (with an appendi... |
| 7 | 0.444 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2864-2910 | no | yes | - | ...ly positive. In particular, it can never be $0$. \begin{thebibliography}{10} \bibitem{Abreu0} M.~Abreu, {\it K{\"a}hler geometry of toric varieties and extremal metrics}, Internat. J. Math {\bf 9} (1998), 641--651. \bibitem{Abreu1} M.~Abreu, {\it K{\"a}hler metrics on toric orbifolds}, J. Differential Geom. {\bf 58} (2001), 151--187. \bibitem{ACG1} V.~Aposto... |
| 8 | 0.441 | `corpus/my_notes/requested_non_arxiv_sources.md` | `text` | Requested non-arXiv and correction pointers > Journal-only or correction pointers | lines 7-23 | no | yes | - | ## Journal-only or correction pointers - Simon K. Donaldson, "Scalar curvature and stability of toric varieties", Journal of Differential Geometry 62 (2002), 289-349. Source: https://projecteuclid.org/euclid.jdg/1090950195 DOI: 10.4310/jdg/1090950195 Local status: bibliographic pointer only. No arXiv identifier was identified in this update. - Sebastien Bouc... |
| 9 | 0.437 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Conjectural picture | lines 716-746 | no | yes | - | ...behaviour of the K\"ahler-Einstein metrics as $\beta\rightarrow \beta_{0}$ is less clear in this case and we leave that discussion for another place. {\bf Remark} Towards the end of the writing of this paper, preprints by Berman \cite{kn:Ber} and Chi Li \cite{kn:CL2} appeared. These both seem to be very relevant to the discussion of this section, and to give... |
| 10 | 0.437 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | Uniqueness of weighted cscK metrics | lines 1005-1042 | no | yes | - | \bibitem{Do-02} S.~K.~Donaldson, {\it Scalar curvature and stability of toric varieties}, J. Differential Geom. {\bf 62} (2002), 289--349. \bibitem{donaldson1} S.~K.~Donaldson, {\it Scalar curvature and projective embeddings {\rm II}.}, Q. J. Math. {\bf 56} (2005), no.3, 345--356. \bibitem{Gauduchon} P.~Gauduchon, {\rm Calabi's extremal metrics: An elementar... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_001 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss the weighted Mabuchi functional?

**Expected sources:** `2007.01345`, `2104.09709`, `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex`
**Expected chunk types:** `definition`, `theorem`, `text`
**Expected terms:** `weighted Mabuchi`, `functional`, `weighted scalar curvature`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.809 | `corpus/arxiv/2309.02279/source/document.tex` | `remark` | Relative weighted K-stability > Twisting test configurations | lines 448-450 | no | no | weighted Mabuchi, functional | \begin{remark} In \cite[Proposition 4.3]{Der18}, the corresponding result in the unweighted case was proved using asymptotics of the Mabuchi functional; the same proof works in this setting with the weighted Mabuchi functional. \end{remark} |
| 2 | 0.805 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Introduction > Results | line 308 | no | yes | weighted Mabuchi, functional | Using the strategy of \cite{GuanUniqueness}, the convexity of the weighted Mabuchi functional allows us to obtain the following basic uniqueness result: |
| 3 | 0.774 | `corpus/arxiv/2412.07968/source/main.tex` | `definition` | Preliminaries > Weighted cscK metrics > Weighted Mabuchi functional | lines 995-997 | no | yes | weighted Mabuchi, functional | \begin{defn} The weighted Mabuchi energy $\M_{v,w}$ is an Euler--Lagrange functional of $\CH^T_\om\ni \phi \mapsto \M'_{v,w}(\phi):=(w(m_\phi) -\Scal_v(\om_\phi))\MA_{v}(\phi)$. \end{defn} |
| 4 | 0.767 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `proof` | Entropy asymptotics > Radial vs.~\na weighted entropy | lines 3375-3376 | no | no | weighted Mabuchi, functional | \begin{proof} By~\cite[Theorem~6.1]{AJL}, the weighted Mabuchi functional $\mab_{v,0}:=\ent_v+\enR_v$ is convex, where $\enR_v:=\en_v^{\p_{K_X}}$ is the weighted Ricci energy. By Lemma~\ref{lem:enconc}~(iii), it follows that $\ent_v+C\en_v^{\phi_\refe}$ is convex as well for any $C>0$ such that $\p_{K_X}+C\phi_\refe$ is psh. \end{proof} |
| 5 | 0.765 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Extension to $\cET(X, \omega)$ > {Weighted twisted energies} | lines 1230-1234 | yes | yes | functional | With these definitions, the weighted twisted Mabuchi functional admits two equivalent formulations. |
| 6 | 0.733 | `corpus/arxiv/2108.12297/source/source.tex` | `text` | Weighted distance, functionals and operators > Weighted functionals | lines 625-631 | no | yes | weighted Mabuchi, functional | \noindent When restricted to $\mathcal{K}(V, \omega_0)^{\mathbb{T}} \subset \mathcal{K}(M, \tilde \omega_0)^{\mathbb{T}}$, this functional is a special case of the weighted Mabuchi functional introduced in \cite{AL}. In our case, the following lemma, established in \cite{VA3}, follows directly from (\ref{weighted-scalarcurv}) and (\ref{weights}). |
| 7 | 0.713 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `theorem` | Regularity of minimizers | lines 4227-4228 | no | yes | weighted Mabuchi, functional | \begin{cor}\label{cor:regmin} Assume $w>0$ on $P$. Then any minimizer of the relative weighted Mabuchi functional $\mab^\rel\colon\cE^{1,S}\to\R\cup\{+\infty\}$ is an $S$-invariant $(v,w)$-weighted extremal metric. \end{cor} |
| 8 | 0.710 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `theorem` | Regularity of minimizers | lines 4224-4225 | no | yes | weighted Mabuchi, functional | \begin{thm}\label{thm:regmin} Any minimizer of the weighted Mabuchi functional $\mab_{v,w}\colon\cE^{1,S}\to\R\cup\{+\infty\}$ lies in $\cH^S$, and hence is an $S$-invariant $(v,w)$-weighted csc metric. \end{thm} |
| 9 | 0.678 | `corpus/arxiv/2108.12297/source/source.tex` | `text` | Weighted toric K-stability > The weighted Mabuchi energy | lines 1363-1369 | no | yes | weighted Mabuchi, functional | \subsection{The weighted Mabuchi energy} The volume form $\omega_0^{[\ell]}$ on $V$ is pushed forward to the measure $dx$ via the moment map $m_{0}$. Seen as functional on $\mathcal{S}(\PL)$ via (\ref{relation-potentials}), the weighted Mabuchi energy $\mathcal{M}_{\v,\w}$ satisfies |
| 10 | 0.674 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Stability notions and proof of the main results > Weighted cscK metrics and the weighted Mabuchi functional | lines 3683-3695 | no | yes | weighted Mabuchi, functional | We shall say for convenience that $\phi\in\cH^T$ (instead of $\ddcT\phi$) is a \emph{$(v,w)$-weighted csc metric} if $$ S_v(\phi)=w(m_\phi). $$ To find weighted csc metrics, we use the \emph{weighted Mabuchi functional} $$ \mab_{v,w}\colon\cH^T\to\R, $$ first introduced by Lahdili~\cite{Lah19,Lah23}. By construction, it is an Euler--Lagrange functional for t... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_002 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss weighted extremal Kahler metrics?

**Expected sources:** `1808.07811`, `2007.01345`, `2104.09709`
**Expected chunk types:** `definition`, `theorem`, `text`
**Expected terms:** `weighted extremal`, `Kahler metrics`, `Lahdili`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.549 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted cscK problem on semisimple principal fibration | lines 2177-2181 | no | yes | weighted extremal | We can now state the main result of this section which extends \cite[Theorem 2]{AJL}: while the latter concerns the existence of extremal metrics on $Y$ ($\v=1$ and $\w=$affine extremal function), here we deal with the general case of weighted extremal metrics. |
| 2 | 0.505 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | unsectioned | lines 146-172 | no | yes | Lahdili | \usepackage[utf8]{inputenc} \title[Weighted cscK metric (II): the continuity method]{Weighted cscK metric (II): the continuity method} %{Weighted cscK metric: existence and applications} \author{Eleonora Di Nezza, Simon Jubert and Abdellah Lahdili} \begin{document} \begin{abstract} In this paper we investigate the existence of metrics with weighted constant... |
| 3 | 0.385 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Applications and Discussions > Extremal K\"ahler metric | lines 1475-1478 | no | yes | - | \subsection{Extremal K\"ahler metric}\label{subsection 9.3} We discuss the situation of extremal K\"ahler(extK) metrics in Theorem~\ref{thm application 2}. To solve the extK equation, we need to choose $T$-invariant coordinates when defining weighted H\"older spaces, and we want to solve for $T$-invariant potential functions. Comparing the expansion of $\ome... |
| 4 | 0.345 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Introduction | lines 80-85 | no | yes | weighted extremal, Lahdili | Alongside weighted cscK metrics, Lahdili introduced a notion of weighted K-stability with respect to smooth degenerations \cite{Lah19}. The definition involves integrating the weighted scalar curvature of a K{\"a}hler metric over the total space of a test configuration, which requires the test configuration be smooth. While this is assumption is sufficient t... |
| 5 | 0.343 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 717-744 | no | yes | Lahdili | ...r proving Theorem~\ref{bigthm_existence_0} is to establish uniform a priori estimates for the solutions to a family of {weighted} cscK equations on the resolution of singularities $\pi: Y \to X$. Denote by $E$ the exceptional set of $\pi$. Consider a family of perturbed K\"ahler metrics $\om_\vep := \pi^\ast \om + \vep \om_Y$ on the resolution for $\vep \in... |
| 6 | 0.339 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Stability notions and proof of the main results > Weighted cscK metrics and the weighted Mabuchi functional | lines 3699-3718 | no | yes | - | ...he relative entropy of $\MA_v(\phi)$ with respect to a $T$-invariant reference volume form $\mu_\refe$; \item the \emph{weighted Ricci energy} $\rr_v(\phi)=\en_v^{\p_\refe}(\phi)$ is a twisted weighted energy with $\p_\refe:=\tfrac12\log\mu_\refe\in C^\infty(K_X)^T$. \end{itemize} The Chen--Tian formula provides a natural lsc extension $$ \mab_{v,w}\colon\cE... |
| 7 | 0.338 | `corpus/arxiv/1808.02813/source/source.tex` | `text` | unsectioned | lines 130-137 | no | yes | weighted extremal, Lahdili | \begin{abstract} We study the existence of weighted extremal K\"ahler metrics in the sense of \cite{aclg17,lahdili} on the total space of an admissible projective bundle over a Hodge K\"ahler manifold of constant scalar curvature. Admissible projective bundles have been defined in \cite{acgt}, and they include the projective line bundles~\cite{hwang-singer}... |
| 8 | 0.421 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted cscK problem on semisimple principal fibration | lines 2104-2110 | no | yes | - | Also, from \cite[Section 5]{AJL}, any Kähler metric \(\omega\) on \(X\) induces a Kähler metric \(\tilde{\omega}\) on \(Y\) such that the restriction \((Y_b, \tilde{\omega}_b)\) of \((Y, \tilde{\omega})\) to a fiber over a point \(b \in B\) is \(\T\)-equivariantly Kähler isomorphic to \((X, \omega)\). Such a metric \(\tilde{\omega}\) on \(Y\) is the \emph{co... |
| 9 | 0.333 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | unsectioned | lines 168-184 | yes | yes | weighted extremal, Lahdili | ...r for Mathematical Research, Peking University, Beijing, China} \email{lahdili.abdellah@gmail.com} \title[Uniqueness of weighted extremal metrics]{Convexity of the weighted Mabuchi functional and the uniqueness of weighted extremal metrics} \begin{abstract} We prove the uniqueness, up to a pull-back by an element of a suitable subgroup of complex automorphis... |
| 10 | 0.320 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction | lines 191-199 | no | yes | - | \section{Introduction}{\label{s:intro}} A central theme in K\"ahler geometry is the search for canonical K\"ahler metrics. The concept of \emph{constant weighted scalar curvature K\"ahler metrics} (weighted cscK for short), introduced by the third author in \cite{Lah19}, provides a unification of various related notions of canonical K\"ahler metrics that sat... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_003 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss convexity of weighted Mabuchi energy along weak geodesics?

**Expected sources:** `2007.01345`, `2303.03263`, `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex`
**Expected chunk types:** `theorem`, `proposition`, `proof`, `text`
**Expected terms:** `convexity`, `weighted Mabuchi`, `weak geodesics`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.865 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | {Convexity of weighted twisted K-energy } > Convexity of weighted twisted K-energy | lines 1467-1470 | yes | yes | convexity, weak geodesics | \subsection{Convexity of weighted twisted K-energy} As an application of the convexity of the twisted energy functional $\enE_v^{\chi}$, we establish the convexity of the weighted twisted Mabuchi energy $\cM_{v,\mathrm{w}}^{\chi}$ along weak geodesics in the finite energy space $\cET(X, \omega)$. |
| 2 | 0.675 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Introduction > Results | line 308 | yes | yes | convexity, weighted Mabuchi | Using the strategy of \cite{GuanUniqueness}, the convexity of the weighted Mabuchi functional allows us to obtain the following basic uniqueness result: |
| 3 | 0.654 | `corpus/arxiv/2007.01345/source/source.tex` | `theorem` | Convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesics | lines 639-641 | yes | yes | weak geodesics | \begin{thm} The $(\uu,\vv)$-Mabuchi energy $\mathcal{M}_{\uu,\vv}$ is continuous along weak geodesics and therefore convex in the pointwise sense. \end{thm} |
| 4 | 0.779 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction | lines 649-651 | yes | yes | convexity, weak geodesics | \begin{cor}[Weighted K-energy convexity for mixed cusp and conic singularities, see Corollary \ref{prop:extention-K-energy-divisor}]\label{cor:mixed-singularities} The weighted twisted Mabuchi functional $\cM_{v,\mathrm{w}}^{2\pi[D]}$ for mixed cusp/conic divisors admits a unique greatest lower semicontinuous extension to $\cET(X, \omega)$, that is moreover... |
| 5 | 0.588 | `corpus/arxiv/1409.7896/source/source.tex` | `text` | Introduction | lines 77-114 | no | yes | convexity, weak geodesics | \section{Introduction} In a recent paper \cite{BB}, R. Berman and B. Berndtsson established the convexity of the Mabuchi energy functional $\cM$ along the so-called \emph{weak geodesics}, answering (affirmatively) to a conjecture proposed by the first named author of this article. Given two K\"ahler metrics in the same cohomology class, it is well-known (cf.... |
| 6 | 0.562 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | \label{sec:Introduction}Introduction > Statement of the main results > Further extensions and applications | lines 414-429 | no | yes | convexity | The relation to previous results is discussed in \cite{bch}. Some further interactions between the Mabuchi functional and the notions of finite energy and entropy are also studied in \cite{bch}. For example, it is shown that the extended Mabuchi functional remains convex along finite energy geodesics. Moreover, using finite energy geodesics one can define a... |
| 7 | 0.667 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction | lines 634-644 | yes | yes | convexity, weak geodesics | \begin{mainthm}[Convexity of weighted twisted K-energy, see Theorem \ref{thm:main}]\label{thm:main0} Let $(X, \omega)$ be a compact K\"ahler manifold, $T \subset \Aut_{red}(X,\chi)$ a compact torus, and $\chi$ a $T$-invariant positive $(1,1)$-current satisfying \eqref{eq: ChiProp}. For smooth positive weight functions $v, \mathrm{w}$ on the moment polytope,... |
| 8 | 0.492 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Introduction | lines 106-118 | no | yes | convexity | \section{Introduction} Bando-Mabuchi \cite{BM} proved that K\"ahler-Einstein metric on Fano manifolds is unique up to holomorphic automorphisms in 1980s. Recently, Berndtsson \cite{Bo} generalized this uniqueness result to conic K\"ahler-Einstein metrics on Fano manifolds, by his observation on the convexity of certain energy functional (the $Ding$-functiona... |
| 9 | 0.610 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Openness of coercivity > Convexity of K-energy with mixed cusp and conic singularities | lines 1528-1534 | yes | yes | convexity, weak geodesics | \begin{cor}[Weighted K-energy convexity for mixed cusp and conic singularities]\label{prop:extention-K-energy-divisor} Let $(X,\omega)$ be a compact connected K\"ahler manifold and let $T\subset\Aut_{red}(X,[D])$ be a compact torus. For smooth weights $v,\mathrm{w}\in C^\infty(\mathfrak{t}^\vee)$ with $v,\mathrm{w}>0$ on the moment polytope $P_X$, the weight... |
| 10 | 0.474 | `corpus/arxiv/1712.06697/source/source.tex` | `text` | Introduction | lines 206-211 | no | yes | convexity | %This essentially follows from the convexity of $K$-energy along weak K\"ahler geodesics, which implies cscK metrics are global minimizers of $K$-energy. %These facts are established in \cite{Ber14-01} and \cite{clp}. %See the end of section 5 for more details. The cscK metric equation can be re-written as a pair of coupled equations |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_004 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss weighted cscK coercivity?

**Expected sources:** `2407.09929`, `2412.07968`, `2503.22183`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `weighted cscK`, `coercivity`, `Mabuchi`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.729 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Existence of singular weighted cscK metrics | lines 1668-1670 | yes | yes | weighted cscK, coercivity | \section{Existence of singular weighted cscK metrics} \label{sect_existence} We shall combine the a priori estimates obtained in the previous section and the uniform coercivity established in \cite{Boucksom_Jonsson_Trusiani_2024} to construct singular weighted cscK metrics. |
| 2 | 0.454 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | Introduction | lines 330-343 | no | yes | coercivity | Standing on other (a priori not clear to be equivalent) definitions of coercivity the kind of results seems to be known to experts. (See the the comments after Remark \ref{constant}.) We give a detail account of the above result. The discussion compares the several definitions of toric stability and coercivity, and clarifies the relationship with the general... |
| 3 | 0.446 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | unsectioned | lines 146-172 | yes | yes | weighted cscK, coercivity, Mabuchi | \usepackage[utf8]{inputenc} \title[Weighted cscK metric (II): the continuity method]{Weighted cscK metric (II): the continuity method} %{Weighted cscK metric: existence and applications} \author{Eleonora Di Nezza, Simon Jubert and Abdellah Lahdili} \begin{document} \begin{abstract} In this paper we investigate the existence of metrics with weighted constant... |
| 4 | 0.409 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | yes | - | ...ction defined on the sphere of infinity ${\mathcal S}_\infty.$ One important technical ingredient to prove existence of cscK from geodesic stability is the following properness theorem, which says that if $K$-energy is ``proper" with respect to a suitably defined distance (defined precisely in Definition \ref{d1.1} below), then cscK exists. To extend the pro... |
| 5 | 0.408 | `corpus/arxiv/2104.09709/source/source.tex` | `text` | Introduction > Main results | line 276 | no | yes | coercivity, Mabuchi | \subsection{Main results} Similarly to the usual cscK case, it is shown in \cite{lahdili2} that the solutions of \eqref{weighted-cscK-0} can be characterized as minimizers of a functional $\cE_{v, w}$ defined on the space of $\T$-invariant K\"ahler metrics in $\alpha$, extending the \emph{Mabuchi energy} to the weighted setting (see Section~\ref{s:weighted-s... |
| 6 | 0.396 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Twisted K\"ahler--Einstein currents and coercivity > Uniqueness of twisted K\"ahler--Einstein currents | lines 1104-1106 | no | yes | coercivity | \subsection{Uniqueness of twisted K\"ahler--Einstein currents}\label{sec:unique} We briefly discuss here how coercivity implies uniqueness of twisted K\"ahler--Einstein currents, under a mild regularity assumption on $\theta$. |
| 7 | 0.387 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | ...phic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelia... |
| 8 | 0.380 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction > Openness of coercivity | lines 660-673 | no | yes | coercivity | \subsubsection*{Openness of coercivity} We now turn to the openness of the coercivity condition.A natural question, repeatedly arising in Kähler geometry, is to understand the stability of cscK metrics—possibly with prescribed singularities—under variations of the underlying data, such as small deformations of the complex structure or perturbations of the Kä... |
| 9 | 0.473 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 635-663 | yes | yes | weighted cscK, coercivity, Mabuchi | \section*{Introduction} The constant scalar curvature K\"ahler (cscK) metric problem has become one of the central focus in K\"ahler geometry during the last decades. The Yau--Tian--Donaldson conjecture asserts that given a compact K\"ahler manifold with a fixed K\"ahler class, the existence of cscK metrics in the K\"ahler class is equivalent to an algebro-g... |
| 10 | 0.368 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | no | yes | - | ...rk) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail in our next paper and refer interested readers to the following works and references therein: |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_005 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss a YTD correspondence for weighted cscK metrics?

**Expected sources:** `2509.15016`, `2503.22183`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `YTD`, `weighted cscK`, `K-stability`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.735 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | unsectioned | lines 146-172 | yes | yes | weighted cscK | \usepackage[utf8]{inputenc} \title[Weighted cscK metric (II): the continuity method]{Weighted cscK metric (II): the continuity method} %{Weighted cscK metric: existence and applications} \author{Eleonora Di Nezza, Simon Jubert and Abdellah Lahdili} \begin{document} \begin{abstract} In this paper we investigate the existence of metrics with weighted constant... |
| 2 | 0.634 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | unsectioned | lines 170-190 | no | yes | weighted cscK | \title{Weighted cscK metrics (I): a priori estimates} \author{Eleonora Di Nezza, Simon Jubert and Abdellah Lahdili} \begin{document} \maketitle \begin{abstract} \noindent Let $X$ be a compact K\"ahler manifold. In this paper we study the existence of constant weighted scalar curvature K\"ahler (weighted cscK) metrics on $X$. More precisely, we establish a pr... |
| 3 | 0.508 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 671-675 | yes | yes | YTD | ...onaldson (YTD) conjecture~\cite{Yau93,Tia97,Don02} predicts that the existence of a constant scalar curvature K\"ahler (cscK) metric (and, more generally, of a `canonical' metric) $\om\in c_1(L)$ is equivalent to a stability condition on $(X,L)$ of purely algebro-geometric nature. In the special case where $X$ is Fano and $L=-K_X$ (for which cscK metrics are... |
| 4 | 0.485 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 595-604 | no | yes | YTD, weighted cscK | \section{Introduction} Finding canonical Kähler metrics is a central theme in complex geometry. In higher dimensions, constant scalar curvature Kähler (cscK) metrics provide an analogue of Poincar\'e’s uniformization theorem; see the surveys \cite{Boucksom_2018, Donaldson_2018_2} for background and further references. Kähler--Einstein metrics form an especia... |
| 5 | 0.450 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 635-663 | no | yes | weighted cscK, K-stability | \section*{Introduction} The constant scalar curvature K\"ahler (cscK) metric problem has become one of the central focus in K\"ahler geometry during the last decades. The Yau--Tian--Donaldson conjecture asserts that given a compact K\"ahler manifold with a fixed K\"ahler class, the existence of cscK metrics in the K\"ahler class is equivalent to an algebro-g... |
| 6 | 0.449 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 289-293 | no | yes | YTD | ...he recent progresses mentioned above, essentially reduce the proof of (the $\bG$-uniform version of) YTD conjecture for cscK metrics to proving that the entropy slope is algebraically approximable. More precisely %Actually, we will use our new results to formulate a main conjecture that will imply the YTD conjecture and may be more amenable to algebraic appr... |
| 7 | 0.448 | `corpus/arxiv/2104.09709/source/source.tex` | `text` | Introduction > Main results | line 276 | no | yes | - | \subsection{Main results} Similarly to the usual cscK case, it is shown in \cite{lahdili2} that the solutions of \eqref{weighted-cscK-0} can be characterized as minimizers of a functional $\cE_{v, w}$ defined on the space of $\T$-invariant K\"ahler metrics in $\alpha$, extending the \emph{Mabuchi energy} to the weighted setting (see Section~\ref{s:weighted-s... |
| 8 | 0.433 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | ...phic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelia... |
| 9 | 0.430 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 316-326 | no | yes | YTD | ...is given in \thmref{openess}. This result should be compared with Donaldson's continuity path of K\"ahler-Einstein cone metrics in the resolution of YTD conjecture for Fano K\"ahler-Einstein metrics \cite{MR3264766,MR3472831}. Donaldson's continuity path deforms the cone angles of K\"ahler-Einstein cone metrics \cite{MR2975584}. The paralleling idea is to ap... |
| 10 | 0.417 | `corpus/arxiv/1808.02813/source/source.tex` | `text` | Introduction > Motivation and Background | lines 156-160 | no | yes | YTD | Thus, finding CSCK metrics in ${\mathcal K}(M, \omega)$ corresponds to finding zeroes of the momentum map ${\boldsymbol \mu}$ whereas finding extremal K\"ahler metrics in ${\mathcal K}(M, \omega)$ corresponds to finding critical points of the Calabi functional ${\bf Cal}(J)=\|\|{\boldsymbol \mu}(J)\|\|^2= \int_M (Scal(g_J)-{\underline S})^2 \omega^m/m!$. \smalls... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_006 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss Lahdili's weighted scalar curvature?

**Expected sources:** `1808.07811`, `2007.01345`
**Expected chunk types:** `definition`, `proposition`, `text`
**Expected terms:** `Lahdili`, `weighted scalar curvature`, `momentum map`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.965 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Stability notions and proof of the main results > Weighted cscK metrics and the weighted Mabuchi functional | lines 3652-3653 | no | yes | Lahdili, weighted scalar curvature | for any $\phi\in\cH_T$, see~\eqref{equ:totaltwMA}. The following more explicit expression of the weighted scalar curvature (which is essentially equivalent to~\cite[Lemma~3.24]{BJT}) shows compatibility with Lahdili's original definition in~\cite{Lah19} (up to a factor $v$.) |
| 2 | 0.741 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Weighted Monge--Amp\`ere Operators and Weighted Energy > Weighted energy > Weighted twisted scalar curvature | lines 966-969 | no | yes | - | \subsubsection{Weighted twisted scalar curvature} We now introduce the weighted twisted scalar curvature. |
| 3 | 0.710 | `corpus/arxiv/2108.12297/source/source.tex` | `text` | A class of toric fibrations > Compatible K\"ahler metrics | lines 463-466 | no | yes | weighted scalar curvature | \noindent where $Scal_a$ is the constant scalar curvature of $(S_a,J_a,\omega_a)$ and $Scal_{\v}(\omega)$ is the $\v$-weighted scalar curvature of $(V,J_V,\omega, \mathbb{T})$, see Definition \ref{weighted-scalar}. |
| 4 | 0.689 | `corpus/arxiv/2309.02279/source/document.tex` | `lemma` | Background > Weighted K-stability | lines 352-354 | no | no | weighted scalar curvature | \begin{lemma}[\cite{Ino20}]\label{lem:average_weighted_scalar_curvature} \[\frac{(c_1(X)_T f'(\alpha_T))(\xi)}{(g'(\alpha_T))(\xi)}=\hat{S}_{v,w},\] where \(\hat{S}_{v,w}\) is the average weighted scalar curvature defined in equation \eqref{eq:average_weighted_scalar_curvature}. \end{lemma} |
| 5 | 0.645 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Weighted cscK equation as a system of elliptic PDEs | lines 408-409 | no | yes | weighted scalar curvature | \section{Weighted cscK equation as a system of elliptic PDEs}{\label{s:wsystem}} The goal of this section is to write the weighted cscK equation \eqref{wcsck} as a system of two elliptic PDEs. We start by showing the identity \eqref{def:scalv2} for the weighted scalar curvature $\Scal_\v(\omega_\varphi)$ defined in \cite{Lah19} by |
| 6 | 0.651 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `remark` | Weighted Monge--Amp\`ere Operators and Weighted Energy > Weighted energy > Weighted twisted scalar curvature | lines 986-988 | no | no | weighted scalar curvature | \begin{remark} When $\chi = 0$ the weighted twisted scalar curvature reduces to the usual weighted scalar curvature $S_v(\om_\f) = \tr_{\om_\f}(\Ric(\om_\f))$. \end{remark} |
| 7 | 0.625 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Weighted Monge--Amp\`ere Operators and Weighted Energy > Weighted energy > Weighted twisted scalar curvature | lines 1015-1016 | no | yes | - | The following result establishes that the sum of the weighted entropy and twisted Ricci energy functionals serves as an Euler-Lagrange functional for the weighted twisted scalar curvature operator. Its proof can be found in \cite[Lemma 3.29]{BJT}. |
| 8 | 0.496 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted cscK problem on semisimple principal fibration | lines 2104-2110 | no | yes | - | ...{question: if $\omega$ $T$-invariant, then what $\tilde{\omega}$ $T$-invariant?} %\textcolor{magenta}{Yes its true. Its discuss in \cite[(24) + below]{AJL}} \smallskip We recall the following fundamental formula for the scalar curvature of a compatible Kähler metric (see \cite[Lemma 5.8]{AJL}): |
| 9 | 0.491 | `corpus/arxiv/1512.06391/source/source.tex` | `text` | A Futaki invariant > The Futaki invariant for a K\"ahler class | lines 351-355 | no | yes | - | ...tric ${\tilde g}_{\omega}(X,Y) = \frac{1}{f_{K, \omega, a}^2} \omega(X, JY)$ is Einstein--Maxwell? \end{problem} By the discussion in the previous section, we are looking for metrics $\omega \in \mathcal{K}_{\Omega}^G$ such that the corresponding scalar curvature of $\tilde g$ |
| 10 | 0.482 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Conjectural picture | lines 686-688 | no | yes | - | where $S$ is the scalar curvature, $\hat{S}$ is the average value of the scalar curvature and $H$ is the Hamiltonian of the circle action. The key point is that in fact the Futaki invariant does not depend on the choice of metric, in a fixed K\"ahler class. There are other definitions which generalise to singular spaces and schemes. What is visible from the... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_007 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss weighted K-stability or weighted Donaldson-Futaki invariants?

**Expected sources:** `2104.09709`, `2503.22183`, `2509.15016`
**Expected chunk types:** `definition`, `theorem`, `text`
**Expected terms:** `weighted K-stability`, `Donaldson-Futaki`, `weighted`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.676 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction > Twisted and log K-stability | lines 202-204 | no | yes | Donaldson-Futaki | A similar result was proven by Sz\'ekelyhidi \cite[Theorem 6]{GS} in the case $L=-K_X$, where it is also shown that the log K-stability is not equivalent to twisted K-stability. Our proof also gives an explicit expression for the difference in the respective Donaldson-Futaki invariants. |
| 2 | 0.675 | `corpus/arxiv/2104.09709/source/source.tex` | `definition` | K-stability via coercivity: Deriving Corollary~\ref{stability} from Theorem~\ref{main} > Non-Archimedean functionals | lines 659-660 | yes | yes | Donaldson-Futaki, weighted | \begin{defn}\label{d:Futaki} The RHS of \eqref{slope1} is independent of $\Omega \in \tstA$ and $\omega \in \alpha$ (see \cite{lahdili2}) and is referred to as the \emph{$(v,w)$-weighted Donaldson-Futaki invariant} of a smooth $\T$-equivariant K\"ahler test configuration $(\tstX, \tstA)$. \end{defn} |
| 3 | 0.668 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Relative weighted K-stability | lines 386-389 | no | yes | weighted K-stability, weighted | \section{Relative weighted K-stability} In this section we study relative weighted K-stability. One such definition was previously given by Lahdili \cite{Lah20b}, who related the condition to existence of a weighted extremal metric. Here we give a separate treatment using inner products associated to test configurations. After showing the two definitions are... |
| 4 | 0.666 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Sufficient geometric criteria for uniform and twisted K-stability > Relationship between twisted and log K-stability | lines 690-692 | no | yes | Donaldson-Futaki | We now show that log K-stability implies twisted K-stability. A similar result was proven by Sz\'ekelyhidi in the case $L=-K_X$ with $X$ smooth \cite[Theorem 6]{GS}. The proof proceeds by an examination of the relevant Donaldson-Futaki invariants. Note that our proof gives an \emph{explicit} form of the difference between the two Donaldson-Futaki invariants.... |
| 5 | 0.434 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 738-760 | yes | yes | Donaldson-Futaki, weighted | ...w$(ii) was proved earlier by Stoppa and Sz\'ekelyhidi~\cite{SSz11}. We refer to~\S\ref{sec:wext2} for the definition of weighted extremal metrics, which correspond to critical points of the relative weighted Mabuchi energy $\mab^\rel$. Beyond extremal metrics in the sense of Calabi, Theorem~B covers K\"ahler--Ricci solitons~\cite{TZ02}, certain types of gene... |
| 6 | 0.419 | `corpus/arxiv/math_0412518/source/slopeobs_archive.tex` | `text` | Slope stability as a necessary condition for K-stability > Toric test configurations | lines 870-884 | no | yes | Donaldson-Futaki | ...slope stability one need only consider normal test configurations (by Proposition 5.1 of \cite{RT}) since their Futaki invariants are smaller and so less stable.) The deformation to the normal cone $(\X,\L_c)$ of this $Z$ corresponds to taking the positive, rational, concave, piecewise linear function $f= \min\big(c,\sum_{i=1}^m\frac{f_i}{m_i}\big)$ in Dona... |
| 7 | 0.408 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | It is an interesting question to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except i... |
| 8 | 0.406 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Proof of Theorem \ref{suff} | lines 3002-3084 | no | yes | Donaldson-Futaki | ...nifolds and homogeneous toric bundles. arXiv:2110.08491. \bibitem{LX14} C.~Li and C.~Xu, Special test configuration and K-stability of Fano varieties. \emph{Ann. of Math.} (2) \textbf{180} (2014) no.1, 197--232. \bibitem{M86} T.~Mabuchi, K-energy maps integrating Futaki invariants. \emph{Tohoku Math. J.} (2) \textbf{38} (1987) no.4, 575--593. \bibitem{M87a}... |
| 9 | 0.392 | `corpus/arxiv/2108.12297/source/source.tex` | `text` | Introduction > Main results | lines 196-228 | no | yes | weighted K-stability, weighted | ...imple principal toric fibration, Conjecture $\ref{Conjecture}$ is true if we replace condition $(3)$ with the notion of weighted uniform K-stability, see Definition $\ref{uniform-K-stable}$. \end{customthm} \noindent In the above statement, in order to define \emph{uniform} (weighted) K-stability (see Definition \ref{uniform-K-stable}), we use normalized con... |
| 10 | 0.390 | `corpus/arxiv/1603.01026/source/source.tex` | `text` | Introduction | lines 387-403 | no | yes | Donaldson-Futaki | ...mum norm considered by Dervan~\cite{Der1}. The norm is zero iff the normalization of $(\cX,\cL)$ is trivial, so uniform K-stability implies K-stability. In~\cite{BHJ1} we advocated the point of view that a test configuration defines a \emph{non-Archimedean metric} on $L$, that is, a metric on the Berkovich analytification of $(X,L)$ with respect to the trivi... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_008 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss weighted twisted cscK metrics?

**Expected sources:** `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex`, `2309.02279`, `2412.07968`
**Expected chunk types:** `definition`, `theorem`, `text`
**Expected terms:** `weighted twisted`, `cscK`, `Mabuchi`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.652 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Existence implies properness and geodesic stability > Existence implies properness | lines 4280-4282 | no | yes | cscK | The counterpart for $\chi$-twisted cscK cone metrics is given below. |
| 2 | 0.521 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 616-633 | yes | yes | weighted twisted, cscK, Mabuchi | where $S_v^{\chi}$ denotes the weighted twisted scalar curvature (see Section~\ref{sec:wen} for the precise definition). The associated Euler-Lagrange functional is the \emph{weighted twisted Mabuchi functional} $\cM_{v,\mathrm{w}}^{\chi}$, which admits a natural decomposition into three components: the weighted entropy term $\ent_v$, the twisted Ricci energ... |
| 3 | 0.464 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 843-864 | no | yes | cscK, Mabuchi | ...as that of Theorem~A, but requires a significant amount of additional work. First, we need to develop the relevant \na weighted pluripotential theory, and make sure that the relevant functionals and operators are defined in a purely algebraic way. Some of this was done in~\cite{HLi23}, but here we also need the \na versions of the twisted weighted \ma energ... |
| 4 | 0.462 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | cscK | ...phic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelia... |
| 5 | 0.448 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 717-744 | yes | yes | cscK, Mabuchi | ...r proving Theorem~\ref{bigthm_existence_0} is to establish uniform a priori estimates for the solutions to a family of {weighted} cscK equations on the resolution of singularities $\pi: Y \to X$. Denote by $E$ the exceptional set of $\pi$. Consider a family of perturbed K\"ahler metrics $\om_\vep := \pi^\ast \om + \vep \om_Y$ on the resolution for $\vep \in... |
| 6 | 0.446 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction > Applications and examples of twisted cscK metrics | lines 173-175 | no | yes | cscK | Twisted cscK metrics are also useful in constructing genuine cscK metrics. Consider a fibration $\pi: X\to B$ with a relatively ample line bundle $L_F$, such that all fibres $X_b$ admit a cscK metric on $L_F\|_b$. Take an ample line bundle $L_B$ and assume moreover that $B$ admits a twisted cscK metric with $T = \pi_*(K_{X/ B} + c L_F)$, where $c$ is a topolo... |
| 7 | 0.421 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | unsectioned | lines 146-172 | no | yes | cscK, Mabuchi | \usepackage[utf8]{inputenc} \title[Weighted cscK metric (II): the continuity method]{Weighted cscK metric (II): the continuity method} %{Weighted cscK metric: existence and applications} \author{Eleonora Di Nezza, Simon Jubert and Abdellah Lahdili} \begin{document} \begin{abstract} In this paper we investigate the existence of metrics with weighted constant... |
| 8 | 0.420 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction | lines 191-199 | no | yes | cscK, Mabuchi | \section{Introduction}{\label{s:intro}} A central theme in K\"ahler geometry is the search for canonical K\"ahler metrics. The concept of \emph{constant weighted scalar curvature K\"ahler metrics} (weighted cscK for short), introduced by the third author in \cite{Lah19}, provides a unification of various related notions of canonical K\"ahler metrics that sat... |
| 9 | 0.418 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | yes | cscK | ...ction defined on the sphere of infinity ${\mathcal S}_\infty.$ One important technical ingredient to prove existence of cscK from geodesic stability is the following properness theorem, which says that if $K$-energy is ``proper" with respect to a suitably defined distance (defined precisely in Definition \ref{d1.1} below), then cscK exists. To extend the pro... |
| 10 | 0.416 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Introduction | lines 80-85 | yes | yes | cscK | Alongside weighted cscK metrics, Lahdili introduced a notion of weighted K-stability with respect to smooth degenerations \cite{Lah19}. The definition involves integrating the weighted scalar curvature of a K{\"a}hler metric over the total space of a test configuration, which requires the test configuration be smooth. While this is assumption is sufficient t... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_009 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss openness for weighted cscK metrics?

**Expected sources:** `2407.09929`, `2412.07968`
**Expected chunk types:** `theorem`, `proof`, `text`
**Expected terms:** `openness`, `weighted cscK`, `coercivity`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.660 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | unsectioned | lines 170-190 | yes | yes | weighted cscK | \title{Weighted cscK metrics (I): a priori estimates} \author{Eleonora Di Nezza, Simon Jubert and Abdellah Lahdili} \begin{document} \maketitle \begin{abstract} \noindent Let $X$ be a compact K\"ahler manifold. In this paper we study the existence of constant weighted scalar curvature K\"ahler (weighted cscK) metrics on $X$. More precisely, we establish a pr... |
| 2 | 0.646 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Preliminaries > Weighted variational formalism in the singular setting | lines 1088-1090 | yes | yes | weighted cscK | \subsection{Weighted variational formalism in the singular setting} We recall here the weighted formalism for the variational problem of singular weighted cscK metrics on K\"ahler varieties with log terminal singularities as introduced in \cite[Sec.~3.8, 4.1]{Boucksom_Jonsson_Trusiani_2024}. |
| 3 | 0.625 | `corpus/arxiv/2506.02360/source/2025_06_03_extremal.tex` | `remark` | Main technical results | lines 416-418 | no | no | weighted cscK | ...\cite{HanLi23} for $g$-solitons. Apostolov--Jubert--Lahdili \cite{AJL23} and Lahdili \cite{Lah19} also proved ones for weighted cscK metrics with respect to K\"ahler test configurations (i.e.~ample test configurations with smooth total space and reduced central fibre); see also Inoue \cite{Ino} for $\mu$-cscK metrics. \end{remark} |
| 4 | 0.476 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Introduction | lines 272-277 | no | yes | openness, weighted cscK | ...d \log(\v(x)), x \rangle$. We note that this weight satisfies $\Lambda_{\varphi_0,\v}(\omega_0)=\tilde{\v}(\mu_0)$. The openness and the existence of a solution (for small time) of the continuity path is established through a generalization of Hasimoto's result \cite{Hash}, and an application of a quantitative version of the Implicit Function Theorem. The pr... |
| 5 | 0.465 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | ...phic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelia... |
| 6 | 0.581 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 717-744 | yes | yes | openness, weighted cscK, coercivity | ...r proving Theorem~\ref{bigthm_existence_0} is to establish uniform a priori estimates for the solutions to a family of {weighted} cscK equations on the resolution of singularities $\pi: Y \to X$. Denote by $E$ the exceptional set of $\pi$. Consider a family of perturbed K\"ahler metrics $\om_\vep := \pi^\ast \om + \vep \om_Y$ on the resolution for $\vep \in... |
| 7 | 0.463 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction > Openness of coercivity | lines 660-673 | no | yes | openness, coercivity | \subsubsection*{Openness of coercivity} We now turn to the openness of the coercivity condition.A natural question, repeatedly arising in Kähler geometry, is to understand the stability of cscK metrics—possibly with prescribed singularities—under variations of the underlying data, such as small deformations of the complex structure or perturbations of the Kä... |
| 8 | 0.455 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | unsectioned | lines 114-137 | no | yes | openness | \title[Existence, Properness and Geodesic stability]{Existence of constant scalar curvature K\"ahler cone metrics, properness and geodesic stability} \author{Kai Zheng} % \address{University of Warwick} \curraddr{Tongji University, Shanghai 200092, P.R. CHINA} \email[Kai Zheng]{kaizheng@amss.ac.cn} %\date{\today} \begin{document} \maketitle \begin{abstract}... |
| 9 | 0.429 | `corpus/arxiv/1712.06697/source/source.tex` | `text` | Introduction | lines 156-166 | no | yes | openness | ...ction{Introduction} This is the first of a series of three papers in the study of of constant scalar curvature K\"ahler metrics (cscK metrics), following a program outlined in \cite{chen15}. In this paper, we focus on establishing a priori estimates for cscK metrics in compact K\"ahler manifold without boundary. Our estimates can be easily adapted to extrema... |
| 10 | 0.424 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Applications and Discussions > Extremal K\"ahler metric | lines 1475-1478 | no | yes | - | \subsection{Extremal K\"ahler metric}\label{subsection 9.3} We discuss the situation of extremal K\"ahler(extK) metrics in Theorem~\ref{thm application 2}. To solve the extK equation, we need to choose $T$-invariant coordinates when defining weighted H\"older spaces, and we want to solve for $T$-invariant potential functions. Comparing the expansion of $\ome... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_010 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss properness of weighted Mabuchi functionals?

**Expected sources:** `2007.01345`, `2104.09709`, `2407.09929`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `properness`, `weighted Mabuchi`, `coercivity`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.670 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `remark` | Appendix > The Log-Mabuchi energy of Poincar\'e type K\"ahler metrics > Potential space of Poincar\'e type K\"ahler metrics | lines 2277-2279 | no | no | - | \begin{remark} By the maximality of the lower semicontinuous extension of the weighted twisted Mabuchi functional $\cM_{v,\mathrm{w}}^{\chi}$, the approximation procedure used in this section yields the same extension of the relevant energy functionals as the one defined in \S\ref{sec:mabext}. \end{remark} |
| 2 | 0.661 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `lemma` | Closeness > Weighted Aubin-Mabuchi functionals | lines 1360-1368 | no | no | - | \begin{lemma}{\label{l:au:ma}} The weighted Aubin-Mabuchi functionals satisfy the following relation \begin{equation*} 0\leq \frac{1}{n+1} I_\v(\varphi) \leq J_\v(\varphi) \leq \frac{n}{n+1} I_\v(\varphi). \end{equation*} \end{lemma} |
| 3 | 0.620 | `corpus/arxiv/2412.07968/source/main.tex` | `definition` | Preliminaries > Weighted cscK metrics > Weighted Mabuchi functional | lines 995-997 | no | no | weighted Mabuchi | \begin{defn} The weighted Mabuchi energy $\M_{v,w}$ is an Euler--Lagrange functional of $\CH^T_\om\ni \phi \mapsto \M'_{v,w}(\phi):=(w(m_\phi) -\Scal_v(\om_\phi))\MA_{v}(\phi)$. \end{defn} |
| 4 | 0.610 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `proof` | Entropy asymptotics > Radial vs.~\na weighted entropy | lines 3375-3376 | no | no | weighted Mabuchi | \begin{proof} By~\cite[Theorem~6.1]{AJL}, the weighted Mabuchi functional $\mab_{v,0}:=\ent_v+\enR_v$ is convex, where $\enR_v:=\en_v^{\p_{K_X}}$ is the weighted Ricci energy. By Lemma~\ref{lem:enconc}~(iii), it follows that $\ent_v+C\en_v^{\phi_\refe}$ is convex as well for any $C>0$ such that $\p_{K_X}+C\phi_\refe$ is psh. \end{proof} |
| 5 | 0.551 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | yes | properness | ...hcal S}_\infty.$ One important technical ingredient to prove existence of cscK from geodesic stability is the following properness theorem, which says that if $K$-energy is ``proper" with respect to a suitably defined distance (defined precisely in Definition \ref{d1.1} below), then cscK exists. To extend the properness theorem to the case of general automor... |
| 6 | 0.525 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | properness | ...\def\bla{BLA BLA BLA BLA} \def\sp{$\spadesuit$} % Yanir's comments \def\cs{$\clubsuit$} % Tamas' comments \title{Tian's properness conjectures and Finsler geometry of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{document}... |
| 7 | 0.504 | `corpus/arxiv/2108.12297/source/source.tex` | `text` | Introduction > Outline of the paper | lines 281-287 | no | yes | properness | \subsection{Outline of the paper} Section \ref{section-scalv} is a brief summary of the notion of weighted $(\v,\w)$-scalar curvature introduced by Lahdili \cite{AL}. In Section 3, we recall the construction and key results of semi-simple principal toric fibration established in \cite{VA2, VA3}. In Section \ref{section-distance}, we introduce weighted distan... |
| 8 | 0.512 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 843-864 | no | yes | weighted Mabuchi | ...as that of Theorem~A, but requires a significant amount of additional work. First, we need to develop the relevant \na weighted pluripotential theory, and make sure that the relevant functionals and operators are defined in a purely algebraic way. Some of this was done in~\cite{HLi23}, but here we also need the \na versions of the twisted weighted \ma energ... |
| 9 | 0.407 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 419-430 | no | yes | - | In the next section, we recall the non-Archimedean and Archimedean functionals, and explain they are related to each other. We state the basic correspondence between finite energy non-Archimedean metrics and maximal geodesic rays as established by Berman-Boucksom-Jonsson. We discuss the twist of non-Archimedean metrics that was introduced in \cite{His16b} fo... |
| 10 | 0.406 | `corpus/arxiv/2104.09709/source/source.tex` | `text` | Introduction > Method of proof | lines 300-302 | yes | yes | weighted Mabuchi, coercivity | \subsection{Method of proof} We now discuss briefly the method of proof of Theorem~\ref{main} above. It is an application of the general coercivity principle~\cite[Thm.~3.4]{DaRu}, see Section~\ref{s:coercivity} below. The latter is used in the cscK case in \cite{BDL}, and our approach is mainly inspired by these two references. Noting that in the weighted e... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_011 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss weighted energy functionals on finite energy spaces?

**Expected sources:** `2007.01345`, `2303.03263`, `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex`
**Expected chunk types:** `definition`, `proposition`, `text`
**Expected terms:** `finite energy`, `weighted energy`, `Mabuchi`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.993 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Extension to $\cET(X, \omega)$ > {Weighted twisted energies} > Extension to finite energy space | lines 1245-1248 | yes | yes | finite energy, weighted energy | \subsubsection{Extension to finite energy space} We now extend the weighted energy functionals to $\cET(X, \omega)$. The following proposition, proven in \cite{AJL} and later refined in \cite{BJT}, establishes the extension of weighted energy functionals to the finite energy space. |
| 2 | 0.962 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Extension to $\cET(X, \omega)$ > {Weighted twisted energies} | lines 1203-1206 | yes | yes | finite energy, weighted energy | \subsection{{Weighted twisted energies}} In this section, we extend the weighted energy functionals to the space $\cET(X, \omega)$ of finite energy $T$-invariant potentials. |
| 3 | 0.916 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Extension to $\cET(X, \omega)$ | lines 1172-1179 | yes | yes | finite energy, weighted energy | \section{Extension to $\cET(X, \omega)$}\label{sec:mabext} In what follows, we extend the weighted Monge--Ampère operator and weighted energy functionals to the space $$ \cET(X, \omega):=\cE^1(X,\omega)^T $$ of $T$-invariant potentials of finite energy. Our treatment is based on \cite{BDL} and \cite{AJL}. |
| 4 | 0.723 | `corpus/arxiv/1808.07811/source/source.tex` | `text` | The $(\uu,\vv)$-equivariant Bergman kernels and boundedness of the $(\uu,\vv)$-Mabuchi energy > Proof of \Cref{thm:mabuchi-bounded} | lines 1994-1995 | no | yes | Mabuchi | ...on1, lahdili2, li, ST} that has been given in the special cases \ref{1i}, \ref{ii}, \ref{iii}. We start by defining the finite dimensional analogues of the $(\uu,\vv)$-Mabuchi energy defined on the spaces ${\rm FS}^{k}_{\uu,\vv}\left(\mathcal{B}^{\T}(\mathcal{H}_k)\right)$ and $\mathcal{B}^{\T}(\mathcal{H}_k)$ as follows, |
| 5 | 0.898 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Extension to $\cET(X, \omega)$ > {Weighted Monge--Ampère operator} | lines 1180-1182 | yes | yes | finite energy | \subsection{{Weighted Monge--Ampère operator}} We start with the fundamental result that the weighted Monge--Ampère operator defined on smooth $T$-invariant K\"ahler potentials admits a continuous extension to the space $\cET(X, \omega)$ of finite energy $T$-invariant potentials. This continuity will be essential in the extension of energy functionals. |
| 6 | 0.630 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | yes | finite energy | ...lelism), thus defines a point at ${\mathcal S}_\infty.$ It is important to understand the converse: when does a locally finite energy geodesic ray define a test configuration? More importantly, can one extend the definition of $\yen$ invariant for analytic test configuration? Note that by Theorem 1.4, we can view $\yen$ invariant as a function defined on the... |
| 7 | 0.627 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 843-864 | no | yes | finite energy, Mabuchi | ...as that of Theorem~A, but requires a significant amount of additional work. First, we need to develop the relevant \na weighted pluripotential theory, and make sure that the relevant functionals and operators are defined in a purely algebraic way. Some of this was done in~\cite{HLi23}, but here we also need the \na versions of the twisted weighted \ma energ... |
| 8 | 0.740 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Weighted Monge--Amp\`ere Operators and Weighted Energy > Weighted energy > Weighted twisted scalar curvature | lines 1015-1016 | yes | yes | - | The following result establishes that the sum of the weighted entropy and twisted Ricci energy functionals serves as an Euler-Lagrange functional for the weighted twisted scalar curvature operator. Its proof can be found in \cite[Lemma 3.29]{BJT}. |
| 9 | 0.731 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | {Convexity of weighted twisted K-energy } > Weak geodesics | lines 1334-1338 | yes | yes | - | \subsection{Weak geodesics} Our analysis of weighted metrics and their functionals' properties builds substantially on the foundational framework developed by Lahdili \cite{Lah}. The proof of convexity follows the work of \cite{BDL} and \cite{AJL}. It was shown by Donaldson \cite{Donaldson-geod} and Semmes \cite{Semmes} that by letting $\tau:=e^{-t+is}$, the... |
| 10 | 0.710 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Weighted Monge--Amp\`ere Operators and Weighted Energy > Weighted Monge--Amp\`ere operators | lines 842-845 | yes | yes | - | by~\eqref{equ:twMAder}. The following lemma (\cite[Lemma 3.10]{BJT}) establishes key symmetry properties of the twisted weighted Monge--Ampère operator, which will be essential for our analysis of energy functionals. |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_012 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss weighted extremal metrics on fibrations or bundles?

**Expected sources:** `1808.07811`, `2104.09709`, `2309.02279`
**Expected chunk types:** `theorem`, `example`, `text`
**Expected terms:** `weighted extremal`, `fibration`, `bundle`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.579 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted cscK problem on semisimple principal fibration | lines 2177-2181 | no | yes | weighted extremal | We can now state the main result of this section which extends \cite[Theorem 2]{AJL}: while the latter concerns the existence of extremal metrics on $Y$ ($\v=1$ and $\w=$affine extremal function), here we deal with the general case of weighted extremal metrics. |
| 2 | 0.543 | `corpus/arxiv/0905.0498/source/source.tex` | `text` | unsectioned | lines 115-134 | no | yes | fibration, bundle | ...ic of constant scalar curvature if and only if $E$ is polystable. We also address the more general existence problem of extremal K\"ahler metrics on such bundles and prove that the splitting of $E$ as a direct sum of stable subbundles is necessary and sufficient condition for the existence of extremal K\"ahler metrics in sufficiently small K\"ahler classes.... |
| 3 | 0.483 | `corpus/arxiv/2110.08491/source/source.tex` | `text` | \bf Introduction | lines 183-187 | no | yes | fibration, bundle | In \cite{D5}, Donaldson suggested to study the existence of K\"ahler metrics of constant scalar curvatures on toric fibrations. He presented the underlying equation, which we call the generalized Abreu equation (see (\ref{gAbreu})). In \cite{CHLLS}, Chen-Han-Li-Lian-Sheng solved the problem for extremal metrics for homogeneous toric bundles with two-dimensio... |
| 4 | 0.481 | `corpus/arxiv/1808.02813/source/source.tex` | `text` | unsectioned | lines 130-137 | no | yes | weighted extremal, bundle | \begin{abstract} We study the existence of weighted extremal K\"ahler metrics in the sense of \cite{aclg17,lahdili} on the total space of an admissible projective bundle over a Hodge K\"ahler manifold of constant scalar curvature. Admissible projective bundles have been defined in \cite{acgt}, and they include the projective line bundles~\cite{hwang-singer}... |
| 5 | 0.464 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Introduction > Results | lines 320-327 | no | yes | fibration, bundle | In Section \ref{section-ssfibrations} we also take an interest in the case of shrinking K\"ahler-Ricci solitons. We explain how these metrics give examples of the type of weighted problem we consider in the case of semisimple principal toric fibrations. Returning to the question of asymptotics, we study the behavior at infinity of shrinking K\"ahler-Ricci so... |
| 6 | 0.456 | `corpus/arxiv/2104.09709/source/source.tex` | `text` | unsectioned | lines 208-225 | yes | yes | weighted extremal, fibration, bundle | \title[Weighted K-stability]{Weighted K-stability and coercivity with applications to extremal K\"ahler and Sasaki metrics } %\subtitle{To appear in {\it Geometry \& Topology}} \author[V. Apostolov]{Vestislav Apostolov} \address{Vestislav Apostolov \\ D{\'e}partement de Math{\'e}matiques\\ UQAM\\ C.P. 8888 \\ Succursale Centre-ville \\ Montr{\'e}al (Qu{\'e}b... |
| 7 | 0.453 | `corpus/arxiv/2108.12297/source/source.tex` | `text` | Introduction > Main results | lines 229-254 | no | yes | fibration, bundle | ...ilding on the proof of Theorem \ref{theoremAA}, a similar statement was established in \cite{VA6} for a larger class of fibrations associated to a certain class of principal $\mathbb{T}$-bundles over products of cscK Hodge manifolds, whose fiber is an arbitrary compact K\"ahler manifold containing $\mathbb{T}$ in its reduced automorphism group. Theorem \ref{... |
| 8 | 0.444 | `corpus/arxiv/math_0511118/source/source.tex` | `text` | unsectioned | lines 119-165 | no | yes | bundle | We obtain a characterization, on a large family of projective bundles, of those `admissible' K\"ahler classes (i.e., the ones compatible with the bundle structure in a way we make precise) which contain an extremal K\"ahler metric. In many cases, such as on geometrically ruled surfaces, every K\"ahler class is admissible. In particular, our results complete... |
| 9 | 0.430 | `corpus/arxiv/1401.0123/source/ExtPK.tex` | `text` | Introduction | lines 337-357 | no | yes | fibration | In Part \ref{sctn_almcscKfamily}, we introduce the notion of a \textit{family of K�hler metrics of almost constant scalar curvature} on a compact manifold, and construct a parametrisation in terms of automorphisms of the manifolds for such families (Proposition \ref{prop_asympparam}). Coming back to the complement of a simple normal crossing divisor in Part... |
| 10 | 0.426 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Proofs of Lemmas \ref{s1is2}, \ref{s1is1} and \ref{s1is2overk} | lines 1659-1726 | no | yes | bundle | ....~M.~J. Calderbank, P. Gauduchon and C. T{\o}nnesen-Friedman, {\it Hamiltonian $2$-forms in K\"ahler geometry} III {\it Extremal metrics and stability}, arXiv:math.DG/??????? \bibitem{Bando-Mabuchi} S. Bando and T. Mabuchi, {\it Uniqueness of Einstein--K\"ahler metrics modulo connected group actions}, in `Algebraic Geometry' (Sendai 1985), Adv. Stud. Pure Ma... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_013 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss the weighted Mabuchi Hessian or geodesic convexity mechanism?

**Expected sources:** `2007.01345`, `2303.03263`
**Expected chunk types:** `proposition`, `proof`, `text`
**Expected terms:** `Hessian`, `geodesic convexity`, `weighted Mabuchi`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.811 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Introduction > Results | line 308 | yes | yes | weighted Mabuchi | Using the strategy of \cite{GuanUniqueness}, the convexity of the weighted Mabuchi functional allows us to obtain the following basic uniqueness result: |
| 2 | 0.766 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | {Convexity of weighted twisted K-energy } > Convexity of weighted twisted K-energy | lines 1467-1470 | no | yes | - | \subsection{Convexity of weighted twisted K-energy} As an application of the convexity of the twisted energy functional $\enE_v^{\chi}$, we establish the convexity of the weighted twisted Mabuchi energy $\cM_{v,\mathrm{w}}^{\chi}$ along weak geodesics in the finite energy space $\cET(X, \omega)$. |
| 3 | 0.589 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | It is an interesting question to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except i... |
| 4 | 0.718 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | {Convexity of weighted twisted K-energy } | lines 1332-1333 | no | yes | - | \section{{Convexity of weighted twisted K-energy }} |
| 5 | 0.563 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | \label{sec:Introduction}Introduction > Statement of the main results | lines 310-335 | no | yes | Hessian | ...nd the inequality \ref{eq:chens ineq in intro} was then obtained by Chen, building on \cite{c-t}. In the case of smooth geodesics it is well-known that the Mabuchi functional $\mathcal{M}$ is \emph{strictly }convex modulo automorphisms, or more precisely modulo the group $\mbox{Aut}_{0}(X)$ defined as the connected component of the identity in the group of a... |
| 6 | 0.697 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction | lines 649-651 | no | no | - | \begin{cor}[Weighted K-energy convexity for mixed cusp and conic singularities, see Corollary \ref{prop:extention-K-energy-divisor}]\label{cor:mixed-singularities} The weighted twisted Mabuchi functional $\cM_{v,\mathrm{w}}^{2\pi[D]}$ for mixed cusp/conic divisors admits a unique greatest lower semicontinuous extension to $\cET(X, \omega)$, that is moreover... |
| 7 | 0.535 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | no | yes | - | An intriguing question motivated from above remark is whether geodesic stability in $\mathcal{E}_0^{\infty}$ (in the sense defined in the above remark) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail i... |
| 8 | 0.525 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Introduction | lines 166-184 | no | yes | Hessian | ...is to understand the existence and uniqueness problem of constant scalar curvature K\"ahler (cscK) metrics. As shown by Mabuchi \cite{M2}, the cscK metrics are the critical points of a functional called $K$-energy or the Mabuchi functional. By definition, a cscK metric satisfies the following equation: \[ R_\varphi = \underline{R} = \frac{[Ric(\omega_0)]\cdo... |
| 9 | 0.504 | `corpus/arxiv/1810.04661/source/source.tex` | `text` | Introduction | lines 252-258 | no | yes | - | Further connections with geodesic rays are explored in \cite{DDL5}, related to the metric geometry of the space of singularity types, and complex Monge--Amp\`ere equations with prescribed singularity. \vspace{-0.3cm} \paragraph{Organization of the paper.} In Section 2 we recall basic facts about the $L^p$ Mabuchi geometry of the space of K\"ahler metrics, th... |
| 10 | 0.489 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | Convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesics | lines 616-618 | yes | yes | - | Now, we can use the arguments of Berman--Berndtsson in \cite{BB} to deduce the weak convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesic segments. We will need the following regularization result which is the main ingredient in the proof of Berman--Berndtsson for the weak convexity of the Mabuchi energy \cite[Theorem 3.3]{BB}. |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_014 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss Lahdili's weighted extremal equation?

**Expected sources:** `1808.07811`, `2007.01345`
**Expected chunk types:** `definition`, `theorem`, `text`
**Expected terms:** `Lahdili`, `weighted extremal equation`, `scalar curvature`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.885 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Relative weighted K-stability | lines 386-389 | no | yes | Lahdili | \section{Relative weighted K-stability} In this section we study relative weighted K-stability. One such definition was previously given by Lahdili \cite{Lah20b}, who related the condition to existence of a weighted extremal metric. Here we give a separate treatment using inner products associated to test configurations. After showing the two definitions are... |
| 2 | 0.854 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Stability notions and proof of the main results > Weighted cscK metrics and the weighted Mabuchi functional | lines 3652-3653 | no | yes | Lahdili, scalar curvature | for any $\phi\in\cH_T$, see~\eqref{equ:totaltwMA}. The following more explicit expression of the weighted scalar curvature (which is essentially equivalent to~\cite[Lemma~3.24]{BJT}) shows compatibility with Lahdili's original definition in~\cite{Lah19} (up to a factor $v$.) |
| 3 | 0.800 | `corpus/arxiv/2309.02279/source/document.tex` | `remark` | Background > Weighted K-stability | lines 346-348 | no | no | Lahdili | \begin{remark} Lahdili has also introduced a weighted Donaldson--Futaki invariant in the case the total space \(\X\) of the K{\"a}hler test configuration is smooth \cite[Definition 11]{Lah19}. By \cite[Proposition 3.26 (3)]{Ino20}, this agrees with the invariant \(\DF_{v,w}(\X,\A_T)\) defined above, and hence Inoue's invariant provides an extension of Lahdil... |
| 4 | 0.604 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Applications and Discussions > Extremal K\"ahler metric | lines 1475-1478 | no | yes | - | \subsection{Extremal K\"ahler metric}\label{subsection 9.3} We discuss the situation of extremal K\"ahler(extK) metrics in Theorem~\ref{thm application 2}. To solve the extK equation, we need to choose $T$-invariant coordinates when defining weighted H\"older spaces, and we want to solve for $T$-invariant potential functions. Comparing the expansion of $\ome... |
| 5 | 0.695 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Relative weighted K-stability > Relative weighted K-(semi/poly)stability | lines 474-483 | no | yes | Lahdili | \subsection{Relative weighted K-(semi/poly)stability} In this section we introduce notions of relative weighted K-(semi/poly)stability. In the non-weighted setting, relative K-stability was initially introduced by Sz{\'e}kelyhidi \cite{Sze07} for algebraic varieties, and later extended to the K{\"a}hler setting by Dervan \cite{Der18}. Although relative weigh... |
| 6 | 0.636 | `corpus/arxiv/2309.02279/source/document.tex` | `theorem` | Introduction | lines 86-88 | no | yes | - | \begin{theorem}\label{thm:main} Let \((X,\alpha_T)\) be a \((v,w)\)-extremal manifold, where \(T\) is maximal in the hamiltonian isometry group of the weighted extremal metric, and the weight functions \(v,w\) satisfy Assumption \ref{ass:weights}. Then \((X,\alpha_T)\) is relatively weighted K-polystable. \end{theorem} |
| 7 | 0.475 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 664-684 | no | yes | scalar curvature | \smallskip We quickly review the basic setup and notations for the weighted cscK metrics below (see Section~\ref{sec:prelim} for more details). \begin{taggedbigset}{(GS)}\label{bigset:GS} Let $X$ be an $n$-dimensional compact K\"ahler variety with log terminal singularities, let $T \subset \Aut_{\red}(X)$ be a maximal real torus in the reduced automorphism g... |
| 8 | 0.448 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | no | yes | - | ...rk) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail in our next paper and refer interested readers to the following works and references therein: |
| 9 | 0.438 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | It is an interesting question to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except i... |
| 10 | 0.399 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Conjectural picture | lines 666-667 | no | yes | - | \section{Conjectural picture} In this final section we discuss what one might expect about the existence problem for metrics with cone singularities on a Fano manifold. It is natural to think of such a metric as a solution of a distributional equation |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_015 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss weighted cscK metrics and moment maps?

**Expected sources:** `1808.07811`, `2007.01345`, `2104.09709`
**Expected chunk types:** `definition`, `proposition`, `text`
**Expected terms:** `moment map`, `weighted cscK`, `scalar curvature`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.657 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | unsectioned | lines 146-172 | no | yes | weighted cscK, scalar curvature | \usepackage[utf8]{inputenc} \title[Weighted cscK metric (II): the continuity method]{Weighted cscK metric (II): the continuity method} %{Weighted cscK metric: existence and applications} \author{Eleonora Di Nezza, Simon Jubert and Abdellah Lahdili} \begin{document} \begin{abstract} In this paper we investigate the existence of metrics with weighted constant... |
| 2 | 0.652 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | unsectioned | lines 170-190 | no | yes | weighted cscK, scalar curvature | \title{Weighted cscK metrics (I): a priori estimates} \author{Eleonora Di Nezza, Simon Jubert and Abdellah Lahdili} \begin{document} \maketitle \begin{abstract} \noindent Let $X$ be a compact K\"ahler manifold. In this paper we study the existence of constant weighted scalar curvature K\"ahler (weighted cscK) metrics on $X$. More precisely, we establish a pr... |
| 3 | 0.601 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Background > Weighted extremal metrics | lines 174-190 | no | yes | moment map, weighted cscK | ...{v}\) or \(\widetilde{w}\) on a subset of \(\mathbb{R}\). In order to apply Inoue's equivariant intersection theory for weighted cscK metrics \cite{Ino20}, we will assume that our weight functions take this form in later sections. Furthermore, suppose we choose another moment map \(\mu'=\mu+\eta\) where \(\eta\in\mathfrak{t}^*\) is a constant. We then define... |
| 4 | 0.492 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Introduction | lines 295-300 | no | yes | - | The paper is organised as follows. In Section \ref{sec:background}, we settle the necessary background material on cscK manifolds. Then, Section \ref{sec:foldable toric surfaces} is devoted to the classification of foldable surfaces and the proofs of Proposition \ref{prop:intro fans} and Proposition \ref{prop:intro}. In Section \ref{sec:local moduli construc... |
| 5 | 0.477 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 664-684 | no | yes | moment map, weighted cscK, scalar curvature | \smallskip We quickly review the basic setup and notations for the weighted cscK metrics below (see Section~\ref{sec:prelim} for more details). \begin{taggedbigset}{(GS)}\label{bigset:GS} Let $X$ be an $n$-dimensional compact K\"ahler variety with log terminal singularities, let $T \subset \Aut_{\red}(X)$ be a maximal real torus in the reduced automorphism g... |
| 6 | 0.551 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Background > Weighted extremal metrics | lines 111-121 | no | yes | moment map, weighted cscK, scalar curvature | \subsection{Weighted extremal metrics}\label{subsec:weighted_extremal_metrics} Here we very briefly review the definitions and our conventions on weighted cscK metrics; a more thorough treatment was already given in \cite{Hal23}. Let \((X,\omega)\) be a compact \(n\)-dimensional K{\"a}hler manifold. The Ricci curvature of \(\omega\) is \[\Ric(\omega):=-\frac... |
| 7 | 0.440 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | no | no | - | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |
| 8 | 0.430 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Introduction > Results | lines 320-327 | no | yes | moment map, weighted cscK | ...f{section-ssfibrations} we also take an interest in the case of shrinking K\"ahler-Ricci solitons. We explain how these metrics give examples of the type of weighted problem we consider in the case of semisimple principal toric fibrations. Returning to the question of asymptotics, we study the behavior at infinity of shrinking K\"ahler-Ricci solitons on the... |
| 9 | 0.428 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 128-143 | no | yes | - | ...of the proof and Outline of the article} \begin{itemize} \item To prepare ourselves with the construction, we recap the momentum construction of Hwang-Singer and discuss the derivation of the desired complete cuspidal SFK metric $\omega_{HS}$ in Section \ref{section 2}. Besides, we introduce the conical family of scalar-flat K\"ahler metrics connecting the B... |
| 10 | 0.423 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 843-864 | no | yes | - | ...as that of Theorem~A, but requires a significant amount of additional work. First, we need to develop the relevant \na weighted pluripotential theory, and make sure that the relevant functionals and operators are defined in a purely algebraic way. Some of this was done in~\cite{HLi23}, but here we also need the \na versions of the twisted weighted \ma energ... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_016 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss weighted K-energy in the notes?

**Expected sources:** `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex`
**Expected chunk types:** `definition`, `proposition`, `text`
**Expected terms:** `weighted K-energy`, `weighted Mabuchi`, `twisted`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.653 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | {Convexity of weighted twisted K-energy } | lines 1332-1333 | yes | yes | twisted | \section{{Convexity of weighted twisted K-energy }} |
| 2 | 0.516 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | - | ...predict that existence of canonical K\"ahler metrics should be equivalent to various notions of properness of Mabuchi's K-energy functional. In some instances this has been verified, especially under restrictive assumptions on the automorphism group. We provide counterexamples to the original conjecture in the presence of continuous automorphisms. The constr... |
| 3 | 0.503 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | no | yes | - | ...rk) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail in our next paper and refer interested readers to the following works and references therein: |
| 4 | 0.487 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | It is an interesting question to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except i... |
| 5 | 0.423 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Applications and Discussions > Extremal K\"ahler metric | lines 1475-1478 | no | yes | - | \subsection{Extremal K\"ahler metric}\label{subsection 9.3} We discuss the situation of extremal K\"ahler(extK) metrics in Theorem~\ref{thm application 2}. To solve the extK equation, we need to choose $T$-invariant coordinates when defining weighted H\"older spaces, and we want to solve for $T$-invariant potential functions. Comparing the expansion of $\ome... |
| 6 | 0.422 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | Uniqueness of weighted cscK metrics | lines 1005-1042 | no | yes | - | ...mulation and foundational results}, arXiv:1902.00664 \bibitem{lahdili3} A. Lahdili, {\it K\"ahler metrics with constant weighted scalar curvature and weighted K-stability }, arXiv:1808.07811. \bibitem{Li} C.~Li, {\it Constant scalar curvature K\"ahler metrics obtains minimum of K-energy}, Int. Math. Res. Not., Vol. {\bf 2011} (2011), No. 9, pp. 2161--2175. \... |
| 7 | 0.410 | `corpus/arxiv/2104.09709/source/source.tex` | `text` | Weighted Futaki invariants | lines 1799-1839 | no | yes | - | ...www.cirget.uqam.ca/$\sim$apostolo/notes.html \bibitem{AC} V. Apostolov and D.~M.~J. Calderbank, {\it The CR geometry of weighted extremal K\"ahler and Sasaki metrics}, Math. Ann, {\bf 379} (2021), 1047--1088. \bibitem{ACL} V.~Apostolov, D.~M.~J. Calderbank, and E.~Legendre, {\it Weighted K-stability of polarized varieties and extremality of Sasaki manifolds}... |
| 8 | 0.398 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Proofs of Lemmas \ref{s1is2}, \ref{s1is1} and \ref{s1is2overk} | lines 1659-1726 | no | yes | - | \begin{thebibliography}{99} %\bibitem{atiyah} M.~F.~Atiyah, {\it Convexity and commuting hamiltonians}, %Bull. London Math. Soc. {\bf 14} (1982), 1--15. \bibitem{ACG1} V. Apostolov, D.~M.~J. Calderbank and P. Gauduchon, {\it The geometry of weakly self-dual K\"ahler surfaces}, Compositio Math. {\bf 135} (2003), 279--322. \bibitem{ACG2} V. Apostolov, D.~M.~J.... |
| 9 | 0.390 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | A local third derivative estimate (after Tian) | lines 3993-4008 | no | yes | - | \section{A local third derivative estimate (after Tian)} A general result due to Tian \cite{tian83}, proved in his M.Sc. thesis, gives a local a priori estimate in $W^{3,2}$ for solutions of both real and complex Monge--Amp\`ere equations under the assumption that the solution has bounded real or complex Hessian and the right hand side is at least H\"older.... |
| 10 | 0.380 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_017 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss weighted scalar curvature in toric coordinates?

**Expected sources:** `2007.01345`, `2104.09709`, `2503.22183`
**Expected chunk types:** `definition`, `example`, `text`
**Expected terms:** `weighted scalar curvature`, `toric`, `coordinates`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.797 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Background > The $v$-scalar curvature | lines 531-534 | no | yes | toric | for prescribed $w \in C^\infty(\overline{P})$. If $M$ is in addition toric, then we can understand the $v$-scalar curvature more explicitly. Indeed, the local computations in \cite[Section 3]{ApGi} (see also \cite[Section 9]{LahdiliWeighted}) give us: |
| 2 | 0.698 | `corpus/arxiv/2110.08491/source/source.tex` | `remark` | \bf Introduction | lines 200-204 | no | no | toric | ...) showed the equivalence between the existence of extremal K\"ahler metrics on the total space of semi-simple principal toric fibrations and weighted uniform $K$-stability of the corresponding Delzant polytopes. The methods in this paper can be applied to explore the problems for which the scalar curvature equations can be reduced to the equations on polytop... |
| 3 | 0.750 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `proposition` | Background > The $v$-scalar curvature | lines 535-540 | no | no | weighted scalar curvature, toric | \begin{prop}\label{vscal-toric} Suppose that $M$ is toric in the sense of Definition \ref{noncompacttoric} and $\omega$ is an AK metric with symplectic potential $u_\omega$. Set $H = \textnormal{Hess}^{-1}(u_\omega)$ as above. Then the $v$-weighted scalar curvature of $\omega$ is given by \begin{equation} \Scalv(\omega) = -\sum \left( vH_{ij} \right)_{ij}. \... |
| 4 | 0.537 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | unsectioned | lines 146-172 | yes | yes | toric | \usepackage[utf8]{inputenc} \title[Weighted cscK metric (II): the continuity method]{Weighted cscK metric (II): the continuity method} %{Weighted cscK metric: existence and applications} \author{Eleonora Di Nezza, Simon Jubert and Abdellah Lahdili} \begin{document} \begin{abstract} In this paper we investigate the existence of metrics with weighted constant... |
| 5 | 0.490 | `corpus/arxiv/2108.12297/source/source.tex` | `text` | Introduction > Outline of the paper | lines 281-287 | no | yes | toric | \subsection{Outline of the paper} Section \ref{section-scalv} is a brief summary of the notion of weighted $(\v,\w)$-scalar curvature introduced by Lahdili \cite{AL}. In Section 3, we recall the construction and key results of semi-simple principal toric fibration established in \cite{VA2, VA3}. In Section \ref{section-distance}, we introduce weighted distan... |
| 6 | 0.477 | `corpus/arxiv/0905.0498/source/source.tex` | `text` | unsectioned | lines 115-134 | no | yes | toric | ...ma$ of genus $\ge 2$. Building on ideas of Fujiki~\cite{fujiki}, we prove that $M$ admits a K\"ahler metric of constant scalar curvature if and only if $E$ is polystable. We also address the more general existence problem of extremal K\"ahler metrics on such bundles and prove that the splitting of $E$ as a direct sum of stable subbundles is necessary and suf... |
| 7 | 0.466 | `corpus/arxiv/2104.09709/source/source.tex` | `text` | Introduction > Applications to the semi-simple principal fibration construction | lines 321-323 | yes | yes | weighted scalar curvature, toric | ...c $\omega_Y$ will vary in a fixed K\"ahler class on $Y$. We also notice that when $(X, \omega_X, \T)$ is a smooth \emph{toric} K\"ahler manifold, the setup above reduces to the theory of \emph{semi-simple rigid} toric fibrations studied in \cite{HFKG1, HFKG2, HFKG4}. Inspired by the results in the latter works, we show that the scalar curvature of $\omega_Y$... |
| 8 | 0.461 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Conjectural picture | lines 686-688 | no | yes | - | where $S$ is the scalar curvature, $\hat{S}$ is the average value of the scalar curvature and $H$ is the Hamiltonian of the circle action. The key point is that in fact the Futaki invariant does not depend on the choice of metric, in a fixed K\"ahler class. There are other definitions which generalise to singular spaces and schemes. What is visible from the... |
| 9 | 0.455 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Applications and Discussions > Extremal K\"ahler metric | lines 1475-1478 | no | yes | coordinates | \subsection{Extremal K\"ahler metric}\label{subsection 9.3} We discuss the situation of extremal K\"ahler(extK) metrics in Theorem~\ref{thm application 2}. To solve the extK equation, we need to choose $T$-invariant coordinates when defining weighted H\"older spaces, and we want to solve for $T$-invariant potential functions. Comparing the expansion of $\ome... |
| 10 | 0.451 | `corpus/arxiv/1512.06391/source/source.tex` | `text` | A Futaki invariant > The Futaki invariant for a K\"ahler class | lines 351-355 | no | yes | - | ...tric ${\tilde g}_{\omega}(X,Y) = \frac{1}{f_{K, \omega, a}^2} \omega(X, JY)$ is Einstein--Maxwell? \end{problem} By the discussion in the previous section, we are looking for metrics $\omega \in \mathcal{K}_{\Omega}^G$ such that the corresponding scalar curvature of $\tilde g$ |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_018 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss weighted extremal metrics and stability on compactifications?

**Expected sources:** `2104.09709`, `2309.02279`, `2412.07968`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `weighted extremal`, `stability`, `compactification`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.617 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted cscK problem on semisimple principal fibration | lines 2177-2181 | no | yes | weighted extremal | We can now state the main result of this section which extends \cite[Theorem 2]{AJL}: while the latter concerns the existence of extremal metrics on $Y$ ($\v=1$ and $\w=$affine extremal function), here we deal with the general case of weighted extremal metrics. |
| 2 | 0.503 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Introduction | lines 80-85 | yes | yes | weighted extremal, stability | Alongside weighted cscK metrics, Lahdili introduced a notion of weighted K-stability with respect to smooth degenerations \cite{Lah19}. The definition involves integrating the weighted scalar curvature of a K{\"a}hler metric over the total space of a test configuration, which requires the test configuration be smooth. While this is assumption is sufficient t... |
| 3 | 0.483 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | no | yes | stability | An intriguing question motivated from above remark is whether geodesic stability in $\mathcal{E}_0^{\infty}$ (in the sense defined in the above remark) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail i... |
| 4 | 0.466 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 717-744 | yes | yes | stability | ...r proving Theorem~\ref{bigthm_existence_0} is to establish uniform a priori estimates for the solutions to a family of {weighted} cscK equations on the resolution of singularities $\pi: Y \to X$. Denote by $E$ the exceptional set of $\pi$. Consider a family of perturbed K\"ahler metrics $\om_\vep := \pi^\ast \om + \vep \om_Y$ on the resolution for $\vep \in... |
| 5 | 0.463 | `corpus/arxiv/1512.06391/source/source.tex` | `text` | Introduction > Outline of the main results | lines 219-238 | no | yes | stability, compactification | ...tive correspondence between compact toric $4$-orbifolds with $b_2=2$, admitting conformally K\"ahler, Einstein--Maxwell metrics on one side, and compact toric $4$-orbifolds with $b_2=2$ admitting an extremal K\"ahler metric with positive scalar curvature on the other (Proposition~\ref{duality}). This leads to many new examples (Corollary~\ref{c:existence}) w... |
| 6 | 0.455 | `corpus/arxiv/2110.08491/source/source.tex` | `remark` | \bf Introduction | lines 200-204 | no | no | stability | \begin{remark} In \cite{Del}, Delcroix expressed $K$-stability of polarized spherical varieties in terms of combinatorial data and provided a combinatorial sufficient condition of $G$-uniform $K$-stability. The appendix of \cite{Del} by Yuji Odaka showed that for non-singular spherical varieties, $G$-uniform $K$-stability is equivalent to existence of cscK m... |
| 7 | 0.452 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Applications and Discussions > Extremal K\"ahler metric | lines 1475-1478 | no | yes | - | \subsection{Extremal K\"ahler metric}\label{subsection 9.3} We discuss the situation of extremal K\"ahler(extK) metrics in Theorem~\ref{thm application 2}. To solve the extK equation, we need to choose $T$-invariant coordinates when defining weighted H\"older spaces, and we want to solve for $T$-invariant potential functions. Comparing the expansion of $\ome... |
| 8 | 0.437 | `corpus/arxiv/math_0511118/source/source.tex` | `text` | unsectioned | lines 119-165 | no | yes | stability | ...sible' K\"ahler classes (i.e., the ones compatible with the bundle structure in a way we make precise) which contain an extremal K\"ahler metric. In many cases, such as on geometrically ruled surfaces, every K\"ahler class is admissible. In particular, our results complete the classification of extremal K\"ahler metrics on geometrically ruled surfaces, answe... |
| 9 | 0.432 | `corpus/arxiv/1801.05907/source/source.tex` | `question` | Introduction | lines 282-283 | no | no | stability | \begin{q} Is the set of points defined by test configurations dense in the sphere of infinity ${\mathcal S}_\infty.\;$ More importantly, does the uniform stability or filtrated stability in the sense of G. Sz$\acute{\text{e}}$kelyhidi\cite{Sz06} imply geodesic stability? \end{q} |
| 10 | 0.427 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Proofs of Lemmas \ref{s1is2}, \ref{s1is1} and \ref{s1is2overk} | lines 1659-1726 | no | yes | stability | ....~M.~J. Calderbank, P. Gauduchon and C. T{\o}nnesen-Friedman, {\it Hamiltonian $2$-forms in K\"ahler geometry} III {\it Extremal metrics and stability}, arXiv:math.DG/??????? \bibitem{Bando-Mabuchi} S. Bando and T. Mabuchi, {\it Uniqueness of Einstein--K\"ahler metrics modulo connected group actions}, in `Algebraic Geometry' (Sendai 1985), Adv. Stud. Pure Ma... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_019 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss weighted cscK continuity or deformation methods?

**Expected sources:** `2407.09929`, `2412.07968`, `2503.22183`
**Expected chunk types:** `theorem`, `proof`, `text`
**Expected terms:** `continuity`, `deformation`, `weighted cscK`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.697 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Estimates for a weighted cscK type equation | lines 364-367 | yes | yes | continuity, weighted cscK | \section{Estimates for a weighted cscK type equation}{\label{s:esti}} As it will be explained in Section \ref{s:close}, in order to run the continuity method to solve the weighted cscK equation we need to consider the following elliptic PDEs system |
| 2 | 0.489 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Introduction | lines 185-188 | no | yes | - | ...to prove the convexity of the $K$-energy. Chen-Paun-Zeng used PDEs method in \cite{CPZ} to prove the uniqueness of the cscK metric and extremal K\"ahler metric. A natural question is: could we prove the uniqueness of cscK metric on more general K\"ahler manifolds? Note that the methods we mentioned above depend on the compactness of the manifold. As a resul... |
| 3 | 0.461 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | It is an interesting question to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except i... |
| 4 | 0.456 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Introduction | lines 66-79 | no | yes | deformation, weighted cscK | ...of K{\"a}hler--Einstein metrics \cite{Cal54}, and later in greater generality for constant scalar curvature K{\"a}hler (cscK) metrics and extremal K{\"a}hler metrics \cite{Cal82}. The existence of a cscK or extremal metric is conjecturally equivalent to various notions of K-stability, through the Yau--Tian--Donaldson conjecture \cite{Yau93, Tia97, Don02}. Th... |
| 5 | 0.453 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 138-162 | no | yes | continuity, deformation | \section{Introduction} %It is suggested by Chen \cite{MR3858468} that, the path of cscK metrics with cone singularities are expected to serve as a continuity method to find the cscK metric aiming to Yau-Tian-Donaldson conjecture, which coincides with Donaldson's continuity method in the K\"ahler-Einstein problem \cite{MR3264768,MR2975584}. In K\"ahler geomet... |
| 6 | 0.433 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction > Openness of coercivity | lines 660-673 | no | yes | deformation | ...f the coercivity condition.A natural question, repeatedly arising in Kähler geometry, is to understand the stability of cscK metrics—possibly with prescribed singularities—under variations of the underlying data, such as small deformations of the complex structure or perturbations of the Kähler (or twisting) class. This viewpoint goes back to the deformation... |
| 7 | 0.410 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction | lines 191-199 | yes | yes | continuity, weighted cscK | ...ntro}} A central theme in K\"ahler geometry is the search for canonical K\"ahler metrics. The concept of \emph{constant weighted scalar curvature K\"ahler metrics} (weighted cscK for short), introduced by the third author in \cite{Lah19}, provides a unification of various related notions of canonical K\"ahler metrics that satisfy special curvature conditions... |
| 8 | 0.402 | `corpus/arxiv/2110.08491/source/source.tex` | `remark` | \bf Introduction | lines 200-204 | no | no | - | ...by Yuji Odaka showed that for non-singular spherical varieties, $G$-uniform $K$-stability is equivalent to existence of cscK metrics. Jubert (see \cite{Jub}) showed the equivalence between the existence of extremal K\"ahler metrics on the total space of semi-simple principal toric fibrations and weighted uniform $K$-stability of the corresponding Delzant pol... |
| 9 | 0.397 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | ...phic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelia... |
| 10 | 0.392 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | regularity of weak minimizers of $K$-energy | lines 1391-1409 | no | yes | continuity | ...is section is to show the minimizers of $K$-energy over $\mathcal{E}^1$ are always smooth. The main ingredients are the continuity path as well as apriori estimates obtained in section 3. The strategy of the proof is somewhat different from the usual variational problem. Indeed, the usual strategy for variational problem will be first to take some smooth var... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### weighted_mabuchi_020 - weighted Mabuchi/Lahdili

**Question:** Where does the corpus discuss non-Archimedean aspects of weighted Mabuchi or weighted stability?

**Expected sources:** `2104.09709`, `2503.22183`, `2509.15016`
**Expected chunk types:** `definition`, `theorem`, `text`
**Expected terms:** `non-Archimedean`, `weighted Mabuchi`, `stability`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.651 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Introduction > Results | line 308 | no | yes | weighted Mabuchi | Using the strategy of \cite{GuanUniqueness}, the convexity of the weighted Mabuchi functional allows us to obtain the following basic uniqueness result: |
| 2 | 0.624 | `corpus/arxiv/2412.07968/source/main.tex` | `definition` | Preliminaries > Weighted cscK metrics > Weighted Mabuchi functional | lines 995-997 | no | yes | weighted Mabuchi | \begin{defn} The weighted Mabuchi energy $\M_{v,w}$ is an Euler--Lagrange functional of $\CH^T_\om\ni \phi \mapsto \M'_{v,w}(\phi):=(w(m_\phi) -\Scal_v(\om_\phi))\MA_{v}(\phi)$. \end{defn} |
| 3 | 0.624 | `corpus/arxiv/2309.02279/source/document.tex` | `remark` | Relative weighted K-stability > Twisting test configurations | lines 448-450 | no | no | weighted Mabuchi | \begin{remark} In \cite[Proposition 4.3]{Der18}, the corresponding result in the unweighted case was proved using asymptotics of the Mabuchi functional; the same proof works in this setting with the weighted Mabuchi functional. \end{remark} |
| 4 | 0.610 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `proof` | Entropy asymptotics > Radial vs.~\na weighted entropy | lines 3375-3376 | yes | no | weighted Mabuchi | \begin{proof} By~\cite[Theorem~6.1]{AJL}, the weighted Mabuchi functional $\mab_{v,0}:=\ent_v+\enR_v$ is convex, where $\enR_v:=\en_v^{\p_{K_X}}$ is the weighted Ricci energy. By Lemma~\ref{lem:enconc}~(iii), it follows that $\ent_v+C\en_v^{\phi_\refe}$ is convex as well for any $C>0$ such that $\p_{K_X}+C\phi_\refe$ is psh. \end{proof} |
| 5 | 0.545 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Introduction | lines 229-234 | yes | yes | weighted Mabuchi | Theorem \ref{t:exi} recovers the main result of \cite{HL25}, in which the authors establish the existence of weighted extremal metrics -a special class of weighted cscK metrics. Moreover, our proof differs in several aspects, particularly in the techniques used to obtain the $C^0$-estimates and in the application of the continuity method. \smallskip The weig... |
| 6 | 0.504 | `corpus/arxiv/1801.05907/source/source.tex` | `question` | Introduction | lines 282-283 | no | no | stability | \begin{q} Is the set of points defined by test configurations dense in the sphere of infinity ${\mathcal S}_\infty.\;$ More importantly, does the uniform stability or filtrated stability in the sense of G. Sz$\acute{\text{e}}$kelyhidi\cite{Sz06} imply geodesic stability? \end{q} |
| 7 | 0.585 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `theorem` | Regularity of minimizers | lines 4227-4228 | yes | yes | weighted Mabuchi | \begin{cor}\label{cor:regmin} Assume $w>0$ on $P$. Then any minimizer of the relative weighted Mabuchi functional $\mab^\rel\colon\cE^{1,S}\to\R\cup\{+\infty\}$ is an $S$-invariant $(v,w)$-weighted extremal metric. \end{cor} |
| 8 | 0.539 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 843-864 | yes | yes | non-Archimedean, weighted Mabuchi, stability | ...as that of Theorem~A, but requires a significant amount of additional work. First, we need to develop the relevant \na weighted pluripotential theory, and make sure that the relevant functionals and operators are defined in a purely algebraic way. Some of this was done in~\cite{HLi23}, but here we also need the \na versions of the twisted weighted \ma energ... |
| 9 | 0.429 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 419-430 | no | yes | non-Archimedean, stability | In the next section, we recall the non-Archimedean and Archimedean functionals, and explain they are related to each other. We state the basic correspondence between finite energy non-Archimedean metrics and maximal geodesic rays as established by Berman-Boucksom-Jonsson. We discuss the twist of non-Archimedean metrics that was introduced in \cite{His16b} fo... |
| 10 | 0.423 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | no | yes | stability | An intriguing question motivated from above remark is whether geodesic stability in $\mathcal{E}_0^{\infty}$ (in the sense defined in the above remark) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail i... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_001 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss convexity of the extended K-energy on finite energy spaces?

**Expected sources:** `1510.01260`
**Expected chunk types:** `theorem`, `proposition`, `proof`
**Expected terms:** `extended K-energy`, `finite energy`, `convexity`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.650 | `corpus/arxiv/1602.03114/source/source.tex` | `text` | Preliminaries > The energy functionals > The (twisted) K-energy | lines 344-346 | no | no | - | \subsubsection*{The (twisted) K-energy} Fix a closed smooth positive $(1,1)$-form $\chi$. The (extended) K-energy $\Kenergy: \mathcal E^1 \to (-\infty,\infty]$ is defined as follows: |
| 2 | 0.584 | `corpus/arxiv/1510.01260/source/source.tex` | `theorem` | Introduction | lines 153-155 | yes | yes | finite energy | \begin{theorem}[Theorem \ref{ExtKEnergyThm}] \label{ExtKEnergyThmIntr} Suppose $(X,\o)$ is a compact connected K\"ahler manifold. The K-energy can be extended to a functional $\mathcal K:\mathcal E^1 \to (-\infty, \infty]$ using formula \eqref{KEnergyDef}. The restricted functional $\mathcal K\|_{\mathcal E^p}$ is the greatest $d_p$-lsc extension of $\mathcal... |
| 3 | 0.545 | `corpus/arxiv/1810.04661/source/source.tex` | `text` | The metric geometry of weak $L^p$ geodesic rays | lines 731-737 | no | no | extended K-energy, convexity | \paragraph{Convexity of the radial K-energy. }Let $p \geq 1$. The \emph{radial K-energy} is defined for any $\{u_t\}_t \in \mathcal R^p_\o$, and is given by the expression $$\mathcal K\{u_t\} := \lim_{t\to \infty}\frac{\mathcal K(u_t)}{t},$$ where $\mathcal K: \mathcal E^p_\o \to (-\infty,\infty]$ is the extended K-energy of Mabuchi from \cite{BBEGZ11,BDL17}... |
| 4 | 0.596 | `corpus/arxiv/1602.03114/source/source.tex` | `conjecture` | Introduction and main results | lines 147-148 | no | no | extended K-energy | \begin{conjecture}[Conjecture 2.9 in \cite{DR17}] \label{conj: DRconj} Suppose $(X,\omega)$ is a compact K\"ahler manifold. The minimizers of the extended K-energy $\Kenergy: \mathcal E^1 \to (-\infty,+\infty]$ are smooth csck metrics. \end{conjecture} |
| 5 | 0.455 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | \label{sec:Introduction}Introduction > Statement of the main results > Further extensions and applications | lines 414-429 | no | no | finite energy, convexity | The relation to previous results is discussed in \cite{bch}. Some further interactions between the Mabuchi functional and the notions of finite energy and entropy are also studied in \cite{bch}. For example, it is shown that the extended Mabuchi functional remains convex along finite energy geodesics. Moreover, using finite energy geodesics one can define a... |
| 6 | 0.446 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 595-604 | no | no | finite energy, convexity | ...ariational advancements \cite{Darvas_Rubinstein_2017, BDL, CC1, CC2} relate cscK existence to coercivity of the Mabuchi K-energy. Li's work \cite{Li22} further connects the variational picture to stability through geodesic rays and model filtrations, and these ideas have recently led to a variational, Yau--Tian--Donaldson-type correspondence in a number of s... |
| 7 | 0.417 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | preliminaries | lines 394-400 | no | no | finite energy, convexity | ...In this section, we will review some basic concepts in K\"ahler geometry as well as some fundamental results involving finite energy currents, which will be needed for our proof of Theorem 1.1 and 1.3. In particular, it includes the characterization of the space $(\mathcal{E}^1,d_1)$, a compactness result on bounded subsets of $\mathcal{E}^1$ with finite en... |
| 8 | 0.409 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | no | finite energy | ...lelism), thus defines a point at ${\mathcal S}_\infty.$ It is important to understand the converse: when does a locally finite energy geodesic ray define a test configuration? More importantly, can one extend the definition of $\yen$ invariant for analytic test configuration? Note that by Theorem 1.4, we can view $\yen$ invariant as a function defined on the... |
| 9 | 0.407 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Introduction > Coercivity and Ding-stability | lines 516-542 | no | no | finite energy, convexity | ...d Ding-stability} We now describe our strategy of proof of Theorem A. Choose a K\"ahler form $\om_0\in c_1(L)$, so that finite energy currents in $c_1(L)$ get parametrized by the space $\cE^1=\cE^1(X,\om_0)$ of finite energy potentials~\cite{GZ,BBGZ}, a complete geodesic space with respect to a metric $d_1$ introduced by Darvas~\cite{Dar15}. By~\cite{BBEGZ},... |
| 10 | 0.496 | `corpus/arxiv/1510.01260/source/source.tex` | `text` | Introduction | lines 145-152 | yes | no | extended K-energy, finite energy, convexity | Our starting point is the observation that the K-energy functional $\mathcal K$ originally defined on $\mathcal H_\o$ admits a natural ``analytic extension" to the finite energy space $\mathcal E^1$ (and hence by restriction to all spaces $\mathcal E^p$). This is simply the extension obtained by interpreting the entropy part (the first term) and the energy p... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_002 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss convexity of K-energy along weak geodesics?

**Expected sources:** `1405.0401`, `1409.7896`, `1510.01260`
**Expected chunk types:** `theorem`, `proof`, `text`
**Expected terms:** `K-energy`, `weak geodesics`, `convexity`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.681 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | unsectioned | lines 126-159 | yes | yes | K-energy, weak geodesics, convexity | ...nname}{Proposition} \providecommand{\remarkname}{Remark} \providecommand{\theoremname}{Theorem} \begin{document} \title{Convexity of the K-energy on the space of K\"ahler metrics and uniqueness of extremal metrics} \author{Robert J. Berman, Bo Berndtsson} \curraddr{Department of Mathemical Sciences, Chalmers University of Technology and University of Gothenb... |
| 2 | 0.675 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction | lines 649-651 | no | yes | K-energy, weak geodesics, convexity | \begin{cor}[Weighted K-energy convexity for mixed cusp and conic singularities, see Corollary \ref{prop:extention-K-energy-divisor}]\label{cor:mixed-singularities} The weighted twisted Mabuchi functional $\cM_{v,\mathrm{w}}^{2\pi[D]}$ for mixed cusp/conic divisors admits a unique greatest lower semicontinuous extension to $\cET(X, \omega)$, that is moreover... |
| 3 | 0.599 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | Convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesics | lines 616-618 | no | yes | convexity | Now, we can use the arguments of Berman--Berndtsson in \cite{BB} to deduce the weak convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesic segments. We will need the following regularization result which is the main ingredient in the proof of Berman--Berndtsson for the weak convexity of the Mabuchi energy \cite[Theorem 3.3]{BB}. |
| 4 | 0.649 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | {Convexity of weighted twisted K-energy } > Convexity of weighted twisted K-energy | lines 1467-1470 | no | yes | K-energy, weak geodesics, convexity | \subsection{Convexity of weighted twisted K-energy} As an application of the convexity of the twisted energy functional $\enE_v^{\chi}$, we establish the convexity of the weighted twisted Mabuchi energy $\cM_{v,\mathrm{w}}^{\chi}$ along weak geodesics in the finite energy space $\cET(X, \omega)$. |
| 5 | 0.483 | `corpus/arxiv/1409.7896/source/source.tex` | `text` | Introduction | lines 77-114 | yes | yes | weak geodesics, convexity | \section{Introduction} In a recent paper \cite{BB}, R. Berman and B. Berndtsson established the convexity of the Mabuchi energy functional $\cM$ along the so-called \emph{weak geodesics}, answering (affirmatively) to a conjecture proposed by the first named author of this article. Given two K\"ahler metrics in the same cohomology class, it is well-known (cf.... |
| 6 | 0.578 | `corpus/arxiv/2007.01345/source/source.tex` | `theorem` | Convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesics | lines 639-641 | no | yes | weak geodesics | \begin{thm} The $(\uu,\vv)$-Mabuchi energy $\mathcal{M}_{\uu,\vv}$ is continuous along weak geodesics and therefore convex in the pointwise sense. \end{thm} |
| 7 | 0.574 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction | lines 634-644 | no | yes | K-energy, weak geodesics, convexity | \begin{mainthm}[Convexity of weighted twisted K-energy, see Theorem \ref{thm:main}]\label{thm:main0} Let $(X, \omega)$ be a compact K\"ahler manifold, $T \subset \Aut_{red}(X,\chi)$ a compact torus, and $\chi$ a $T$-invariant positive $(1,1)$-current satisfying \eqref{eq: ChiProp}. For smooth positive weight functions $v, \mathrm{w}$ on the moment polytope,... |
| 8 | 0.570 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | Convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesics | lines 430-431 | no | yes | weak geodesics, convexity | \section{Convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesics} The following formulas allow us to compute the second variations of the energy functionals $\mathcal{E}^{\theta}_{\uu}$ and $\mathcal{E}_{\vv}$ along weak geodesics. |
| 9 | 0.423 | `corpus/arxiv/1712.06697/source/source.tex` | `text` | Introduction | lines 206-211 | no | yes | convexity | %This essentially follows from the convexity of $K$-energy along weak K\"ahler geodesics, which implies cscK metrics are global minimizers of $K$-energy. %These facts are established in \cite{Ber14-01} and \cite{clp}. %See the end of section 5 for more details. The cscK metric equation can be re-written as a pair of coupled equations |
| 10 | 0.412 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Introduction | lines 106-118 | no | yes | convexity | ...{Bo} generalized this uniqueness result to conic K\"ahler-Einstein metrics on Fano manifolds, by his observation on the convexity of certain energy functional (the $Ding$-functional) along geodesics in the space of all K\"ahler potentials. And Berndtsson's method is further generalized to prove the uniqueness of singular K\"ahler-Einstein metrics on \emph{kl... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_003 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss the Berman-Darvas-Lu extension of Mabuchi energy?

**Expected sources:** `1510.01260`
**Expected chunk types:** `definition`, `theorem`, `text`
**Expected terms:** `Berman`, `Darvas`, `Lu`, `Mabuchi energy`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.703 | `corpus/arxiv/1409.7896/source/source.tex` | `text` | Fiber-wise approximation of $\cG$ > Continuity at the boundary | lines 806-808 | no | yes | - | where $E$ is the energy part of the Mabuchi functional, and $H$ is the entropy part. As a consequence of our previous results, we establish here the following statement. |
| 2 | 0.655 | `corpus/arxiv/2104.09709/source/source.tex` | `text` | Introduction > Method of proof | lines 300-302 | no | yes | Lu, Mabuchi energy | \subsection{Method of proof} We now discuss briefly the method of proof of Theorem~\ref{main} above. It is an application of the general coercivity principle~\cite[Thm.~3.4]{DaRu}, see Section~\ref{s:coercivity} below. The latter is used in the cscK case in \cite{BDL}, and our approach is mainly inspired by these two references. Noting that in the weighted e... |
| 3 | 0.652 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 375-393 | no | yes | Berman, Darvas, Lu | Given the recent work by J. Street\cite{Street12}, Berman-Darvas-Lu\cite{Darvas1602}, the weak Calabi flow always exists globally. Perhaps one can prove this conjecture via improving regularity of weak Calabi flow. On the other hand, one may hope to prove this conjecture on K\"ahler classes which already admit constant scalar curvature K\"ahler metrics and p... |
| 4 | 0.649 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Stability notions and proof of the main results > Weighted cscK metrics and the weighted Mabuchi functional | lines 3699-3718 | no | yes | Lu | ...ropy of $\MA_v(\phi)$ with respect to a $T$-invariant reference volume form $\mu_\refe$; \item the \emph{weighted Ricci energy} $\rr_v(\phi)=\en_v^{\p_\refe}(\phi)$ is a twisted weighted energy with $\p_\refe:=\tfrac12\log\mu_\refe\in C^\infty(K_X)^T$. \end{itemize} The Chen--Tian formula provides a natural lsc extension $$ \mab_{v,w}\colon\cE^{1,T}\to\R\cup... |
| 5 | 0.632 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | Lu | ...uestion to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except in the Fano manifold wh... |
| 6 | 0.597 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Preliminaries > Geodesic rays > Finite energy rays | lines 1133-1140 | no | yes | Berman, Darvas, Lu | ...s a psh Hermitian metric on $p_1^*L$, i.e. it is locally represented by plurisubharmonic potential functions. A (finite energy) geodesic joining $\vphi_i, i=1,2\in \cE^1(L)$ is by definition the largest psh path dominated by $\vphi_0$ and $\vphi_1$. Any (finite energy) {\it geodesic ray} in this paper is a finite energy geodesic ray emanating from the fixed... |
| 7 | 0.581 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `remark` | Appendix > The Log-Mabuchi energy of Poincar\'e type K\"ahler metrics > Potential space of Poincar\'e type K\"ahler metrics | lines 2277-2279 | no | no | - | \begin{remark} By the maximality of the lower semicontinuous extension of the weighted twisted Mabuchi functional $\cM_{v,\mathrm{w}}^{\chi}$, the approximation procedure used in this section yields the same extension of the relevant energy functionals as the one defined in \S\ref{sec:mabext}. \end{remark} |
| 8 | 0.576 | `corpus/arxiv/1512.06391/source/source.tex` | `text` | A Futaki invariant > The Futaki invariant for a K\"ahler class | lines 351-355 | no | yes | - | ...tric ${\tilde g}_{\omega}(X,Y) = \frac{1}{f_{K, \omega, a}^2} \omega(X, JY)$ is Einstein--Maxwell? \end{problem} By the discussion in the previous section, we are looking for metrics $\omega \in \mathcal{K}_{\Omega}^G$ such that the corresponding scalar curvature of $\tilde g$ |
| 9 | 0.551 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | ...r dimension. Nevertheless, it would be interesting to study what goes through the new difficulties. We expect the right extension of the notion of foldable fans in higher dimension to be fans whose lattice automorphism group admit a subgroup that acts with no fixed point. This raises several questions : \begin{enumerate} \item Do all crystallographic groups... |
| 10 | 0.533 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | Darvas, Lu | ...s of Tian predict that existence of canonical K\"ahler metrics should be equivalent to various notions of properness of Mabuchi's K-energy functional. In some instances this has been verified, especially under restrictive assumptions on the automorphism group. We provide counterexamples to the original conjecture in the presence of continuous automorphisms.... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_004 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss finite energy spaces E1 and the Mabuchi functional?

**Expected sources:** `1510.01260`, `1602.03114`
**Expected chunk types:** `definition`, `theorem`, `text`
**Expected terms:** `E1`, `finite energy`, `Mabuchi`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.871 | `corpus/arxiv/1409.7896/source/source.tex` | `text` | Fiber-wise approximation of $\cG$ > Continuity at the boundary | lines 806-808 | no | yes | Mabuchi | where $E$ is the energy part of the Mabuchi functional, and $H$ is the entropy part. As a consequence of our previous results, we establish here the following statement. |
| 2 | 0.681 | `corpus/arxiv/1602.03114/source/source.tex` | `text` | Preliminaries > The energy functionals > The (twisted) K-energy | lines 368-379 | yes | yes | finite energy, Mabuchi | where $\bar{S}_\chi = nV^{-1}\int_X (\Ric(\omega) - \chi) \wedge \omega^{n-1}$. Hence, the critical points of $\Kenergy_{\chi}$ are the twisted csck potentials, as these satisfy $\bar S_{\chi}-S_{\omega_u} + \Tr^{\omega_u}(\chi)=0$. In \cite[Proposition 5.26]{DR17} it is shown that this functional naturally extends to the $L^1$-Mabuchi completion of $\Homega... |
| 3 | 0.674 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Introduction > Coercivity and Ding-stability | lines 516-542 | no | yes | finite energy | ...d Ding-stability} We now describe our strategy of proof of Theorem A. Choose a K\"ahler form $\om_0\in c_1(L)$, so that finite energy currents in $c_1(L)$ get parametrized by the space $\cE^1=\cE^1(X,\om_0)$ of finite energy potentials~\cite{GZ,BBGZ}, a complete geodesic space with respect to a metric $d_1$ introduced by Darvas~\cite{Dar15}. By~\cite{BBEGZ},... |
| 4 | 0.665 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | \label{sec:Introduction}Introduction > Statement of the main results > Further extensions and applications | lines 414-429 | no | yes | finite energy, Mabuchi | The relation to previous results is discussed in \cite{bch}. Some further interactions between the Mabuchi functional and the notions of finite energy and entropy are also studied in \cite{bch}. For example, it is shown that the extended Mabuchi functional remains convex along finite energy geodesics. Moreover, using finite energy geodesics one can define a... |
| 5 | 0.811 | `corpus/arxiv/1409.7896/source/source.tex` | `text` | Fiber-wise approximation of $\cG$ > Convexity | lines 616-617 | no | yes | Mabuchi | \noindent Let $\cM_k$ be the Mabuchi functional evaluated on the weak geodesic $\cG$, with the entropy term modified by using $\log\omega_{t, k}^n$ instead of $\log\cG^n$, i.e. |
| 6 | 0.635 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 419-430 | no | yes | finite energy, Mabuchi | In the next section, we recall the non-Archimedean and Archimedean functionals, and explain they are related to each other. We state the basic correspondence between finite energy non-Archimedean metrics and maximal geodesic rays as established by Berman-Boucksom-Jonsson. We discuss the twist of non-Archimedean metrics that was introduced in \cite{His16b} fo... |
| 7 | 0.622 | `corpus/arxiv/1510.01260/source/source.tex` | `text` | Introduction | lines 145-152 | yes | yes | finite energy | Our starting point is the observation that the K-energy functional $\mathcal K$ originally defined on $\mathcal H_\o$ admits a natural ``analytic extension" to the finite energy space $\mathcal E^1$ (and hence by restriction to all spaces $\mathcal E^p$). This is simply the extension obtained by interpreting the entropy part (the first term) and the energy p... |
| 8 | 0.620 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction > The minimum norm and the Mabuchi functional. | lines 132-133 | no | yes | Mabuchi | \subsection{The minimum norm and the Mabuchi functional.}\label{introminnorm} To motivate Conjecture \ref{introconjecture} further, we now discuss the link between uniform K-stability with respect to the minimum norm and coercivity of the Mabuchi functional, referring to \cite{XC} for an introduction to the Mabuchi functional. Let $(X,L)$ be a smooth polaris... |
| 9 | 0.607 | `corpus/arxiv/1801.05907/source/source.tex` | `question` | Introduction | lines 261-263 | no | no | finite energy | \begin{q} How do we characterize the set of $\psi\in L^p(M,\omega)$ ($p\geq1$) which is the initial velocity of a locally finite energy geodesic ray with unit speed? Or more importantly, is the set of velocities (which give rise to a locally finite geodesic ray) a convex subset of $L^p(M, \omega)? $ \end{q} |
| 10 | 0.600 | `corpus/arxiv/2104.09709/source/source.tex` | `text` | Introduction > Method of proof | lines 300-302 | no | yes | finite energy, Mabuchi | \subsection{Method of proof} We now discuss briefly the method of proof of Theorem~\ref{main} above. It is an application of the general coercivity principle~\cite[Thm.~3.4]{DaRu}, see Section~\ref{s:coercivity} below. The latter is used in the cscK case in \cite{BDL}, and our approach is mainly inspired by these two references. Noting that in the weighted e... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_005 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss weak minimizers of the K-energy and regularity?

**Expected sources:** `1602.03114`
**Expected chunk types:** `theorem`, `proof`, `text`
**Expected terms:** `weak minimizers`, `K-energy`, `regularity`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.931 | `corpus/arxiv/1510.01260/source/source.tex` | `text` | Extension of the twisted K-energy > Uniqueness of twisted K-energy minimizers | lines 1009-1010 | no | yes | K-energy | %As a strategy to find minimizers of the K-energy, one may consider finding minimizers of the twisted K-energy first and then consider the limit as the twisting form goes to zero. This was put forward in recent works \cite{c4,cpz}, in case of smooth minimizers, and below we provide a partial weak analog of one of their results: |
| 2 | 0.835 | `corpus/arxiv/2104.09709/source/source.tex` | `text` | Regularity of the weak minimizers of the weighted Mabuchi energy | lines 1418-1419 | no | yes | weak minimizers, regularity | \section{Regularity of the weak minimizers of the weighted Mabuchi energy}\label{s:regularity} In this section, we establish the regularity of the weak minimizers of $\cE_{v,w}$. |
| 3 | 0.730 | `corpus/arxiv/1602.03114/source/source.tex` | `text` | Introduction and main results | lines 141-146 | yes | yes | weak minimizers, K-energy, regularity | ...f Fano manifolds) in \cite[Theorem 2.4]{DR17}, and this paper also linked the resolution of the general conjecture to a regularity question on weak minimizers of the K-energy that we elaborate now. We denote by $(\mathcal E^1,d_1)$ the metric completion of $\Homega$ with respect to the $L^1$-type Mabuchi path length metric $d_1$. We refer to Sections 2.1-2.2... |
| 4 | 0.557 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | K-energy, regularity | ...predict that existence of canonical K\"ahler metrics should be equivalent to various notions of properness of Mabuchi's K-energy functional. In some instances this has been verified, especially under restrictive assumptions on the automorphism group. We provide counterexamples to the original conjecture in the presence of continuous automorphisms. The constr... |
| 5 | 0.534 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 305-310 | no | yes | weak minimizers, regularity | ...1605}. For the converse direction, Darvas and Rubinstein in \cite{Dar-Rub-17} have reduced this problem to a problem of regularity of weak minimizers of $K$-energy over the space $\mathcal{E}^1$, which we resolved in the second paper \cite{cc2}. (In the special case of toric varieties, Zhou-Zhu\cite{zz08} proved the existence of toric invariant weak minimize... |
| 6 | 0.640 | `corpus/arxiv/1602.03114/source/source.tex` | `conjecture` | Introduction and main results | lines 147-148 | yes | no | K-energy | \begin{conjecture}[Conjecture 2.9 in \cite{DR17}] \label{conj: DRconj} Suppose $(X,\omega)$ is a compact K\"ahler manifold. The minimizers of the extended K-energy $\Kenergy: \mathcal E^1 \to (-\infty,+\infty]$ are smooth csck metrics. \end{conjecture} |
| 7 | 0.500 | `corpus/arxiv/1801.00656/source/source.tex` | `remark` | Introduction | lines 290-292 | no | no | regularity | \begin{rem}W. He and Y. Zeng \cite{He-Zeng} proved Chen's conjecture on the regularity of $C^{1,1}$ minimizers of $K$-energy. Their original proof contains an unnecessary assumption that the $(1,1)$ current defined by the minimizer has a strictly positive lower bound which can be removed by adopting a weak K\"ahler-Ricci flow method initiated in Section 7 of... |
| 8 | 0.491 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | \label{sec:Introduction}Introduction > Statement of the main results > Further extensions and applications | lines 372-401 | no | yes | weak minimizers, K-energy, regularity | ...loited in the companion paper \cite{bch} by Lu and the first author, is that it also has bearings on the uniqueness and regularity problem for very weak minimizers of the (twisted) Mabuchi functional. The point is that, extending the results in \cite{bbegz} concerning the case when $[\omega]=c_{1}(X)$, the Mabuchi functional, as defined by formula \ref{eq:fo... |
| 9 | 0.465 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Background materials > Riemannian geometry of the space of K\"ahler potentials | lines 389-393 | no | yes | regularity | ...he other hand, Chen \cite{Ch00a} proved that the Dirichlet problem of \eqref{geod_MA} always has a unique solution in a weak sense (\cite{BT76}). After successive refinement in \cite{Bl12} and \cite{CTW17}, it is proved that the weak solution has $C^{1,1}$ regularity. |
| 10 | 0.434 | `corpus/arxiv/1712.06697/source/source.tex` | `remark` | Introduction | lines 266-269 | no | no | - | \begin{rem} In Theorem \ref{t1.1} and the first part of Theorem \ref{t1.2}, it is sufficient to assume that $\varphi$ remains bounded under $L^1$ geodesic distance, due to the fact that cscK metrics are minimizers of $K$-energy. We will discuss this matter in more detail in our next paper of the series. \end{rem} |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_006 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss properness of the K-energy and existence of cscK metrics?

**Expected sources:** `1602.03114`, `1506.07129`, `1801.00656`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `properness`, `K-energy`, `cscK`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.781 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 179-182 | no | yes | properness, cscK | We will prove that the existence of cscK cone metrics in terms of the properness of the log $K$-energy. |
| 2 | 0.687 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Preliminaries > More functionals | lines 1285-1287 | no | yes | cscK | %By proving Theorem \ref{thm-Echislope}, we will show that this is well-defined and does not depend on the choice of the decreasing sequence $\Phi_m$. The constant scalar curvature K\"{a}hler metrics are global minimizers of Mabuchi functional $\bfM(\vphi)$. We now have the following important analytic criterion for the existence of cscK metrics: |
| 3 | 0.710 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | no | no | cscK | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |
| 4 | 0.695 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Regularity and uniqueness of log $\chi$-twisted $K$-energy minimisers | lines 4049-4050 | no | yes | properness, cscK | ...and uniqueness of the log $\chi$-twisted $K$-energy minimisers. They will be used in the next section to prove that the existence of cscK cone metrics implies the properness of the log $K$-energy. |
| 5 | 0.531 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | yes | properness, cscK | ...iant as a function defined on the sphere of infinity ${\mathcal S}_\infty.$ One important technical ingredient to prove existence of cscK from geodesic stability is the following properness theorem, which says that if $K$-energy is ``proper" with respect to a suitably defined distance (defined precisely in Definition \ref{d1.1} below), then cscK exists. To e... |
| 6 | 0.520 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | yes | yes | properness, K-energy | ...\def\bla{BLA BLA BLA BLA} \def\sp{$\spadesuit$} % Yanir's comments \def\cs{$\clubsuit$} % Tamas' comments \title{Tian's properness conjectures and Finsler geometry of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{document}... |
| 7 | 0.513 | `corpus/arxiv/1712.06697/source/source.tex` | `text` | Introduction | lines 156-166 | no | yes | properness, cscK | ...ction{Introduction} This is the first of a series of three papers in the study of of constant scalar curvature K\"ahler metrics (cscK metrics), following a program outlined in \cite{chen15}. In this paper, we focus on establishing a priori estimates for cscK metrics in compact K\"ahler manifold without boundary. Our estimates can be easily adapted to extrema... |
| 8 | 0.488 | `corpus/arxiv/1810.04661/source/source.tex` | `text` | Introduction | lines 90-102 | no | yes | properness, K-energy, cscK | ...ecture \cite{Do99}. The main result is obtained via a detailed analysis of the rays associated to the space of K\"ahler metrics. Suppose $(X,\omega)$ is a compact K\"ahler manifold with $\dim X =n$. We consider $\mathcal H$, the space of K\"ahler metrics cohomologous to $\omega$, with its $L^p$ type Mabuchi metric structures $(\mathcal H,d_p), \ p \geq 1$ \c... |
| 9 | 0.424 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 247-263 | yes | yes | properness, cscK | Note that the direction that existence of cscK implies properness has been established by Berman-Darvas-Lu\cite{Darvas1605} recently. For the converse (namely the existence part), Darvas and Rubinstein have reduced this problem in \cite{DR} to a question of regularity of minimizers. In our paper, we will use continuity method to bypass this question and esta... |
| 10 | 0.514 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | unsectioned | lines 114-137 | no | yes | properness, cscK | \title[Existence, Properness and Geodesic stability]{Existence of constant scalar curvature K\"ahler cone metrics, properness and geodesic stability} \author{Kai Zheng} % \address{University of Warwick} \curraddr{Tongji University, Shanghai 200092, P.R. CHINA} \email[Kai Zheng]{kaizheng@amss.ac.cn} %\date{\today} \begin{document} \maketitle \begin{abstract}... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_007 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss Tian properness conjectures modulo automorphisms?

**Expected sources:** `1506.07129`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `Tian`, `properness`, `automorphisms`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.928 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | yes | yes | Tian, properness, automorphisms | ...ovpt}} \def\bla{BLA BLA BLA BLA} \def\sp{$\spadesuit$} % Yanir's comments \def\cs{$\clubsuit$} % Tamas' comments \title{Tian's properness conjectures and Finsler geometry of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{do... |
| 2 | 0.616 | `corpus/arxiv/0912.4095/source/source.tex` | `text` | Introduction | lines 99-111 | no | yes | automorphisms | In particular the theorem applies when $M$ admits a cscK metric and has continuous automorphisms, proving that $M$ is K-polystable with respect to all test- configurations that commute with a maximal torus of automorphisms, but note that this is a priori a weaker condition than K-polystability (see the next section for the detailed definitions). Note that by... |
| 3 | 0.577 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 247-263 | no | yes | Tian, properness | Note that the direction that existence of cscK implies properness has been established by Berman-Darvas-Lu\cite{Darvas1605} recently. For the converse (namely the existence part), Darvas and Rubinstein have reduced this problem in \cite{DR} to a question of regularity of minimizers. In our paper, we will use continuity method to bypass this question and esta... |
| 4 | 0.558 | `corpus/arxiv/2208.12493/source/toric-lecture-notes.tex` | `text` | Existence: an overview > The Chen--Cheng and He results | lines 1535-1543 | no | yes | Tian, properness, automorphisms | ...cement by He~\cite{He} to cover the extremal K\"ahler metric case. The key notion for these results to hold is the {\it properness} of the relative K-energy with respect to a reductive complex Lie group, first introduced by Tian~\cite{Tian} in the Fano case, and adapted by Zhou--Zhu~\cite{ZZ1} to the general K\"ahler case. We start by explaining the general... |
| 5 | 0.490 | `corpus/arxiv/1602.03114/source/source.tex` | `text` | Introduction and main results | lines 111-126 | no | yes | Tian, properness, automorphisms | ...essary conditions under which $\mathcal H$ admits constant scalar curvature K\"ahler (csck) metrics, in terms of energy properness. We now elaborate on the terminology necessary to state our main results. To have a one-to-one correspondence between potentials and metrics, we consider the space $$\Hnormalize := \Homega \cap \AM^{-1}(0),$$ and we always work o... |
| 6 | 0.488 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | yes | properness | ...hcal S}_\infty.$ One important technical ingredient to prove existence of cscK from geodesic stability is the following properness theorem, which says that if $K$-energy is ``proper" with respect to a suitably defined distance (defined precisely in Definition \ref{d1.1} below), then cscK exists. To extend the properness theorem to the case of general automor... |
| 7 | 0.481 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `text` | Introduction | lines 251-260 | no | yes | Tian | We discuss in~\S\ref{sectFORMALsol} consequences of this last result and open problems in relation with the relative toric version of the Yau--Tian--Donaldson conjecture. In the next section we gather facts, definition, key results and recall brief explanations on the topic of toric extremal (almost) K\"ahler metrics. Section~\ref{sectMAIN} contains the proo... |
| 8 | 0.472 | `corpus/arxiv/math_0412518/source/slopeobs_archive.tex` | `text` | Introduction > Acknowledgments | lines 213-225 | no | yes | Tian | ...who suggested looking at stability of projective bundles $\PP(E)$ via the degeneration mentioned in (\ref{ext1}). As we discuss there, the deformation to the normal cone collapses to this degeneration in one special case, and it was this case that motivated our study of the normal cone; without his invaluable suggestion we would never have looked at stabilit... |
| 9 | 0.440 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 138-162 | no | yes | Tian, properness, automorphisms | ...cscK metrics with cone singularities are expected to serve as a continuity method to find the cscK metric aiming to Yau-Tian-Donaldson conjecture, which coincides with Donaldson's continuity method in the K\"ahler-Einstein problem \cite{MR3264768,MR2975584}. In K\"ahler geometry, Yau-Tian-Donaldson (YTD) conjecture states the equivalence between the existenc... |
| 10 | 0.528 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | Results | lines 628-647 | yes | yes | Tian, properness | \section{Results} Much of the progress on Conjecture \ref{TianConj} has focused on the case of \KEno, \KE edge, or \KR soliton metrics. In the setting of \KE metrics, one direction of the conjecture (properness implies existence) follows from work of Ding--Tian \cite{dt}, while the converse for Conjecture \ref{TianConj} (i) was established by Tian \cite{Tian... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_008 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss uniform K-stability and energy asymptotics?

**Expected sources:** `1603.01026`
**Expected chunk types:** `theorem`, `definition`, `text`
**Expected terms:** `uniform K-stability`, `energy asymptotics`, `non-Archimedean`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.705 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction > The minimum norm and the Mabuchi functional. | lines 132-133 | no | yes | uniform K-stability | ...imum norm and the Mabuchi functional.}\label{introminnorm} To motivate Conjecture \ref{introconjecture} further, we now discuss the link between uniform K-stability with respect to the minimum norm and coercivity of the Mabuchi functional, referring to \cite{XC} for an introduction to the Mabuchi functional. Let $(X,L)$ be a smooth polarised variety and fix... |
| 2 | 0.604 | `corpus/my_notes/requested_non_arxiv_sources.md` | `text` | Requested non-arXiv and correction pointers > Journal-only or correction pointers | lines 7-23 | no | yes | uniform K-stability | ...ter only. No arXiv identifier was identified in this update. - Sebastien Boucksom, Tomoyuki Hisamoto, Mattias Jonsson, "Uniform K-stability and asymptotics of energy functionals in Kahler geometry", JEMS 21 (2019), 2905-2944. ArXiv source in corpus: `corpus/arxiv/1603.01026`. EMS page with correction pointer: https://ems.press/journals/jems/articles/16240 Lo... |
| 3 | 0.595 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 419-430 | no | yes | uniform K-stability, non-Archimedean | ...d Archimedean functionals, and explain they are related to each other. We state the basic correspondence between finite energy non-Archimedean metrics and maximal geodesic rays as established by Berman-Boucksom-Jonsson. We discuss the twist of non-Archimedean metrics that was introduced in \cite{His16b} for smooth ones and more generally developed in \cite{L... |
| 4 | 0.543 | `corpus/arxiv/1603.01026/source/source.tex` | `text` | Introduction | lines 387-403 | yes | yes | uniform K-stability, non-Archimedean | ...the minimum norm considered by Dervan~\cite{Der1}. The norm is zero iff the normalization of $(\cX,\cL)$ is trivial, so uniform K-stability implies K-stability. In~\cite{BHJ1} we advocated the point of view that a test configuration defines a \emph{non-Archimedean metric} on $L$, that is, a metric on the Berkovich analytification of $(X,L)$ with respect to t... |
| 5 | 0.663 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction | lines 129-131 | no | yes | uniform K-stability | It follows that uniform K-stability indeed implies K-stability. |
| 6 | 0.521 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | ...uestion to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except in the Fano manifold wh... |
| 7 | 0.648 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction | lines 103-107 | no | yes | uniform K-stability | Our motivation for this conjecture is twofold: firstly, we can prove this uniform K-stability holds in several geometric situations. Secondly, there is a strong link between uniform K-stability in this sense and coercivity of the Mabuchi functional, which we describe in Section \ref{introminnorm}. There are three related themes in the present work, which we... |
| 8 | 0.448 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 843-864 | no | yes | energy asymptotics, non-Archimedean | ...lgebraic way. Some of this was done in~\cite{HLi23}, but here we also need the \na versions of the twisted weighted \ma energy and weighted \ma measure; these turn out to be rather delicate to handle (see also the very recent work~\cite{HLiuklt}). Second, we need to show that the (Archimedean) energy functionals and operators, defined on the space $\cE^{1,T}... |
| 9 | 0.439 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | no | yes | - | ...rk) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail in our next paper and refer interested readers to the following works and references therein: |
| 10 | 0.401 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | unsectioned | lines 161-222 | no | yes | uniform K-stability | ...newtheorem*{dfn1}{\bf{Definition 1}} \newtheorem*{dfn2}{\bf{Definition 2}} \newtheorem*{dfn3}{\bf{Definition 3}} \title[Uniform stability for equivariant polarizations]{Uniform stability and coercivity for equivariant polarizations} \date{\today} \author{Tomoyuki Hisamoto} \address{Graduate School of Mathematics\\ Nagoya University\\ Furocho\\ Chikusa\\ Nago... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_009 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss geodesic rays and non-Archimedean energy functionals?

**Expected sources:** `1603.01026`, `1510.01260`
**Expected chunk types:** `definition`, `proposition`, `text`
**Expected terms:** `geodesic rays`, `non-Archimedean`, `energy functionals`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.959 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 419-430 | no | yes | geodesic rays, non-Archimedean | In the next section, we recall the non-Archimedean and Archimedean functionals, and explain they are related to each other. We state the basic correspondence between finite energy non-Archimedean metrics and maximal geodesic rays as established by Berman-Boucksom-Jonsson. We discuss the twist of non-Archimedean metrics that was introduced in \cite{His16b} fo... |
| 2 | 0.822 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Non-Archimedean limits of metrics and measures > Non-Archimedean limits of metrics | lines 2430-2432 | no | yes | geodesic rays, non-Archimedean | \subsection{Non-Archimedean limits of metrics} Beyond geodesic rays, there are other situations when rays of metrics give rise to non-Archimedean metrics/potentials. Following~\cite[\S 3]{BHJ2}, we introduce: |
| 3 | 0.791 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Non-Archimedean potentials of finite energy and geodesic rays | lines 1528-1532 | no | yes | geodesic rays, non-Archimedean | \section{Non-Archimedean potentials of finite energy and geodesic rays}\label{S202} As above, $(X,\om_0)$ is a compact K\"ahler manifold, and $L$ is an ample $\Q$-line bundle with $\om_0\in c_1(L)$. Using part of the proof of Theorem~\ref{thm:coerstab}, we now undertake a deeper study the relationship between psh rays and non-Archimedean $L$-psh functions, a... |
| 4 | 0.642 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Extension to $\cET(X, \omega)$ > {Weighted twisted energies} > Extension to finite energy space | lines 1245-1248 | no | yes | energy functionals | \subsubsection{Extension to finite energy space} We now extend the weighted energy functionals to $\cET(X, \omega)$. The following proposition, proven in \cite{AJL} and later refined in \cite{BJT}, establishes the extension of weighted energy functionals to the finite energy space. |
| 5 | 0.750 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Weighted pluripotential theory > Non-Archimedean weighted pluripotential theory | lines 3305-3309 | no | yes | geodesic rays | The proof of Theorem~\ref{thm:wMA} carries over to the \na case without change, noting that the \na analogues of~\eqref{equ:enconc} and~\eqref{equ:IvI} follow by passing to slopes at infinity along geodesic rays, using Theorem~\ref{thm:NAMAext}. For later use we also show: |
| 6 | 0.730 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Valuations and stability > Non-Archimedean functionals and stability | lines 1185-1188 | no | yes | non-Archimedean | \subsection{Non-Archimedean functionals and stability}\label{S204} In~\cite{BHJ1}, non-Archimedean versions of a number of usual functionals on $\cH$ were introduced. They are defined as functionals on $\cHNA$, the idea being that the non-Archimedean version of a functional $F$ should compute the slopes at infinity of $F$ along psh rays in $\cHNA$ with algeb... |
| 7 | 0.582 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | no | yes | - | An intriguing question motivated from above remark is whether geodesic stability in $\mathcal{E}_0^{\infty}$ (in the sense defined in the above remark) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail i... |
| 8 | 0.721 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 301-303 | no | yes | geodesic rays, non-Archimedean | ...ficulty in proving \eqref{eq-conjH} is that there is not yet an explicit formula for $\bfH'^\infty$ for general maximal geodesic rays. On the other hand, for any finite energy $\phi\in \mcE^{1,\NA}(L)$, Boucksom-Jonsson in \cite{BoJ18b} defined the following non-Archimedean entropy in their study of K-stability (see \eqref{eq-AXsup}-\eqref{eq-HNAphi1}): |
| 9 | 0.717 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Preliminaries > Non-Archimedean theory > Finite energy metrics and measures | lines 714-718 | no | yes | non-Archimedean, energy functionals | All the Archimedean energy functionals in \eqref{eq-EE1}-\eqref{eq-defI} can be defined by replacing the Archimedean integrals in section \ref{sec-Archrays} by the corresponding non-Archimedean integrals. For example we have |
| 10 | 0.713 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Preliminaries > Non-Archimedean theory > Finite energy metrics and measures | line 774 | no | yes | non-Archimedean, energy functionals | The following lemma, which says that non-Archimedean energy functionals reduce to the corresponding intersection products, can be verified directly using Theorem \ref{thm-BoJ}. |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_010 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss the d1 metric on finite energy potentials?

**Expected sources:** `1510.01260`, `1506.07129`, `1602.03114`
**Expected chunk types:** `definition`, `lemma`, `text`
**Expected terms:** `d1 metric`, `finite energy`, `potentials`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.866 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Regularity and uniqueness of log $\chi$-twisted $K$-energy minimisers > The complete space $\mathcal E^1$ | lines 4051-4054 | no | yes | potentials | \subsection{The complete space $\mathcal E^1$} Recall that $\mathcal H$ is the space of smooth K\"ahler potentials in $\Om=[\om_0]$. Let $\vphi$ be a K\"ahler potential in $\mathcal H$, the tangent space of $\mathcal H$ at $\vphi$ is the set of smooth functions $C^{\infty}(X)$. The $d_1$ metric is defined to be |
| 2 | 0.848 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | preliminaries > The complete geodesic metric space $(\mathcal{E}^p,d_p)$ | lines 513-515 | no | yes | finite energy, potentials | For later use, here we describe how to obtain ``finite energy geodesics" from the $C^{1,1}$ geodesics between smooth potentials. |
| 3 | 0.789 | `corpus/arxiv/2506.02360/source/2025_06_03_extremal.tex` | `text` | Preliminaries > Calabi's extremal metrics | lines 204-206 | no | yes | finite energy, potentials | We write $\CE^1$ for the finite energy space, which is the completion of $\CH$ with respect to the distance $d_1$; see Darvas' monograph \cite{darmonograph} for more details. We write $(\mathcal{H})^{\mathbb{K}}$ for the $\mathbb{K}$-invariant K\"ahler potentials, and similarly for $(\mathcal{E}^1)^{\mathbb{K}}$. Given a vector field $v$ induced by the $\mat... |
| 4 | 0.788 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `conjecture` | Introduction > Openness of coercivity | lines 715-729 | no | no | finite energy, potentials | \begin{conj}[{Existence of $(1,1,2\pi[D])$-extremal Poincar\'e-type K\"ahler metrics}]\label{conj:twisted_extremal} Let $(X, \omega)$ be a compact K\"ahler manifold and let $D$ be a smooth divisor. Let $T$ be a maximal compact torus in the reduced automorphism group $\Aut_{red}(X, D)$. The manifold $X$ admits a $T$-invariant $(1,1,2\pi[D])$-extremal metric i... |
| 5 | 0.752 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | yes | finite energy, potentials | ...cite{Ross11}, the authors defined a notion of analytic test configurations which is an one-parameter family of K\"ahler potentials, concave with respect to this parameter. They proved that each analytic test configuration defines a unique geodesic ray (up to parallelism), thus defines a point at ${\mathcal S}_\infty.$ It is important to understand the conver... |
| 6 | 0.679 | `corpus/arxiv/1602.03114/source/source.tex` | `text` | Preliminaries > The energy functionals > The (twisted) K-energy | lines 368-379 | yes | yes | finite energy, potentials | where $\bar{S}_\chi = nV^{-1}\int_X (\Ric(\omega) - \chi) \wedge \omega^{n-1}$. Hence, the critical points of $\Kenergy_{\chi}$ are the twisted csck potentials, as these satisfy $\bar S_{\chi}-S_{\omega_u} + \Tr^{\omega_u}(\chi)=0$. In \cite[Proposition 5.26]{DR17} it is shown that this functional naturally extends to the $L^1$-Mabuchi completion of $\Homega... |
| 7 | 0.676 | `corpus/arxiv/1510.01260/source/source.tex` | `text` | Introduction | lines 129-144 | yes | yes | finite energy, potentials | ...cture. To avoid the difficulties arising in PDE theory related to long time existence, we recast the Calabi flow in the metric completion of ${(\mathcal H_\o,d_2)}$ following Streets \cite{st1,st2}, who applied the work of Mayer \cite{may} and Ba\u c\'ak \cite{ba} concerning gradient flows of convex functionals on Hadamard spaces (i.e. CAT(0)-spaces) to the... |
| 8 | 0.842 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | preliminaries > The complete geodesic metric space $(\mathcal{E}^p,d_p)$ | lines 500-502 | no | yes | finite energy, potentials | A fundamental conjecture of V. Guedj \cite{Guedj14} stated that the completion of the space ${\mathcal H}$ of smooth potentials equipped with the $L^2$ metric is precisely the space $ {\mathcal E}^2 (M, \omega_0)$ of potentials of finite energy. This has been shown by Darvas \cite{Darvas1402}, \cite{Darvas1403}, in which he has shown similar characterization... |
| 9 | 0.669 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Introduction > Coercivity and Ding-stability | lines 516-542 | no | yes | finite energy, potentials | ...d Ding-stability} We now describe our strategy of proof of Theorem A. Choose a K\"ahler form $\om_0\in c_1(L)$, so that finite energy currents in $c_1(L)$ get parametrized by the space $\cE^1=\cE^1(X,\om_0)$ of finite energy potentials~\cite{GZ,BBGZ}, a complete geodesic space with respect to a metric $d_1$ introduced by Darvas~\cite{Dar15}. By~\cite{BBEGZ},... |
| 10 | 0.781 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | preliminaries > The complete geodesic metric space $(\mathcal{E}^p,d_p)$ | lines 487-488 | no | yes | - | \subsection{The complete geodesic metric space $(\mathcal{E}^p,d_p)$} Following Mabuchi, T. Darvas \cite{Darvas1402} introduced the notion of $d_1$ on $\mathcal{H}$. |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_011 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss lower semicontinuity of the extended Mabuchi functional?

**Expected sources:** `1510.01260`
**Expected chunk types:** `theorem`, `proposition`, `proof`
**Expected terms:** `lower semicontinuity`, `extended Mabuchi`, `finite energy`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.746 | `corpus/arxiv/1004.2012/source/Kempf_Ness_uniqueness_12272011.tex` | `theorem` | Stability of the Calabi flow | lines 1418-1422 | no | yes | - | \begin{thm}(\cite{Ch4}) For any $J\in\U$, the Mabuchi functional $E$ on the space of K\"ahler metrics compatible with $J$ is bounded below, and the lower bound is achieved by the infimum along the Calabi flow initiating from $J$. \end{thm} |
| 2 | 0.722 | `corpus/arxiv/1409.7896/source/source.tex` | `text` | Fiber-wise approximation of $\cG$ > Continuity at the boundary | lines 806-808 | no | no | - | where $E$ is the energy part of the Mabuchi functional, and $H$ is the entropy part. As a consequence of our previous results, we establish here the following statement. |
| 3 | 0.623 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | no | - | ...elow? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except in the Fano manifold where the authors proved it indirectly in route of CDS's theorem.\\ We have the following theorem which is useful to our characterization of borde... |
| 4 | 0.550 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | \label{sec:Introduction}Introduction > Statement of the main results > Further extensions and applications | lines 414-429 | no | no | extended Mabuchi, finite energy | The relation to previous results is discussed in \cite{bch}. Some further interactions between the Mabuchi functional and the notions of finite energy and entropy are also studied in \cite{bch}. For example, it is shown that the extended Mabuchi functional remains convex along finite energy geodesics. Moreover, using finite energy geodesics one can define a... |
| 5 | 0.534 | `corpus/arxiv/1801.00656/source/source.tex` | `theorem` | preliminaries > Convexity of $K$-energy | lines 577-581 | no | yes | finite energy | \begin{thm}\label{t2.4new}(\cite{Darvas1602}, Theorem 4.7) The $K$-energy defined in (\ref{K}) can be extended to a functional $K:\mathcal{E}^1\rightarrow\mathbb{R}\cup\{+\infty\}$. Besides, the extended functional $K\|_{\mathcal{E}^1}$ is the greatest $d_1$-lower semi-continuous extension of $K\|_{\mathcal{H}}$. Moreover, $K\|_{\mathcal{E}^1}$ is convex along... |
| 6 | 0.527 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction > The minimum norm and the Mabuchi functional. | lines 132-133 | no | no | - | \subsection{The minimum norm and the Mabuchi functional.}\label{introminnorm} To motivate Conjecture \ref{introconjecture} further, we now discuss the link between uniform K-stability with respect to the minimum norm and coercivity of the Mabuchi functional, referring to \cite{XC} for an introduction to the Mabuchi functional. Let $(X,L)$ be a smooth polaris... |
| 7 | 0.516 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Extension to $\cET(X, \omega)$ > {Weighted twisted energies} > Extension to finite energy space | lines 1293-1295 | no | no | lower semicontinuity | The following proposition establishes the lower semicontinuity and existence of smooth approximations for the entropy functionals on the space $\cET(X, \omega)$. We closely follow the approach developed in \cite{AJL} and \cite{BDL}. |
| 8 | 0.508 | `corpus/arxiv/1509.04561/source/source.tex` | `example` | Twisted K\"ahler--Einstein currents and coercivity > The twisted K-energy | lines 972-981 | no | no | - | \begin{exam}\label{exam:Mab} The usual Mabuchi K-energy functional, extended to a functional $$ \opM\colon\cE^1\to\R\cup\{+\infty\} $$ as in~\cite{BDL}, has entropy growth. Indeed, denoting by $\Ent(\mu)$ the entropy of a measure $\mu$ relative to $V^{-1}\om_0^n$, the Chen--Tian formula~\cite{Che00b,TianBook} expresses $\opM(u)-\Ent(\MA(u))$ as linear combin... |
| 9 | 0.499 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | no | - | ...s of Tian predict that existence of canonical K\"ahler metrics should be equivalent to various notions of properness of Mabuchi's K-energy functional. In some instances this has been verified, especially under restrictive assumptions on the automorphism group. We provide counterexamples to the original conjecture in the presence of continuous automorphisms.... |
| 10 | 0.484 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Preliminaries > More functionals | lines 1285-1287 | no | no | - | %By proving Theorem \ref{thm-Echislope}, we will show that this is well-defined and does not depend on the choice of the decreasing sequence $\Phi_m$. The constant scalar curvature K\"{a}hler metrics are global minimizers of Mabuchi functional $\bfM(\vphi)$. We now have the following important analytic criterion for the existence of cscK metrics: |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_012 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss entropy terms in the extension of K-energy?

**Expected sources:** `1510.01260`, `1810.04661`
**Expected chunk types:** `definition`, `proposition`, `text`
**Expected terms:** `entropy`, `K-energy`, `finite energy`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.763 | `corpus/arxiv/1509.04561/source/source.tex` | `example` | Twisted K\"ahler--Einstein currents and coercivity > The twisted K-energy | lines 972-981 | no | no | entropy, K-energy | \begin{exam}\label{exam:Mab} The usual Mabuchi K-energy functional, extended to a functional $$ \opM\colon\cE^1\to\R\cup\{+\infty\} $$ as in~\cite{BDL}, has entropy growth. Indeed, denoting by $\Ent(\mu)$ the entropy of a measure $\mu$ relative to $V^{-1}\om_0^n$, the Chen--Tian formula~\cite{Che00b,TianBook} expresses $\opM(u)-\Ent(\MA(u))$ as linear combin... |
| 2 | 0.738 | `corpus/arxiv/1510.01260/source/source.tex` | `text` | Introduction | lines 145-152 | yes | yes | entropy, K-energy, finite energy | Our starting point is the observation that the K-energy functional $\mathcal K$ originally defined on $\mathcal H_\o$ admits a natural ``analytic extension" to the finite energy space $\mathcal E^1$ (and hence by restriction to all spaces $\mathcal E^p$). This is simply the extension obtained by interpreting the entropy part (the first term) and the energy p... |
| 3 | 0.670 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Stability notions and proof of the main results > Weighted cscK metrics and the weighted Mabuchi functional | lines 3699-3718 | no | yes | entropy | where \begin{itemize} \item the weighed entropy $\ent_v(\phi)=\Ent(\MA_v(\phi)\|\mu_\refe)$ is the relative entropy of $\MA_v(\phi)$ with respect to a $T$-invariant reference volume form $\mu_\refe$; \item the \emph{weighted Ricci energy} $\rr_v(\phi)=\en_v^{\p_\refe}(\phi)$ is a twisted weighted energy with $\p_\refe:=\tfrac12\log\mu_\refe\in C^\infty(K_X)^T... |
| 4 | 0.668 | `corpus/arxiv/1602.03114/source/source.tex` | `text` | Preliminaries > The energy functionals > The (twisted) K-energy | lines 353-355 | no | yes | entropy, K-energy | where $\textup{Ent}(\omega^n,\omega^n_u)$ is the entropy of the measure $\omega_u^n$ with respect to $\omega^n$: $$\textup{Ent}(\omega^n,\omega^n_u)=V^{-1}\int_X \log(\omega_u^n/\omega^n)\omega_u^n,$$ and $\overline{S}=\frac{1}{V}\int_X S_\omega \omega^n$ is the average scalar curvature, that can be seen to be independent of the choice of background metric.... |
| 5 | 0.725 | `corpus/arxiv/1509.04561/source/source.tex` | `example` | Twisted K\"ahler--Einstein currents and coercivity > The coercivity criterion | lines 1059-1060 | no | no | entropy, K-energy | \begin{exam} The dichotomy (a)--(b) applies in particular to the Mabuchi K-energy functional of any compact K\"ahler manifold, which is geodesically convex by~\cite{BB17,CLP,BDL}, and has entropy growth by Example~\ref{exam:Mab}. \end{exam} |
| 6 | 0.537 | `corpus/arxiv/2104.09709/source/source.tex` | `text` | Introduction > Method of proof | lines 300-302 | no | yes | finite energy | \subsection{Method of proof} We now discuss briefly the method of proof of Theorem~\ref{main} above. It is an application of the general coercivity principle~\cite[Thm.~3.4]{DaRu}, see Section~\ref{s:coercivity} below. The latter is used in the cscK case in \cite{BDL}, and our approach is mainly inspired by these two references. Noting that in the weighted e... |
| 7 | 0.534 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | preliminaries | lines 394-400 | no | yes | entropy, finite energy | ...acterization of the space $(\mathcal{E}^1,d_1)$, a compactness result on bounded subsets of $\mathcal{E}^1$ with finite entropy. We also include results on the convexity of $K$-energy along $C^{1,1}$ geodesics as well as its extension to the space $\mathcal{E}^1$. For more detailed account on these topics, we refer to a recent survey paper by Demailly \cite{... |
| 8 | 0.527 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | K-energy | ...predict that existence of canonical K\"ahler metrics should be equivalent to various notions of properness of Mabuchi's K-energy functional. In some instances this has been verified, especially under restrictive assumptions on the automorphism group. We provide counterexamples to the original conjecture in the presence of continuous automorphisms. The constr... |
| 9 | 0.525 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | ...r dimension. Nevertheless, it would be interesting to study what goes through the new difficulties. We expect the right extension of the notion of foldable fans in higher dimension to be fans whose lattice automorphism group admit a subgroup that acts with no fixed point. This raises several questions : \begin{enumerate} \item Do all crystallographic groups... |
| 10 | 0.500 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | It is an interesting question to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except i... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_013 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss weak geodesic segments in the space of Kahler potentials?

**Expected sources:** `1405.0401`, `1409.7896`, `1510.01260`
**Expected chunk types:** `definition`, `lemma`, `text`
**Expected terms:** `weak geodesic segments`, `Kahler potentials`, `convexity`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.792 | `corpus/arxiv/1405.0401/source/source.tex` | `theorem` | \label{sec:Introduction}Introduction > Statement of the main results | lines 255-260 | yes | no | - | \begin{thm} \label{thm:main intro}For any K\"ahler class $[\omega]$ the Mabuchi functional $\mathcal{M}$ is convex along the weak geodesic $u_{t}$ connecting any two points $u_{0}$ and $u_{1}$ in the space $\mathcal{H}$ of $\omega-$K\"ahler potentials. \end{thm} |
| 2 | 0.749 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | Convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesics | lines 616-618 | no | yes | weak geodesic segments, convexity | Now, we can use the arguments of Berman--Berndtsson in \cite{BB} to deduce the weak convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesic segments. We will need the following regularization result which is the main ingredient in the proof of Berman--Berndtsson for the weak convexity of the Mabuchi energy \cite[Theorem 3.3]{BB}. |
| 3 | 0.736 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 185-190 | no | yes | - | ...where the functional $I$ is defined by (\ref{IJ}). The reason we need to use $\mathcal{H}_0$ is to preclude the trivial geodesic $\rho(t)=\varphi_0+ct$ where $c$ is a constant. In the original writing of S. K. Donaldson, he didn't specify the regularity of these geodesic rays in this conjecture. In this paper, we avoid this issue by working in the space $\ma... |
| 4 | 0.622 | `corpus/arxiv/1510.01260/source/source.tex` | `text` | Preliminaries > Weak convergence in a CAT(0) space | lines 496-509 | yes | yes | - | where $\lambda = d(q,s)/ d(q,r)$. A basic property of CAT(0) spaces is that geodesic segments joining different points are unique. For more about these spaces we refer to \cite{bh}. Let $\{x_n\}_n$ be a bounded sequence in a CAT(0) metric space $(M,d)$. For $x \in M$, we set $$r(x,\{x_n\}_n) = \limsup d(x, x_n).$$ The \emph{asymptotic radius} $\{x_n\}_n$ is... |
| 5 | 0.594 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `lemma` | Appendix > The Log-Mabuchi energy of Poincar\'e type K\"ahler metrics > Potential space of Poincar\'e type K\"ahler metrics | lines 2091-2093 | no | yes | - | \begin{lemma}\label{lem:poincare-E1} The space $\tmom$ of Poincar\'e type potentials is contained in the finite energy space $\mathcal{E}^1(X, \omega)$. \end{lemma} |
| 6 | 0.503 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | yes | - | ...cite{Ross11}, the authors defined a notion of analytic test configurations which is an one-parameter family of K\"ahler potentials, concave with respect to this parameter. They proved that each analytic test configuration defines a unique geodesic ray (up to parallelism), thus defines a point at ${\mathcal S}_\infty.$ It is important to understand the conver... |
| 7 | 0.488 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted cscK problem on semisimple principal fibration | lines 2104-2110 | no | yes | - | Also, from \cite[Section 5]{AJL}, any Kähler metric \(\omega\) on \(X\) induces a Kähler metric \(\tilde{\omega}\) on \(Y\) such that the restriction \((Y_b, \tilde{\omega}_b)\) of \((Y, \tilde{\omega})\) to a fiber over a point \(b \in B\) is \(\T\)-equivariantly Kähler isomorphic to \((X, \omega)\). Such a metric \(\tilde{\omega}\) on \(Y\) is the \emph{co... |
| 8 | 0.599 | `corpus/arxiv/2007.01345/source/source.tex` | `theorem` | Convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesics | lines 526-528 | no | no | weak geodesic segments | \begin{cor}\label{Cor-E-theta-strict} Let $\theta$ be a $\T$-invariant K\"ahler form. The functional $\mathcal{E}_{\uu}^{\theta}$ is strictly convex on weak geodesic segments. In particular $\mathcal{E}_{\uu}^{\theta}$ has at most one critical point in $\mathcal{K}^{1,1}(X,\omega)^{\T}$. \end{cor} |
| 9 | 0.456 | `corpus/arxiv/1810.04661/source/source.tex` | `text` | Introduction | lines 126-128 | no | yes | - | ...etrics is problematic for $p \neq 2$. It was pointed out in the comments following \cite[Theorem 4.17]{Da15} that $d_1$-geodesic segments connecting the different points of $(\mathcal E^1_{\omega},d_1)$ are not unique. However, as a consequence of the above result it follows that uniqueness of $d_p$-geodesic segments does hold in case $p>1$: |
| 10 | 0.419 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Existence implies properness and geodesic stability | lines 4230-4242 | no | yes | - | \section{Existence implies properness and geodesic stability}\label{Existence implies properness and geodesic stability} The properness conjecture predicts the properness of Mabuchi's $K$-energy is equivalent to the existence of cscK metrics. We then formulate the properness of an energy functional $F$ in the space of smooth K\"ahler potentials $\mathcal H$... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_014 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss the relation between minimizers of K-energy and cscK metrics?

**Expected sources:** `1602.03114`, `1801.00656`, `1510.01260`
**Expected chunk types:** `theorem`, `proof`, `text`
**Expected terms:** `minimizers`, `K-energy`, `cscK metrics`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.923 | `corpus/arxiv/1602.03114/source/source.tex` | `conjecture` | Introduction and main results | lines 147-148 | yes | no | minimizers, K-energy, cscK metrics | \begin{conjecture}[Conjecture 2.9 in \cite{DR17}] \label{conj: DRconj} Suppose $(X,\omega)$ is a compact K\"ahler manifold. The minimizers of the extended K-energy $\Kenergy: \mathcal E^1 \to (-\infty,+\infty]$ are smooth csck metrics. \end{conjecture} |
| 2 | 0.884 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Preliminaries > More functionals | lines 1285-1287 | no | yes | minimizers, cscK metrics | %By proving Theorem \ref{thm-Echislope}, we will show that this is well-defined and does not depend on the choice of the decreasing sequence $\Phi_m$. The constant scalar curvature K\"{a}hler metrics are global minimizers of Mabuchi functional $\bfM(\vphi)$. We now have the following important analytic criterion for the existence of cscK metrics: |
| 3 | 0.882 | `corpus/arxiv/1712.06697/source/source.tex` | `remark` | Introduction | lines 266-269 | no | no | minimizers, cscK metrics | \begin{rem} In Theorem \ref{t1.1} and the first part of Theorem \ref{t1.2}, it is sufficient to assume that $\varphi$ remains bounded under $L^1$ geodesic distance, due to the fact that cscK metrics are minimizers of $K$-energy. We will discuss this matter in more detail in our next paper of the series. \end{rem} |
| 4 | 0.595 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | minimizers, K-energy | ...ef\cs{$\clubsuit$} % Tamas' comments \title{Tian's properness conjectures and Finsler geometry of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{document} \maketitle \begin{abstract} Well-known conjectures of Tian predict t... |
| 5 | 0.550 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 635-663 | no | yes | minimizers, cscK metrics | \section*{Introduction} The constant scalar curvature K\"ahler (cscK) metric problem has become one of the central focus in K\"ahler geometry during the last decades. The Yau--Tian--Donaldson conjecture asserts that given a compact K\"ahler manifold with a fixed K\"ahler class, the existence of cscK metrics in the K\"ahler class is equivalent to an algebro-g... |
| 6 | 0.549 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 671-675 | no | yes | cscK metrics | ...onaldson (YTD) conjecture~\cite{Yau93,Tia97,Don02} predicts that the existence of a constant scalar curvature K\"ahler (cscK) metric (and, more generally, of a `canonical' metric) $\om\in c_1(L)$ is equivalent to a stability condition on $(X,L)$ of purely algebro-geometric nature. In the special case where $X$ is Fano and $L=-K_X$ (for which cscK metrics are... |
| 7 | 0.534 | `corpus/arxiv/1510.01260/source/source.tex` | `text` | Extension of the twisted K-energy > Uniqueness of twisted K-energy minimizers | lines 1009-1010 | yes | yes | minimizers, K-energy | %As a strategy to find minimizers of the K-energy, one may consider finding minimizers of the twisted K-energy first and then consider the limit as the twisting form goes to zero. This was put forward in recent works \cite{c4,cpz}, in case of smooth minimizers, and below we provide a partial weak analog of one of their results: |
| 8 | 0.503 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 273-284 | yes | yes | - | ...to understand geometrically for what K\"ahler classes this invariant is $1$ but do not admit constant scalar curvature metrics. More broadly, it is interesting to estimate the upper and lower bound of this invariant. It is not hard to see the relation between the invariant introduced in \cite{Sz11} and the invariant introduced above when restricted to the c... |
| 9 | 0.502 | `corpus/arxiv/math_0511118/source/source.tex` | `text` | K-stability and admissible extremal K\"ahler metrics > Introduction to stability | lines 1969-1994 | no | yes | - | \subsection{Introduction to stability}\label{intro} For a Hodge manifold $(M,\Omega$), the existence of a CSC K\"ahler metric in $\Omega$ is conjectured to be equivalent to a notion of {\it stability}~\cite{CT,Do1,Do2,luo,PT,tian,zhang} for the polarized projective variety $(M,L)$, where $L$ is a line bundle on $M$ with $c_1(L)= \Omega/2\pi$. This conjecture... |
| 10 | 0.497 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Introduction | lines 295-300 | no | yes | - | The paper is organised as follows. In Section \ref{sec:background}, we settle the necessary background material on cscK manifolds. Then, Section \ref{sec:foldable toric surfaces} is devoted to the classification of foldable surfaces and the proofs of Proposition \ref{prop:intro fans} and Proposition \ref{prop:intro}. In Section \ref{sec:local moduli construc... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_015 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss coercivity of K-energy in finite energy geometry?

**Expected sources:** `1602.03114`, `1506.07129`, `1510.01260`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `coercivity`, `K-energy`, `finite energy`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.541 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | unsectioned | lines 161-222 | no | yes | coercivity, K-energy | ...2}} \newtheorem*{dfn3}{\bf{Definition 3}} \title[Uniform stability for equivariant polarizations]{Uniform stability and coercivity for equivariant polarizations} \date{\today} \author{Tomoyuki Hisamoto} \address{Graduate School of Mathematics\\ Nagoya University\\ Furocho\\ Chikusa\\ Nagoya\\ Japan} \email{hisamoto@math.nagoya-u.ac.jp} \subjclass[2010]{Prima... |
| 2 | 0.499 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | yes | finite energy | ...lelism), thus defines a point at ${\mathcal S}_\infty.$ It is important to understand the converse: when does a locally finite energy geodesic ray define a test configuration? More importantly, can one extend the definition of $\yen$ invariant for analytic test configuration? Note that by Theorem 1.4, we can view $\yen$ invariant as a function defined on the... |
| 3 | 0.493 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Introduction > Coercivity and Ding-stability | lines 516-542 | no | yes | coercivity, K-energy, finite energy | \subsection*{Coercivity and Ding-stability} We now describe our strategy of proof of Theorem A. Choose a K\"ahler form $\om_0\in c_1(L)$, so that finite energy currents in $c_1(L)$ get parametrized by the space $\cE^1=\cE^1(X,\om_0)$ of finite energy potentials~\cite{GZ,BBGZ}, a complete geodesic space with respect to a metric $d_1$ introduced by Darvas~\cit... |
| 4 | 0.492 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | preliminaries | lines 394-400 | no | yes | finite energy | \section{preliminaries} In this section, we will review some basic concepts in K\"ahler geometry as well as some fundamental results involving finite energy currents, which will be needed for our proof of Theorem 1.1 and 1.3. In particular, it includes the characterization of the space $(\mathcal{E}^1,d_1)$, a compactness result on bounded subsets of $\mathc... |
| 5 | 0.482 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | yes | yes | K-energy | ...\spadesuit$} % Yanir's comments \def\cs{$\clubsuit$} % Tamas' comments \title{Tian's properness conjectures and Finsler geometry of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{document} \maketitle \begin{abstract} Well-k... |
| 6 | 0.472 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 595-604 | no | yes | coercivity, K-energy, finite energy | \section{Introduction} Finding canonical Kähler metrics is a central theme in complex geometry. In higher dimensions, constant scalar curvature Kähler (cscK) metrics provide an analogue of Poincar\'e’s uniformization theorem; see the surveys \cite{Boucksom_2018, Donaldson_2018_2} for background and further references. Kähler--Einstein metrics form an especia... |
| 7 | 0.472 | `corpus/arxiv/1510.01260/source/source.tex` | `text` | Introduction | lines 145-152 | yes | yes | K-energy, finite energy | Our starting point is the observation that the K-energy functional $\mathcal K$ originally defined on $\mathcal H_\o$ admits a natural ``analytic extension" to the finite energy space $\mathcal E^1$ (and hence by restriction to all spaces $\mathcal E^p$). This is simply the extension obtained by interpreting the entropy part (the first term) and the energy p... |
| 8 | 0.441 | `corpus/arxiv/1602.03114/source/source.tex` | `text` | Introduction and main results | lines 130-135 | yes | yes | coercivity, K-energy | We refer to Section 2 for the precise definitions of $J_\omega$ and $\Kenergy$. Tian conjectured that existence of constant scalar curvature K\"ahler (csck) metrics in $\Homega$ should be equivalent to J-properness of the K-energy $\Kenergy$ \cite[Remark 5.2]{t1},\cite{tianbook} and this was proved for Fano manifolds with $G$ trivial \cite{t2,tz}. In \cite[T... |
| 9 | 0.437 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | unsectioned | lines 126-159 | no | yes | K-energy | ...n} \providecommand{\remarkname}{Remark} \providecommand{\theoremname}{Theorem} \begin{document} \title{Convexity of the K-energy on the space of K\"ahler metrics and uniqueness of extremal metrics} \author{Robert J. Berman, Bo Berndtsson} \curraddr{Department of Mathemical Sciences, Chalmers University of Technology and University of Gothenburg. SE-412 96 Go... |
| 10 | 0.393 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Proofs of Lemmas \ref{s1is2}, \ref{s1is1} and \ref{s1is2overk} | lines 1659-1726 | no | yes | - | .... London Math. Soc. {\bf 14} (1982), 1--15. \bibitem{ACG1} V. Apostolov, D.~M.~J. Calderbank and P. Gauduchon, {\it The geometry of weakly self-dual K\"ahler surfaces}, Compositio Math. {\bf 135} (2003), 279--322. \bibitem{ACG2} V. Apostolov, D.~M.~J. Calderbank and P. Gauduchon, {\it Hamiltonian $2$-forms in K\"ahler geometry} I {\it General Theory}, J. Dif... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_016 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss convexity of Ding or Mabuchi functionals in singular settings?

**Expected sources:** `1405.0401`, `1510.01260`, `1810.04661`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `Ding functional`, `Mabuchi`, `singular`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.727 | `corpus/arxiv/1603.01026/source/source.tex` | `text` | The logarithmic setting > Non-Archimedean functionals | lines 1982-1987 | no | yes | Ding functional, Mabuchi | the infimum taken over all valuations $v$ on $X$ that are divisorial or trivial. The Ding functional $D_B^\NA$ is translation invariant and pullback invariant. The formula for the Mabuchi functional simplifies in the log Fano case to |
| 2 | 0.651 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Introduction | lines 106-118 | no | yes | Mabuchi, singular | \section{Introduction} Bando-Mabuchi \cite{BM} proved that K\"ahler-Einstein metric on Fano manifolds is unique up to holomorphic automorphisms in 1980s. Recently, Berndtsson \cite{Bo} generalized this uniqueness result to conic K\"ahler-Einstein metrics on Fano manifolds, by his observation on the convexity of certain energy functional (the $Ding$-functiona... |
| 3 | 0.520 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | ...M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except in the Fano manifold where the authors proved it indirectly in route of CDS's th... |
| 4 | 0.508 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 706-710 | no | yes | Mabuchi, singular | ...\equiv 1$ on $\frak{t}^\vee$ (hence $\log$-concave). In the smooth setup, existence results under the coercivity of the Mabuchi functional are obtained by \cite{Chen_Cheng_2021_2} and \cite{He_2019} for cscK and extremal metrics, respectively. Our Theorem~\ref{bigthm_existence_0}, in particular, extends their results to singular settings. We state a direct c... |
| 5 | 0.508 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 595-604 | no | yes | Mabuchi, singular | \section{Introduction} Finding canonical Kähler metrics is a central theme in complex geometry. In higher dimensions, constant scalar curvature Kähler (cscK) metrics provide an analogue of Poincar\'e’s uniformization theorem; see the surveys \cite{Boucksom_2018, Donaldson_2018_2} for background and further references. Kähler--Einstein metrics form an especia... |
| 6 | 0.494 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | Mabuchi, singular | ...s of Tian predict that existence of canonical K\"ahler metrics should be equivalent to various notions of properness of Mabuchi's K-energy functional. In some instances this has been verified, especially under restrictive assumptions on the automorphism group. We provide counterexamples to the original conjecture in the presence of continuous automorphisms.... |
| 7 | 0.477 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | \label{sec:Introduction}Introduction > Statement of the main results | lines 310-335 | yes | yes | Mabuchi | ...arity theory and approximation arguments and the inequality \ref{eq:chens ineq in intro} was then obtained by Chen, building on \cite{c-t}. In the case of smooth geodesics it is well-known that the Mabuchi functional $\mathcal{M}$ is \emph{strictly }convex modulo automorphisms, or more precisely modulo the group $\mbox{Aut}_{0}(X)$ defined as the connected c... |
| 8 | 0.462 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `text` | Futaki invariant computed with respect to the conically singular metrics > Scalar curvature as a current | lines 1544-1549 | no | yes | singular | ...lar curvature as a current} \label{scscaldist} In order to compute the log Futaki invariant with respect to a conically singular metric $\omega_{sing}$, we need to make sense of $\mathrm{Ric}(\omega_{sing}) \wedge \omega_{sing}^{n-1}$ globally on $X$. However, this is not well-defined for a general conically singular metric $\omega_{sing}$, as we discuss in... |
| 9 | 0.456 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Introduction > Coercivity and Ding-stability | lines 516-542 | no | yes | Ding functional, singular | \subsection*{Coercivity and Ding-stability} We now describe our strategy of proof of Theorem A. Choose a K\"ahler form $\om_0\in c_1(L)$, so that finite energy currents in $c_1(L)$ get parametrized by the space $\cE^1=\cE^1(X,\om_0)$ of finite energy potentials~\cite{GZ,BBGZ}, a complete geodesic space with respect to a metric $d_1$ introduced by Darvas~\cit... |
| 10 | 0.437 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | no | no | singular | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_017 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss finite energy geodesics and pluripotential theory?

**Expected sources:** `1510.01260`, `1405.0401`, `1810.04661`
**Expected chunk types:** `definition`, `theorem`, `text`
**Expected terms:** `finite energy geodesics`, `pluripotential`, `Kahler`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.830 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | \label{sec:Introduction}Introduction > \label{sub:Bergman-kernel-asymptotics}Bergman kernel asymptotics | lines 909-915 | yes | yes | pluripotential | ...the formula in the previous proposition. Theorem \ref{thm:main intro} claims that this functional is convex along weak geodesics. It is not a priori clear that the functional is continuous along weak geodesics. (We thank S\'ebastien Boucksom and Mihai P\u aun for pointing this out to us.) It does follow from pluripotential theory that the energy parts of th... |
| 2 | 0.781 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | preliminaries > The complete geodesic metric space $(\mathcal{E}^p,d_p)$ | lines 513-515 | no | yes | finite energy geodesics | For later use, here we describe how to obtain ``finite energy geodesics" from the $C^{1,1}$ geodesics between smooth potentials. |
| 3 | 0.761 | `corpus/arxiv/1510.01260/source/source.tex` | `text` | Introduction | lines 162-164 | yes | yes | finite energy geodesics | Finally, as a consequence of Theorem \ref{ExtKEnergyThmIntr} we obtain that the space of finite $\chi$-entropy potentials $\textup{Ent}_\chi(X,\o)$ is geodesically closed, and in case $\Ric \o \geq \beta$ the twisted entropy is convex along finite energy geodesics, giving the K\"ahler analog of a central result of Lott-Sturm-Villani in optimal transport theo... |
| 4 | 0.751 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Finite energy potentials and psh geodesics | lines 612-616 | no | yes | - | \section{Finite energy potentials and psh geodesics}\label{sec:E1} In what follows, $(X,\om_0)$ denotes an $n$-dimensional compact K\"ahler manifold. In this preliminary section, we discuss plurisubharmonic (psh) paths and geodesics in the space of $\om_0$-psh functions on $X$. Most results are known, except perhaps for the characterization of geodesics give... |
| 5 | 0.709 | `corpus/arxiv/1602.03114/source/source.tex` | `text` | The finite energy continuity method | lines 561-563 | no | yes | finite energy geodesics | As promised in the above argument, we provide the following lemma, which generalizes \cite[Lemma 3.5]{bb} to finite energy geodesics with one smooth endpoint: |
| 6 | 0.681 | `corpus/arxiv/1810.04661/source/source.tex` | `text` | Uniform convexity and uniqueness of geodesics | lines 484-486 | yes | yes | - | Finally we point out that using the above result one can show that the finite energy geodesic segments of $\mathcal E^p_\o$ are the only metric geodesics when $p>1$: |
| 7 | 0.648 | `corpus/arxiv/2007.01345/source/source.tex` | `theorem` | Convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesics | lines 639-641 | no | yes | - | \begin{thm} The $(\uu,\vv)$-Mabuchi energy $\mathcal{M}_{\uu,\vv}$ is continuous along weak geodesics and therefore convex in the pointwise sense. \end{thm} |
| 8 | 0.727 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | preliminaries | lines 394-400 | no | yes | - | ...In this section, we will review some basic concepts in K\"ahler geometry as well as some fundamental results involving finite energy currents, which will be needed for our proof of Theorem 1.1 and 1.3. In particular, it includes the characterization of the space $(\mathcal{E}^1,d_1)$, a compactness result on bounded subsets of $\mathcal{E}^1$ with finite en... |
| 9 | 0.702 | `corpus/arxiv/1405.0401/source/source.tex` | `theorem` | \label{sec:Introduction}Introduction > \label{sub:Bergman-kernel-asymptotics}Bergman kernel asymptotics | lines 1077-1079 | yes | yes | - | \begin{thm} \label{thm:continuity text} $\mathcal{M}$ is continuous along weak geodesics and therefore convex in the pointwise sense. \end{thm} |
| 10 | 0.699 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | preliminaries > Convexity of $K$-energy | lines 557-559 | no | yes | finite energy geodesics | \subsection{Convexity of $K$-energy} In this subsection, we record some known results about the convexity of $K$-energy and $J_{\chi}$ functional along $C^{1,1}$ geodesics and also finite energy geodesics. In \cite{chen00}, the first named author proved the following result about the convexity of the functional $J_{\chi}$. |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_018 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss automorphism groups in properness and K-energy arguments?

**Expected sources:** `1506.07129`, `1602.03114`, `1801.00656`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `automorphism group`, `properness`, `K-energy`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.632 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | automorphism group | ...that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be obstructed (see \cite{IltenTuro}). Finally, the toric MMP (that produces the cl... |
| 2 | 0.617 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | Remarks about stability and coercivity in the general setting | lines 1215-1219 | no | yes | automorphism group | \section{Remarks about stability and coercivity in the general setting} In relation with Theorem B, we discuss the definition of stability proposed in the introduction, which would work for general polarizations and automorphism groups. %The results support our torus formulation given in the previous sections. |
| 3 | 0.614 | `corpus/arxiv/1803.09506/source/source.tex` | `remark` | Singular constant scalar curvature K\"ahler metrics > Examples > Reference metrics | lines 2682-2683 | no | no | automorphism group, properness | \begin{rem}About the assumption on the automorphism group in \thmref{singular csck construction}, we remark that in the K\"ahler-Einstein case, Theorem 5.4 in \cite{MR3956691} shows that the $J$-properness of the Mabuchi energy implies the triviality of the automorphism group $Aut(X,D)$. \end{rem} |
| 4 | 0.584 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | yes | yes | automorphism group, properness, K-energy | ...\def\bla{BLA BLA BLA BLA} \def\sp{$\spadesuit$} % Yanir's comments \def\cs{$\clubsuit$} % Tamas' comments \title{Tian's properness conjectures and Finsler geometry of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{document}... |
| 5 | 0.578 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | yes | automorphism group, properness | ...hcal S}_\infty.$ One important technical ingredient to prove existence of cscK from geodesic stability is the following properness theorem, which says that if $K$-energy is ``proper" with respect to a suitably defined distance (defined precisely in Definition \ref{d1.1} below), then cscK exists. To extend the properness theorem to the case of general automor... |
| 6 | 0.563 | `corpus/arxiv/1610.07998/source/source.tex` | `theorem` | Introduction | lines 344-346 | no | yes | automorphism group, K-energy | %\begin{thmB} %Let $(X, L)$ be a polarized manifold. Assume that the K-energy functional is $\Aut^0(X, L)$-coercive on $\cH_r$ for some large $r\in\N$ and moreover $(X, L)$ is asymptotic Chow-semistable. Then $\Aut^0(X, L)$ is a reductive algebraic group. In particular, if a toric polarization $(X, L)$ is uniformly K-polystable and asymptotically Chow-semist... |
| 7 | 0.423 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Introduction > Recent developments | lines 570-578 | no | yes | automorphism group, K-energy | ...K\"ahler--Einstein metrics in~\cite{LTW1,LTW2} are applicable in the case when the log Fano pair in question has finite automorphism group. The general case was recently treated by Chi Li~\cite{Li19} using a notion of uniform K-stability relative to suitable reductive subgroups of the automorphism groups. See also~\cite{His16a,His16b} for some earlier work.... |
| 8 | 0.411 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | yes | yes | - | ...rk) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail in our next paper and refer interested readers to the following works and references therein: |
| 9 | 0.509 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | unsectioned | lines 161-222 | no | yes | automorphism group, K-energy | ...in{document} \begin{abstract} We introduce uniform K-stability and its relationship with the coercivity property of the K-energy functional, for general polarized manifolds. Since the automorphism groups are not necessarily finite, size of the norm measuring uniformity should be reduced with respect to the group action. About this point we explain that it is... |
| 10 | 0.399 | `corpus/arxiv/0805.0128/source/extremal2a.tex` | `text` | Introduction | lines 219-255 | no | yes | - | ...ate in Section 3, the only other restriction on $A$ comes when, in two places, we use the fact that $A$ is positive (in arguments involving the maximum principle) Thus the main result in this paper extends to positive functions $A$ if one assumes an {\it a priori} estimate (6). However the uses we make of (6) are to overcome some rather technical difficultie... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_019 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss energy functionals on singular or weak Kahler potentials?

**Expected sources:** `1510.01260`, `1810.04661`, `2102.05277`
**Expected chunk types:** `definition`, `proposition`, `text`
**Expected terms:** `energy functionals`, `weak potentials`, `singular`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.695 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Background materials > Energy functionals | lines 394-395 | no | yes | energy functionals | \subsection{Energy functionals} In this subsection, we recall functionals on the space of K\"ahler potentials. |
| 2 | 0.680 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 616-633 | no | yes | energy functionals, singular | ...hi}$, which admits a natural decomposition into three components: the weighted entropy term $\ent_v$, the twisted Ricci energy term $\enR_v^{\chi}$, and the weighted energy term $\enE_{v\mathrm{w}}$. Here $\cET(X, \omega)$ denotes the space of $T$-invariant finite energy potentials, which is the metric completion of the space of smooth $T$-invariant K\"ahler... |
| 3 | 0.663 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | Convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesics | lines 430-431 | no | yes | energy functionals | \section{Convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesics} The following formulas allow us to compute the second variations of the energy functionals $\mathcal{E}^{\theta}_{\uu}$ and $\mathcal{E}_{\vv}$ along weak geodesics. |
| 4 | 0.583 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | no | no | singular | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |
| 5 | 0.671 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Extension to $\cET(X, \omega)$ > {Weighted twisted energies} | lines 1203-1206 | no | yes | energy functionals | \subsection{{Weighted twisted energies}} In this section, we extend the weighted energy functionals to the space $\cET(X, \omega)$ of finite energy $T$-invariant potentials. |
| 6 | 0.531 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted cscK problem on semisimple principal fibration | lines 2104-2110 | no | yes | - | Also, from \cite[Section 5]{AJL}, any Kähler metric \(\omega\) on \(X\) induces a Kähler metric \(\tilde{\omega}\) on \(Y\) such that the restriction \((Y_b, \tilde{\omega}_b)\) of \((Y, \tilde{\omega})\) to a fiber over a point \(b \in B\) is \(\T\)-equivariantly Kähler isomorphic to \((X, \omega)\). Such a metric \(\tilde{\omega}\) on \(Y\) is the \emph{co... |
| 7 | 0.651 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 595-604 | no | yes | energy functionals, singular | \section{Introduction} Finding canonical Kähler metrics is a central theme in complex geometry. In higher dimensions, constant scalar curvature Kähler (cscK) metrics provide an analogue of Poincar\'e’s uniformization theorem; see the surveys \cite{Boucksom_2018, Donaldson_2018_2} for background and further references. Kähler--Einstein metrics form an especia... |
| 8 | 0.644 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Extension to $\cET(X, \omega)$ > {Weighted Monge--Ampère operator} | lines 1180-1182 | no | yes | energy functionals | \subsection{{Weighted Monge--Ampère operator}} We start with the fundamental result that the weighted Monge--Ampère operator defined on smooth $T$-invariant K\"ahler potentials admits a continuous extension to the space $\cET(X, \omega)$ of finite energy $T$-invariant potentials. This continuity will be essential in the extension of energy functionals. |
| 9 | 0.636 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | The weighted Mabuchi energy on $\mathcal{K}^{1,1}(X,\omega)^{\T}$ | line 348 | no | yes | energy functionals | Let $\uu\in C^{\infty}(\PP_\alpha,\mathbb{R}_{>0})$ and $\vv\in C^{\infty}(\PP_\alpha,\mathbb{R})$ two smooth functions. Now, we give the energy functionals allowing to define the $(\uu,\vv)$-Mabuchi energy \eqref{Mabuchi} on weak geodesic segments. |
| 10 | 0.628 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Extension to $\cET(X, \omega)$ | lines 1172-1179 | no | yes | energy functionals | \section{Extension to $\cET(X, \omega)$}\label{sec:mabext} In what follows, we extend the weighted Monge--Ampère operator and weighted energy functionals to the space $$ \cET(X, \omega):=\cE^1(X,\omega)^T $$ of $T$-invariant potentials of finite energy. Our treatment is based on \cite{BDL} and \cite{AJL}. |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### bdl_finite_energy_020 - Berman-Darvas-Lu finite energy convexity

**Question:** Where does the corpus discuss Berman-Darvas-Lu convexity as an input to YTD-type arguments?

**Expected sources:** `1510.01260`, `1603.01026`, `1602.03114`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `Berman-Darvas-Lu`, `convexity`, `YTD`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.832 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Applications and Discussions > Extremal K\"ahler metric | lines 1475-1478 | no | yes | - | \subsection{Extremal K\"ahler metric}\label{subsection 9.3} We discuss the situation of extremal K\"ahler(extK) metrics in Theorem~\ref{thm application 2}. To solve the extK equation, we need to choose $T$-invariant coordinates when defining weighted H\"older spaces, and we want to solve for $T$-invariant potential functions. Comparing the expansion of $\ome... |
| 2 | 0.801 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | Convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesics | lines 616-618 | no | yes | convexity | Now, we can use the arguments of Berman--Berndtsson in \cite{BB} to deduce the weak convexity of the $(\uu,\vv)$-Mabuchi energy along weak geodesic segments. We will need the following regularization result which is the main ingredient in the proof of Berman--Berndtsson for the weak convexity of the Mabuchi energy \cite[Theorem 3.3]{BB}. |
| 3 | 0.752 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 375-393 | no | yes | Berman-Darvas-Lu | Given the recent work by J. Street\cite{Street12}, Berman-Darvas-Lu\cite{Darvas1602}, the weak Calabi flow always exists globally. Perhaps one can prove this conjecture via improving regularity of weak Calabi flow. On the other hand, one may hope to prove this conjecture on K\"ahler classes which already admit constant scalar curvature K\"ahler metrics and p... |
| 4 | 0.706 | `corpus/arxiv/0805.0128/source/extremal2a.tex` | `text` | Introduction | lines 219-255 | no | yes | - | ...ate in Section 3, the only other restriction on $A$ comes when, in two places, we use the fact that $A$ is positive (in arguments involving the maximum principle) Thus the main result in this paper extends to positive functions $A$ if one assumes an {\it a priori} estimate (6). However the uses we make of (6) are to overcome some rather technical difficultie... |
| 5 | 0.696 | `corpus/arxiv/1803.09506/source/source.tex` | `proof` | Existence implies properness and geodesic stability > Existence implies properness | lines 4294-4296 | no | no | - | \begin{proof} The proof is similar to the proof given above. The major new input is the use of uniqueness of cscK cone metrics, \thmref{Uniqueness}. \end{proof} |
| 6 | 0.675 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | It is an interesting question to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except i... |
| 7 | 0.656 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | \label{sec:Introduction}Introduction > Statement of the main results | lines 310-335 | no | yes | convexity | ...r $X.$ The general case was treated by Chen-Tian in \cite{c-t}, using their partial regularity theory and approximation arguments and the inequality \ref{eq:chens ineq in intro} was then obtained by Chen, building on \cite{c-t}. In the case of smooth geodesics it is well-known that the Mabuchi functional $\mathcal{M}$ is \emph{strictly }convex modulo automor... |
| 8 | 0.618 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 434-454 | no | yes | Berman-Darvas-Lu, YTD | %To apply this to YTD conjecture, one may even assume that $\Phi$ is $C^{1,\bar{1}}$ by \cite{DL19}. %Based on some new arguments, we will further reduce the above conjecture to a more algebraic one (see Conjecture \ref{conj-SNA}). In section \ref{sec-YTD1}, we will define a non-Archimedean entropy using the non-Archimedean analogue of supremum characterizat... |
| 9 | 0.611 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | - | \def\Rico{\Ric\,\!\o} \def\Q{{\bf ????????????}} \def\a{\alpha} \def\be{\beta} \def\o{\omega} \def\O{\Omega} \def\th{\theta} \def\Th{\Theta} \def\vp{\varphi} \def\eps{\epsilon} \def\vps{\varphi_s} \def\ovp{{\o_{\vp}}} \def\on{\omega^n} \def\ovpn{\omega_{\vp}^n} \def\ovps{\omega_{\vp_s}} \def\ovpsn{\omega_{\vp_s}^n} \def\intM{\int_M} \def\Ric{\hbox{\rm Ric}\,... |
| 10 | 0.758 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Introduction | lines 113-119 | no | yes | - | ...Poincar\'e type K\"ahler metric setting is defined using the Futaki character introduced in \cite{Auv13-2}, and we will discuss in more detail in Section~\ref{subsection 9.3}. Here, we just mention that it is a holomorphic vector field depending only on the K\"ahler class and maximal compact subgroup $K$. From \cite{Auv14} Theorem 4, the condition (\ref{theo... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### chen_cheng_csck_001 - Chen-Cheng cscK estimates

**Question:** Where does the corpus discuss Chen-Cheng cscK estimates?

**Expected sources:** `1712.06697`, `1801.00656`
**Expected chunk types:** `theorem`, `lemma`, `proof`
**Expected terms:** `Chen-Cheng`, `estimates`, `cscK`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.701 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 220-223 | no | no | Chen-Cheng, estimates, cscK | In Section \ref{a priori estimates}, we establish a priori estimates for \eqref{2nd pde} in both the cscK cone problem and the degenerate cases. The a priori estimates of Chen-Cheng rely on fixed smooth K\"ahler metric. In the conical setting, their a priori estimates can not be applied directly, since the a priori estimates are required to be obtained with... |
| 2 | 0.626 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction > Main results and strategy of the proof | lines 252-257 | no | no | Chen-Cheng, estimates, cscK | \subsection{Main results and strategy of the proof} %The goal of this paper is to derive $C^{2}$ a priori estimates for K\"ahler potentials $\varphi \in \mathcal{K}(X,\omega_0)^\T$ corresponding to weighted cscK metrics, generalizing Chen-Cheng estimates in the classical cscK case. The starting point is to re-write the $4$th order non-linear PDE in \eqref{wc... |
| 3 | 0.456 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 409-415 | no | no | Chen-Cheng, cscK | ...result was known by combining the works of Zhou-Zhu \cite{ZZ08}, Chen-Li-Sheng \cite{CLS14}, Hisamoto \cite{His16b} and Chen-Cheng \cite{CC18a, CC18b}. This previous proof depends on Donaldson's deep analysis of K\"{a}hler geometry on toric manifolds (\cite{Don02}). On the other hand, the proof given combines our analysis with the fundamental works on non-Ar... |
| 4 | 0.450 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | unsectioned | lines 596-634 | no | no | Chen-Cheng, estimates, cscK | ...angle}\)}% \mathclose{\copy\@brx\kern-0.5\wd\@brx\usebox{\@brx}}} \makeatother \setcounter{tocdepth}{1} \title{Weighted cscK metrics on K\"ahler varieties} \author{Chung-Ming Pan} \address[Chung-Ming Pan]{Centre interuniversitaire de recherches en g\'eom\'etrie et topologie (CIRGET); Universit\'e du Qu\'ebec \`a Montr\'eal; Case postale 8888, Succursale cent... |
| 5 | 0.509 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 186-204 | no | no | Chen-Cheng, estimates, cscK | ...redients. One is the approximation scheme of the log $K$-energy, which leads to the construction of approximate twisted cscK metrics. Then we will show that this approximate sequence converges to a cscK cone metric by applying the a priori estimates given in Section \ref{a priori estimates}, that is the other ingredient of the proof of the log properness the... |
| 6 | 0.397 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Background materials > $d_{1}$-distances, reduced $d_{1}$-distances and the reduced J-functionals | lines 626-627 | no | no | Chen-Cheng | By using the theory of Chen-Cheng and He \cite{CC17}, \cite{CC18a}, \cite{CC18b}, \cite{He18}, and the arguments in \cite{Li19}, we shall show the following theorem. |
| 7 | 0.493 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction | lines 191-199 | no | no | Chen-Cheng, estimates, cscK | ...rch for canonical K\"ahler metrics. The concept of \emph{constant weighted scalar curvature K\"ahler metrics} (weighted cscK for short), introduced by the third author in \cite{Lah19}, provides a unification of various related notions of canonical K\"ahler metrics that satisfy special curvature conditions. We present here the first of two papers, focused on... |
| 8 | 0.385 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | no | cscK | ...ction defined on the sphere of infinity ${\mathcal S}_\infty.$ One important technical ingredient to prove existence of cscK from geodesic stability is the following properness theorem, which says that if $K$-energy is ``proper" with respect to a suitably defined distance (defined precisely in Definition \ref{d1.1} below), then cscK exists. To extend the pro... |
| 9 | 0.461 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | unsectioned | lines 114-137 | no | no | Chen-Cheng, cscK | ...{\today} \begin{document} \maketitle \begin{abstract} We show that the existence of constant scalar curvature K\"ahler (cscK) metrics with cone singularities is equivalent to the properness of log $K$-energy. We also prove their equivalence to the geodesic stability. They are extensions of the solution of the properness conjecture and Donaldson's geodesic st... |
| 10 | 0.365 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | no | cscK | ...phic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelia... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### chen_cheng_csck_002 - Chen-Cheng cscK estimates

**Question:** Where does the corpus discuss cscK metrics with general automorphism group?

**Expected sources:** `1801.00656`, `1801.05907`
**Expected chunk types:** `theorem`, `proof`, `text`
**Expected terms:** `general automorphism group`, `cscK`, `Chen-Cheng`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.753 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Existence implies properness and geodesic stability > Geodesic stability > General automorphism group | lines 4424-4431 | no | yes | general automorphism group, cscK | \subsubsection{General automorphism group}\label{Donaldson geodesic stability conjecture: general case} In this section, \thmref{Existence implies properness discrete} and \thmref{geodesic conjecture} will be extended to general case, that is the automorphism group is non-trivial. This section is a generalisation of \cite{arXiv:1801.05907}. We remark that th... |
| 2 | 0.722 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | cscK | ...that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be obstructed (see \cite{IltenTuro}). Finally, the toric MMP (that produces the cl... |
| 3 | 0.654 | `corpus/arxiv/1412.0648/source/twisted.tex` | `conjecture` | Introduction | line 102 | no | no | cscK | \begin{conjecture}\label{introconjecture} A polarised manifold $(X,L)$ with discrete automorphism group admits a cscK metric if and only if it is uniformly K-stable with respect to the minimum norm. \end{conjecture} |
| 4 | 0.602 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | yes | yes | general automorphism group, cscK | ...ction defined on the sphere of infinity ${\mathcal S}_\infty.$ One important technical ingredient to prove existence of cscK from geodesic stability is the following properness theorem, which says that if $K$-energy is ``proper" with respect to a suitably defined distance (defined precisely in Definition \ref{d1.1} below), then cscK exists. To extend the pro... |
| 5 | 0.646 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `theorem` | Background on cscK metrics and their moduli > Extremal K\"ahler metrics | lines 315-318 | no | yes | cscK | \begin{theorem}[\cite{matsushima57,Lichn}] \label{theo:MatLich} Assume that $X$ carries a cscK metric. Then the automorphism group of $X$ is reductive. \end{theorem} |
| 6 | 0.497 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Introduction > Recent developments | lines 570-578 | no | yes | cscK | ...bation argument on a resolution of singularities. As in the current paper, the existence results for K\"ahler--Einstein metrics in~\cite{LTW1,LTW2} are applicable in the case when the log Fano pair in question has finite automorphism group. The general case was recently treated by Chi Li~\cite{Li19} using a notion of uniform K-stability relative to suitable... |
| 7 | 0.495 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | - | ...ef\cs{$\clubsuit$} % Tamas' comments \title{Tian's properness conjectures and Finsler geometry of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{document} \maketitle \begin{abstract} Well-known conjectures of Tian predict t... |
| 8 | 0.491 | `corpus/arxiv/math_0412518/source/slopeobs_archive.tex` | `remark` | Examples > Unstable rational manifolds | lines 2116-2127 | no | no | cscK | ...cture}. The case of $\PP^2$ blown up at $\ge4$ points gives smooth polarised del Pezzo surfaces with $\aut(X)=0$ but no cscK metric in certain classes. This is in contrast to the case of the anticanonical polarisation for which Tian \cite{Ti1} proved the ``folklore conjecture", that smooth Fano surfaces have a K\"ahler-Einstein metric if and only if their ho... |
| 9 | 0.485 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 671-675 | no | yes | cscK | ...onaldson (YTD) conjecture~\cite{Yau93,Tia97,Don02} predicts that the existence of a constant scalar curvature K\"ahler (cscK) metric (and, more generally, of a `canonical' metric) $\om\in c_1(L)$ is equivalent to a stability condition on $(X,L)$ of purely algebro-geometric nature. In the special case where $X$ is Fano and $L=-K_X$ (for which cscK metrics are... |
| 10 | 0.480 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | Remarks about stability and coercivity in the general setting | lines 1310-1312 | no | yes | - | For a general polarization it seems still difficult to derive coercivity from uniform stability. We proceed to explain the relation with constant scalar curvature K\"ahler metrics. The next statement shows that we should take $G$ as the full automorphism group. |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### chen_cheng_csck_003 - Chen-Cheng cscK estimates

**Question:** Where does the corpus discuss a priori estimates for the cscK equation?

**Expected sources:** `1712.06697`, `1801.00656`
**Expected chunk types:** `theorem`, `lemma`, `proof`
**Expected terms:** `a priori estimates`, `cscK equation`, `Chen-Cheng`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.776 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | A priori estimates | lines 2694-2698 | no | no | a priori estimates | \section{A priori estimates}\label{a priori estimates} In this section, we derive the a priori estimates of the cscK metrics with both cone singularities and degeneration. |
| 2 | 0.743 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Existence of singular weighted cscK metrics | lines 1668-1670 | no | no | a priori estimates | \section{Existence of singular weighted cscK metrics} \label{sect_existence} We shall combine the a priori estimates obtained in the previous section and the uniform coercivity established in \cite{Boucksom_Jonsson_Trusiani_2024} to construct singular weighted cscK metrics. |
| 3 | 0.698 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | unsectioned | lines 170-190 | no | no | a priori estimates | \title{Weighted cscK metrics (I): a priori estimates} \author{Eleonora Di Nezza, Simon Jubert and Abdellah Lahdili} \begin{document} \maketitle \begin{abstract} \noindent Let $X$ be a compact K\"ahler manifold. In this paper we study the existence of constant weighted scalar curvature K\"ahler (weighted cscK) metrics on $X$. More precisely, we establish a pr... |
| 4 | 0.619 | `corpus/arxiv/1712.06697/source/source.tex` | `text` | Introduction | lines 156-166 | yes | no | a priori estimates, cscK equation | ...roduction} This is the first of a series of three papers in the study of of constant scalar curvature K\"ahler metrics (cscK metrics), following a program outlined in \cite{chen15}. In this paper, we focus on establishing a priori estimates for cscK metrics in compact K\"ahler manifold without boundary. Our estimates can be easily adapted to extremal K\"ahle... |
| 5 | 0.602 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | no | - | ...st, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be obstructed (see \cite{IltenTuro}). Finally, the toric MMP (that produces the classification of toric surfaces) produces singular varieties... |
| 6 | 0.574 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 143-151 | no | no | a priori estimates, cscK equation | ...rics in K\"ahler manifolds without boundary \cite{cc1}, \cite{cc2}. In this paper, we continue our study of the twisted cscK equation \[ t(R_\varphi -\underline{R}) = (1-t) (tr_\varphi \chi- \underline{\chi}), \qquad {\rm where}\;\; t\in [0,1]. \] We studied a priori estimates for the preceding equation with $t=1$ in \cite{cc1} and studied this one-parameter... |
| 7 | 0.692 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 220-223 | no | no | a priori estimates, Chen-Cheng | In Section \ref{a priori estimates}, we establish a priori estimates for \eqref{2nd pde} in both the cscK cone problem and the degenerate cases. The a priori estimates of Chen-Cheng rely on fixed smooth K\"ahler metric. In the conical setting, their a priori estimates can not be applied directly, since the a priori estimates are required to be obtained with... |
| 8 | 0.551 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Introduction | lines 272-277 | no | no | a priori estimates | ...roof for closeness is divided into two parts: we first prove closeness up to a time $t < 1$, primarily relying on the a priori estimates for weighted cscK metrics established in our previous work \cite{DJL}. To extend the closeness to $t = 1$, we derive $W^{1,2p}$-estimates for solutions of a $(\v,\w)$-cscK type equation: |
| 9 | 0.530 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | \Holder estimates for second derivatives | lines 3248-3257 | no | no | a priori estimates | \section{\Holder estimates for second derivatives} \label{HolderSection} In the interior of $\MsmD$ the Evans--Krylov regularity theory for \MA equations (Theorem~\ref{EvansKrylovThm}) may be applied to obtain the a priori interior $\calC^{2,\gamma}$ estimate for a solution $\vp$ on any ball $B'$ depending on $\calC^0$ estimates for $\vp$ and $\Delta_\o \vp$... |
| 10 | 0.468 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Background > $v$-solitons and Real Monge-Amp\`ere equations | lines 669-670 | no | no | - | As we will see in Section \ref{stability-section}, this is also true for the more general $(v,\, w)$-cscK problem under certain assumptions on the weights and the metric. Notably, in the absence of the real Monge-Amp\`ere equation \eqref{rMA1}, there is no analog of the a priori integrability condition \eqref{vsoliton-finitevolume}. |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### chen_cheng_csck_004 - Chen-Cheng cscK estimates

**Question:** Where does the corpus discuss properness and existence of cscK metrics via Chen-Cheng?

**Expected sources:** `1801.00656`, `1602.03114`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `properness`, `existence`, `cscK`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.752 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | unsectioned | lines 114-137 | no | yes | properness, existence, cscK | \title[Existence, Properness and Geodesic stability]{Existence of constant scalar curvature K\"ahler cone metrics, properness and geodesic stability} \author{Kai Zheng} % \address{University of Warwick} \curraddr{Tongji University, Shanghai 200092, P.R. CHINA} \email[Kai Zheng]{kaizheng@amss.ac.cn} %\date{\today} \begin{document} \maketitle \begin{abstract}... |
| 2 | 0.734 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 179-182 | no | yes | properness, existence, cscK | We will prove that the existence of cscK cone metrics in terms of the properness of the log $K$-energy. |
| 3 | 0.721 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | no | no | existence, cscK | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |
| 4 | 0.665 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 138-162 | no | yes | properness, existence, cscK | \section{Introduction} %It is suggested by Chen \cite{MR3858468} that, the path of cscK metrics with cone singularities are expected to serve as a continuity method to find the cscK metric aiming to Yau-Tian-Donaldson conjecture, which coincides with Donaldson's continuity method in the K\"ahler-Einstein problem \cite{MR3264768,MR2975584}. In K\"ahler geomet... |
| 5 | 0.528 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction | lines 191-199 | no | yes | existence, cscK | \section{Introduction}{\label{s:intro}} A central theme in K\"ahler geometry is the search for canonical K\"ahler metrics. The concept of \emph{constant weighted scalar curvature K\"ahler metrics} (weighted cscK for short), introduced by the third author in \cite{Lah19}, provides a unification of various related notions of canonical K\"ahler metrics that sat... |
| 6 | 0.526 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | yes | properness, existence, cscK | ...iant as a function defined on the sphere of infinity ${\mathcal S}_\infty.$ One important technical ingredient to prove existence of cscK from geodesic stability is the following properness theorem, which says that if $K$-energy is ``proper" with respect to a suitably defined distance (defined precisely in Definition \ref{d1.1} below), then cscK exists. To e... |
| 7 | 0.655 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Regularity and uniqueness of log $\chi$-twisted $K$-energy minimisers | lines 4049-4050 | no | yes | properness, existence, cscK | ...and uniqueness of the log $\chi$-twisted $K$-energy minimisers. They will be used in the next section to prove that the existence of cscK cone metrics implies the properness of the log $K$-energy. |
| 8 | 0.641 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 186-204 | no | yes | properness, existence, cscK | \bigskip In Section \ref{Properness conjecture: automorphism is trivial} we prove one direction of the log properness \thmref{cone properness conjecture}, that is 'properness $\implies$ existence'. Precise statements are given in \thmref{properclosedness}, \thmref{Properness implies existence general}. The proof relies on two ingredients. One is the approxim... |
| 9 | 0.501 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | unsectioned | lines 596-634 | no | yes | existence, cscK | ...angle}\)}% \mathclose{\copy\@brx\kern-0.5\wd\@brx\usebox{\@brx}}} \makeatother \setcounter{tocdepth}{1} \title{Weighted cscK metrics on K\"ahler varieties} \author{Chung-Ming Pan} \address[Chung-Ming Pan]{Centre interuniversitaire de recherches en g\'eom\'etrie et topologie (CIRGET); Universit\'e du Qu\'ebec \`a Montr\'eal; Case postale 8888, Succursale cent... |
| 10 | 0.483 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 225-232 | no | yes | existence, cscK | ...odge class. The Yau-Tian-Donaldson (YTD) conjecture aims to give a sufficient and necessary algebraic condition for the existence of constant scalar curvature K\"{a}hler (cscK) metric in the K\"{a}hler class $[\omega]$. Recently there have been significant progresses towards this conjecture, especially on the analytic part (see \cite{BDL17, BDL18, CC17,CC18a... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### chen_cheng_csck_005 - Chen-Cheng cscK estimates

**Question:** Where does the corpus discuss the fourth-order cscK equation and scalar curvature estimates?

**Expected sources:** `1712.06697`, `1801.00656`
**Expected chunk types:** `theorem`, `lemma`, `proof`
**Expected terms:** `fourth-order`, `scalar curvature`, `estimates`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.717 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | Coercivity for the toric case > Torus-invariant metrics | lines 929-932 | no | no | fourth-order, scalar curvature | We say $u$ is normalized at this end. The scalar curvature is given by a fourth-order differential of $u$. |
| 2 | 0.571 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction > Organisation of the paper | lines 335-346 | no | no | fourth-order, scalar curvature, estimates | ...and references to pluripotential theory. Section \ref{s:wsystem} is dedicated to establish the equivalence between the fourth-order PDE \eqref{wcsck} and the system of elliptic PDE's \eqref{weightedsystem:intro}. %In order to do so, in Lemma \ref{l:scalv} we establish the alternative definition of the weighted scalar curvature as the weighted trace of the w... |
| 3 | 0.543 | `corpus/arxiv/1712.06697/source/source.tex` | `text` | Introduction | lines 156-166 | yes | no | scalar curvature, estimates | \section{Introduction} This is the first of a series of three papers in the study of of constant scalar curvature K\"ahler metrics (cscK metrics), following a program outlined in \cite{chen15}. In this paper, we focus on establishing a priori estimates for cscK metrics in compact K\"ahler manifold without boundary. Our estimates can be easily adapted to extr... |
| 4 | 0.491 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `text` | Momentum-constructed cscK metrics with cone singularities along a divisor > Some properties of momentum-constructed metrics with $\varphi' (b) = -2 \beta$ | lines 1107-1115 | no | no | scalar curvature, estimates | We now prove the following estimates on the Ricci curvature and the scalar curvature of $\omega_{\varphi}$ around the $\infty$-section, i.e. when $\tau \to b$. %where we still use $z_1$ for the fibrewise coordinate around the $\infty$-section with $z_1=0$ defining the $\infty$-section $D$.%, where we note that it does not need the $\sigma$-constancy hypothes... |
| 5 | 0.485 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 273-284 | yes | no | scalar curvature, estimates | ...it is interesting to understand geometrically for what K\"ahler classes this invariant is $1$ but do not admit constant scalar curvature metrics. More broadly, it is interesting to estimate the upper and lower bound of this invariant. It is not hard to see the relation between the invariant introduced in \cite{Sz11} and the invariant introduced above when re... |
| 6 | 0.433 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Singular constant scalar curvature K\"ahler metrics > Singular cscK metrics | lines 2534-2546 | no | no | estimates | \begin{ques} Could we obtain Laplacian estimate or higher order estimates of the singular cscK metric $\omega_\vphi=\om^Y_K+i\p\bar\p\vphi$? Does it satisfy the following couple of equations on the regular part $Y_{reg}\setminus \tri$, \begin{equation}\label{singular cscK} \left\{ \begin{aligned} &\om_\vphi^n=e^F\om_\theta^n,\\ &\tri_{\vphi} F=\tr_{\om_\vphi... |
| 7 | 0.431 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Introduction | lines 166-184 | no | no | scalar curvature | ...i}{\partial z_\alpha \bar \partial z_\beta}\right) {\sqrt{-1}\over 2} d\,z^\alpha \wedge \overline{d\, z^\beta}. $$ Its scalar curvature $R_\varphi$ is defined as: \[ R_\varphi = - g_\varphi^{\alpha\bar \beta} \frac{\partial^2}{\partial z_\alpha \partial \bar{z}_\beta}\log \det(g_{\varphi,i\bar j}). \] The central problem in K\"ahler geometry which goes back... |
| 8 | 0.429 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 155-163 | no | no | scalar curvature, estimates | We are able to extend many of our previous estimates in \cite{cc1}, \cite{cc2} to these more general right hand side as (\ref{rhs}). These new apriori estimates are crucial for us to extend our proof of Donaldson's conjecture on geodesic stability and the Properness conjecture for $K$-energy to the setting with general automorphism group. The results in this... |
| 9 | 0.424 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 717-744 | no | no | estimates | The strategy for proving Theorem~\ref{bigthm_existence_0} is to establish uniform a priori estimates for the solutions to a family of {weighted} cscK equations on the resolution of singularities $\pi: Y \to X$. Denote by $E$ the exceptional set of $\pi$. Consider a family of perturbed K\"ahler metrics $\om_\vep := \pi^\ast \om + \vep \om_Y$ on the resolution... |
| 10 | 0.421 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Preliminaries > More functionals | lines 1285-1287 | no | no | scalar curvature | %By proving Theorem \ref{thm-Echislope}, we will show that this is well-defined and does not depend on the choice of the decreasing sequence $\Phi_m$. The constant scalar curvature K\"{a}hler metrics are global minimizers of Mabuchi functional $\bfM(\vphi)$. We now have the following important analytic criterion for the existence of cscK metrics: |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### chen_cheng_csck_006 - Chen-Cheng cscK estimates

**Question:** Where does the corpus discuss twisted cscK or continuity paths related to Chen-Cheng estimates?

**Expected sources:** `1712.06697`, `1801.00656`, `1412.0648`
**Expected chunk types:** `theorem`, `lemma`, `text`
**Expected terms:** `twisted cscK`, `continuity path`, `Chen-Cheng`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.869 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | preliminaries > $K$-energy and twisted $K$-energy | lines 460-463 | yes | yes | continuity path | In the following, we will assume $\chi>0$, that is, $\chi$ is a K\"ahler form. The equation (\ref{2.12}) with $t \in [0,1]$ is the continuity path proposed in \cite{chen15} to solve the cscK equation. More generally, one can consider similar twisted paths in order to solve (\ref{2.6n}). Namely we consider |
| 2 | 0.741 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 220-223 | no | yes | Chen-Cheng | In Section \ref{a priori estimates}, we establish a priori estimates for \eqref{2nd pde} in both the cscK cone problem and the degenerate cases. The a priori estimates of Chen-Cheng rely on fixed smooth K\"ahler metric. In the conical setting, their a priori estimates can not be applied directly, since the a priori estimates are required to be obtained with... |
| 3 | 0.696 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction | lines 191-199 | no | yes | continuity path, Chen-Cheng | ...rch for canonical K\"ahler metrics. The concept of \emph{constant weighted scalar curvature K\"ahler metrics} (weighted cscK for short), introduced by the third author in \cite{Lah19}, provides a unification of various related notions of canonical K\"ahler metrics that satisfy special curvature conditions. We present here the first of two papers, focused on... |
| 4 | 0.604 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 409-415 | no | yes | Chen-Cheng | ...result was known by combining the works of Zhou-Zhu \cite{ZZ08}, Chen-Li-Sheng \cite{CLS14}, Hisamoto \cite{His16b} and Chen-Cheng \cite{CC18a, CC18b}. This previous proof depends on Donaldson's deep analysis of K\"{a}hler geometry on toric manifolds (\cite{Don02}). On the other hand, the proof given combines our analysis with the fundamental works on non-Ar... |
| 5 | 0.663 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction > Main results and strategy of the proof | lines 252-257 | no | yes | Chen-Cheng | \subsection{Main results and strategy of the proof} %The goal of this paper is to derive $C^{2}$ a priori estimates for K\"ahler potentials $\varphi \in \mathcal{K}(X,\omega_0)^\T$ corresponding to weighted cscK metrics, generalizing Chen-Cheng estimates in the classical cscK case. The starting point is to re-write the $4$th order non-linear PDE in \eqref{wc... |
| 6 | 0.518 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Introduction | lines 326-370 | no | yes | continuity path | ...ults in \S 4 then show that the solution is polyhomogeneous. The key new ingredient for deriving the nonlinear a priori estimates is the new {\it Ricci continuity method}, which can be considered as a continuity method analogue of the Ricci flow. This was introduced in the context of the Ricci iteration by the third named author \cite{R}, and one point of th... |
| 7 | 0.638 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 186-204 | no | yes | twisted cscK, Chen-Cheng | ...two ingredients. One is the approximation scheme of the log $K$-energy, which leads to the construction of approximate twisted cscK metrics. Then we will show that this approximate sequence converges to a cscK cone metric by applying the a priori estimates given in Section \ref{a priori estimates}, that is the other ingredient of the proof of the log proper... |
| 8 | 0.493 | `corpus/arxiv/1712.06697/source/source.tex` | `text` | Introduction | lines 156-166 | yes | yes | continuity path | ...roduction} This is the first of a series of three papers in the study of of constant scalar curvature K\"ahler metrics (cscK metrics), following a program outlined in \cite{chen15}. In this paper, we focus on establishing a priori estimates for cscK metrics in compact K\"ahler manifold without boundary. Our estimates can be easily adapted to extremal K\"ahle... |
| 9 | 0.612 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 138-162 | no | yes | Chen-Cheng | \section{Introduction} %It is suggested by Chen \cite{MR3858468} that, the path of cscK metrics with cone singularities are expected to serve as a continuity method to find the cscK metric aiming to Yau-Tian-Donaldson conjecture, which coincides with Donaldson's continuity method in the K\"ahler-Einstein problem \cite{MR3264768,MR2975584}. In K\"ahler geomet... |
| 10 | 0.599 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | unsectioned | lines 114-137 | no | yes | Chen-Cheng | ...{\today} \begin{document} \maketitle \begin{abstract} We show that the existence of constant scalar curvature K\"ahler (cscK) metrics with cone singularities is equivalent to the properness of log $K$-energy. We also prove their equivalence to the geodesic stability. They are extensions of the solution of the properness conjecture and Donaldson's geodesic st... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### chen_cheng_csck_007 - Chen-Cheng cscK estimates

**Question:** Where does the corpus discuss cscK existence when the automorphism group is non-discrete?

**Expected sources:** `1801.00656`, `1801.05907`
**Expected chunk types:** `theorem`, `proof`, `text`
**Expected terms:** `automorphism group`, `non-discrete`, `cscK existence`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.734 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `theorem` | Background on cscK metrics and their moduli > Extremal K\"ahler metrics | lines 315-318 | no | yes | automorphism group | \begin{theorem}[\cite{matsushima57,Lichn}] \label{theo:MatLich} Assume that $X$ carries a cscK metric. Then the automorphism group of $X$ is reductive. \end{theorem} |
| 2 | 0.719 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | yes | yes | automorphism group | ...sic ray (up to parallelism), thus defines a point at ${\mathcal S}_\infty.$ It is important to understand the converse: when does a locally finite energy geodesic ray define a test configuration? More importantly, can one extend the definition of $\yen$ invariant for analytic test configuration? Note that by Theorem 1.4, we can view $\yen$ invariant as a fun... |
| 3 | 0.703 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | no | no | - | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |
| 4 | 0.692 | `corpus/arxiv/1412.0648/source/twisted.tex` | `conjecture` | Introduction | line 102 | no | no | automorphism group | \begin{conjecture}\label{introconjecture} A polarised manifold $(X,L)$ with discrete automorphism group admits a cscK metric if and only if it is uniformly K-stable with respect to the minimum norm. \end{conjecture} |
| 5 | 0.682 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Introduction > Recent developments | lines 570-578 | no | yes | automorphism group, non-discrete | ..., but additionally uses a delicate perturbation argument on a resolution of singularities. As in the current paper, the existence results for K\"ahler--Einstein metrics in~\cite{LTW1,LTW2} are applicable in the case when the log Fano pair in question has finite automorphism group. The general case was recently treated by Chi Li~\cite{Li19} using a notion of... |
| 6 | 0.627 | `corpus/arxiv/math_0412518/source/slopeobs_archive.tex` | `text` | Definition of K-stability > Relationship to constant scalar curvature K\"ahler metrics | lines 365-398 | no | yes | automorphism group, non-discrete | One direction of this conjecture, that existence of a cscK metric implies stability, has almost been proved: in \cite{Do5} it is shown that a cscK metric implies K-semistability. Before that paper one had a slightly weaker result by using balanced metrics: if $\aut(X)=0$ then the existence of a cscK metric implies that the Kodaira embedding of $(X,L^{\otimes... |
| 7 | 0.722 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | automorphism group | ...nal case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be obstructed (see \cite{Ilten... |
| 8 | 0.703 | `corpus/arxiv/1803.09506/source/source.tex` | `theorem` | Existence implies properness and geodesic stability > Existence implies properness | lines 4248-4251 | no | yes | automorphism group | \begin{thm}\label{Existence implies properness discrete}Assume that the automorphism group $Aut(X;D)$ is discrete. Suppose that there exists a constant scalar curvature K\"ahler cone metric $\om_{cscK}$. Then the log $K$-energy is proper. Moreover, the log $K$-energy is coercive. \end{thm} |
| 9 | 0.533 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | Introduction | lines 253-260 | no | yes | automorphism group | ...r with recently developed algebraic methods to check the stability condition. The uniform estimate even helps seeking a cscK metric. We refer to \cite{BBJ15} for the detail of this direction. %When the automorphism group $\Aut(X, L)$ is not discrete one have to replace K-stability to K-polystability; $M^{\NA}(\cX, \cL)\geq0$ for any $(\cX, \cL)$ and the equa... |
| 10 | 0.510 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 671-675 | no | yes | automorphism group | ...bundle on $X$. Broadly understood, the Yau--Tian--Donaldson (YTD) conjecture~\cite{Yau93,Tia97,Don02} predicts that the existence of a constant scalar curvature K\"ahler (cscK) metric (and, more generally, of a `canonical' metric) $\om\in c_1(L)$ is equivalent to a stability condition on $(X,L)$ of purely algebro-geometric nature. In the special case where $... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### chen_cheng_csck_008 - Chen-Cheng cscK estimates

**Question:** Where does the corpus discuss regularity of weak cscK minimizers?

**Expected sources:** `1602.03114`, `1801.00656`
**Expected chunk types:** `theorem`, `proof`, `text`
**Expected terms:** `weak minimizers`, `regularity`, `cscK`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.622 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 305-310 | no | yes | weak minimizers, regularity, cscK | The direction that existence of cscK implies properness has been established by Berman, Darvas and Lu in \cite{Darvas1605}. For the converse direction, Darvas and Rubinstein in \cite{Dar-Rub-17} have reduced this problem to a problem of regularity of weak minimizers of $K$-energy over the space $\mathcal{E}^1$, which we resolved in the second paper \cite{cc2... |
| 2 | 0.555 | `corpus/arxiv/2104.09709/source/source.tex` | `text` | Regularity of the weak minimizers of the weighted Mabuchi energy | lines 1418-1419 | no | yes | weak minimizers, regularity | \section{Regularity of the weak minimizers of the weighted Mabuchi energy}\label{s:regularity} In this section, we establish the regularity of the weak minimizers of $\cE_{v,w}$. |
| 3 | 0.538 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | regularity of weak minimizers of $K$-energy | lines 1391-1409 | yes | yes | weak minimizers, regularity, cscK | \section{regularity of weak minimizers of $K$-energy} Our main goal in this section is to show the minimizers of $K$-energy over $\mathcal{E}^1$ are always smooth. The main ingredients are the continuity path as well as apriori estimates obtained in section 3. The strategy of the proof is somewhat different from the usual variational problem. Indeed, the usu... |
| 4 | 0.537 | `corpus/arxiv/1712.06697/source/source.tex` | `remark` | Introduction | lines 266-269 | no | no | cscK | \begin{rem} In Theorem \ref{t1.1} and the first part of Theorem \ref{t1.2}, it is sufficient to assume that $\varphi$ remains bounded under $L^1$ geodesic distance, due to the fact that cscK metrics are minimizers of $K$-energy. We will discuss this matter in more detail in our next paper of the series. \end{rem} |
| 5 | 0.466 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Preliminaries > More functionals | lines 1285-1287 | no | yes | cscK | %By proving Theorem \ref{thm-Echislope}, we will show that this is well-defined and does not depend on the choice of the decreasing sequence $\Phi_m$. The constant scalar curvature K\"{a}hler metrics are global minimizers of Mabuchi functional $\bfM(\vphi)$. We now have the following important analytic criterion for the existence of cscK metrics: |
| 6 | 0.459 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | regularity | ...on of it (in the presence of automorphisms) in the general case of constant scalar curvature metrics to a conjecture on regularity of minimizers of the K-energy in the Finsler metric completion. Finally, our results also resolve Tian's conjecture on the Moser--Trudinger inequality for Fano manifolds with \KE metrics. \end{abstract} |
| 7 | 0.454 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Background materials > Riemannian geometry of the space of K\"ahler potentials | lines 389-393 | no | yes | regularity | ...he other hand, Chen \cite{Ch00a} proved that the Dirichlet problem of \eqref{geod_MA} always has a unique solution in a weak sense (\cite{BT76}). After successive refinement in \cite{Bl12} and \cite{CTW17}, it is proved that the weak solution has $C^{1,1}$ regularity. |
| 8 | 0.451 | `corpus/arxiv/1510.01260/source/source.tex` | `text` | Extension of the twisted K-energy > Uniqueness of twisted K-energy minimizers | lines 1009-1010 | no | yes | - | %As a strategy to find minimizers of the K-energy, one may consider finding minimizers of the twisted K-energy first and then consider the limit as the twisting form goes to zero. This was put forward in recent works \cite{c4,cpz}, in case of smooth minimizers, and below we provide a partial weak analog of one of their results: |
| 9 | 0.448 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Singular constant scalar curvature K\"ahler metrics > Singular cscK metrics | lines 2534-2546 | no | no | regularity, cscK | \begin{ques} Could we obtain Laplacian estimate or higher order estimates of the singular cscK metric $\omega_\vphi=\om^Y_K+i\p\bar\p\vphi$? Does it satisfy the following couple of equations on the regular part $Y_{reg}\setminus \tri$, \begin{equation}\label{singular cscK} \left\{ \begin{aligned} &\om_\vphi^n=e^F\om_\theta^n,\\ &\tri_{\vphi} F=\tr_{\om_\vphi... |
| 10 | 0.421 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | cscK | ...phic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelia... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### chen_cheng_csck_009 - Chen-Cheng cscK estimates

**Question:** Where does the corpus discuss the J-flow or J-equation as background to cscK estimates?

**Expected sources:** `1712.06697`, `1801.00656`
**Expected chunk types:** `definition`, `theorem`, `text`
**Expected terms:** `J-flow`, `J-equation`, `cscK estimates`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.712 | `corpus/arxiv/1803.09506/source/source.tex` | `remark` | Introduction | lines 245-247 | no | no | - | \begin{rem} These estimates are also obtained for cscK cone metric by directly making use of the conical background metric as shown in \cite{arXiv:1805.04944}, which are considered to be the limit of \thmref{A priori estimates}. \end{rem} |
| 2 | 0.686 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Introduction | lines 295-300 | no | yes | - | The paper is organised as follows. In Section \ref{sec:background}, we settle the necessary background material on cscK manifolds. Then, Section \ref{sec:foldable toric surfaces} is devoted to the classification of foldable surfaces and the proofs of Proposition \ref{prop:intro fans} and Proposition \ref{prop:intro}. In Section \ref{sec:local moduli construc... |
| 3 | 0.621 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | yes | - | It is an interesting question to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except i... |
| 4 | 0.589 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Linear analysis | lines 1203-1232 | no | yes | - | ...linear elliptic theory needed to handle the existence, deformation and regularity theory for canonical edge metrics. We discuss this from two points of view, reviewing the estimates obtained by Donaldson in the wedge H\"older spaces, and also describing how to obtain analogous estimates in the edge H\"older spaces. These latter estimates are obtained through... |
| 5 | 0.584 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | more general cscK type equations > Reduction of $C^{1,1}$ estimates to $W^{2,p}$ estimates | lines 678-681 | yes | yes | - | \subsection{Reduction of $C^{1,1}$ estimates to $W^{2,p}$ estimates} This is the part where the main difference comes up with cscK case and we will highlight this difference. We will be brief at places where the proof works in the same way as cscK case. The exact result we will prove is the following: |
| 6 | 0.581 | `corpus/arxiv/1412.0648/source/twisted.tex` | `remark` | K-stability of twisted cscK metrics > The argument in a fixed projective space | line 348 | no | no | J-flow | \begin{remark} There is an interesting analogy here with Stoppa's proof that the existence of a twisted cscK metric implies semistability with respect to test configurations arising from deformation to the normal cone \cite{JS}. Indeed, his proof involves an asymptotic expansion of the twisted Mabuchi functional, which is the sum of the usual Mabuchi functio... |
| 7 | 0.562 | `corpus/arxiv/1205.0056/source/cone_metrics.tex` | `text` | A priori estimates | lines 1223-1227 | no | yes | - | in the space $C^{2,\a}_\b$. We will specify the conditions on $\Psi_0$ in each estimate. Since the curvature conditions of the background metrics are required when we derive the a priori estimates, we explain an observation on how to choose appropriate background metrics. If we take $\Om_{1}$ as the background metric, we obtain an equivalent equation |
| 8 | 0.537 | `corpus/arxiv/1712.06697/source/source.tex` | `text` | Some local estimates | lines 1432-1439 | yes | yes | - | \section{Some local estimates} In this section, we show some localized version of our previous estimates. Suppose we have a solution $\varphi$ to (\ref{csck1}), (\ref{csck2}) in the unit ball $B_1(0)\subset\mathbb{C}^n$. First we can find a potential $\rho$ to the background metric $g$, namely $$ \omega_0=\sqrt{-1}\partial\bar{\partial}\rho,\textrm{ in $B_1(... |
| 9 | 0.521 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | - | \def\Rico{\Ric\,\!\o} \def\Q{{\bf ????????????}} \def\a{\alpha} \def\be{\beta} \def\o{\omega} \def\O{\Omega} \def\th{\theta} \def\Th{\Theta} \def\vp{\varphi} \def\eps{\epsilon} \def\vps{\varphi_s} \def\ovp{{\o_{\vp}}} \def\on{\omega^n} \def\ovpn{\omega_{\vp}^n} \def\ovps{\omega_{\vp_s}} \def\ovpsn{\omega_{\vp_s}^n} \def\intM{\int_M} \def\Ric{\hbox{\rm Ric}\,... |
| 10 | 0.644 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Singular constant scalar curvature K\"ahler metrics > Singular cscK metrics | lines 2534-2546 | no | no | - | \begin{ques} Could we obtain Laplacian estimate or higher order estimates of the singular cscK metric $\omega_\vphi=\om^Y_K+i\p\bar\p\vphi$? Does it satisfy the following couple of equations on the regular part $Y_{reg}\setminus \tri$, \begin{equation}\label{singular cscK} \left\{ \begin{aligned} &\om_\vphi^n=e^F\om_\theta^n,\\ &\tri_{\vphi} F=\tr_{\om_\vphi... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### chen_cheng_csck_010 - Chen-Cheng cscK estimates

**Question:** Where does the corpus discuss Chen-Cheng's reduction of cscK existence to geodesic stability or properness?

**Expected sources:** `1801.00656`, `1801.05907`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `geodesic stability`, `properness`, `cscK existence`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.765 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | line 212 | yes | yes | geodesic stability | This notion of geodesic stability is equivalent to existence of cscK: |
| 2 | 0.740 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | no | no | - | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |
| 3 | 0.697 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | yes | yes | geodesic stability, properness | ...potentials, concave with respect to this parameter. They proved that each analytic test configuration defines a unique geodesic ray (up to parallelism), thus defines a point at ${\mathcal S}_\infty.$ It is important to understand the converse: when does a locally finite energy geodesic ray define a test configuration? More importantly, can one extend the de... |
| 4 | 0.686 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Existence implies properness and geodesic stability > Geodesic stability | lines 4300-4303 | no | yes | geodesic stability | \subsection{Geodesic stability}\label{Geodesic stability} The geodesic stability conjecture for cscK metric was proposed in Donaldson \cite{MR1736211}, aiming to detecting the existence of cscK metrics by using the geodesic rays. |
| 5 | 0.677 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 138-162 | no | yes | geodesic stability, properness | \section{Introduction} %It is suggested by Chen \cite{MR3858468} that, the path of cscK metrics with cone singularities are expected to serve as a continuity method to find the cscK metric aiming to Yau-Tian-Donaldson conjecture, which coincides with Donaldson's continuity method in the K\"ahler-Einstein problem \cite{MR3264768,MR2975584}. In K\"ahler geomet... |
| 6 | 0.657 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | unsectioned | lines 114-137 | no | yes | geodesic stability, properness | \title[Existence, Properness and Geodesic stability]{Existence of constant scalar curvature K\"ahler cone metrics, properness and geodesic stability} \author{Kai Zheng} % \address{University of Warwick} \curraddr{Tongji University, Shanghai 200092, P.R. CHINA} \email[Kai Zheng]{kaizheng@amss.ac.cn} %\date{\today} \begin{document} \maketitle \begin{abstract}... |
| 7 | 0.514 | `corpus/arxiv/1810.04661/source/source.tex` | `text` | Introduction | lines 90-102 | no | yes | geodesic stability, properness | \section{Introduction} In this paper we prove the essentially optimal form of Donaldson's geodesic stability conjecture \cite{Do99}. The main result is obtained via a detailed analysis of the rays associated to the space of K\"ahler metrics. Suppose $(X,\omega)$ is a compact K\"ahler manifold with $\dim X =n$. We consider $\mathcal H$, the space of K\"ahler... |
| 8 | 0.617 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | yes | yes | - | It is an interesting question to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except i... |
| 9 | 0.492 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | yes | yes | geodesic stability | An intriguing question motivated from above remark is whether geodesic stability in $\mathcal{E}_0^{\infty}$ (in the sense defined in the above remark) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail i... |
| 10 | 0.569 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 346-353 | yes | yes | geodesic stability | It is not immediately clear if filtrated stability alone will be sufficient to imply the existence of cscK metrics. More broadly, there are some intriguing questions which might link a stability notion in the algebraic sense to some analytical or geometric stability. With Theorem \ref{t1.8new} in mind, one wonders if we can replace the $L^1$ stability condit... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### chen_cheng_csck_011 - Chen-Cheng cscK estimates

**Question:** Where does the corpus discuss K-energy minimizers and Chen-Cheng regularity?

**Expected sources:** `1801.00656`, `1602.03114`
**Expected chunk types:** `theorem`, `proof`, `text`
**Expected terms:** `K-energy minimizers`, `regularity`, `Chen-Cheng`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.815 | `corpus/arxiv/1510.01260/source/source.tex` | `text` | Extension of the twisted K-energy > Uniqueness of twisted K-energy minimizers | lines 1009-1010 | no | yes | - | %As a strategy to find minimizers of the K-energy, one may consider finding minimizers of the twisted K-energy first and then consider the limit as the twisting form goes to zero. This was put forward in recent works \cite{c4,cpz}, in case of smooth minimizers, and below we provide a partial weak analog of one of their results: |
| 2 | 0.678 | `corpus/arxiv/1602.03114/source/source.tex` | `conjecture` | Introduction and main results | lines 147-148 | yes | no | - | \begin{conjecture}[Conjecture 2.9 in \cite{DR17}] \label{conj: DRconj} Suppose $(X,\omega)$ is a compact K\"ahler manifold. The minimizers of the extended K-energy $\Kenergy: \mathcal E^1 \to (-\infty,+\infty]$ are smooth csck metrics. \end{conjecture} |
| 3 | 0.677 | `corpus/arxiv/2104.09709/source/source.tex` | `text` | Regularity of the weak minimizers of the weighted Mabuchi energy | lines 1418-1419 | no | yes | regularity | \section{Regularity of the weak minimizers of the weighted Mabuchi energy}\label{s:regularity} In this section, we establish the regularity of the weak minimizers of $\cE_{v,w}$. |
| 4 | 0.618 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | regularity | ...predict that existence of canonical K\"ahler metrics should be equivalent to various notions of properness of Mabuchi's K-energy functional. In some instances this has been verified, especially under restrictive assumptions on the automorphism group. We provide counterexamples to the original conjecture in the presence of continuous automorphisms. The constr... |
| 5 | 0.531 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 220-223 | no | yes | Chen-Cheng | ...priori estimates for \eqref{2nd pde} in both the cscK cone problem and the degenerate cases. The a priori estimates of Chen-Cheng rely on fixed smooth K\"ahler metric. In the conical setting, their a priori estimates can not be applied directly, since the a priori estimates are required to be obtained with respect to a K\"ahler cone metric. The K\"ahler con... |
| 6 | 0.516 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Background materials > $d_{1}$-distances, reduced $d_{1}$-distances and the reduced J-functionals | lines 626-627 | no | yes | Chen-Cheng | By using the theory of Chen-Cheng and He \cite{CC17}, \cite{CC18a}, \cite{CC18b}, \cite{He18}, and the arguments in \cite{Li19}, we shall show the following theorem. |
| 7 | 0.471 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 409-415 | no | yes | Chen-Cheng | ...result was known by combining the works of Zhou-Zhu \cite{ZZ08}, Chen-Li-Sheng \cite{CLS14}, Hisamoto \cite{His16b} and Chen-Cheng \cite{CC18a, CC18b}. This previous proof depends on Donaldson's deep analysis of K\"{a}hler geometry on toric manifolds (\cite{Don02}). On the other hand, the proof given combines our analysis with the fundamental works on non-Ar... |
| 8 | 0.468 | `corpus/arxiv/1712.06697/source/source.tex` | `remark` | Introduction | lines 266-269 | no | no | - | \begin{rem} In Theorem \ref{t1.1} and the first part of Theorem \ref{t1.2}, it is sufficient to assume that $\varphi$ remains bounded under $L^1$ geodesic distance, due to the fact that cscK metrics are minimizers of $K$-energy. We will discuss this matter in more detail in our next paper of the series. \end{rem} |
| 9 | 0.455 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | yes | yes | - | ...rk) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail in our next paper and refer interested readers to the following works and references therein: |
| 10 | 0.444 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | unsectioned | lines 596-634 | no | yes | Chen-Cheng | ...eighted cscK metrics when the weighted Mabuchi functional is coercive for an extremal weight. This extends the works of Chen-Cheng and He to the singular weighted setting. Moreover, we provide a method for constructing examples of singular cscK metrics inspired by the work of Arezzo--Pacard. In contrast to the usual gluing techniques, our approach does not r... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### chen_cheng_csck_012 - Chen-Cheng cscK estimates

**Question:** Where does the corpus discuss scalar curvature bounds in Chen-Cheng theory?

**Expected sources:** `1712.06697`, `1801.00656`
**Expected chunk types:** `lemma`, `proposition`, `proof`
**Expected terms:** `scalar curvature bounds`, `Chen-Cheng`, `estimate`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.613 | `corpus/arxiv/2104.09709/source/source.tex` | `text` | Introduction | lines 234-236 | no | no | - | \section*{Introduction} This paper is concerned with the existence and obstruction theory of a class of special K\"ahler metrics, called \emph{weighted constant scalar curvature metrics}, which were introduced by the third named author in \cite{lahdili2}, giving a vast extension of the notion of K\"ahler metrics of constant scalar curvature (cscK for short),... |
| 2 | 0.584 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Background materials > $d_{1}$-distances, reduced $d_{1}$-distances and the reduced J-functionals | lines 626-627 | no | no | Chen-Cheng | By using the theory of Chen-Cheng and He \cite{CC17}, \cite{CC18a}, \cite{CC18b}, \cite{He18}, and the arguments in \cite{Li19}, we shall show the following theorem. |
| 3 | 0.578 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | unsectioned | lines 114-137 | no | no | Chen-Cheng | \title[Existence, Properness and Geodesic stability]{Existence of constant scalar curvature K\"ahler cone metrics, properness and geodesic stability} \author{Kai Zheng} % \address{University of Warwick} \curraddr{Tongji University, Shanghai 200092, P.R. CHINA} \email[Kai Zheng]{kaizheng@amss.ac.cn} %\date{\today} \begin{document} \maketitle \begin{abstract}... |
| 4 | 0.500 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction | lines 191-199 | no | no | Chen-Cheng, estimate | ...central theme in K\"ahler geometry is the search for canonical K\"ahler metrics. The concept of \emph{constant weighted scalar curvature K\"ahler metrics} (weighted cscK for short), introduced by the third author in \cite{Lah19}, provides a unification of various related notions of canonical K\"ahler metrics that satisfy special curvature conditions. We pres... |
| 5 | 0.496 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 225-232 | no | no | Chen-Cheng | ...an-Donaldson (YTD) conjecture aims to give a sufficient and necessary algebraic condition for the existence of constant scalar curvature K\"{a}hler (cscK) metric in the K\"{a}hler class $[\omega]$. Recently there have been significant progresses towards this conjecture, especially on the analytic part (see \cite{BDL17, BDL18, CC17,CC18a,CC18b, DL19}) and the... |
| 6 | 0.492 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | unsectioned | lines 596-634 | no | no | Chen-Cheng, estimate | ...terminal singularities, A priori estimates} \begin{document} \maketitle \begin{abstract} We study the weighted constant scalar curvature K\"ahler equations on mildly singular K\"ahler varieties. Assuming the existence of a suitable resolution of singularities, we establish the existence of singular weighted cscK metrics when the weighted Mabuchi functional i... |
| 7 | 0.448 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Conjectural picture | lines 686-688 | no | no | - | where $S$ is the scalar curvature, $\hat{S}$ is the average value of the scalar curvature and $H$ is the Hamiltonian of the circle action. The key point is that in fact the Futaki invariant does not depend on the choice of metric, in a fixed K\"ahler class. There are other definitions which generalise to singular spaces and schemes. What is visible from the... |
| 8 | 0.442 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted cscK problem on semisimple principal fibration | lines 2104-2110 | no | no | - | ...{question: if $\omega$ $T$-invariant, then what $\tilde{\omega}$ $T$-invariant?} %\textcolor{magenta}{Yes its true. Its discuss in \cite[(24) + below]{AJL}} \smallskip We recall the following fundamental formula for the scalar curvature of a compatible Kähler metric (see \cite[Lemma 5.8]{AJL}): |
| 9 | 0.439 | `corpus/arxiv/1512.06391/source/source.tex` | `text` | A Futaki invariant > The Futaki invariant for a K\"ahler class | lines 351-355 | no | no | - | ...tric ${\tilde g}_{\omega}(X,Y) = \frac{1}{f_{K, \omega, a}^2} \omega(X, JY)$ is Einstein--Maxwell? \end{problem} By the discussion in the previous section, we are looking for metrics $\omega \in \mathcal{K}_{\Omega}^G$ such that the corresponding scalar curvature of $\tilde g$ |
| 10 | 0.425 | `corpus/arxiv/1712.06697/source/source.tex` | `text` | Introduction | lines 187-196 | yes | no | estimate | One conspicuous and memorable feature of CDS's proof is the heavy use of Cheeger-Colding theory on manifold with Ricci curvature bounded from below. The apriori bound on Ricci curvature for KE metrics make such an application of Cheeger Colding theory seamlessly smooth and effective. However, if we want to attack this general conjecture, there will be a daun... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### chen_cheng_csck_013 - Chen-Cheng cscK estimates

**Question:** Where does the corpus discuss properness modulo automorphisms for cscK metrics?

**Expected sources:** `1506.07129`, `1801.00656`, `1801.05907`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `properness modulo automorphisms`, `cscK`, `K-energy`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.668 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 179-182 | no | yes | cscK | We will prove that the existence of cscK cone metrics in terms of the properness of the log $K$-energy. |
| 2 | 0.602 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | yes | yes | K-energy | ...\def\bla{BLA BLA BLA BLA} \def\sp{$\spadesuit$} % Yanir's comments \def\cs{$\clubsuit$} % Tamas' comments \title{Tian's properness conjectures and Finsler geometry of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{document}... |
| 3 | 0.556 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | yes | yes | cscK | ...ction defined on the sphere of infinity ${\mathcal S}_\infty.$ One important technical ingredient to prove existence of cscK from geodesic stability is the following properness theorem, which says that if $K$-energy is ``proper" with respect to a suitably defined distance (defined precisely in Definition \ref{d1.1} below), then cscK exists. To extend the pro... |
| 4 | 0.657 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | no | no | cscK | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |
| 5 | 0.434 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | \label{sec:Introduction}Introduction > Statement of the main results | lines 310-335 | no | yes | - | ...}. In the case of smooth geodesics it is well-known that the Mabuchi functional $\mathcal{M}$ is \emph{strictly }convex modulo automorphisms, or more precisely modulo the group $\mbox{Aut}_{0}(X)$ defined as the connected component of the identity in the group of all biholomorphisms of $X.$ If one could establish the corresponding strict convexity for \emph{... |
| 6 | 0.429 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | cscK | ...phic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enumerate} \bibliographystyle{amsplain} \bibliography{RepDefAbelia... |
| 7 | 0.424 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Introduction | lines 106-118 | no | yes | cscK | ...ntroduction} Bando-Mabuchi \cite{BM} proved that K\"ahler-Einstein metric on Fano manifolds is unique up to holomorphic automorphisms in 1980s. Recently, Berndtsson \cite{Bo} generalized this uniqueness result to conic K\"ahler-Einstein metrics on Fano manifolds, by his observation on the convexity of certain energy functional (the $Ding$-functional) along g... |
| 8 | 0.415 | `corpus/arxiv/1712.06697/source/source.tex` | `text` | Introduction | lines 156-166 | no | yes | cscK | ...ction{Introduction} This is the first of a series of three papers in the study of of constant scalar curvature K\"ahler metrics (cscK metrics), following a program outlined in \cite{chen15}. In this paper, we focus on establishing a priori estimates for cscK metrics in compact K\"ahler manifold without boundary. Our estimates can be easily adapted to extrema... |
| 9 | 0.392 | `corpus/arxiv/1808.07811/source/source.tex` | `theorem` | A variational setting > The $(\uu,\vv)$-Mabuchi energy | lines 757-759 | no | yes | cscK | \begin{cor} If $(X,\T)$ is a compact toric K\"ahler manifold, then the $(\uu,\vv)$-cscK metrics with $\uu\in C^\infty(\PP,\R_{>0})$, $\vv\in C^\infty(\PP,\R)$, are unique modulo ${\rm Aut}_{\rm red}^{\T}(X)$ the $\T$-equivariant automorphisms of $X$. \end{cor} |
| 10 | 0.382 | `corpus/arxiv/1602.03114/source/source.tex` | `text` | Introduction and main results | lines 111-126 | no | yes | cscK, K-energy | ...f Hodge theory, up to a constant, this space is in a one-to-one correspondence with $\mathcal H$, the space of K\"ahler metrics cohomologous to $\omega$. The problem of finding canonical metrics in $\mathcal H$ goes back to Calabi in 50's. In this work we will point necessary conditions under which $\mathcal H$ admits constant scalar curvature K\"ahler (csck... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### chen_cheng_csck_014 - Chen-Cheng cscK estimates

**Question:** Where does the corpus discuss cscK estimates in relation to the Calabi functional?

**Expected sources:** `1712.06697`, `math_0412518`, `1801.00656`
**Expected chunk types:** `theorem`, `proposition`, `text`
**Expected terms:** `Calabi functional`, `cscK estimates`, `scalar curvature`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.776 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | K-stability of twisted cscK metrics > Lower bounds on the twisted Calabi functional | lines 292-294 | no | yes | Calabi functional | Our strategy to prove Theorem \ref{stabilityofcscK} is to first prove the following lower bound on the twisted Calabi functional, which is the twisted analogue of \cite[Theorem 2]{D2}. |
| 2 | 0.610 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 273-284 | yes | yes | scalar curvature | ...ics. More broadly, it is interesting to estimate the upper and lower bound of this invariant. It is not hard to see the relation between the invariant introduced in \cite{Sz11} and the invariant introduced above when restricted to the canonical K\"ahler class in Fano manifold, where we take $[\chi]$ to be the first Chern class in (\ref{1.1nn}) above. Hopeful... |
| 3 | 0.598 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 220-223 | no | yes | - | In Section \ref{a priori estimates}, we establish a priori estimates for \eqref{2nd pde} in both the cscK cone problem and the degenerate cases. The a priori estimates of Chen-Cheng rely on fixed smooth K\"ahler metric. In the conical setting, their a priori estimates can not be applied directly, since the a priori estimates are required to be obtained with... |
| 4 | 0.575 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | unsectioned | lines 162-212 | no | yes | Calabi functional, scalar curvature | ...veloped by Donaldson. In~\cite{Don02} he showed that in the case of toric surfaces K-stability implies that the Mabuchi functional is bounded from below (this was later extended by Zhou-Zhu~\cite{ZZ06} to show properness of the Mabuchi functional) and a minimising sequence has a subsequence that converges in a weak sense. In~\cite{Don05_1} Donaldson proved i... |
| 5 | 0.564 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | yes | - | ...ction defined on the sphere of infinity ${\mathcal S}_\infty.$ One important technical ingredient to prove existence of cscK from geodesic stability is the following properness theorem, which says that if $K$-energy is ``proper" with respect to a suitably defined distance (defined precisely in Definition \ref{d1.1} below), then cscK exists. To extend the pro... |
| 6 | 0.555 | `corpus/arxiv/1712.06697/source/source.tex` | `text` | Introduction | lines 156-166 | yes | yes | scalar curvature | ...roduction} This is the first of a series of three papers in the study of of constant scalar curvature K\"ahler metrics (cscK metrics), following a program outlined in \cite{chen15}. In this paper, we focus on establishing a priori estimates for cscK metrics in compact K\"ahler manifold without boundary. Our estimates can be easily adapted to extremal K\"ahle... |
| 7 | 0.547 | `corpus/arxiv/1004.2012/source/Kempf_Ness_uniqueness_12272011.tex` | `text` | Stability of the Calabi flow | lines 1059-1074 | no | yes | - | The Calabi flow equation in the form (\ref{Calabi flow H}) was first proposed by E. Calabi(\cite{Ca1}, \cite{Ca2}) to find extremal metrics in a fixed K\"ahler class. The short time existence was established by Chen-He(\cite{CH1}). They also proved the global existence assuming Ricci curvature bound. \\ The equation (\ref{Calabi flow J}) also has its own adv... |
| 8 | 0.547 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Background on cscK metrics and their moduli > Extremal K\"ahler metrics | lines 312-314 | no | yes | Calabi functional, scalar curvature | \subsection{Extremal K\"ahler metrics} \label{sec:extremal} Extremal K\"ahler metrics were introduced by Calabi \cite{Calabi} and provide canonical representatives of K\"ahler classes. They are defined as the critical points of the so-called Calabi functional, that assigns to each K\"ahler metric in $\Omega$ the $L^2$-norm of its scalar curvature. They inclu... |
| 9 | 0.541 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 717-744 | no | yes | - | The strategy for proving Theorem~\ref{bigthm_existence_0} is to establish uniform a priori estimates for the solutions to a family of {weighted} cscK equations on the resolution of singularities $\pi: Y \to X$. Denote by $E$ the exceptional set of $\pi$. Consider a family of perturbed K\"ahler metrics $\om_\vep := \pi^\ast \om + \vep \om_Y$ on the resolution... |
| 10 | 0.531 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Linear analysis | lines 1203-1232 | no | yes | - | ...linear elliptic theory needed to handle the existence, deformation and regularity theory for canonical edge metrics. We discuss this from two points of view, reviewing the estimates obtained by Donaldson in the wedge H\"older spaces, and also describing how to obtain analogous estimates in the edge H\"older spaces. These latter estimates are obtained through... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### chen_cheng_csck_015 - Chen-Cheng cscK estimates

**Question:** Where does the corpus discuss Chen-Cheng estimates as an ingredient in later weighted or conic cscK work?

**Expected sources:** `1712.06697`, `1801.00656`, `2407.09929`, `1803.09506`
**Expected chunk types:** `theorem`, `text`, `citation_context`
**Expected terms:** `Chen-Cheng`, `weighted cscK`, `conic cscK`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.752 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 220-223 | yes | yes | Chen-Cheng | In Section \ref{a priori estimates}, we establish a priori estimates for \eqref{2nd pde} in both the cscK cone problem and the degenerate cases. The a priori estimates of Chen-Cheng rely on fixed smooth K\"ahler metric. In the conical setting, their a priori estimates can not be applied directly, since the a priori estimates are required to be obtained with... |
| 2 | 0.660 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction > Main results and strategy of the proof | lines 252-257 | yes | yes | Chen-Cheng, weighted cscK | \subsection{Main results and strategy of the proof} %The goal of this paper is to derive $C^{2}$ a priori estimates for K\"ahler potentials $\varphi \in \mathcal{K}(X,\omega_0)^\T$ corresponding to weighted cscK metrics, generalizing Chen-Cheng estimates in the classical cscK case. The starting point is to re-write the $4$th order non-linear PDE in \eqref{wc... |
| 3 | 0.570 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | unsectioned | lines 596-634 | no | yes | Chen-Cheng, weighted cscK | ...m@th{#1\rangle}\)}% \mathclose{\copy\@brx\kern-0.5\wd\@brx\usebox{\@brx}}} \makeatother \setcounter{tocdepth}{1} \title{Weighted cscK metrics on K\"ahler varieties} \author{Chung-Ming Pan} \address[Chung-Ming Pan]{Centre interuniversitaire de recherches en g\'eom\'etrie et topologie (CIRGET); Universit\'e du Qu\'ebec \`a Montr\'eal; Case postale 8888, Succur... |
| 4 | 0.698 | `corpus/arxiv/1803.09506/source/source.tex` | `remark` | Introduction | lines 245-247 | yes | no | - | \begin{rem} These estimates are also obtained for cscK cone metric by directly making use of the conical background metric as shown in \cite{arXiv:1805.04944}, which are considered to be the limit of \thmref{A priori estimates}. \end{rem} |
| 5 | 0.555 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Introduction | lines 106-118 | no | yes | conic cscK | ...s unique up to holomorphic automorphisms in 1980s. Recently, Berndtsson \cite{Bo} generalized this uniqueness result to conic K\"ahler-Einstein metrics on Fano manifolds, by his observation on the convexity of certain energy functional (the $Ding$-functional) along geodesics in the space of all K\"ahler potentials. And Berndtsson's method is further generali... |
| 6 | 0.668 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 186-204 | yes | yes | Chen-Cheng | ...atements are given in \thmref{properclosedness}, \thmref{Properness implies existence general}. The proof relies on two ingredients. One is the approximation scheme of the log $K$-energy, which leads to the construction of approximate twisted cscK metrics. Then we will show that this approximate sequence converges to a cscK cone metric by applying the a prio... |
| 7 | 0.513 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | yes | - | ...an view $\yen$ invariant as a function defined on the sphere of infinity ${\mathcal S}_\infty.$ One important technical ingredient to prove existence of cscK from geodesic stability is the following properness theorem, which says that if $K$-energy is ``proper" with respect to a suitably defined distance (defined precisely in Definition \ref{d1.1} below), th... |
| 8 | 0.628 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction | lines 191-199 | yes | yes | Chen-Cheng, weighted cscK | ...ntro}} A central theme in K\"ahler geometry is the search for canonical K\"ahler metrics. The concept of \emph{constant weighted scalar curvature K\"ahler metrics} (weighted cscK for short), introduced by the third author in \cite{Lah19}, provides a unification of various related notions of canonical K\"ahler metrics that satisfy special curvature conditions... |
| 9 | 0.499 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Linear analysis | lines 1203-1232 | no | yes | - | ...linear elliptic theory needed to handle the existence, deformation and regularity theory for canonical edge metrics. We discuss this from two points of view, reviewing the estimates obtained by Donaldson in the wedge H\"older spaces, and also describing how to obtain analogous estimates in the edge H\"older spaces. These latter estimates are obtained through... |
| 10 | 0.613 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 138-162 | yes | yes | Chen-Cheng | \section{Introduction} %It is suggested by Chen \cite{MR3858468} that, the path of cscK metrics with cone singularities are expected to serve as a continuity method to find the cscK metric aiming to Yau-Tian-Donaldson conjecture, which coincides with Donaldson's continuity method in the K\"ahler-Einstein problem \cite{MR3264768,MR2975584}. In K\"ahler geomet... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### my_notes_cp1_001 - my_notes CP1 cone-to-cusp examples

**Question:** Where do my notes discuss CP1 with moment polytope [-1,1] and one conic point?

**Expected sources:** `corpus/my_notes/toric_manifolds_mixed_conic_cusp/notes/one_conic_point.tex`
**Expected chunk types:** `example`, `definition`, `text`
**Expected terms:** `CP1`, `[-1,1]`, `conic point`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.214 | `corpus/my_notes/toric_manifolds_mixed_conic_cusp/notes/one_conic_point.tex` | `text` | \(\mathbb{CP}^1\) with one conic point: symplectic picture > Setup | lines 9-15 | yes | yes | [-1,1] | \subsection*{Setup} Let \(T=S^1\) act on \(\mathbb{CP}^1\), fixing the two poles. The moment polytope is \[ P=[-1,1]. \] We consider a metric with cone angle \(2\pi\beta\) at \(x=-1\), and smooth behavior at \(x=1\). |
| 2 | 0.752 | `corpus/arxiv/dg-ga_9711014/paper.pdf` | `text` | unsectioned | p. 3 | no | yes | - | a suitable power of the K¨ ahler class. Calabi’s family of ext remal metrics on CP 2♯CP 2 is discussed in §6. Acknowledgements: This work was carried out while I was a postdoctoral member of the School of Mathematics of the Institute for Adva nced Study. I take this opportunity to thank the staﬀ and faculty of the Ins titute for providing a wonderful environ... |
| 3 | 0.870 | `corpus/my_notes/toric_manifolds_mixed_conic_cusp/notes/one_conic_point.tex` | `text` | \(\mathbb{CP}^1\) with one conic point: symplectic picture | lines 7-8 | yes | yes | conic point | \section*{\(\mathbb{CP}^1\) with one conic point: symplectic picture} |
| 4 | 0.685 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `theorem` | Constant scalar curvature case and interpretation in term of metric with cone angle singularity > Log K--stability of labelled polytopes and cscK metric with cone angle singularity | lines 687-689 | no | no | - | % \begin{theorem}[\cite{zz}] % Let $(P,\lab)$ be a labelled polytope such that there exists a solution $\pot \in \mS(P,\lab)$ to the equation \eqref{eq:extCDT} with $\exv_{(P,\lab)}$ constant. Then $(P,\lab)$ is {\it K--stable}. In particular, if $(M,\omega,T)$ is a toric compact manifold with moment polytope $P$ which admits a compatible $T$--invariant cscK... |
| 5 | 0.549 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | ...foldable fans in higher dimension to be fans whose lattice automorphism group admit a subgroup that acts with no fixed point. This raises several questions : \begin{enumerate} \item Do all crystallographic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric... |
| 6 | 0.532 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} | lines 2640-2648 | no | yes | - | ...endixB} For the proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} we will change point of view slightly and use explicit computations for quadrilaterals in $\mathbb{R}^2$ with the standard lattice $\mathbb{Z}^2$. The moment polytope corresponding to a Hirzebruch surface has at least one pair of parallel edges. Therefore... |
| 7 | 0.644 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `proposition` | Constant scalar curvature case and interpretation in term of metric with cone angle singularity > The normal and the angle | lines 617-619 | no | no | - | ...egin{proposition} \label{propCONEangleMETRIC} % Let $(M,\omega,T)$ be a toric compact symplectic manifold with labelled moment polytope $(P,\labb,\Lambda)$ and momentum map $x: M\ra \kt^*$. For any labelling $\lab$ of $P$, any potential $\pot\in\mS(P,\lab)$ provides a K\"ahler metric $g_\pot$, defined via~\eqref{ActionAnglemetric}, smooth and compatible with... |
| 8 | 0.643 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `proposition` | Miscellaneous > The normal and the angle | lines 543-545 | no | no | - | ...\label{propCONEangleMETRIC} \cite{RKE_legendre} Let $(M,\omega,T)$ be a toric compact symplectic manifold with labelled moment polytope $(P,\labb,\Lambda)$ and momentum map $x: M\ra \kt^*$. For any labelling $\lab$ of $P$, any potential $\pot\in\mS(P,\lab)$ provides a K\"ahler metric $g_\pot$, defined via~\eqref{ActionAnglemetric}, smooth and compatible with... |
| 9 | 0.503 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | unsectioned | lines 162-212 | no | yes | - | ...04} (see also Mabuchi~\cite{Mab04_1} for a different definition). Given the interpretation of the scalar curvature as a moment map, what one needs to do is to find a stability criterion satisfied by the orbit of a critical point of the norm squared of the moment map in general. The norm squared of the moment map was studied by Kirwan~\cite{Kir84}, but not ex... |
| 10 | 0.494 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction > Openness of coercivity | lines 690-697 | no | yes | - | Combining Theorem \ref{thm:coeropen} with Zheng's characterization \cite[Theorem 1.2]{Zheng20} of the existence of cscK cone metrics in terms of coercivity, we obtain the following existence results. We note that while Theorem \ref{thm:coeropen} applies to simple normal crossing divisors, the following corollaries are restricted to smooth divisors and the un... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### my_notes_cp1_002 - my_notes CP1 cone-to-cusp examples

**Question:** Where do my notes discuss CP1 or a moment interval with one cusp point?

**Expected sources:** `corpus/my_notes/toric_manifolds_mixed_conic_cusp/notes/one_cusp_point.tex`
**Expected chunk types:** `example`, `definition`, `text`
**Expected terms:** `CP1`, `cusp point`, `moment interval`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: no
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.942 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} | lines 2640-2648 | no | yes | - | ...endixB} For the proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} we will change point of view slightly and use explicit computations for quadrilaterals in $\mathbb{R}^2$ with the standard lattice $\mathbb{Z}^2$. The moment polytope corresponding to a Hirzebruch surface has at least one pair of parallel edges. Therefore... |
| 2 | 0.752 | `corpus/arxiv/dg-ga_9711014/paper.pdf` | `text` | unsectioned | p. 3 | no | yes | - | a suitable power of the K¨ ahler class. Calabi’s family of ext remal metrics on CP 2♯CP 2 is discussed in §6. Acknowledgements: This work was carried out while I was a postdoctoral member of the School of Mathematics of the Institute for Adva nced Study. I take this opportunity to thank the staﬀ and faculty of the Ins titute for providing a wonderful environ... |
| 3 | 0.706 | `corpus/arxiv/2405.11952/source/main.tex` | `text` | Momentum construction of scalar-flat K\"ahler metric | lines 157-160 | no | yes | - | \section{Momentum construction of scalar-flat K\"ahler metric}\label{section 2} In this section, we discuss how the momentum construction in \cite{HS02} gives rise to the cuspidal SFK metric on the punctured line bundle $\mathcal{O}(-1)^*$ appeared in the introduction. Let $p: (L, h)\rightarrow (M^m,\omega_M)$ be an Hermitian holomorphic line bundle with cur... |
| 4 | 0.695 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | unsectioned | lines 162-212 | no | yes | - | ...04} (see also Mabuchi~\cite{Mab04_1} for a different definition). Given the interpretation of the scalar curvature as a moment map, what one needs to do is to find a stability criterion satisfied by the orbit of a critical point of the norm squared of the moment map in general. The norm squared of the moment map was studied by Kirwan~\cite{Kir84}, but not ex... |
| 5 | 0.691 | `corpus/arxiv/1801.05907/source/source.tex` | `question` | Introduction | lines 261-263 | no | no | - | \begin{q} How do we characterize the set of $\psi\in L^p(M,\omega)$ ($p\geq1$) which is the initial velocity of a locally finite energy geodesic ray with unit speed? Or more importantly, is the set of velocities (which give rise to a locally finite geodesic ray) a convex subset of $L^p(M, \omega)? $ \end{q} |
| 6 | 0.681 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | ...foldable fans in higher dimension to be fans whose lattice automorphism group admit a subgroup that acts with no fixed point. This raises several questions : \begin{enumerate} \item Do all crystallographic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric... |
| 7 | 0.665 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | ....7, can we extend it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic topology, how far is the class of Calabi dream manifolds from the class of all smooth minimal models of general type? %\item Motived by Conjecture 1 in \cite{LeSz13}, we may ask whether a K\"ahler manifold with $... |
| 8 | 0.785 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Explicit Donaldson metrics on quadrilaterals > Toric products | lines 1440-1450 | no | yes | - | ...lzant polytopes are parallelograms, namely $X= \C P^1 \times \C P^1$. The result above trivially produces products of a cusp metric on $\C P^1\setminus \{{\rm pt} \}$ with a Fubini-Study metric on another copy of $\C P^1$, or the product of two cusp metrics on $(\C P^1\setminus \{{\rm pt} \}) \times (\C P^1\setminus \{{\rm pt} \})$, according to whether $Z \... |
| 9 | 0.582 | `corpus/arxiv/1512.06391/source/source.tex` | `text` | Further observations > Uniqueness in a given conformal class | lines 1057-1066 | no | yes | - | %\subsection{Uniqueness in a given conformal class} Einstein--Maxwell metrics in the conformal class of a given K\"ahler metric $g$ on $(M,J)$ are solutions to the Yamabe problem. It is therefore natural ask whether the Einstein--Maxwell condition would imply uniqueness of the metric in the given conformal class? %In the case when $(g, \omega)$ is a K\"ahler... |
| 10 | 0.561 | `corpus/arxiv/math_0401320/source/hfkg2.tex` | `example` | Hamiltonian actions and toric geometry > Restricted toric manifolds | lines 947-984 | no | yes | - | ...`tame' $S^1$ subgroups generated by the normals are given by $\lambda_1=0$, $\lambda_2=0$ or $\lambda_1=\lambda_2$. The momentum map of the $S^1$ action is then the projection of the momentum map of $\T$ along the corresponding face of the Delzant polytope $\Delta$ (which is a simplex). The momentum map of `wild' $S^1$ subgroups, such as $\lambda_1=\lambda^2... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### my_notes_cp1_003 - my_notes CP1 cone-to-cusp examples

**Question:** Where do my notes discuss cone angle beta and the Guillemin boundary term?

**Expected sources:** `corpus/my_notes/toric_manifolds_mixed_conic_cusp/notes/one_conic_point.tex`, `corpus/my_notes/toric_manifolds_mixed_conic_cusp/tables/notation_table.tex`
**Expected chunk types:** `definition`, `example`, `text`
**Expected terms:** `cone angle beta`, `Guillemin`, `boundary term`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.203 | `corpus/my_notes/toric_manifolds_mixed_conic_cusp/notes/one_conic_point.tex` | `text` | \(\mathbb{CP}^1\) with one conic point: symplectic picture > Conic Guillemin condition | lines 16-23 | yes | yes | Guillemin | \subsection*{Conic Guillemin condition} A symplectic potential has the form \[ u(x)=\frac{1}{2\beta}(1+x)\log(1+x)+\frac12(1-x)\log(1-x)+h(x), \qquad h\in C^\infty. \] The logarithmic terms describe the boundary behavior, and the coefficient \(\beta^{-1}\) encodes the cone angle \(2\pi\beta\). |
| 2 | 0.964 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `text` | Momentum-constructed cscK metrics with cone singularities along a divisor > Proof of Theorem \ref{mainthmmc} > Construction of conically singular cscK metrics on $\mathbb{X}= \prj (\mathcal{F} \oplus \cx)$ | lines 1215-1217 | no | yes | - | with some constant $\sigma'_0$, for a profile $\varphi$ that is strictly positive on the interior $(-b,b)$ of $I$ with boundary conditions $\varphi (b) = \varphi (-b) =0$ and $\varphi' (-b)=-2$. The value $\varphi' (b)$ has more to do with the cone singularities of the metric $\omega_{\varphi}$, and we shall see at the end that the metric $\omega_{\varphi}$... |
| 3 | 0.842 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Constant scalar curvature K\"ahler cone metrics > Geodesics in the space of K\"ahler cone metrics | lines 427-428 | no | yes | - | \subsection{Geodesics in the space of K\"ahler cone metrics}\label{Cone geodesics} The $L^2$ metric is extended in the space $\mathcal H_\beta$. It is shown in \cite{MR3405866} that the geodesic equation is a degenerate complex Monge-Amp\`ere equation with cone singularities in the product manifold $\mathfrak X=X\times [0,1]\times S^1$. The existence, unique... |
| 4 | 0.839 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Conjectural picture | line 690 | no | yes | - | This definition can be motivated, in the framework of metrics with cone singularity along $\Delta$, by adding a suitable distributional term to the scalar curvature, in the manner of (27) and substituting into (29). Under plausible assumptions about the behaviour around the singular set, the definition implies that if there is an invariant constant scalar cu... |
| 5 | 0.831 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction > Openness of coercivity | lines 698-700 | no | no | - | ...smooth divisor and assume that $X$ admits no nonzero holomorphic vector field preserving $D$. If $[\om]$ admits a cscK cone metric with cone angle $\alpha_0 \in (0,1)$, then there exists a neighborhood $\mathcal{U}$ of $\alpha_0$ in $(0,1)$ such that $[\om]$ admits a cscK cone metric with cone angle $\alpha$ for any $\alpha \in \mathcal{U}$. \end{cor} |
| 6 | 0.740 | `corpus/arxiv/1205.0056/source/cone_metrics.tex` | `text` | Introduction | lines 599-606 | no | yes | - | In general the K\"ahler cone metrics do not have bounded geometry. The Riemannian curvature of $\om$ is bounded from below when when the cone angle is less than $\frac{1}{2}$. We will compute that the Levi-Civita connection of the model cone metric defined in \eqref{model cone} under the cone coordinate (see \eqref{conetransform}) is bounded when the cone an... |
| 7 | 0.815 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Openness of coercivity > Coercivity > Applications to conic and cusp singularities | lines 1829-1834 | no | yes | - | ...to two important geometric settings: perturbations from cusp singularities to conic singularities, and perturbations of cone angles for conic singularities. The following theorem shows that coercivity is an open condition with respect to the cone angle parameters. |
| 8 | 0.809 | `corpus/arxiv/1803.09506/source/source.tex` | `theorem` | Introduction | lines 183-185 | no | no | - | \begin{thm}[Log properness theorem]\label{cone properness conjecture} Assume that $\Om$ is a K\"ahler class and the cone angle satisfies $0<\beta\leq 1$. Then $\Om$ admits a constant scalar curvature K\"ahler cone metric with cone angle $\beta$ is equivalent to the properness of the log $K$-energy. \end{thm} |
| 9 | 0.802 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `conjecture` | Log Futaki invariant and log $K$-stability > Log $K$-stability | lines 725-727 | no | no | - | \begin{conjecture} \label{logdtyconj} $((X,D);L)$ is log $K$-polystable with cone angle $2 \pi \beta$ if and only if $X$ admits a cscK metric in $c_1(L)$ with cone singularities along $D$ with cone angle $2 \pi \beta$. \end{conjecture} |
| 10 | 0.770 | `corpus/arxiv/1803.09506/source/source.tex` | `theorem` | Introduction | lines 312-315 | no | no | - | \begin{thm}[Openness theorem]\label{openess main} Assume that $Aut(X;D)$ is discrete and $C_1(L_D)> 0$. The cscK cone path is open when the cone angle $\beta>0$. \end{thm} |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### my_notes_cp1_004 - my_notes CP1 cone-to-cusp examples

**Question:** Where do my notes discuss Poincare cusp parameters alpha and beta?

**Expected sources:** `corpus/my_notes/toric_manifolds_mixed_conic_cusp/tables/notation_table.tex`
**Expected chunk types:** `definition`, `text`
**Expected terms:** `alpha`, `beta`, `Poincare cusp`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: no
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.127 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Openness of coercivity > Coercivity > Applications to conic and cusp singularities | lines 1829-1834 | no | yes | - | \subsubsection*{Applications to conic and cusp singularities} Having established the general openness result for coercivity under perturbations (Proposition \ref{prop:coercivity-weighted-twisted} and Proposition \ref{prop:cusp-to-conic}), we now apply it to two important geometric settings: perturbations from cusp singularities to conic singularities, and pe... |
| 2 | 0.834 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Explicit Donaldson metrics on quadrilaterals > Regular ambitoric structures | lines 1785-1786 | no | yes | - | The proofs of Proposition \ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} are presented in Appendix \ref{AppendixB}. |
| 3 | 0.813 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Convex Preliminaries > Polarized toric manifolds | lines 1349-1350 | no | yes | - | and $D_{j} \coloneqq \mu_{P}^{-1}(F_{j})$. By setting $c_{j}$ the Poincare dual of $D_{j}$, we have |
| 4 | 0.789 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Preliminaries > Quasi coordinates | line 300 | no | yes | - | We say that a holomorphic coordinate of $X$ is a cusp coordinate if in this coordinate we have $D=\{z_n=0\}$. Let us prove a lemma using the quasi coordinate. |
| 5 | 0.788 | `corpus/arxiv/2405.11952/source/main.tex` | `lemma` | Momentum construction of scalar-flat K\"ahler metric | lines 217-219 | no | no | - | \begin{lem} The metric $g_0$ on $\Delta^*(L)$ can be extended to a complete SFK metric on $L^*$, and near $\tau=0$, it's a finite-area cusp. \end{lem} |
| 6 | 0.770 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Preliminaries > {\kah} metrics of Poincar\'{e} type and the weighted {\hol} space | lines 199-201 | no | yes | - | \begin{equation} \varphi_{\delta}^{*} \omega_{cusp} = \frac{\sqrt{-1} d \zeta \wedge d \overline{\zeta}}{(1-\|\zeta\|^2 )^2}, \end{equation} |
| 7 | 0.896 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction > Openness of coercivity | lines 701-703 | no | yes | - | More significantly, our framework allows us to deduce existence of small-angle conic metrics from coercivity at the cusp (Poincar\'e) limit. |
| 8 | 0.715 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | Summary of the momentum construction | lines 3129-3133 | no | yes | - | We now show that in the case of a complete metric if the order of vanishing of the momentum profile is precisely 2, then the metric is asymptotically hyperbolic as in Definition~\ref{defn:cuspsing}. |
| 9 | 0.838 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `proof` | Appendix > The Log-Mabuchi energy of Poincar\'e type K\"ahler metrics > Potential space of Poincar\'e type K\"ahler metrics | lines 2216-2218 | no | no | - | \begin{proof} The variation formulas follow from the discussion in Section \ref{sec:weighted-energy} and Lemma \ref{lem:symmetry_E1_general}. The finiteness for $\tmom$ is established by the computations in the proof of Lemma \ref{lem:poincare-finite-volume}. \end{proof} |
| 10 | 0.780 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `lemma` | Appendix > The Log-Mabuchi energy of Poincar\'e type K\"ahler metrics > Potential space of Poincar\'e type K\"ahler metrics | lines 2007-2009 | no | no | - | \begin{lemma}\label{lem:poincare-finite-volume} The volume of any Poincar\'e type metric $\om_\f$ is finite. More precisely, the volume is the topological constant $[\om]^n$. \end{lemma} |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### my_notes_cp1_005 - my_notes CP1 cone-to-cusp examples

**Question:** Where do my notes give a dictionary between Kahler geometry and toric moment-polytope expressions?

**Expected sources:** `corpus/my_notes/toric_manifolds_mixed_conic_cusp/tables/kenergy_table.tex`
**Expected chunk types:** `definition`, `text`
**Expected terms:** `dictionary`, `Kahler`, `moment polytope`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.661 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | unsectioned | lines 146-172 | no | yes | - | ...is paper we investigate the existence of metrics with weighted constant scalar curvature (wcscK for short) on a compact Kähler manifold $X$: this notion include constant scalar curvature K\"ahler metrics, weighted solitons, Calabi’s extremal Kähler metrics and extremal metric on semisimple principal fibrations. We prove that the coercivity of the weighted Ma... |
| 2 | 0.636 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 3 | 0.633 | `corpus/arxiv/0805.0128/source/extremal2a.tex` | `theorem` | Introduction | lines 126-130 | no | no | Kahler | \begin{cor} If a polarised complex toric surface with zero Futaki invariant is K-stable it admits a constant scalar curvature Kahler metric. \end{cor} |
| 4 | 0.584 | `corpus/arxiv/1801.05907/source/source.tex` | `question` | Introduction | lines 261-263 | no | no | - | \begin{q} How do we characterize the set of $\psi\in L^p(M,\omega)$ ($p\geq1$) which is the initial velocity of a locally finite energy geodesic ray with unit speed? Or more importantly, is the set of velocities (which give rise to a locally finite geodesic ray) a convex subset of $L^p(M, \omega)? $ \end{q} |
| 5 | 0.558 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Proofs of Lemmas \ref{s1is2}, \ref{s1is1} and \ref{s1is2overk} | lines 1659-1726 | no | yes | - | .... London Math. Soc. {\bf 14} (1982), 1--15. \bibitem{ACG1} V. Apostolov, D.~M.~J. Calderbank and P. Gauduchon, {\it The geometry of weakly self-dual K\"ahler surfaces}, Compositio Math. {\bf 135} (2003), 279--322. \bibitem{ACG2} V. Apostolov, D.~M.~J. Calderbank and P. Gauduchon, {\it Hamiltonian $2$-forms in K\"ahler geometry} I {\it General Theory}, J. Dif... |
| 6 | 0.516 | `corpus/arxiv/2208.12493/source/toric-lecture-notes.tex` | `text` | Polarized projective toric varieties | line 734 | no | yes | - | From the considerations in Section~\ref{s:fan}, we get a correspondence between smooth toric projective varieties and complex toric varieties defined via the Delzant construction. It is however not entirely clear how this correspondence translates in terms of Delzant polytopes or, in other words, how to construct a polarized toric variety from a given Delzan... |
| 7 | 0.494 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Proof of Theorem \ref{suff} | lines 2778-2847 | no | yes | - | ...onvDF}. %\begin{acknowledgements} %\end{acknowledgements} \begin{thebibliography}{99} \bibitem{Ab03} M.~Abreu, K\"ahler geometry of toric manifolds in symplectic coordinates. \emph{Symplectic and contact topology: interactions and perspectives (Toronto, ON/Montreal, QC, 2001)}, 1--24, Fields Inst. Commun., \textbf{35}, \emph{Amer. Math. Soc., Providence, RI}... |
| 8 | 0.491 | `corpus/arxiv/math_0407486/source/intest2.tex` | `text` | Estimates for higher derivatives > Rescaling sections | lines 854-914 | no | yes | Kahler | \begin{thebibliography}{99} \bibitem{kn:Abr} M. Abreu {\em Kahler geometry of toric varieties and extremal metrics} Int. J. Math. {\bf 9} 641-651 1998 \bibitem{kn:An} M. T. Anderson {\em Orbifold compactness for spaces of Riemannian metrics and applications} Math. Annalen {\bf 331} 739-778 2005 \bibitem{kn:Caf} L.A. Caffarelli {\em Interior $W^{2}_{p}$ estim... |
| 9 | 0.478 | `corpus/arxiv/dg-ga_9711014/paper.pdf` | `text` | unsectioned | p. 2 | no | yes | - | ...such that the image of the cor- responding moment map φ is precisely ∆. The triple ( X∆,ω,φ ) is called a (symplectic) toric variety. It follows from the constructi on, due to Delzant [4], that X∆ comes also equipped with an intrinsic T n-invariant complex structure compatible with the intrinsic symplectic form. In other wor ds, X∆ has an in- trinsic “toric... |
| 10 | 0.477 | `corpus/arxiv/math_0401320/source/hfkg2.tex` | `text` | Rigid hamiltonian torus actions | lines 1113-1125 | no | yes | - | ...onian torus actions}\label{s:rigid} In this section, we introduce the notion of a {\it rigid hamiltonian torus action}. Toric K\"ahler manifolds automatically carry such an action: our goal is to extend some of the rigid properties of toric K\"ahler manifolds to rigid torus actions in general, and to classify them. In the first three subsections we study res... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### my_notes_cp1_006 - my_notes CP1 cone-to-cusp examples

**Question:** Where do my notes discuss the symplectic potential for a one-conic CP1 model?

**Expected sources:** `corpus/my_notes/toric_manifolds_mixed_conic_cusp/notes/one_conic_point.tex`
**Expected chunk types:** `example`, `definition`, `text`
**Expected terms:** `symplectic potential`, `one conic`, `CP1`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.920 | `corpus/arxiv/2108.12297/source/source.tex` | `remark` | Weighted toric K-stability > Complex and symplectic points of view | lines 1279-1281 | no | no | symplectic potential | \begin{remark} In the above Proposition and Definition, we use as a model metric the Guillemin K\"ahler metric $(g_0, J_0)$ \cite{VG}, given by $(\ref{metric-toric2})$ for the symplectic potential \[ u_0 := \frac{1}{2} \sum_{j=1}^d L_j \log L_j,\] where $L_j, j=1, \ldots, d$ are the affine-linear functions defining the polytope. This introduces a discrepancy... |
| 2 | 0.821 | `corpus/arxiv/1708.05253/source/source.tex` | `text` | Levi--K\"ahler reduction for products of spheres > Products of simplices and products of spheres | lines 1628-1630 | no | yes | symplectic potential | We now give a closed formula for the symplectic potential of $h_\Ll$. |
| 3 | 0.785 | `corpus/arxiv/2110.10386/source/source.tex` | `theorem` | Convex Preliminaries > Symplectic potentials | lines 1434-1437 | no | no | symplectic potential | \begin{theorem}[\cite{Ab03}, \cite{Apo19}, \cite{Don05}, \cite{G94b}]\label{GuiAb} Every $S$-invariant K\"ahler metric in the class $c_{1}(L_{P})$ has a symplectic potential $u$ in $\mathcal{S}$. Conversely, every function belongs to $\mathcal{S}$ is a symplectic potential for some $S$-invariant K\"ahler metric in $c_{1}(L_{P})$. \end{theorem} |
| 4 | 0.771 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Background > $v$-solitons and Real Monge-Amp\`ere equations | line 571 | no | yes | symplectic potential | Let $u$ be the corresponding symplectic potential, i.e. $u = L(\phi)$ where $L$ denotes the Legendre transform. Define a function $\rho_u \in C^\infty(P)$ by |
| 5 | 0.760 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted toric Yau-Tian-Dolnaldson correspondence > Existence via estimates | lines 2027-2029 | no | yes | symplectic potential | where $\varphi_u \in \mathcal{K}(X,\omega_0)^\T$ is the K\"ahler potential corresponding the symplectic potential $u$ via the Legendre transform (see \cite{SKD, Gui}). |
| 6 | 0.752 | `corpus/arxiv/2208.12493/source/toric-lecture-notes.tex` | `text` | The scalar curvature | lines 939-942 | no | yes | symplectic potential | We now consider a $\T$-invariant, $\omega$-compatible K\"aher metric on a symplectic toric manifold $(M, \omega, \T)$, written on $M^0$ in the form \eqref{g} where ${\bf G} = {\rm Hess}(u)$ for a symplectic potential $u \in S(\Delta, {\bf L})$. |
| 7 | 0.752 | `corpus/arxiv/dg-ga_9711014/paper.pdf` | `text` | unsectioned | p. 3 | no | yes | - | a suitable power of the K¨ ahler class. Calabi’s family of ext remal metrics on CP 2♯CP 2 is discussed in §6. Acknowledgements: This work was carried out while I was a postdoctoral member of the School of Mathematics of the Institute for Adva nced Study. I take this opportunity to thank the staﬀ and faculty of the Ins titute for providing a wonderful environ... |
| 8 | 0.697 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | ...it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic topology, how far is the class of Calabi dream manifolds from the class of all smooth minimal models of general type? %\item Motived by Conjecture 1 in \cite{LeSz13}, we may ask whether a K\"ahler manifold with $C_1 \leq 0$ and n... |
| 9 | 0.683 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 10 | 0.665 | `corpus/arxiv/1512.06391/source/source.tex` | `text` | Further observations > Uniqueness in a given conformal class | lines 1057-1066 | no | yes | - | ...l holds true for a compact orbifold and implies that $D^g df = h g$, for some function $h$. Using that $f$ is a Killing potential, the latter is equivalent to $dd^c f = h \omega$, showing that $h=const$ and, therefore, also $f=const$ by the maximum principle (which holds true on a compact orbifold). Thus, the uniqueness of the Einstein--Maxwell metric holds... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### my_notes_cp1_007 - my_notes CP1 cone-to-cusp examples

**Question:** Where do my notes discuss the symplectic potential for a one-cusp CP1 model?

**Expected sources:** `corpus/my_notes/toric_manifolds_mixed_conic_cusp/notes/one_cusp_point.tex`
**Expected chunk types:** `example`, `definition`, `text`
**Expected terms:** `symplectic potential`, `one cusp`, `CP1`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.920 | `corpus/arxiv/2108.12297/source/source.tex` | `remark` | Weighted toric K-stability > Complex and symplectic points of view | lines 1279-1281 | no | no | symplectic potential | \begin{remark} In the above Proposition and Definition, we use as a model metric the Guillemin K\"ahler metric $(g_0, J_0)$ \cite{VG}, given by $(\ref{metric-toric2})$ for the symplectic potential \[ u_0 := \frac{1}{2} \sum_{j=1}^d L_j \log L_j,\] where $L_j, j=1, \ldots, d$ are the affine-linear functions defining the polytope. This introduces a discrepancy... |
| 2 | 0.821 | `corpus/arxiv/1708.05253/source/source.tex` | `text` | Levi--K\"ahler reduction for products of spheres > Products of simplices and products of spheres | lines 1628-1630 | no | yes | symplectic potential | We now give a closed formula for the symplectic potential of $h_\Ll$. |
| 3 | 0.785 | `corpus/arxiv/2110.10386/source/source.tex` | `theorem` | Convex Preliminaries > Symplectic potentials | lines 1434-1437 | no | no | symplectic potential | \begin{theorem}[\cite{Ab03}, \cite{Apo19}, \cite{Don05}, \cite{G94b}]\label{GuiAb} Every $S$-invariant K\"ahler metric in the class $c_{1}(L_{P})$ has a symplectic potential $u$ in $\mathcal{S}$. Conversely, every function belongs to $\mathcal{S}$ is a symplectic potential for some $S$-invariant K\"ahler metric in $c_{1}(L_{P})$. \end{theorem} |
| 4 | 0.771 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Background > $v$-solitons and Real Monge-Amp\`ere equations | line 571 | no | yes | symplectic potential | Let $u$ be the corresponding symplectic potential, i.e. $u = L(\phi)$ where $L$ denotes the Legendre transform. Define a function $\rho_u \in C^\infty(P)$ by |
| 5 | 0.760 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Applications > Weighted toric Yau-Tian-Dolnaldson correspondence > Existence via estimates | lines 2027-2029 | no | yes | symplectic potential | where $\varphi_u \in \mathcal{K}(X,\omega_0)^\T$ is the K\"ahler potential corresponding the symplectic potential $u$ via the Legendre transform (see \cite{SKD, Gui}). |
| 6 | 0.752 | `corpus/arxiv/2208.12493/source/toric-lecture-notes.tex` | `text` | The scalar curvature | lines 939-942 | no | yes | symplectic potential | We now consider a $\T$-invariant, $\omega$-compatible K\"aher metric on a symplectic toric manifold $(M, \omega, \T)$, written on $M^0$ in the form \eqref{g} where ${\bf G} = {\rm Hess}(u)$ for a symplectic potential $u \in S(\Delta, {\bf L})$. |
| 7 | 0.752 | `corpus/arxiv/dg-ga_9711014/paper.pdf` | `text` | unsectioned | p. 3 | no | yes | - | a suitable power of the K¨ ahler class. Calabi’s family of ext remal metrics on CP 2♯CP 2 is discussed in §6. Acknowledgements: This work was carried out while I was a postdoctoral member of the School of Mathematics of the Institute for Adva nced Study. I take this opportunity to thank the staﬀ and faculty of the Ins titute for providing a wonderful environ... |
| 8 | 0.697 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | ...it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic topology, how far is the class of Calabi dream manifolds from the class of all smooth minimal models of general type? %\item Motived by Conjecture 1 in \cite{LeSz13}, we may ask whether a K\"ahler manifold with $C_1 \leq 0$ and n... |
| 9 | 0.683 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 10 | 0.665 | `corpus/arxiv/1512.06391/source/source.tex` | `text` | Further observations > Uniqueness in a given conformal class | lines 1057-1066 | no | yes | - | ...l holds true for a compact orbifold and implies that $D^g df = h g$, for some function $h$. Using that $f$ is a Killing potential, the latter is equivalent to $dd^c f = h \omega$, showing that $h=const$ and, therefore, also $f=const$ by the maximum principle (which holds true on a compact orbifold). Thus, the uniqueness of the Einstein--Maxwell metric holds... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### my_notes_cp1_008 - my_notes CP1 cone-to-cusp examples

**Question:** Where do my notes discuss cone-to-cusp limiting behavior in the CP1 examples?

**Expected sources:** `corpus/my_notes/toric_manifolds_mixed_conic_cusp/notes/one_conic_point.tex`, `corpus/my_notes/toric_manifolds_mixed_conic_cusp/notes/one_cusp_point.tex`
**Expected chunk types:** `example`, `remark`, `text`
**Expected terms:** `cone-to-cusp`, `limit`, `CP1`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.799 | `corpus/arxiv/1302.6979/source/ambitoric2.tex` | `text` | Examples > Extremal ambitoric compactifications | lines 1824-1850 | no | yes | limit | ...\al_k,\be_k$, we have a one parameter family of Bach-flat ambitoric orbifolds. Positivity of $s_+$ can be obtained by a limiting argument, provided $P$ is chosen so that the corresponding Bochner-flat metric (in~\ref{s:weighted-proj-plane}) has positive scalar curvature. We thus obtain infinitely many new examples of compact ambihermitian Einstein $4$-orbifo... |
| 2 | 0.796 | `corpus/arxiv/math_0611002/source/thesis.tex` | `remark` | A metric degeneration | lines 3265-3270 | no | yes | - | \begin{rem}\label{rem:sesh} In general we expect that we could allow $c+d$ to be as large as the Seshadri constant of the zero section by possibly changing our choice of $\omega_M$ and $h$, but we do not wish to discuss this in this thesis. \end{rem} |
| 3 | 0.752 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 4 | 0.734 | `corpus/arxiv/math_0511118/source/source.tex` | `remark` | Existence and nonexistence results for extremal K\"ahler metrics > Extremal K\"ahler metrics over a Riemann surface | lines 1727-1735 | no | yes | - | \begin{rem}\label{general-christina} In absence of blow-downs, we recover the examples of~\cite{christina1} on (complex) pseudo-Hirzebruch surfaces $P(\cO\oplus\cL)\to\Sigma$, where there are K\"ahler classes which do not contain an extremal K\"ahler metric (if $\Sigma$ has genus $\mathbf g>1$). Our result extends these examples to higher rank projective bun... |
| 5 | 0.715 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | no | yes | - | ...rk) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail in our next paper and refer interested readers to the following works and references therein: |
| 6 | 0.693 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `remark` | Log Futaki invariant and log $K$-stability > Log $K$-stability | lines 714-716 | no | yes | - | \begin{remark} We need some restriction on the singularities of $\mathcal{X}$ and $\mathcal{D}$ to define log $K$-stability (cf.~Remark \ref{pathsingkstble}), when the log test configuration is not product or trivial (cf.~\cite{os}), but we do not discuss this issue since only the product log test configurations will be important for us later. \end{remark} |
| 7 | 0.673 | `corpus/arxiv/1801.05907/source/source.tex` | `question` | Introduction | lines 261-263 | no | no | - | \begin{q} How do we characterize the set of $\psi\in L^p(M,\omega)$ ($p\geq1$) which is the initial velocity of a locally finite energy geodesic ray with unit speed? Or more importantly, is the set of velocities (which give rise to a locally finite geodesic ray) a convex subset of $L^p(M, \omega)? $ \end{q} |
| 8 | 0.668 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Introduction | lines 242-243 | no | yes | - | In the general case where there exist nontrivial holomorphic vector fields on $D$, if we want to prove the uniqueness of cscK metrics, we may need to assume that they have similar asymptotic behavior near $D$. Enlightened by this idea, we prove the Theorem 1.2 below. |
| 9 | 0.656 | `corpus/arxiv/dg-ga_9711014/paper.pdf` | `text` | unsectioned | p. 2 | no | yes | - | ...inatorial formula, while the ex tremal condition is R being an aﬃne function on ∆ ⊂ Rn. A simple analysis of some examples leads quickly to the conclusion that, except for the case of c artesian products of complex projective spaces, the canonical toric metric do es not satisfy the extremal condition. However Guillemin’s construction not only gives an explic... |
| 10 | 0.640 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Semisimple principal fibrations > K\"ahler-Ricci solitons > K\"ahler-Ricci solitons on line bundles | lines 1707-1711 | no | yes | - | \subsubsection{K\"ahler-Ricci solitons on line bundles}\label{section-chili} In this section we discuss the examples of non-compact complete shrinking K\"ahler-Ricci solitons which are built out of certain negative line bundles $L \to B$ over a compact Fano manifold $B$. Starting with Cao \cite{Caosoliton} and Feldman-Ilmanen-Knopf \cite{FIK} in the case of... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### my_notes_cp1_009 - my_notes CP1 cone-to-cusp examples

**Question:** Where do my notes discuss notation for mixed conic and cusp toric manifolds?

**Expected sources:** `corpus/my_notes/toric_manifolds_mixed_conic_cusp/tables/notation_table.tex`
**Expected chunk types:** `definition`, `text`
**Expected terms:** `notation`, `mixed conic`, `cusp`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.865 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Openness of coercivity > Coercivity > Applications to conic and cusp singularities | lines 1829-1834 | no | yes | cusp | \subsubsection*{Applications to conic and cusp singularities} Having established the general openness result for coercivity under perturbations (Proposition \ref{prop:coercivity-weighted-twisted} and Proposition \ref{prop:cusp-to-conic}), we now apply it to two important geometric settings: perturbations from cusp singularities to conic singularities, and pe... |
| 2 | 0.860 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction | lines 649-651 | no | no | cusp | \begin{cor}[Weighted K-energy convexity for mixed cusp and conic singularities, see Corollary \ref{prop:extention-K-energy-divisor}]\label{cor:mixed-singularities} The weighted twisted Mabuchi functional $\cM_{v,\mathrm{w}}^{2\pi[D]}$ for mixed cusp/conic divisors admits a unique greatest lower semicontinuous extension to $\cET(X, \omega)$, that is moreover... |
| 3 | 0.805 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction > Openness of coercivity | lines 674-689 | no | no | cusp | \begin{mainthm}[Openness of coercivity for mixed cusp and conic singularities, see Theorem \ref{thm:coeropen0}]\label{thm:coeropen} Fix smooth weights $v,\mathrm{w}\in C^\infty(\ft^\vee)$ with $v,\mathrm{w}>0$ on the (normalized) moment polytope $P$. Let $D=\sum_{i=1}^k D_i + \sum_{j=k+1}^N (1-\alpha_j)D_j$ be a simple normal crossing divisor, and consider t... |
| 4 | 0.774 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 645-648 | no | yes | cusp | ...imple normal crossing divisor $D=\sum_{i=1}^k D_i + \sum_{j=k+1}^N (1-\alpha_j)D_j$ where the first $k$ components have cusp singularities (cone angle $0$) and the remaining components have conic singularities (cone angle $2\pi\alpha_j$ for $\alpha_j \in (0,1)$). This connects to Auvray's foundational work \cite{Auvray13,Auvray,Auvray1,Auvray18} and the anal... |
| 5 | 0.608 | `corpus/arxiv/2110.08491/source/source.tex` | `text` | \bf Introduction | lines 171-172 | no | yes | - | In this paper, we consider toric manifolds and homogeneous toric bundles. The equation for toric manifolds is (\ref{eqn-1.3}). We prove the following theorem. |
| 6 | 0.606 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 7 | 0.710 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Openness of coercivity > Convexity of K-energy with mixed cusp and conic singularities | lines 1501-1506 | no | yes | cusp | \subsection{Convexity of K-energy with mixed cusp and conic singularities} Consider the case where $\chi$ is the current of integration along a simple normal crossing divisor $D=\sum_{i=1}^k D_i + \sum_{j=k+1}^N (1-\alpha_j)D_j$ where the first $k$ components $D_1,\ldots,D_k$ have coefficient $1$ (corresponding to cusp singularities with cone angle $0$), and... |
| 8 | 0.676 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Openness of coercivity > Convexity of K-energy with mixed cusp and conic singularities | lines 1528-1534 | no | no | cusp | \begin{cor}[Weighted K-energy convexity for mixed cusp and conic singularities]\label{prop:extention-K-energy-divisor} Let $(X,\omega)$ be a compact connected K\"ahler manifold and let $T\subset\Aut_{red}(X,[D])$ be a compact torus. For smooth weights $v,\mathrm{w}\in C^\infty(\mathfrak{t}^\vee)$ with $v,\mathrm{w}>0$ on the moment polytope $P_X$, the weight... |
| 9 | 0.525 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | Introduction | lines 220-222 | no | yes | - | ...rk) implies geodesic stability in $\mathcal{E}_0^1$? The first named author believes the answer is affirmative. We will discuss this question and other stability notions in algebraic manifolds in greater detail in our next paper and refer interested readers to the following works and references therein: |
| 10 | 0.622 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 652-659 | no | yes | cusp | Regarding Corollary \ref{cor:mixed-singularities}, we emphasize that while \cite{Xu_Zheng25} and \cite{Xu25} restrict their attention to smooth divisors, our framework handles general twisted positive $(1,1)$-currents $\chi$, thereby covering simple normal crossing divisors. More specifically, Xu \cite{Xu25} and Xu--Zheng \cite{Xu_Zheng25} established unique... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### my_notes_cp1_010 - my_notes CP1 cone-to-cusp examples

**Question:** Where do my notes discuss weighted or twisted K-energy together with the CP1 examples?

**Expected sources:** `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex`, `corpus/my_notes/toric_manifolds_mixed_conic_cusp/tables/kenergy_table.tex`
**Expected chunk types:** `definition`, `proposition`, `text`
**Expected terms:** `weighted`, `twisted K-energy`, `CP1`
**Preferred sections:** -
**Negative:** no
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: yes
- Expected chunk type in top-k: yes
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.127 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | {Convexity of weighted twisted K-energy } | lines 1332-1333 | yes | yes | weighted, twisted K-energy | \section{{Convexity of weighted twisted K-energy }} |
| 2 | 0.767 | `corpus/arxiv/1602.03114/source/source.tex` | `text` | Preliminaries > The energy functionals > The (twisted) K-energy | lines 344-346 | no | yes | - | \subsubsection*{The (twisted) K-energy} Fix a closed smooth positive $(1,1)$-form $\chi$. The (extended) K-energy $\Kenergy: \mathcal E^1 \to (-\infty,\infty]$ is defined as follows: |
| 3 | 0.752 | `corpus/arxiv/1801.05907/source/source.tex` | `question` | Introduction | lines 261-263 | no | no | - | \begin{q} How do we characterize the set of $\psi\in L^p(M,\omega)$ ($p\geq1$) which is the initial velocity of a locally finite energy geodesic ray with unit speed? Or more importantly, is the set of velocities (which give rise to a locally finite geodesic ray) a convex subset of $L^p(M, \omega)? $ \end{q} |
| 4 | 0.887 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction | lines 649-651 | yes | no | weighted | \begin{cor}[Weighted K-energy convexity for mixed cusp and conic singularities, see Corollary \ref{prop:extention-K-energy-divisor}]\label{cor:mixed-singularities} The weighted twisted Mabuchi functional $\cM_{v,\mathrm{w}}^{2\pi[D]}$ for mixed cusp/conic divisors admits a unique greatest lower semicontinuous extension to $\cET(X, \omega)$, that is moreover... |
| 5 | 0.698 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | yes | - | ...predict that existence of canonical K\"ahler metrics should be equivalent to various notions of properness of Mabuchi's K-energy functional. In some instances this has been verified, especially under restrictive assumptions on the automorphism group. We provide counterexamples to the original conjecture in the presence of continuous automorphisms. The constr... |
| 6 | 0.870 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `proposition` | {Convexity of weighted twisted K-energy } > Weak geodesics | lines 1451-1457 | yes | yes | weighted, twisted K-energy | \begin{prop}\label{prop:extention-K-energy} Let $(\varphi_t)_{t\in[0,1]} \subset \cH^{1,1}(X,\omega)^T$ be a weak geodesic segment with endpoints $\varphi_0, \varphi_1 \in \cH^T(X, \omega)$. Then the weighted twisted K-energy, decomposed as \[ \cM_{v,\mathrm{w}}^{\chi}(\varphi_t) = \cM_{v,\mathrm{w}}(\varphi_t) + \enE_v^{\chi}(\varphi_t), \] defines a convex... |
| 7 | 0.691 | `corpus/arxiv/dg-ga_9711014/paper.pdf` | `text` | unsectioned | p. 3 | no | yes | - | a suitable power of the K¨ ahler class. Calabi’s family of ext remal metrics on CP 2♯CP 2 is discussed in §6. Acknowledgements: This work was carried out while I was a postdoctoral member of the School of Mathematics of the Institute for Adva nced Study. I take this opportunity to thank the staﬀ and faculty of the Ins titute for providing a wonderful environ... |
| 8 | 0.829 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction > Openness of coercivity | lines 660-673 | yes | yes | weighted, twisted K-energy | ...our setting, we adapt the variational viewpoint to establish the openness of the \emph{twist class} with respect to the twisted energy. It is natural to work with the \emph{relative} (i.e.\ $T^\C$-invariant) version of the weighted twisted K-energy. Indeed, as in the classical cscK problem, the vanishing of the (weighted twisted) Futaki character is a necess... |
| 9 | 0.663 | `corpus/arxiv/1512.06391/source/source.tex` | `text` | Further observations > Uniqueness in a given conformal class | lines 1057-1066 | no | yes | weighted | ...eness of the Einstein--Maxwell metric holds true in the K\"ahler--Einstein case. %The same conclusion holds true on any weighted projective plane, by virtue of Theorem~\ref{wpp-classification}. For compact $4$-orbifolds this is not true in general. An example of that is ${CP}^1\times {CP}^1$ which admits in each conformal class the product cscK metric, and i... |
| 10 | 0.636 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | yes | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_001 - negative/non-established claims

**Question:** Does the corpus prove a general Chen-Cheng theorem for mixed conic and cusp toric manifolds?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `general Chen-Cheng theorem`, `mixed conic cusp`, `toric manifolds`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.834 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Openness of coercivity > Coercivity > Applications to conic and cusp singularities | lines 1829-1834 | no | no | - | \subsubsection*{Applications to conic and cusp singularities} Having established the general openness result for coercivity under perturbations (Proposition \ref{prop:coercivity-weighted-twisted} and Proposition \ref{prop:cusp-to-conic}), we now apply it to two important geometric settings: perturbations from cusp singularities to conic singularities, and pe... |
| 2 | 0.746 | `corpus/arxiv/2110.08491/source/source.tex` | `text` | \bf Introduction | lines 171-172 | no | no | toric manifolds | In this paper, we consider toric manifolds and homogeneous toric bundles. The equation for toric manifolds is (\ref{eqn-1.3}). We prove the following theorem. |
| 3 | 0.646 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 409-415 | no | no | toric manifolds | ...result was known by combining the works of Zhou-Zhu \cite{ZZ08}, Chen-Li-Sheng \cite{CLS14}, Hisamoto \cite{His16b} and Chen-Cheng \cite{CC18a, CC18b}. This previous proof depends on Donaldson's deep analysis of K\"{a}hler geometry on toric manifolds (\cite{Don02}). On the other hand, the proof given combines our analysis with the fundamental works on non-Ar... |
| 4 | 0.604 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | no | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 5 | 0.579 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | %\begin{q} There is a few open questions for the Calabi dream manifolds: %\begin{enumerate} %\item What linear combinations of Chern numbers are nonnegative for all Calabi dream manifolds? %\item In Corollary 1.7, can we extend it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic to... |
| 6 | 0.568 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 220-223 | no | no | - | ...priori estimates for \eqref{2nd pde} in both the cscK cone problem and the degenerate cases. The a priori estimates of Chen-Cheng rely on fixed smooth K\"ahler metric. In the conical setting, their a priori estimates can not be applied directly, since the a priori estimates are required to be obtained with respect to a K\"ahler cone metric. The K\"ahler con... |
| 7 | 0.536 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Introduction | lines 185-188 | no | no | - | ...e cscK metric and extremal K\"ahler metric. A natural question is: could we prove the uniqueness of cscK metric on more general K\"ahler manifolds? Note that the methods we mentioned above depend on the compactness of the manifold. As a result, it is interesting to consider the following Poincar\'e type K\"ahler metric which is non-compact and complete: On $... |
| 8 | 0.532 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | no | - | ...e (defined precisely in Definition \ref{d1.1} below), then cscK exists. To extend the properness theorem to the case of general automorphism group, we need to extend the notion of properness (c.f. \cite{Darvas1605} \cite{Dar-Rub-17}). |
| 9 | 0.519 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Introduction | lines 128-133 | no | no | toric manifolds | ...em \ref{equiv_strengthenings} does not require the Delzant condition and that this equivalence also holds for polarized toric \emph{varieties}. Let $(X, L)$ be a polarized toric manifold associated to an integral Delzant polytope $P \subset \mathbf{R}^{n}$. We say that $(X, L)$ is \emph{uniformly relatively K-polystable} if $P$ satisfies the condition $(J)_{... |
| 10 | 0.629 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction | lines 649-651 | no | no | - | \begin{cor}[Weighted K-energy convexity for mixed cusp and conic singularities, see Corollary \ref{prop:extention-K-energy-divisor}]\label{cor:mixed-singularities} The weighted twisted Mabuchi functional $\cM_{v,\mathrm{w}}^{2\pi[D]}$ for mixed cusp/conic divisors admits a unique greatest lower semicontinuous extension to $\cET(X, \omega)$, that is moreover... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_002 - negative/non-established claims

**Question:** Does the corpus contain a complete proof of my own new theorem?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `complete proof`, `own new theorem`, `novelty`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: no
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.809 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Relative K-polystability of weighted extremal manifolds > Expansions of weighted invariants | lines 702-704 | no | no | - | Given all this, we can finally complete the proof of Theorem \ref{thm:main}: |
| 2 | 0.696 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | K-stability of twisted cscK metrics > Test configurations and the asymptotic argument | lines 413-415 | no | no | - | Postponing the proof of Lemma \ref{dgtoag} for the moment, we complete the proof of Proposition \ref{limitisdf}. |
| 3 | 0.688 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | no | - | ...veral questions : \begin{enumerate} \item Do all crystallographic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \end{enume... |
| 4 | 0.616 | `corpus/arxiv/math_0511118/source/source.tex` | `text` | Admissible extremal K\"ahler metrics > K-energy and the extremal polynomial | lines 1264-1269 | no | no | - | In the next paragraph, where we complete the proof of Theorem~\ref{main-thm}, we shall show that positivity of $F_{\Omega}$ on $(-1,1)$ is a necessary and sufficient condition for the existence of an extremal K\"ahler metric in $\Omega$. |
| 5 | 0.530 | `corpus/arxiv/0803.4095/source/source.tex` | `text` | Introduction | lines 106-112 | no | no | - | To sum up the main ingredients for our proof (besides Theorem \ref{calabi}) are: \begin{enumerate} \item A well known embedding result for test configurations (Proposition \ref{embed}), together with the algebro-geometric estimate Proposition \ref{repulsive}; \item A blowup formula for the Donaldson-Futaki invariant proved by the author \cite{io} Theorem 1.3... |
| 6 | 0.523 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | no | - | In the intriguing paper \cite{Ross11}, the authors defined a notion of analytic test configurations which is an one-parameter family of K\"ahler potentials, concave with respect to this parameter. They proved that each analytic test configuration defines a unique geodesic ray (up to parallelism), thus defines a point at ${\mathcal S}_\infty.$ It is important... |
| 7 | 0.509 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | \label{sec:Introduction}Introduction > Statement of the main results | lines 261-297 | no | no | - | ...}) that the partial regularity results do not hold as stated in \cite{c-t}, so it seems that the earlier proofs are not complete. We start with the following corollary which follows immediately from the previous theorem, using the ``sub-slope property'' of convex functions. |
| 8 | 0.486 | `corpus/arxiv/1004.2012/source/Kempf_Ness_uniqueness_12272011.tex` | `text` | Stability of the Calabi flow | lines 1059-1074 | no | no | - | The Calabi flow equation in the form (\ref{Calabi flow H}) was first proposed by E. Calabi(\cite{Ca1}, \cite{Ca2}) to find extremal metrics in a fixed K\"ahler class. The short time existence was established by Chen-He(\cite{CH1}). They also proved the global existence assuming Ricci curvature bound. \\ The equation (\ref{Calabi flow J}) also has its own adv... |
| 9 | 0.473 | `corpus/my_notes/requested_non_arxiv_sources.md` | `text` | Requested non-arXiv and correction pointers > Journal-only or correction pointers | lines 7-23 | no | no | - | ...iform K-stability and asymptotics of energy functionals in Kahler geometry", JEMS 21 (2019), 2905-2944. ArXiv source in corpus: `corpus/arxiv/1603.01026`. EMS page with correction pointer: https://ems.press/journals/jems/articles/16240 Local status: arXiv paper downloaded; correction pointer recorded here. - S.-Y. Cheng and S.-T. Yau, "On the existence of a... |
| 10 | 0.461 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Existence results for cscK metrics > Uniform stability for model filtrations | lines 2158-2173 | no | no | - | ...er of $\bG$. Set $N_\bZ={\rm Hom}(\bC^*, \bT)$ and $N_\bR=N_\bZ\otimes_\bZ\bR$. Let $\bK$ be a maximal compact subgroup containing $(S^1)^r$. A main goal in this section is to prove Theorem \ref{thm-existfiltr}. We will first prove a weaker statement which says that uniform K-stability over $\cE^{1,\NA}$ implies the cscK (Proposition \ref{prop-exist1}). This... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_003 - negative/non-established claims

**Question:** Where does this corpus establish a Floer homology spectral sequence for these metrics?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `Floer homology`, `spectral sequence`, `cscK metrics`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.535 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 220-223 | no | no | - | In Section \ref{a priori estimates}, we establish a priori estimates for \eqref{2nd pde} in both the cscK cone problem and the degenerate cases. The a priori estimates of Chen-Cheng rely on fixed smooth K\"ahler metric. In the conical setting, their a priori estimates can not be applied directly, since the a priori estimates are required to be obtained with... |
| 2 | 0.533 | `corpus/arxiv/math_0401320/source/hfkg2.tex` | `text` | Hamiltonian actions and toric geometry > Compatible K\"ahler metrics: compactification | lines 676-699 | no | no | - | ...o compatible uniformizing charts. On the other hand we learn nothing about the dependence of the angular coordinates on metrics which induce different $S^2\mathfrak{t}$-valued functions on the interior of the Delzant polytope. Thus the above lemma does not suffice to clarify Abreu's proof. The issue of the compactification of toric K\"ahler metrics is an imp... |
| 3 | 0.523 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | unsectioned | lines 170-190 | no | no | cscK metrics | \title{Weighted cscK metrics (I): a priori estimates} \author{Eleonora Di Nezza, Simon Jubert and Abdellah Lahdili} \begin{document} \maketitle \begin{abstract} \noindent Let $X$ be a compact K\"ahler manifold. In this paper we study the existence of constant weighted scalar curvature K\"ahler (weighted cscK) metrics on $X$. More precisely, we establish a pr... |
| 4 | 0.521 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Preliminaries > More functionals | lines 1285-1287 | no | no | cscK metrics | %By proving Theorem \ref{thm-Echislope}, we will show that this is well-defined and does not depend on the choice of the decreasing sequence $\Phi_m$. The constant scalar curvature K\"{a}hler metrics are global minimizers of Mabuchi functional $\bfM(\vphi)$. We now have the following important analytic criterion for the existence of cscK metrics: |
| 5 | 0.502 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 717-744 | no | no | cscK metrics | The strategy for proving Theorem~\ref{bigthm_existence_0} is to establish uniform a priori estimates for the solutions to a family of {weighted} cscK equations on the resolution of singularities $\pi: Y \to X$. Denote by $E$ the exceptional set of $\pi$. Consider a family of perturbed K\"ahler metrics $\om_\vep := \pi^\ast \om + \vep \om_Y$ on the resolution... |
| 6 | 0.495 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | no | - | ...ef\cs{$\clubsuit$} % Tamas' comments \title{Tian's properness conjectures and Finsler geometry of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{document} \maketitle \begin{abstract} Well-known conjectures of Tian predict t... |
| 7 | 0.480 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Background > Weighted K-stability | lines 295-304 | no | no | - | ...gular test configurations, and this is the theory we will use here. We assume the reader is familiar with equivariant cohomology and the de Rham representation of this theory, as well as equivariant locally finite homology and its duality with equivariant cohomology; see the appendix of \cite{Ino20} for all the necessary details. Let \(Y\) be a \(T\)-equivar... |
| 8 | 0.476 | `corpus/arxiv/1712.06697/source/source.tex` | `text` | Introduction | lines 156-166 | no | no | cscK metrics | ...ction{Introduction} This is the first of a series of three papers in the study of of constant scalar curvature K\"ahler metrics (cscK metrics), following a program outlined in \cite{chen15}. In this paper, we focus on establishing a priori estimates for cscK metrics in compact K\"ahler manifold without boundary. Our estimates can be easily adapted to extrema... |
| 9 | 0.469 | `corpus/arxiv/0805.0128/source/extremal2a.tex` | `text` | Introduction | lines 219-255 | no | no | - | ...bound on a fixed ball about the origin and we have $\left(\ufl\right)^{ij}_{ij}= c^{-1} u_{ij}^{ij}$. Then if we have a sequence $u^{(\alpha)}$ such that $\left(u^{(\alpha)}\right)^{ij}_{ij}$ is suitably small we can make a sequence of such re-scalings to get a new sequence $\ufl^{(\alpha)}$, bounded in $C^{0}$ and with $\left(\ufl^{(\alpha)}\right)^{ij}_{ij... |
| 10 | 0.465 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Introduction | lines 289-325 | no | no | - | ...om an important advance by Donaldson \cite{D}, alluded to just above, whose insightful observations make it possible to establish good linear estimates. He proves a deformation theorem, showing that the set of attainable cone angles for KE edge metrics is open. The key to his work is the identification of a function space in the space of bounded functions on... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_004 - negative/non-established claims

**Question:** Does the corpus prove a general YTD theorem for arbitrary mixed conic-cusp weighted cscK metrics?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `general YTD theorem`, `mixed conic-cusp`, `weighted cscK`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.774 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Existence of singular weighted cscK metrics > Proof of Theorem~\ref{bigthm_existence_0} | lines 1721-1723 | no | no | weighted cscK | \subsection{Proof of Theorem~\ref{bigthm_existence_0}} We now prove the following result on the existence of singular weighted cscK metrics. |
| 2 | 0.612 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | unsectioned | lines 626-656 | no | no | - | ...f non-Archimedean pluripotential theory, of the Yau--Tian--Donaldson conjecture for constant scalar curvature and, more generally, weighted extremal K\"ahler metrics with prescribed compact symmetry group on an arbitrary polarized projective manifold. This is accomplished by extending important previous work of Chi Li to the weighted case, and by establishin... |
| 3 | 0.597 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 289-293 | no | no | - | In fact, a more general result is true (see Theorem \ref{thm-EcQslopeconv}), which will be used in our study of YTD conjecture in section \ref{sec-YTD}. The above two results, combined with the recent progresses mentioned above, essentially reduce the proof of (the $\bG$-uniform version of) YTD conjecture for cscK metrics to proving that the entropy slope is... |
| 4 | 0.547 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | no | - | ...IltenTuro}). Finally, the toric MMP (that produces the classification of toric surfaces) produces singular varieties in general. So our main ingredients to prove Theorem \ref{theo:intro} do not generalise, a priori, in higher dimension. Nevertheless, it would be interesting to study what goes through the new difficulties. We expect the right extension of the... |
| 5 | 0.533 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | no | - | ...ction defined on the sphere of infinity ${\mathcal S}_\infty.$ One important technical ingredient to prove existence of cscK from geodesic stability is the following properness theorem, which says that if $K$-energy is ``proper" with respect to a suitably defined distance (defined precisely in Definition \ref{d1.1} below), then cscK exists. To extend the pro... |
| 6 | 0.505 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction > Twisted and log K-stability | lines 199-200 | no | no | - | ...t of a fixed test configuration with respect to some twisting $T$ is precisely the log Donaldson-Futaki invariant for a general $D \in \|2T\|$. That the existence of a twisted cscK metric depends on an arbitrary choice of twisting $\alpha$ is analogous to the arbitrary choice of $D$ in the study of cscK metrics with cone singularities along a divisor. We relat... |
| 7 | 0.479 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 316-326 | no | no | - | ...is given in \thmref{openess}. This result should be compared with Donaldson's continuity path of K\"ahler-Einstein cone metrics in the resolution of YTD conjecture for Fano K\"ahler-Einstein metrics \cite{MR3264766,MR3472831}. Donaldson's continuity path deforms the cone angles of K\"ahler-Einstein cone metrics \cite{MR2975584}. The paralleling idea is to ap... |
| 8 | 0.446 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Introduction | lines 185-188 | no | no | - | ...to prove the convexity of the $K$-energy. Chen-Paun-Zeng used PDEs method in \cite{CPZ} to prove the uniqueness of the cscK metric and extremal K\"ahler metric. A natural question is: could we prove the uniqueness of cscK metric on more general K\"ahler manifolds? Note that the methods we mentioned above depend on the compactness of the manifold. As a resul... |
| 9 | 0.442 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Relative K-polystability of weighted extremal manifolds | lines 579-584 | no | no | weighted cscK | \section{Relative K-polystability of weighted extremal manifolds} In this section we prove Theorem \ref{thm:main}, that a weighted extremal manifold is relatively weighted K-polystable. The style of argument we use was coined by Stoppa for polarised cscK manifolds with discrete automorphism group \cite{Sto09,Sto11}. It was then generalised to the setting of... |
| 10 | 0.552 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 671-675 | no | no | - | ...onaldson (YTD) conjecture~\cite{Yau93,Tia97,Don02} predicts that the existence of a constant scalar curvature K\"ahler (cscK) metric (and, more generally, of a `canonical' metric) $\om\in c_1(L)$ is equivalent to a stability condition on $(X,L)$ of purely algebro-geometric nature. In the special case where $X$ is Fano and $L=-K_X$ (for which cscK metrics are... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_005 - negative/non-established claims

**Question:** Does the corpus establish existence of cscK Poincare metrics on every log Calabi-Yau pair?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `every log Calabi-Yau pair`, `existence`, `cscK Poincare`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.782 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Introduction | lines 85-93 | no | no | existence | \section{Introduction} In {\kah} geometry, the existence of {\bf constant scalar curvature {\kah} (cscK) metrics} is a fundamental problem. There are many works on the existence of cscK metrics on the complement of a divisor on a compact {\kah} manifold. In particular, Auvray have studied cscK (more generally, extremal {\kah}) metrics of Poincar\'{e} type, i... |
| 2 | 0.778 | `corpus/arxiv/1803.09506/source/source.tex` | `question` | Introduction | lines 327-329 | no | no | existence | \begin{ques} In big cohomology class, is existence of singular cscK metrics equivalent to geometric stability? \end{ques} |
| 3 | 0.720 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 179-182 | no | no | existence | We will prove that the existence of cscK cone metrics in terms of the properness of the log $K$-energy. |
| 4 | 0.713 | `corpus/arxiv/2210.11862/source/source.tex` | `text` | Preliminaries > {\kah} metrics with cone singularities | lines 320-325 | no | no | existence | The existence of cscK cone metrics is related to algebro-geometric stability which is called log $K$-polystability. |
| 5 | 0.527 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `text` | Introduction and the statement of the results > Log Futaki invariant computed with respect to the conically singular metrics | lines 369-370 | no | no | existence | \subsection{Log Futaki invariant computed with respect to the conically singular metrics} \label{intscmsfi} Although the log Futaki invariant is conjectured to be related to the existence of conically singular cscK metrics, the log Futaki invariant itself is computed with respect to a \textit{smooth} \kah metric in $c_1 (L)$. We now consider the following qu... |
| 6 | 0.520 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | unsectioned | lines 87-95 | no | no | existence | We prove that the existence of a twisted constant scalar curvature K\"ahler metric implies uniform twisted K-stability with respect to the minimum norm, when the twisting is ample. We give algebro-geometric proofs of uniform K-stability in the general type and Calabi-Yau cases, as well as in the Fano case under an alpha invariant condition. Our results hold... |
| 7 | 0.503 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 635-663 | no | no | existence | \section*{Introduction} The constant scalar curvature K\"ahler (cscK) metric problem has become one of the central focus in K\"ahler geometry during the last decades. The Yau--Tian--Donaldson conjecture asserts that given a compact K\"ahler manifold with a fixed K\"ahler class, the existence of cscK metrics in the K\"ahler class is equivalent to an algebro-g... |
| 8 | 0.489 | `corpus/arxiv/1401.0128/source/Note_PKFutaki.tex` | `text` | Introduction | lines 238-273 | no | no | existence | ...a K�hler-Einstein metric: the Chern class in question must then have a sign, which, if definite, forces K�hler-Einstein metrics to lie % shall be looked for in a consequently fixed K�hler class. %-- when $c_1(K)=0$, %Calabi-Yau theorem gives a K�hler-Einstein metric in any K�hler class. %By Calabi-Yau theorem again, and Bochner's technique, %there is no non-... |
| 9 | 0.474 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Introduction > Recent developments | lines 570-578 | no | no | existence | ...version of Theorem~A was proved by Li, Tian and Wang in~\cite{LTW1,LTW2} for an arbitrary (possibly singular) log Fano pair. The proof is based on the methods in this paper, but additionally uses a delicate perturbation argument on a resolution of singularities. As in the current paper, the existence results for K\"ahler--Einstein metrics in~\cite{LTW1,LTW2... |
| 10 | 0.464 | `corpus/arxiv/1712.06697/source/source.tex` | `text` | Introduction | lines 156-166 | no | no | existence | ...ction{Introduction} This is the first of a series of three papers in the study of of constant scalar curvature K\"ahler metrics (cscK metrics), following a program outlined in \cite{chen15}. In this paper, we focus on establishing a priori estimates for cscK metrics in compact K\"ahler manifold without boundary. Our estimates can be easily adapted to extrema... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_006 - negative/non-established claims

**Question:** Does the corpus prove smooth convergence from all cone angles to a cusp metric without hypotheses?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `smooth convergence`, `all cone angles`, `without hypotheses`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.992 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Openness of coercivity > Coercivity > Applications to conic and cusp singularities | lines 1829-1834 | no | no | - | \subsubsection*{Applications to conic and cusp singularities} Having established the general openness result for coercivity under perturbations (Proposition \ref{prop:coercivity-weighted-twisted} and Proposition \ref{prop:cusp-to-conic}), we now apply it to two important geometric settings: perturbations from cusp singularities to conic singularities, and pe... |
| 2 | 0.701 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Introduction | lines 289-325 | no | no | all cone angles | ...ake it possible to establish good linear estimates. He proves a deformation theorem, showing that the set of attainable cone angles for KE edge metrics is open. The key to his work is the identification of a function space in the space of bounded functions on which the linearized \MA equation is solvable. We realized, immediately following the appearance of... |
| 3 | 0.670 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | ...are nonnegative for all Calabi dream manifolds? %\item In Corollary 1.7, can we extend it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic topology, how far is the class of Calabi dream manifolds from the class of all smooth minimal models of general type? %\item Motived by Conjec... |
| 4 | 0.629 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | no | - | ...ises several questions : \begin{enumerate} \item Do all crystallographic groups arise as lattice automorphism groups of smooth complete fans? \item Do all foldable toric varieties admit a cscK metric? \item Are foldable toric varieties unobstructed? \item What are the singularities of the moduli space of cscK metrics around cscK foldable toric varieties? \en... |
| 5 | 0.752 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction > Openness of coercivity | lines 704-706 | no | no | - | \begin{cor}[From cusp coercivity to small-angle conic existence]\label{cor:cusp-to-conic-existence} Let $D$ be a smooth divisor and assume that $X$ admits no nonzero holomorphic vector field preserving $D$. Assume the twisted Mabuchi functional $\cM^{2\pi[D]}$ is coercive on $\cE^1(X, \omega)$. Then there exists $\varepsilon > 0$ such that for any $\alpha \i... |
| 6 | 0.730 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Openness of coercivity > Convexity of K-energy with mixed cusp and conic singularities | lines 1501-1506 | no | no | - | \subsection{Convexity of K-energy with mixed cusp and conic singularities} Consider the case where $\chi$ is the current of integration along a simple normal crossing divisor $D=\sum_{i=1}^k D_i + \sum_{j=k+1}^N (1-\alpha_j)D_j$ where the first $k$ components $D_1,\ldots,D_k$ have coefficient $1$ (corresponding to cusp singularities with cone angle $0$), and... |
| 7 | 0.578 | `corpus/arxiv/1205.0056/source/cone_metrics.tex` | `text` | Introduction | lines 599-606 | no | no | - | In general the K\"ahler cone metrics do not have bounded geometry. The Riemannian curvature of $\om$ is bounded from below when when the cone angle is less than $\frac{1}{2}$. We will compute that the Levi-Civita connection of the model cone metric defined in \eqref{model cone} under the cone coordinate (see \eqref{conetransform}) is bounded when the cone an... |
| 8 | 0.576 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 316-326 | no | no | - | ...ment is given in \thmref{openess}. This result should be compared with Donaldson's continuity path of K\"ahler-Einstein cone metrics in the resolution of YTD conjecture for Fano K\"ahler-Einstein metrics \cite{MR3264766,MR3472831}. Donaldson's continuity path deforms the cone angles of K\"ahler-Einstein cone metrics \cite{MR2975584}. The paralleling idea is... |
| 9 | 0.527 | `corpus/arxiv/1102.1196/source/source.tex` | `text` | Conjectural picture | lines 679-684 | no | no | all cone angles | Note that if $\beta=\nu^{-1}$ for an integer $\nu$, our metrics with cone singularities are {\it orbifold} metrics, so a great deal of standard theory can be brought to bear. See the recent work \cite{kn:RT} of Ross and Thomas, for example. \ Suppose that we are in a case when solutions exist for small cone angles but not for cone angles close to $1$. We wou... |
| 10 | 0.512 | `corpus/arxiv/1510.01260/source/source.tex` | `text` | Introduction | lines 190-197 | no | no | - | $\bullet$ By the consistency result discussed above, the previous theorem in particular applies to the smooth Calabi flow (when it exists) and it should be stressed that the result and its elaborations discussed below are new also in this smooth case. In particular it generalizes results of the first author on the smooth Calabi flow on Fano manifolds without... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_007 - negative/non-established claims

**Question:** Does the corpus prove the Abreu equation has a smooth solution on every labeled polytope?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `Abreu equation`, `every labeled polytope`, `smooth solution`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: yes

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.974 | `corpus/arxiv/1008.2607/source/source.tex` | `conjecture` | K\"{a}hler geometry on toric surfaces > $K$-stability and existence of extremal metrics | lines 696-699 | no | no | Abreu equation | \begin{conjecture}\label{conjecture_2.1.3} Let $\Delta$ be a Delzant polytope. If $(\Delta, K)$ is uniformly stable, the Abreu equation $ \mc S(u)=K $ admits a solution in $\mc C^\infty(\Delta,v)$, \end{conjecture} |
| 2 | 0.973 | `corpus/arxiv/0909.4512/source/source.tex` | `text` | Introduction | lines 74-79 | no | no | - | ...that $\zeta_{(\Delta,u)}$ is independent of the symplectic potential $G\in S(\Delta,u)$ and may also be defined as the solution of a linear system depending only on $(\Delta,u)$, see \S~\ref{sectSURVEYmetric}. If $(\Delta,u)$ is a rational labeled polytope associated to a symplectic toric orbifold, then the symplectic gradient of the pull-back by the moment... |
| 3 | 0.956 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `theorem` | Uniform $K$--stability and Extremal almost K\"ahler metrics > Uniform $K$--stability and Chen--Li--Sheng result | lines 426-427 | no | no | Abreu equation | \begin{theorem}\label{theoCLS}\cite{CLS} If $(P,\sigma)$ is a labelled polytope and that there exists a solution $\pot\in\mS(P,\sigma)$ of the Abreu equation \eqref{eqABREUintro} then $(P,\sigma)$ is uniformly $K$--stable. \end{theorem} |
| 4 | 0.873 | `corpus/arxiv/2208.12493/source/toric-lecture-notes.tex` | `theorem` | Uniform K-stability | lines 1526-1527 | no | no | Abreu equation | \begin{thm}[\bf Chen--Li--Sheng~\cite{CLS0}]\label{thm:existence-to-uniform} If $(\Delta, {\bf L})$ is a compact convex simple labelled polytope in $\R^m$ such that the Abreu equation \eqref{Abreu-equation} admits a solution in $\cS(\Delta, {\bf L})$, then $(\Delta, {\bf L})$ is $*$-uniformly K-stable. \end{thm} |
| 5 | 0.970 | `corpus/arxiv/0909.4512/source/source.tex` | `conjecture` | Introduction | lines 95-96 | no | no | - | \begin{conjecture}\label{conjecturDoSz} Let $(\Delta, u)$ be a labeled polytope. There is a solution $G\in\mS(\Delta, u)$ to the equation~(\ref{extrem}) if and only if $(\Delta, u)$ is analytically relatively $K$--stable with respect to toric degenerations. \end{conjecture} |
| 6 | 0.950 | `corpus/arxiv/0909.4512/source/source.tex` | `text` | Introduction | lines 97-102 | no | no | - | ...ing the continuity method~\cite{don:scalar,don:estimate,don:extMcond,don:csc}. Zhou--Zhu proved that the existence of a solution of~(\ref{extrem}) implies analytical relative $K$--stability, see~\cite[Proposition 2.2]{zz}\footnote{The result is stated for toric manifolds but the proof goes through for any labeled polytope.}.\\ In this paper, we consider the... |
| 7 | 0.937 | `corpus/arxiv/1008.2607/source/source.tex` | `conjecture` | K\"{a}hler geometry on toric surfaces > $K$-stability and existence of extremal metrics | lines 683-689 | no | no | Abreu equation | \begin{conjecture}\label{conjecture_2.1.2} If $(\Delta, K)$ is polystable, the Abreu equation $ \mc S(u)=K $ admits a solution in $\mc C_\infty(\Delta)$, where $\mc C_\infty(\Delta)$ consists of smooth convex functions on $\Delta$ that are continuous on $\bar\Delta$. \end{conjecture} |
| 8 | 0.741 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Background materials > Riemannian geometry of the space of K\"ahler potentials | lines 389-393 | no | no | smooth solution | Unfortunately, the Dirichlet problem of the equation \eqref{geod_MA} does not usually have a smooth solution (see \cite{LV13}). This means that in general one cannot find a smooth geodesic segment connecting two points in $\mathcal{H}_{0}^{S}$. On the other hand, Chen \cite{Ch00a} proved that the Dirichlet problem of \eqref{geod_MA} always has a unique solut... |
| 9 | 0.727 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | K-stability of toric varieties | lines 2388-2401 | no | no | - | \section{K-stability of toric varieties}\label{sec:kstabtoric} Let $\Delta\subset\mathbf{R}^n$ be the moment polytope of a smooth polarised toric variety. The polytope is defined by a finite number of linear inequalities $h_k(x)\geq c_k$, where the $h_k$ are linear maps from $\mathbf{R}^n$ to $\mathbf{R}$ which induce primitive maps from the integer lattice... |
| 10 | 0.725 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `proposition` | Explicit Donaldson metrics on quadrilaterals > Toric products | lines 1435-1439 | no | no | Abreu equation | \begin{prop}\label{parallelogram} Let $(\Delta,{\bf L},F)$ be a labelled parallelogram in $\R^2$. Then the Abreu equation \eqref{abreu1} admits a solution in $\cS(\Delta, {\bf L}, F)$ iff $F$ doesn't contain opposite sides. In this case, there exists a solution explicitly given by \eqref{U-parallelogram}. \end{prop} |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_008 - negative/non-established claims

**Question:** Does the corpus establish weighted Mabuchi convexity for all singular weak geodesics without regularity assumptions?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `weighted Mabuchi convexity`, `all singular weak geodesics`, `without regularity`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: no
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.899 | `corpus/arxiv/2104.09709/source/source.tex` | `text` | Regularity of the weak minimizers of the weighted Mabuchi energy | lines 1418-1419 | no | no | - | \section{Regularity of the weak minimizers of the weighted Mabuchi energy}\label{s:regularity} In this section, we establish the regularity of the weak minimizers of $\cE_{v,w}$. |
| 2 | 0.881 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | {Convexity of weighted twisted K-energy } > Convexity of weighted twisted K-energy | lines 1467-1470 | no | no | - | \subsection{Convexity of weighted twisted K-energy} As an application of the convexity of the twisted energy functional $\enE_v^{\chi}$, we establish the convexity of the weighted twisted Mabuchi energy $\cM_{v,\mathrm{w}}^{\chi}$ along weak geodesics in the finite energy space $\cET(X, \omega)$. |
| 3 | 0.635 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Introduction > Results | line 308 | no | no | - | Using the strategy of \cite{GuanUniqueness}, the convexity of the weighted Mabuchi functional allows us to obtain the following basic uniqueness result: |
| 4 | 0.608 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | \label{sec:Introduction}Introduction > Statement of the main results | lines 310-335 | no | no | - | ...lass of an ample line bundle $L$ over $X.$ The general case was treated by Chen-Tian in \cite{c-t}, using their partial regularity theory and approximation arguments and the inequality \ref{eq:chens ineq in intro} was then obtained by Chen, building on \cite{c-t}. In the case of smooth geodesics it is well-known that the Mabuchi functional $\mathcal{M}$ is \... |
| 5 | 0.577 | `corpus/arxiv/1409.7896/source/source.tex` | `text` | Introduction | lines 77-114 | no | no | - | \section{Introduction} In a recent paper \cite{BB}, R. Berman and B. Berndtsson established the convexity of the Mabuchi energy functional $\cM$ along the so-called \emph{weak geodesics}, answering (affirmatively) to a conjecture proposed by the first named author of this article. Given two K\"ahler metrics in the same cohomology class, it is well-known (cf.... |
| 6 | 0.719 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction | lines 649-651 | no | no | - | \begin{cor}[Weighted K-energy convexity for mixed cusp and conic singularities, see Corollary \ref{prop:extention-K-energy-divisor}]\label{cor:mixed-singularities} The weighted twisted Mabuchi functional $\cM_{v,\mathrm{w}}^{2\pi[D]}$ for mixed cusp/conic divisors admits a unique greatest lower semicontinuous extension to $\cET(X, \omega)$, that is moreover... |
| 7 | 0.598 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction | lines 634-644 | no | no | - | \begin{mainthm}[Convexity of weighted twisted K-energy, see Theorem \ref{thm:main}]\label{thm:main0} Let $(X, \omega)$ be a compact K\"ahler manifold, $T \subset \Aut_{red}(X,\chi)$ a compact torus, and $\chi$ a $T$-invariant positive $(1,1)$-current satisfying \eqref{eq: ChiProp}. For smooth positive weight functions $v, \mathrm{w}$ on the moment polytope,... |
| 8 | 0.470 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 717-744 | no | no | - | The strategy for proving Theorem~\ref{bigthm_existence_0} is to establish uniform a priori estimates for the solutions to a family of {weighted} cscK equations on the resolution of singularities $\pi: Y \to X$. Denote by $E$ the exceptional set of $\pi$. Consider a family of perturbed K\"ahler metrics $\om_\vep := \pi^\ast \om + \vep \om_Y$ on the resolution... |
| 9 | 0.466 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | no | - | ...s of Tian predict that existence of canonical K\"ahler metrics should be equivalent to various notions of properness of Mabuchi's K-energy functional. In some instances this has been verified, especially under restrictive assumptions on the automorphism group. We provide counterexamples to the original conjecture in the presence of continuous automorphisms.... |
| 10 | 0.439 | `corpus/arxiv/1603.01743/source/source.tex` | `text` | Introduction | lines 106-118 | no | no | - | \section{Introduction} Bando-Mabuchi \cite{BM} proved that K\"ahler-Einstein metric on Fano manifolds is unique up to holomorphic automorphisms in 1980s. Recently, Berndtsson \cite{Bo} generalized this uniqueness result to conic K\"ahler-Einstein metrics on Fano manifolds, by his observation on the convexity of certain energy functional (the $Ding$-functiona... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_009 - negative/non-established claims

**Question:** Does the corpus prove Chen-Cheng estimates in the noncompact cusp setting directly?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `Chen-Cheng estimates`, `noncompact cusp`, `direct proof`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.919 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | Introduction | lines 220-223 | no | no | - | In Section \ref{a priori estimates}, we establish a priori estimates for \eqref{2nd pde} in both the cscK cone problem and the degenerate cases. The a priori estimates of Chen-Cheng rely on fixed smooth K\"ahler metric. In the conical setting, their a priori estimates can not be applied directly, since the a priori estimates are required to be obtained with... |
| 2 | 0.546 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | The uniform estimate in the positive case > Poincar\'e and Sobolev inequalities | lines 2513-2521 | no | no | - | ...inequality holds as soon as $s>\eps>0$. The following argument is the analogue of \cite[Lemma 6.12]{Tbook} in this edge setting, and also generalizes \cite[Lemma 3]{LT} to higher dimensions. The second part is the same assertion as \cite[Proposition 8]{D}. The proof here takes advantage of the fine regularity results for solutions available to us. |
| 3 | 0.533 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Preliminaries > Quasi coordinates | line 300 | no | no | - | We say that a holomorphic coordinate of $X$ is a cusp coordinate if in this coordinate we have $D=\{z_n=0\}$. Let us prove a lemma using the quasi coordinate. |
| 4 | 0.499 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction > Main results and strategy of the proof | lines 252-257 | no | no | Chen-Cheng estimates | \subsection{Main results and strategy of the proof} %The goal of this paper is to derive $C^{2}$ a priori estimates for K\"ahler potentials $\varphi \in \mathcal{K}(X,\omega_0)^\T$ corresponding to weighted cscK metrics, generalizing Chen-Cheng estimates in the classical cscK case. The starting point is to re-write the $4$th order non-linear PDE in \eqref{wc... |
| 5 | 0.420 | `corpus/my_notes/requested_non_arxiv_sources.md` | `text` | Requested non-arXiv and correction pointers | lines 1-6 | no | no | - | # Requested non-arXiv and correction pointers This note records requested sources that were not added as full arXiv papers in the 2026-05-04 update. The arXiv-backed requests were downloaded directly into `corpus/arxiv/` and should be cited from those source folders, not from this note. |
| 6 | 0.412 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | unsectioned | lines 596-634 | no | no | - | ...day} \subjclass{53C55, 32J27, 32Q20, 32W20, 35A23} \keywords{Weighted cscK metric, Log terminal singularities, A priori estimates} \begin{document} \maketitle \begin{abstract} We study the weighted constant scalar curvature K\"ahler equations on mildly singular K\"ahler varieties. Assuming the existence of a suitable resolution of singularities, we establish... |
| 7 | 0.514 | `corpus/arxiv/1803.09506/source/source.tex` | `text` | unsectioned | lines 114-137 | no | no | - | ...properness conjecture and Donaldson's geodesic stability conjecture of the cscK problem for smooth K\"ahler metrics by Chen-Cheng to the setting of cscK cone metrics. One applications of our main results is that we introduce and construct singular cscK metrics with possible degeneration in big cohomology class. As another application, we also prove both ope... |
| 8 | 0.397 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Background materials > $d_{1}$-distances, reduced $d_{1}$-distances and the reduced J-functionals | lines 626-627 | no | no | - | By using the theory of Chen-Cheng and He \cite{CC17}, \cite{CC18a}, \cite{CC18b}, \cite{He18}, and the arguments in \cite{Li19}, we shall show the following theorem. |
| 9 | 0.368 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | no | - | ...to group actions. This approach also allows us to formulate and prove new optimal versions of Tian's conjecture in the setting of smooth and singular K\"ahler--Einstein metrics, with or without automorphisms, as well as for K\"ahler--Ricci solitons. Moreover, we reduce both Tian's original conjecture (in the absence of automorphisms) and our modification of... |
| 10 | 0.364 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Closeness > Closeness at time one | lines 1705-1708 | no | no | - | We follow the ideas in Chen-Cheng \cite{CC21c}. %%Hence in the notation of Theorem \ref{t:estimates:w12p} $(\beta_0)_i=\frac{1-t_i}{t_i}\omega_0$ and $f_i=\frac{1-t_i}{t_i}h_i$. By \cite[Lemma 3.12]{CC21c} and the initial arguments in \cite[Proposition 3.13]{CC21c}, for any $p>1$, there exists $\varepsilon_p>0$ such that if $t_i \in (1-\varepsilon_p,1)$, one... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_010 - negative/non-established claims

**Question:** Does the corpus prove uniqueness of weighted extremal Poincare metrics on all toric varieties?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `uniqueness`, `weighted extremal Poincare`, `all toric varieties`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.593 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | no | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 2 | 0.582 | `corpus/arxiv/1808.07811/source/source.tex` | `text` | unsectioned | lines 250-256 | no | no | - | We illustrate our theory with specific computations on smooth toric varieties and on the toric fibre bundles introduced in \cite{ACGT}. As an application, we obtain a Yau--Tian--Donaldson type correspondence for $(\uu,\vv)$-extremal K\"ahler classes on ${\mathbb P}^1$-bundles over products of compact Hodge cscK manifolds, thus extending some of the results i... |
| 3 | 0.555 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 645-648 | no | no | - | ...ature on extensions and convexity of energy functionals, notably \cite{BB,BDL,Lah,AJL,BJT}, we prove convexity of \emph{weighted, twisted K-energy} along weak geodesics in the space of \emph{$T$-invariant finite-energy potentials}. Our contribution is twofold: we simultaneously incorporate \emph{Lahdili-type weights} and a \emph{twist by a positive $(1,1)$-c... |
| 4 | 0.490 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | unsectioned | lines 168-184 | no | no | uniqueness | ...national Center for Mathematical Research, Peking University, Beijing, China} \email{lahdili.abdellah@gmail.com} \title[Uniqueness of weighted extremal metrics]{Convexity of the weighted Mabuchi functional and the uniqueness of weighted extremal metrics} \begin{abstract} We prove the uniqueness, up to a pull-back by an element of a suitable subgroup of compl... |
| 5 | 0.461 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | unsectioned | lines 146-172 | no | no | - | \usepackage[utf8]{inputenc} \title[Weighted cscK metric (II): the continuity method]{Weighted cscK metric (II): the continuity method} %{Weighted cscK metric: existence and applications} \author{Eleonora Di Nezza, Simon Jubert and Abdellah Lahdili} \begin{document} \begin{abstract} In this paper we investigate the existence of metrics with weighted constant... |
| 6 | 0.457 | `corpus/arxiv/2110.08491/source/source.tex` | `remark` | \bf Introduction | lines 200-204 | no | no | - | \begin{remark} In \cite{Del}, Delcroix expressed $K$-stability of polarized spherical varieties in terms of combinatorial data and provided a combinatorial sufficient condition of $G$-uniform $K$-stability. The appendix of \cite{Del} by Yuji Odaka showed that for non-singular spherical varieties, $G$-uniform $K$-stability is equivalent to existence of cscK m... |
| 7 | 0.446 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Introduction | lines 185-188 | no | no | uniqueness | ...e{CLP} another way to prove the convexity of the $K$-energy. Chen-Paun-Zeng used PDEs method in \cite{CPZ} to prove the uniqueness of the cscK metric and extremal K\"ahler metric. A natural question is: could we prove the uniqueness of cscK metric on more general K\"ahler manifolds? Note that the methods we mentioned above depend on the compactness of the ma... |
| 8 | 0.419 | `corpus/arxiv/1008.2607/source/source.tex` | `text` | Introduction | lines 99-167 | no | no | uniqueness | \section{Introduction} \v\n Extremal metrics, introduced by E. Calabi, have been studied intensively in the past 20 years. There are three aspects of the topic: sufficient conditions for existence, necessary conditions for existence and the uniqueness of extremal metric. The necessary conditions for the existence are conjectured to be related to certain stab... |
| 9 | 0.410 | `corpus/arxiv/0909.4512/source/source.tex` | `text` | Introduction | lines 132-142 | no | no | - | Note that explicit Sasaki--Einstein metrics of this type have been found in~\cite{exMS,other2} and toric Sasaki--Einstein metrics have been systematically studied in~\cite{futakiChoOno,futakiOnoWang}.\\ In order to prove Theorem~\ref{mainTHEOparall}, we consider the cases of \defin{generic} labeled quadrilaterals (that is, quadrilaterals which have no parall... |
| 10 | 0.407 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 717-744 | no | no | - | ...r proving Theorem~\ref{bigthm_existence_0} is to establish uniform a priori estimates for the solutions to a family of {weighted} cscK equations on the resolution of singularities $\pi: Y \to X$. Denote by $E$ the exceptional set of $\pi$. Consider a family of perturbed K\"ahler metrics $\om_\vep := \pi^\ast \om + \vep \om_Y$ on the resolution for $\vep \in... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_011 - negative/non-established claims

**Question:** Does the corpus contain a complete classification of all mixed cone-cusp CP1 limits?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `complete classification`, `mixed cone-cusp`, `CP1 limits`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.879 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | no | - | ...from dimension $3$, toric varieties may be obstructed (see \cite{IltenTuro}). Finally, the toric MMP (that produces the classification of toric surfaces) produces singular varieties in general. So our main ingredients to prove Theorem \ref{theo:intro} do not generalise, a priori, in higher dimension. Nevertheless, it would be interesting to study what goes t... |
| 2 | 0.772 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `remark` | Introduction | lines 253-255 | no | no | complete classification | ...are foldable (see e.g. \cite{TipTohoku} for a family of examples with unbounded Picard rank, and \cite{WangZhou} for a complete classification of polarised cscK toric surfaces up to Picard rank $4$). It would be interesting to produce examples of non foldable toric cscK surfaces. \end{remark} |
| 3 | 0.595 | `corpus/arxiv/0805.0128/source/extremal2b.tex` | `text` | $C^{\infty}$ limits away from the vertices | lines 2-12 | no | no | - | \section{$C^{\infty}$ limits away from the vertices} In the previous section we obtained a uniform bound on the quantity $D(p;u)$ along the interior of each edge. We now use this to get complete control of the solution away from the vertices. This is straightforward, given the results from \cite{kn:D3}, if we have a lower bound on the Riemannian distance fun... |
| 4 | 0.563 | `corpus/arxiv/math_0511118/source/source.tex` | `text` | unsectioned | lines 340-381 | no | no | complete classification | ...dmissible (see Remark~\ref{classes-adm}), and therefore Theorem~\ref{main-thm} describes exactly which K\"ahler classes contain an extremal K\"ahler metric. This is the case when $M=P(\cO\oplus\cL)\to S$ is an admissible geometrically ruled complex surface; the extremal polynomial $F_\Omega(z)$ is then a quartic divisible by $1-z^2$. We thus obtain a complet... |
| 5 | 0.541 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | %\begin{q} There is a few open questions for the Calabi dream manifolds: %\begin{enumerate} %\item What linear combinations of Chern numbers are nonnegative for all Calabi dream manifolds? %\item In Corollary 1.7, can we extend it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic to... |
| 6 | 0.485 | `corpus/arxiv/1512.06391/source/source.tex` | `text` | Further observations > Uniqueness in a given conformal class | lines 1057-1066 | no | no | - | ...\"ahler--Einstein case. %The same conclusion holds true on any weighted projective plane, by virtue of Theorem~\ref{wpp-classification}. For compact $4$-orbifolds this is not true in general. An example of that is ${CP}^1\times {CP}^1$ which admits in each conformal class the product cscK metric, and in some conformal classes also the metrics of \cite{LeB0}.... |
| 7 | 0.465 | `corpus/arxiv/0909.4512/source/source.tex` | `text` | Toric orbifolds and extremal metrics -- a quick survey. > Sasaki toric geometry. > Contact toric manifolds. | lines 261-264 | no | no | - | ...The image, $\im \hat{\mu}$, of the contact moment map of a compact contact toric manifold $(N, \mD, \hat{T})$ does not contain $0$ and $\mC= \im \hat{\mu} \cup \{0\}$ is a convex, polyhedral cone which is good with respect to the lattice of circle subgroups, $\Lambda \subset \hat{\mathfrak{t}}$. $\mC$ is called \defin{the moment cone}. Conversely, any conve... |
| 8 | 0.456 | `corpus/my_notes/requested_non_arxiv_sources.md` | `text` | Requested non-arXiv and correction pointers > Journal-only or correction pointers | lines 7-23 | no | no | - | ...iform K-stability and asymptotics of energy functionals in Kahler geometry", JEMS 21 (2019), 2905-2944. ArXiv source in corpus: `corpus/arxiv/1603.01026`. EMS page with correction pointer: https://ems.press/journals/jems/articles/16240 Local status: arXiv paper downloaded; correction pointer recorded here. - S.-Y. Cheng and S.-T. Yau, "On the existence of a... |
| 9 | 0.447 | `corpus/arxiv/dg-ga_9711014/paper.pdf` | `text` | unsectioned | p. 1 | no | no | - | ...Extremal Metrics Miguel Abreu ∗ Institute for Advanced Study revised version November 26, 2024 1991 Mathematics Subject Classiﬁcation: Primary 53C55, Se condary 14M25 53C25 58F05. Abstract A (symplectic) toric variety X, of real dimension 2 n, is completely determined by its moment polytope ∆ ⊂ Rn. Recently Guillemin gave an explicit combinatorial way of con... |
| 10 | 0.446 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | no | - | ...y of the space of K\"ahler metrics} \author{Tam\'as Darvas and Yanir A. Rubinstein \blfootnote{2010 Mathematics subject classification 53C55, 32W20, 32U05.} } \date{\vspace{-0.3in}} \begin{document} \maketitle \begin{abstract} Well-known conjectures of Tian predict that existence of canonical K\"ahler metrics should be equivalent to various notions of proper... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_012 - negative/non-established claims

**Question:** Does the corpus prove that every toric destabilizing test configuration is detected by the current notes?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `every toric destabilizing test configuration`, `current notes`, `detected`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: no
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.752 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | no | - | In the intriguing paper \cite{Ross11}, the authors defined a notion of analytic test configurations which is an one-parameter family of K\"ahler potentials, concave with respect to this parameter. They proved that each analytic test configuration defines a unique geodesic ray (up to parallelism), thus defines a point at ${\mathcal S}_\infty.$ It is important... |
| 2 | 0.696 | `corpus/arxiv/2110.10386/source/source.tex` | `text` | Convex Preliminaries > Non-Archimedean functionals on polarized toric manifolds | lines 1896-1902 | no | no | - | \subsection{Non-Archimedean functionals on polarized toric manifolds}\label{sec:NAToricEnergy} In this subsection, we give convex analytic expression of non-Archimedean functionals for toric test configurations. Let $f \in \mathcal{C}_{PL}^{\mathbf{Q}}$. For simplicity we assume $f$ is integral. Choose $L \in \mathbf{Z}_{>0}$ so that $L - f > 0$ on $P$. Then... |
| 3 | 0.550 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | no | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 4 | 0.544 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Introduction | lines 95-103 | no | no | - | These results rely on the already proven fact that a weighted extremal manifold is relatively weighted K-semistable. This was first shown with respect to smooth degenerations by Lahdili using asymptotic slope techniques \cite{Lah19}, and then extended to singular degenerations by Inoue \cite{Ino20}, who used a continuity argument to reduce to Lahdili's resul... |
| 5 | 0.535 | `corpus/arxiv/1808.07811/source/source.tex` | `text` | Introduction | lines 299-314 | no | no | - | ...efinition of the Futaki invariant $\mathcal{F}_{1, \vv_{\rm ext}}$ reduces to the relative Futaki invariant of a smooth test configuration introduced in \cite{Dervan, Sz}, so in this special case \Cref{thm:main} above is established in \cite{Dervan}. \smallskip A natural question that arises in the case when the test-configuration is a polarized projective v... |
| 6 | 0.521 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 827-842 | no | no | - | Indeed, this implies that (uniform) $\hK$-polystability is equivalent to (uniform) geodesic polystability, so that Theorem~A follows from Theorem~A'. The second point in Theorem~C is due to Chi Li~\cite{LiGeod}. To explain our proof of the first point (the toric case of which was established in~\cite[Theorem~10]{Berm19}) recall that the Chen--Tian formula~\c... |
| 7 | 0.518 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Sufficient geometric criteria for uniform and twisted K-stability > A blowing-up formalism for twisted K-stability | lines 576-580 | no | no | - | Recall from Definition \ref{twisteddf} that the definition of a twisted test configuration requires a scheme $\pi:\scX\to\C$ together with $\C^*$-equivariant line bundles $\scL,\scT$ which restrict to $L$ and $T$ respectively over the non-zero fibres. On the other hand, the definition of the twisted Donaldson-Futaki invariant does not require any lifting of... |
| 8 | 0.478 | `corpus/arxiv/1811.05693/source/etakm_REM.tex` | `text` | Introduction | lines 236-247 | no | no | - | % % Moreover, the original notion of $K$--stability~\cite{yau,tianKstab,don:scalTORICstab} has been proved to be probably too weak in all generality~\cite{ACGTFex} and one of the suggested raffinement is the uniform $K$--stability~\cite{szekelyhidi}. The convex affine geometry point of view has been exploited successfully to provide a complete understanding... |
| 9 | 0.475 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Introduction > Coercivity and Ding-stability | lines 516-542 | no | no | - | ...ty and Ding-stability} We now describe our strategy of proof of Theorem A. Choose a K\"ahler form $\om_0\in c_1(L)$, so that finite energy currents in $c_1(L)$ get parametrized by the space $\cE^1=\cE^1(X,\om_0)$ of finite energy potentials~\cite{GZ,BBGZ}, a complete geodesic space with respect to a metric $d_1$ introduced by Darvas~\cite{Dar15}. By~\cite{BB... |
| 10 | 0.468 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 250-256 | no | no | - | ...ar{1}}$-geodesics proved earlier in \cite{BB17}. To make contact with the YTD conjecture, we would like to know whether destabilizing geodesic rays are algebraically approximable, meaning that whether they can be approximated by a decreasing sequence of geodesic rays associated to test configurations. Such geodesic rays are maximal in the sense of Berman-Bou... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_013 - negative/non-established claims

**Question:** Does the corpus establish a numerical algorithm with certified proof for solving all Abreu equations?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `numerical algorithm`, `certified proof`, `all Abreu equations`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: no
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.000 | `corpus/arxiv/1409.7896/source/source.tex` | `text` | What is to be proved | lines 224-241 | no | no | - | ...ct computation (this would be enough to conclude, by letting $A\to \infty$). However, it does not seem to be so easy to establish the crucial property (c) (we refer the the paper \cite{CT}, section 6, in order to have a glimpse at the difficulties/consequences of such a statement). In order to overcome this issue, we will consider in the next paragraph a dif... |
| 2 | 0.977 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Labelled polytopes and the Abreu--Guillemin theory for K\"ahler metrics of Poincar\'e type > Donaldson metrics on a labelled polytope | line 738 | no | no | - | The extremality of the K\"ahler metric \eqref{toric-g} with $u\in \cS(\Delta, {\bf L})$ reduces to solving the {\it Abreu equation}~\cite{Abreu0} |
| 3 | 0.874 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | A priori estimates | lines 1182-1193 | no | no | - | \section{A priori estimates} In this section, we shall establish a priori estimates for weighted cscK equations on compact K\"ahler manifolds when the reference metrics are degenerating. These estimates are crucial to obtain the existence of singular weighted cscK metrics in Section \ref{sect_existence}. \smallskip In the sequel, we always assume the followi... |
| 4 | 0.821 | `corpus/arxiv/0905.0498/source/source.tex` | `text` | Rigid toric bundles and the generalized Calabi construction > The extremal equation and stability of its solutions under small perturbation | lines 1542-1547 | no | no | - | ...the type we consider, finding a {\it compatible} extremal K\"ahler metric $(g,\omega)$ of the form \eqref{M} reduces to solving the equation (for a unknown symplectic potential $U \in {\cS}(\Delta)$) |
| 5 | 0.810 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Constructions of WBF K\"ahler metrics > WBF K\"ahler metrics over a ruled surface | lines 1050-1056 | no | no | - | Without loss, we look for solutions to $h_1(x_1,x_2)=0=h_2(x_1,x_2)$ with $x_1>x_2$ and $x_1>0$. Solving $h_1=0$ for $s_1$, we find that $s_1$ must be positive, hence $s_1=2/q_{1}$ for some integer $q_{1}\geq 1$. We then establish the following three lemmas, the proofs of which can be found in Appendix~\ref{appC}. |
| 6 | 0.677 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | %\begin{q} There is a few open questions for the Calabi dream manifolds: %\begin{enumerate} %\item What linear combinations of Chern numbers are nonnegative for all Calabi dream manifolds? %\item In Corollary 1.7, can we extend it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic to... |
| 7 | 0.624 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | no | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 8 | 0.565 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | no | - | In the intriguing paper \cite{Ross11}, the authors defined a notion of analytic test configurations which is an one-parameter family of K\"ahler potentials, concave with respect to this parameter. They proved that each analytic test configuration defines a unique geodesic ray (up to parallelism), thus defines a point at ${\mathcal S}_\infty.$ It is important... |
| 9 | 0.563 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | Introduction | lines 289-325 | no | no | - | ...om an important advance by Donaldson \cite{D}, alluded to just above, whose insightful observations make it possible to establish good linear estimates. He proves a deformation theorem, showing that the set of attainable cone angles for KE edge metrics is open. The key to his work is the identification of a function space in the space of bounded functions on... |
| 10 | 0.702 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Constructions of WBF K\"ahler metrics | lines 641-655 | no | no | - | ...1+t)\bigr)\\ +x_a\bigl((d_0+1)(1+x_a)+(d_\infty+1)(1-x_a)-2s_ax_a\bigr)(1-t^2)\Bigr)dt. \end{multline} Our strategy for solving this problem is to use the equations $\{h_a=0:a\in\cA\}$ to determine $\{x_a:a\in\cA\}$ as functions of $\{s_a:a\in\cA\}$. For given $s_a=p_a/q_a$, we obtain a WBF K\"ahler metric on the corresponding projective bundle iff we can fi... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_014 - negative/non-established claims

**Question:** Does the corpus prove an equivalence between weighted K-stability and ordinary K-stability in all cases?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `weighted K-stability`, `ordinary K-stability`, `all cases`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.690 | `corpus/arxiv/2108.12297/source/source.tex` | `text` | Introduction > Main results | lines 196-228 | no | no | weighted K-stability | ...imple principal toric fibration, Conjecture $\ref{Conjecture}$ is true if we replace condition $(3)$ with the notion of weighted uniform K-stability, see Definition $\ref{uniform-K-stable}$. \end{customthm} \noindent In the above statement, in order to define \emph{uniform} (weighted) K-stability (see Definition \ref{uniform-K-stable}), we use normalized con... |
| 2 | 0.670 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | unsectioned | lines 87-95 | no | no | - | We prove that the existence of a twisted constant scalar curvature K\"ahler metric implies uniform twisted K-stability with respect to the minimum norm, when the twisting is ample. We give algebro-geometric proofs of uniform K-stability in the general type and Calabi-Yau cases, as well as in the Fano case under an alpha invariant condition. Our results hold... |
| 3 | 0.650 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Relative weighted K-stability | lines 386-389 | no | no | weighted K-stability | \section{Relative weighted K-stability} In this section we study relative weighted K-stability. One such definition was previously given by Lahdili \cite{Lah20b}, who related the condition to existence of a weighted extremal metric. Here we give a separate treatment using inner products associated to test configurations. After showing the two definitions are... |
| 4 | 0.578 | `corpus/arxiv/1603.01026/source/source.tex` | `text` | Introduction | lines 544-609 | no | no | - | ...ent follows from a result by Paul~\cite[Corollary~1.1]{Paul13}.} \medskip Let us now comment on the relation of uniform K-stability to the existence of K\"ahler-Einstein metrics on Fano manifolds. In~\cite{CDS15}, Chen, Donaldson and Sun proved that a Fano manifold $X$ admits a K\"ahler-Einstein metric iff it is K-polystable; see also~\cite{Tian15}. Since th... |
| 5 | 0.538 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 635-663 | no | no | - | ...\"ahler class, the existence of cscK metrics in the K\"ahler class is equivalent to an algebro-geometric notion called "K-stability". \smallskip Several progresses in the literature \cite{Darvas_Rubinstein_2017, Berman_Darvas_Lu_2020, Chen_Cheng_2021_1, Chen_Cheng_2021_2} have shown that the existence of a unique cscK metric in a K\"ahler class is equivalent... |
| 6 | 0.520 | `corpus/arxiv/2001.01366/source/source.tex` | `text` | Introduction and main results | lines 376-377 | no | no | - | ...is a test configuration, i.e. when $\mcL$ is semiample, then the intersection formula \eqref{eq-Mmodel} reduces to the ordinary intersection formula for for non-Archimedean Mabuchi functional as written down in \eqref{eq-Mslope}. Correspondingly, the The K-stability notion in the above definition strengthens the usual definition of K-stability via test conf... |
| 7 | 0.516 | `corpus/arxiv/math_0412518/source/slopeobs_archive.tex` | `text` | Definition of K-stability | lines 226-241 | no | no | - | \section{Definition of K-stability} Tian \cite{Ti2,Ti3} introduced a notion of K-stability using differential geometry. Donaldson \cite{Do3} gave an algebro-geometric definition that allows arbitrarily singular central fibre and which we use here. The relation between the two is studied in \cite{PT}. There is a strong formal link between K-stability and stab... |
| 8 | 0.508 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction > Organisation of the paper | lines 335-346 | no | no | - | ...: we provide definitions and references to pluripotential theory. Section \ref{s:wsystem} is dedicated to establish the equivalence between the fourth-order PDE \eqref{wcsck} and the system of elliptic PDE's \eqref{weightedsystem:intro}. %In order to do so, in Lemma \ref{l:scalv} we establish the alternative definition of the weighted scalar curvature as the... |
| 9 | 0.477 | `corpus/arxiv/0803.4095/source/source.tex` | `example` | Proof of Theorem \ref{main_teo} | lines 322-327 | no | no | - | ...ces $V_d$ of degree $d \leq 6$ admit a K\"ahler-Einstein metric. For $d \leq 5$, $V_d$ has discrete automorphism group. K-stability in the sense of Tian for $V_d$, $d \leq 5$ follows from \cite{tian} Theorem 1.2. K-stability with respect to ``good" test configurations follows from \cite{paul} Theorem 2. Our Theorem \ref{main_teo} refines this to K-stability... |
| 10 | 0.581 | `corpus/arxiv/1412.0648/source/twisted.tex` | `text` | Introduction | lines 103-107 | no | no | - | Our motivation for this conjecture is twofold: firstly, we can prove this uniform K-stability holds in several geometric situations. Secondly, there is a strong link between uniform K-stability in this sense and coercivity of the Mabuchi functional, which we describe in Section \ref{introminnorm}. There are three related themes in the present work, which we... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_015 - negative/non-established claims

**Question:** Does the corpus prove finite energy K-energy convexity for arbitrary non-Kahler complex manifolds?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `finite energy`, `non-Kahler`, `K-energy convexity`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.683 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | {Convexity of weighted twisted K-energy } | lines 1332-1333 | no | no | - | \section{{Convexity of weighted twisted K-energy }} |
| 2 | 0.570 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Introduction | lines 185-188 | no | no | - | Chen-Li-Paun provided in \cite{CLP} another way to prove the convexity of the $K$-energy. Chen-Paun-Zeng used PDEs method in \cite{CPZ} to prove the uniqueness of the cscK metric and extremal K\"ahler metric. A natural question is: could we prove the uniqueness of cscK metric on more general K\"ahler manifolds? Note that the methods we mentioned above depend... |
| 3 | 0.532 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | no | finite energy | ...lelism), thus defines a point at ${\mathcal S}_\infty.$ It is important to understand the converse: when does a locally finite energy geodesic ray define a test configuration? More importantly, can one extend the definition of $\yen$ invariant for analytic test configuration? Note that by Theorem 1.4, we can view $\yen$ invariant as a function defined on the... |
| 4 | 0.502 | `corpus/arxiv/1509.04561/source/source.tex` | `text` | Introduction > Coercivity and Ding-stability | lines 516-542 | no | no | finite energy | ...d Ding-stability} We now describe our strategy of proof of Theorem A. Choose a K\"ahler form $\om_0\in c_1(L)$, so that finite energy currents in $c_1(L)$ get parametrized by the space $\cE^1=\cE^1(X,\om_0)$ of finite energy potentials~\cite{GZ,BBGZ}, a complete geodesic space with respect to a metric $d_1$ introduced by Darvas~\cite{Dar15}. By~\cite{BBEGZ},... |
| 5 | 0.478 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | \label{sec:Introduction}Introduction > Statement of the main results > Further extensions and applications | lines 414-429 | no | no | finite energy | ...revious results is discussed in \cite{bch}. Some further interactions between the Mabuchi functional and the notions of finite energy and entropy are also studied in \cite{bch}. For example, it is shown that the extended Mabuchi functional remains convex along finite energy geodesics. Moreover, using finite energy geodesics one can define a notion of ``weak... |
| 6 | 0.475 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | no | - | ...predict that existence of canonical K\"ahler metrics should be equivalent to various notions of properness of Mabuchi's K-energy functional. In some instances this has been verified, especially under restrictive assumptions on the automorphism group. We provide counterexamples to the original conjecture in the presence of continuous automorphisms. The constr... |
| 7 | 0.543 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `text` | Introduction | lines 595-604 | no | no | finite energy, K-energy convexity | \section{Introduction} Finding canonical Kähler metrics is a central theme in complex geometry. In higher dimensions, constant scalar curvature Kähler (cscK) metrics provide an analogue of Poincar\'e’s uniformization theorem; see the surveys \cite{Boucksom_2018, Donaldson_2018_2} for background and further references. Kähler--Einstein metrics form an especia... |
| 8 | 0.434 | `corpus/arxiv/1801.00656/source/source.tex` | `text` | preliminaries | lines 394-400 | no | no | finite energy | ...In this section, we will review some basic concepts in K\"ahler geometry as well as some fundamental results involving finite energy currents, which will be needed for our proof of Theorem 1.1 and 1.3. In particular, it includes the characterization of the space $(\mathcal{E}^1,d_1)$, a compactness result on bounded subsets of $\mathcal{E}^1$ with finite en... |
| 9 | 0.432 | `corpus/arxiv/1602.03114/source/source.tex` | `text` | Introduction and main results | lines 130-135 | no | no | - | We refer to Section 2 for the precise definitions of $J_\omega$ and $\Kenergy$. Tian conjectured that existence of constant scalar curvature K\"ahler (csck) metrics in $\Homega$ should be equivalent to J-properness of the K-energy $\Kenergy$ \cite[Remark 5.2]{t1},\cite{tianbook} and this was proved for Fano manifolds with $G$ trivial \cite{t2,tz}. In \cite[T... |
| 10 | 0.431 | `corpus/arxiv/1510.01260/source/source.tex` | `text` | Introduction | lines 145-152 | no | no | finite energy | Our starting point is the observation that the K-energy functional $\mathcal K$ originally defined on $\mathcal H_\o$ admits a natural ``analytic extension" to the finite energy space $\mathcal E^1$ (and hence by restriction to all spaces $\mathcal E^p$). This is simply the extension obtained by interpreting the entropy part (the first term) and the energy p... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_016 - negative/non-established claims

**Question:** Does the corpus prove that all cusp limits preserve algebraic K-polystability automatically?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `all cusp limits`, `algebraic K-polystability`, `automatically`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.767 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Preliminaries > Quasi coordinates | line 300 | no | no | - | We say that a holomorphic coordinate of $X$ is a cusp coordinate if in this coordinate we have $D=\{z_n=0\}$. Let us prove a lemma using the quasi coordinate. |
| 2 | 0.699 | `corpus/arxiv/1412.0648/source/twisted.tex` | `remark` | K-stability of twisted cscK metrics > The argument in a fixed projective space | line 346 | no | no | automatically | \begin{remark} We use here in an essential way that $\alpha$ is semi-positive. This means that $f(t)$ is a sum of two convex functions, which must therefore be convex. For example, there is \emph{a priori} no link between solutions to $$S(\omega) + \Lambda_{\omega}\alpha = C_{\alpha}$$ and algebraic geometry, since the corresponding function $f(t)$ is no lon... |
| 3 | 0.653 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 224-231 | no | no | - | ...resting question to ask if the converse is also true. Namely if $(M,[\omega_0])$ is geodesic semistable, does it follow that $K$-energy is bounded from below? Note that for the corresponding statement in the algebraic case, we don't know how to conclude the existence of a lower bound of $K$-energy from $K$-stability or uniform stability except in the Fano ma... |
| 4 | 0.644 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | no | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 5 | 0.618 | `corpus/arxiv/math_0511118/source/source.tex` | `text` | unsectioned | lines 388-418 | no | no | - | It is natural to ask if (relative) K-polystability in the sense of~\cite{Do2,szekelyhidi} implies the existence of a CSC (or extremal) K\"ahler metric in $\Omega$. We find that this is true if $\dim S\leq 4$, but for $\dim S\geq 6$, we are only able to show that the extremal polynomial is positive on $(-1,1)\cap\Q$. Before our work, it was believed that K-po... |
| 6 | 0.613 | `corpus/arxiv/0803.4095/source/source.tex` | `remark` | Proof of Theorem \ref{main_teo} | lines 319-321 | no | no | - | ...nd} for a suitable normalisation of $F$ over all nonproduct test configurations. This condition is called \emph{uniform K-polystability}. In \cite{gabor} Section 3.1.1 it is shown that the correct normalisation in the case of algebraic surfaces coincides with that of Theorem \ref{calabi}, namely $\frac{F(\mathcal{X})}{\\|\mathcal{X}\\|}$. For toric surfaces K-... |
| 7 | 0.558 | `corpus/arxiv/math_0611002/source/thesis.tex` | `text` | K-stability | lines 1832-1842 | no | no | - | ...athbf{C}^*$-action induced by the extremal vector field. This is defined as in Section~\ref{sec:FMprelim}, by requiring that $F(\alpha)=\langle\chi,\alpha\rangle$ for all $\mathbf{C}^*$-actions $\alpha$ in the torus. Because of the difference between the algebraic and differential-geometric definitions of the Futaki invariant and inner product, this is half... |
| 8 | 0.546 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 865-884 | no | no | - | ...K\"ahler manifold $(X,\omega)$. In this context, Dervan--Ross~\cite{DR17} and Sj\"ostr\"om-Dyrefelt~\cite{SD18} proved that the existence of a cscK metric implies K-semistability, and even uniform K-stability when the automorphism group is finite. More recently, Mesquita-Piccione~\cite{MP} made a nontrivial adaptation of~\cite{LiGeod} and gave a sufficient... |
| 9 | 0.513 | `corpus/arxiv/0912.4095/source/source.tex` | `text` | Introduction | lines 99-111 | no | no | - | In particular the theorem applies when $M$ admits a cscK metric and has continuous automorphisms, proving that $M$ is K-polystable with respect to all test- configurations that commute with a maximal torus of automorphisms, but note that this is a priori a weaker condition than K-polystability (see the next section for the detailed definitions). Note that by... |
| 10 | 0.509 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | %\begin{q} There is a few open questions for the Calabi dream manifolds: %\begin{enumerate} %\item What linear combinations of Chern numbers are nonnegative for all Calabi dream manifolds? %\item In Corollary 1.7, can we extend it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic to... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_017 - negative/non-established claims

**Question:** Does the corpus establish a complete theorem for mixed conic-cusp extremal metrics with arbitrary automorphism group?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `mixed conic-cusp extremal`, `arbitrary automorphism group`, `complete theorem`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: no
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.752 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | no | - | ...that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be obstructed (see \cite{IltenTuro}). Finally, the toric MMP (that produces the cl... |
| 2 | 0.653 | `corpus/arxiv/2309.02279/source/document.tex` | `text` | Relative K-polystability of weighted extremal manifolds | lines 579-584 | no | no | - | \section{Relative K-polystability of weighted extremal manifolds} In this section we prove Theorem \ref{thm:main}, that a weighted extremal manifold is relatively weighted K-polystable. The style of argument we use was coined by Stoppa for polarised cscK manifolds with discrete automorphism group \cite{Sto09,Sto11}. It was then generalised to the setting of... |
| 3 | 0.623 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `proof` | Constructions of WBF K\"ahler metrics > WBF K\"ahler metrics over a ruled surface | lines 1152-1157 | no | no | - | \begin{proof} A WBF K\"ahler metric is in particular extremal and since extremal K\"ahler metrics on these manifolds are cohomogeneity one, hence admissible (up to automorphism), cf.~\cite{calabi1}, this follows from the above theorem and Corollary~\ref{koiso-sakane-examples}. \end{proof} |
| 4 | 0.618 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 717-744 | no | no | - | The strategy for proving Theorem~\ref{bigthm_existence_0} is to establish uniform a priori estimates for the solutions to a family of {weighted} cscK equations on the resolution of singularities $\pi: Y \to X$. Denote by $E$ the exceptional set of $\pi$. Consider a family of perturbed K\"ahler metrics $\om_\vep := \pi^\ast \om + \vep \om_Y$ on the resolution... |
| 5 | 0.613 | `corpus/arxiv/1610.07998/source/source.tex` | `text` | Remarks about stability and coercivity in the general setting | lines 1310-1312 | no | no | - | For a general polarization it seems still difficult to derive coercivity from uniform stability. We proceed to explain the relation with constant scalar curvature K\"ahler metrics. The next statement shows that we should take $G$ as the full automorphism group. |
| 6 | 0.603 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | unsectioned | lines 626-656 | no | no | - | ...niversity of Michigan\\ Ann Arbor, MI 48109-1043\\ USA} \email{mattiasj@umich.edu} \begin{document} \begin{abstract} We establish a version, formulated in terms of non-Archimedean pluripotential theory, of the Yau--Tian--Donaldson conjecture for constant scalar curvature and, more generally, weighted extremal K\"ahler metrics with prescribed compact symmetry... |
| 7 | 0.601 | `corpus/arxiv/math_0412518/source/slopeobs_archive.tex` | `text` | Introduction | lines 149-171 | no | no | - | ...se is a curve, the Narasimhan-Seshadri theorem gives a cscK metric on the projectivisation of any polystable bundle (of arbitrary rank) in any K\"ahler class, and we are able to give an almost complete converse (there is a small discrepancy for bundles which are strictly semistable but not polystable until the results of \cite{Do2, Do5,Mab} are improved to g... |
| 8 | 0.596 | `corpus/arxiv/0912.4095/source/source.tex` | `text` | Introduction | lines 78-85 | no | no | - | Using a different approach, this was recently extended to manifolds with not necessarily discrete automorphism groups by Mabuchi~\cite{Mab1}, \cite{Mab2}. The aim of the present paper is to generalise this theorem to the case of extremal metrics. In this case the conjecture analogous to Conjecture \ref{conj:1} was formulated by the second named author in \ci... |
| 9 | 0.590 | `corpus/arxiv/2503.22183/source/Weighted_CscK_II.tex` | `text` | Introduction | lines 229-234 | no | no | - | Theorem \ref{t:exi} recovers the main result of \cite{HL25}, in which the authors establish the existence of weighted extremal metrics -a special class of weighted cscK metrics. Moreover, our proof differs in several aspects, particularly in the techniques used to obtain the $C^0$-estimates and in the application of the continuity method. \smallskip The weig... |
| 10 | 0.578 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | no | - | ...ed precisely in Definition \ref{d1.1} below), then cscK exists. To extend the properness theorem to the case of general automorphism group, we need to extend the notion of properness (c.f. \cite{Darvas1605} \cite{Dar-Rub-17}). |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_018 - negative/non-established claims

**Question:** Does the corpus prove that the CP1 cone-to-cusp notes are already publication-ready?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `CP1 cone-to-cusp notes`, `publication-ready`, `proof`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.488 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Discussion and perspectives > Higher dimensional case | lines 1438-1454 | no | no | - | \subsection{Higher dimensional case} \label{sec:higher dimension} Many features that hold for toric surfaces fail in higher dimension. First, even when it is reductive, the identity component of the automorphism group of a non-rigid toric variety will not a priori be isomorphic to the torus (see \cite{Nill}). Then, from dimension $3$, toric varieties may be... |
| 2 | 0.480 | `corpus/arxiv/1512.06391/source/source.tex` | `text` | Further observations > Uniqueness in a given conformal class | lines 1057-1066 | no | no | proof | ...case when $(g, \omega)$ is a K\"ahler--Einstein metric on a compact complex manifold $(M,J)$, the Obata theorem implies that there are no non-constant conformal factors $f$ such that $\tilde g = \frac{1}{f^2} g$ is Einstein--Maxwell. The same conclusion holds in the orbifold case, as the Bochner argument in the proof of this classical result still holds true... |
| 3 | 0.454 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | no | - | ...igurations which is an one-parameter family of K\"ahler potentials, concave with respect to this parameter. They proved that each analytic test configuration defines a unique geodesic ray (up to parallelism), thus defines a point at ${\mathcal S}_\infty.$ It is important to understand the converse: when does a locally finite energy geodesic ray define a test... |
| 4 | 0.443 | `corpus/arxiv/2108.12297/source/source.tex` | `text` | Introduction > Main results | lines 275-280 | no | no | - | \noindent When $\textnormal{\textbf{g}}=0$, the existence part of Corollary $\ref{prop-ex}$ was already obtained in \cite{EL}. We prove in addition that these extremal metrics are given by the Calabi ansatz of \cite{VA2}. |
| 5 | 0.439 | `corpus/arxiv/dg-ga_9711014/paper.pdf` | `text` | unsectioned | p. 10 | no | no | - | ...ex automorphisms is not reductive, a nd so, due to a theorem of Matsushima [8] and Lichn´ erowicz [7], we know apr iori that these metrics have non-constant scalar curvature. The purpose of this section is to recast Calabi’s simplest example, CP 2♯CP 2, in the language of the previous sections. For yet another approach to Calabi’s families of e xtremal metri... |
| 6 | 0.428 | `corpus/arxiv/1506.07129/source/source.tex` | `text` | unsectioned | lines 389-495 | no | no | - | ...0, 32U05.} } \date{\vspace{-0.3in}} \begin{document} \maketitle \begin{abstract} Well-known conjectures of Tian predict that existence of canonical K\"ahler metrics should be equivalent to various notions of properness of Mabuchi's K-energy functional. In some instances this has been verified, especially under restrictive assumptions on the automorphism grou... |
| 7 | 0.422 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 827-842 | no | no | proof | Indeed, this implies that (uniform) $\hK$-polystability is equivalent to (uniform) geodesic polystability, so that Theorem~A follows from Theorem~A'. The second point in Theorem~C is due to Chi Li~\cite{LiGeod}. To explain our proof of the first point (the toric case of which was established in~\cite[Theorem~10]{Berm19}) recall that the Chen--Tian formula~\c... |
| 8 | 0.400 | `corpus/arxiv/1801.00656/source/source.tex` | `question` | preliminaries > Calabi dream Manifolds | lines 608-615 | no | no | - | %\begin{q} There is a few open questions for the Calabi dream manifolds: %\begin{enumerate} %\item What linear combinations of Chern numbers are nonnegative for all Calabi dream manifolds? %\item In Corollary 1.7, can we extend it to the case of $C_1 < 0$ and without or minimal surfaces of general type? More generally, from the point of view of symplectic to... |
| 9 | 0.396 | `corpus/arxiv/1105.5216/source/source.tex` | `text` | A local third derivative estimate (after Tian) | lines 3993-4008 | no | no | proof | ...al a priori estimate in $W^{3,2}$ for solutions of both real and complex Monge--Amp\`ere equations under the assumption that the solution has bounded real or complex Hessian and the right hand side is at least H\"older. By the classical integral characterization of H\"older spaces this implies a uniform H\"older estimate on the Laplacian. This result can be... |
| 10 | 0.394 | `corpus/arxiv/1711.08424/source/Poincare-metrics.tex` | `text` | Proof of Proposition~\ref{stable-Hirzebruch} and Corollary~\ref{Hirzebruch-non-poincare} > The proof of Corollary~\ref{Hirzebruch-non-poincare} | lines 2847-2852 | no | no | - | The cases of $K_2$ and $K_4$ are the cases when $Z$ is the zero or infinity section in $X$. This is already treated in Corollary~\ref{Hirzebruch} where we know that there exists Poincar\'e type extremal metrics. The above computations then confirm that the condition of equation~\eqref{hyperbolicity-condition} holds, which we also know by general theory regar... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_019 - negative/non-established claims

**Question:** Does the corpus prove a general bridge between Floer theory and weighted Mabuchi convexity?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `Floer theory`, `weighted Mabuchi convexity`, `general bridge`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: no
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.764 | `corpus/arxiv/2303.03263/source/arxiv-2.tex` | `text` | Introduction > Results | line 308 | no | no | - | Using the strategy of \cite{GuanUniqueness}, the convexity of the weighted Mabuchi functional allows us to obtain the following basic uniqueness result: |
| 2 | 0.600 | `corpus/my_notes/weighted_twisted/paper/weighted_twisted.tex` | `theorem` | Introduction | lines 649-651 | no | no | - | \begin{cor}[Weighted K-energy convexity for mixed cusp and conic singularities, see Corollary \ref{prop:extention-K-energy-divisor}]\label{cor:mixed-singularities} The weighted twisted Mabuchi functional $\cM_{v,\mathrm{w}}^{2\pi[D]}$ for mixed cusp/conic divisors admits a unique greatest lower semicontinuous extension to $\cET(X, \omega)$, that is moreover... |
| 3 | 0.588 | `corpus/arxiv/2410.14130/source/source.tex` | `text` | Introduction | lines 185-188 | no | no | - | Chen-Li-Paun provided in \cite{CLP} another way to prove the convexity of the $K$-energy. Chen-Paun-Zeng used PDEs method in \cite{CPZ} to prove the uniqueness of the cscK metric and extremal K\"ahler metric. A natural question is: could we prove the uniqueness of cscK metric on more general K\"ahler manifolds? Note that the methods we mentioned above depend... |
| 4 | 0.585 | `corpus/arxiv/1405.0401/source/source.tex` | `text` | \label{sec:Introduction}Introduction > Statement of the main results | lines 310-335 | no | no | - | ...ss in question is integral, i.e. when it coincides with the first Chern class of an ample line bundle $L$ over $X.$ The general case was treated by Chen-Tian in \cite{c-t}, using their partial regularity theory and approximation arguments and the inequality \ref{eq:chens ineq in intro} was then obtained by Chen, building on \cite{c-t}. In the case of smooth... |
| 5 | 0.557 | `corpus/arxiv/2007.01345/source/source.tex` | `text` | unsectioned | lines 168-184 | no | no | - | ...r for Mathematical Research, Peking University, Beijing, China} \email{lahdili.abdellah@gmail.com} \title[Uniqueness of weighted extremal metrics]{Convexity of the weighted Mabuchi functional and the uniqueness of weighted extremal metrics} \begin{abstract} We prove the uniqueness, up to a pull-back by an element of a suitable subgroup of complex automorphis... |
| 6 | 0.557 | `corpus/arxiv/2509.15016/source/wytd_arxiv1.tex` | `text` | Introduction | lines 865-884 | no | no | - | ...ref{sec:NAppt}, we review the surprisingly parallel words of global complex analytic and non-Archimedean pluripotential theory, respectively. The relation between the non-Archimedean and complex analytic worlds is explored in~\S\ref{sec:NAlimmet}, where we first prove some new results about maximal geodesic rays, and then set up a general framework for viewi... |
| 7 | 0.509 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction > Organisation of the paper | lines 335-346 | no | no | - | ...notations and results which will be used throughout the paper: we provide definitions and references to pluripotential theory. Section \ref{s:wsystem} is dedicated to establish the equivalence between the fourth-order PDE \eqref{wcsck} and the system of elliptic PDE's \eqref{weightedsystem:intro}. %In order to do so, in Lemma \ref{l:scalv} we establish the... |
| 8 | 0.502 | `corpus/arxiv/1810.04661/source/source.tex` | `text` | Introduction | lines 252-258 | no | no | - | ...singularity. \vspace{-0.3cm} \paragraph{Organization of the paper.} In Section 2 we recall basic facts about the $L^p$ Mabuchi geometry of the space of K\"ahler metrics, the relative Kolodziej type estimate of \cite{DDL4}, and we prove weighted versions of the classical inequalities of Clarkson and Ball--Carlen--Lieb that will be needed later. In Section 3... |
| 9 | 0.502 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Proofs of Lemmas \ref{s1is2}, \ref{s1is1} and \ref{s1is2overk} | lines 1659-1726 | no | no | - | \begin{thebibliography}{99} %\bibitem{atiyah} M.~F.~Atiyah, {\it Convexity and commuting hamiltonians}, %Bull. London Math. Soc. {\bf 14} (1982), 1--15. \bibitem{ACG1} V. Apostolov, D.~M.~J. Calderbank and P. Gauduchon, {\it The geometry of weakly self-dual K\"ahler surfaces}, Compositio Math. {\bf 135} (2003), 279--322. \bibitem{ACG2} V. Apostolov, D.~M.~J.... |
| 10 | 0.500 | `corpus/arxiv/2412.07968/source/main.tex` | `text` | Introduction | lines 635-663 | no | no | - | ...021_2} have shown that the existence of a unique cscK metric in a K\"ahler class is equivalent to the coercivity of the Mabuchi functional, whose minimizers are cscK metrics. Boucksom--Hisamoto--Jonsson~\cite{Boucksom_Hisamoto_Jonsson_2019} demonstrated that the coercivity of the Mabuchi functional implies uniform K-stability (see \cite{Dervan_Ross_2017, Der... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:

### negative_non_established_020 - negative/non-established claims

**Question:** Does the corpus establish that the local RAG system verifies mathematical proofs?

**Expected sources:** -
**Expected chunk types:** -
**Expected terms:** `RAG system`, `verifies mathematical proofs`, `establish`
**Preferred sections:** -
**Negative:** yes
**Review status:** `unreviewed`
**Review notes:** -
**Correction needed:** -

**Diagnostics:**
- Expected source in top-k: no
- Expected chunk type in top-k: no
- Expected terms in top-k: yes
- Citation-context chunks in top-k: 0
- Negative strong-looking evidence manual review needed: no

| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |
| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.617 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `text` | Futaki invariant computed with respect to the conically singular metrics > Some estimates for the conically singular metrics of elementary form | lines 1444-1445 | no | no | - | Pick a local coordinate system $(z_1 , \dots , z_n)$ around a point in $X$ so that $D$ is locally given by $\{ z_1 = 0 \}$. We then write |
| 2 | 0.527 | `corpus/arxiv/math_0511119/source/hfkg4.tex` | `text` | Constructions of WBF K\"ahler metrics > WBF K\"ahler metrics over a ruled surface | lines 1050-1056 | no | no | establish | Without loss, we look for solutions to $h_1(x_1,x_2)=0=h_2(x_1,x_2)$ with $x_1>x_2$ and $x_1>0$. Solving $h_1=0$ for $s_1$, we find that $s_1$ must be positive, hence $s_1=2/q_{1}$ for some integer $q_{1}\geq 1$. We then establish the following three lemmas, the proofs of which can be found in Appendix~\ref{appC}. |
| 3 | 0.552 | `corpus/arxiv/1508.02640/source/2017_11_16_conic_modified.tex` | `text` | Futaki invariant computed with respect to the conically singular metrics > Some estimates for the conically singular metrics of elementary form | lines 1493-1497 | no | no | - | %In particular, we have the following estimate which will be used several times in what follows. Suppose that $f$ is a function of order $\|z_1\|^{2 \beta}$. We now evaluate the Ricci curvature of $\hat{\omega}$. In terms of the local coordinate system $(z_1 , \dots , z_n)$ as above, we have |
| 4 | 0.418 | `corpus/arxiv/2104.09709/source/source.tex` | `text` | Introduction > Structure of the paper | lines 345-346 | no | no | establish | ...d from \cite{lahdili2, lahdili3}. In Section~\ref{s:v-KRS}, we recall the notion of $v$-solitons from \cite{M1,HL}, and establish the equivalences stated in Propositions~\ref{tilde v} and \ref{SE}. Sections \ref{s:coercivity} and \ref{s:stability} review and recast in the weighted setting respectively the coercivity principle of \cite{DaRu} and its applicati... |
| 5 | 0.414 | `corpus/arxiv/0805.0128/source/extremal2a.tex` | `text` | Introduction | lines 219-255 | no | no | - | ...rom the use of this estimate in Section 3, the only other restriction on $A$ comes when, in two places, we use the fact that $A$ is positive (in arguments involving the maximum principle) Thus the main result in this paper extends to positive functions $A$ if one assumes an {\it a priori} estimate (6). However the uses we make of (6) are to overcome some rat... |
| 6 | 0.382 | `corpus/arxiv/2407.09929/source/Weighted_cscK.tex` | `text` | Introduction > Organisation of the paper | lines 335-346 | no | no | establish | ...hich will be used throughout the paper: we provide definitions and references to pluripotential theory. Section \ref{s:wsystem} is dedicated to establish the equivalence between the fourth-order PDE \eqref{wcsck} and the system of elliptic PDE's \eqref{weightedsystem:intro}. %In order to do so, in Lemma \ref{l:scalv} we establish the alternative definition o... |
| 7 | 0.377 | `corpus/arxiv/2402.01159/source/ToricSurfacesModuli.tex` | `text` | Introduction | lines 295-300 | no | no | - | ...anifolds. Then, Section \ref{sec:foldable toric surfaces} is devoted to the classification of foldable surfaces and the proofs of Proposition \ref{prop:intro fans} and Proposition \ref{prop:intro}. In Section \ref{sec:local moduli construction}, we carry over the construction of the local moduli spaces, and prove Theorem \ref{theo:intro}. Finally, in Section... |
| 8 | 0.372 | `corpus/arxiv/1801.05907/source/source.tex` | `text` | Introduction | lines 284-292 | no | no | - | ...igurations which is an one-parameter family of K\"ahler potentials, concave with respect to this parameter. They proved that each analytic test configuration defines a unique geodesic ray (up to parallelism), thus defines a point at ${\mathcal S}_\infty.$ It is important to understand the converse: when does a locally finite energy geodesic ray define a test... |
| 9 | 0.362 | `corpus/arxiv/1803.09506/source/source.tex` | `remark` | Introduction | lines 281-283 | no | no | - | \begin{rem} We remark that when $Aut(X;D)$ is discrete, those results cover the important example in the K\"ahler-Einstein problem. That is when $X$ is a Fano manifold and $D$ is a smooth divisor in the linear system $\|-\lambda K_X\|$ for some $\lambda\in \mathbb Z^+$, there does not exist any holomorphic vector field tangential to $D$ \cite{MR2975584,MR31075... |
| 10 | 0.358 | `corpus/arxiv/math_0401320/source/hfkg2.tex` | `text` | Hamiltonian actions and toric geometry > Compatible K\"ahler metrics: compactification | lines 676-699 | no | no | establish | Note that this lemma makes essential use of the completeness of $(M,g)$. It can, however, be extended to compact orbifolds, for instance by lifting the distance isometry to compatible uniformizing charts. On the other hand we learn nothing about the dependence of the angular coordinates on metrics which induce different $S^2\mathfrak{t}$-valued functions on... |

**Manual relevance notes:**
- rank 1:
- rank 2:
- rank 3:

Promote to gold? yes/no

Correction needed:
