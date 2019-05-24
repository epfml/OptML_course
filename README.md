# EPFL Course - Optimization for Machine Learning - CS-439

[Official coursebook information](http://edu.epfl.ch/coursebook/en/optimization-for-machine-learning-CS-439)

`Lectures:` Fri 13:15-15:00 in [BC01](https://plan.epfl.ch/?room==BC%2001)

`Exercises:` Fri 15:15-17:00 in [BC01](https://plan.epfl.ch/?room==BC%2001)

This course teaches an overview of modern mathematical optimization methods, for applications in machine learning and data science. In particular, scalability of algorithms to large datasets will be discussed in theory and in implementation.

### Team
 - Instructor: Martin Jaggi [martin.jaggi@epfl.ch](mailto:martin.jaggi@epfl.ch)
 - Assistants:
   - Anastasia Koloskova [anastasia.koloskova@epfl.ch](mailto:anastasia.koloskova@epfl.ch)
   - Sai Praneeth Karimireddy [sai.karimireddy@epfl.ch](mailto:prakhar.gupta@epfl.ch)
   - Thijs Vogels [thijs.vogels@epfl.ch](mailto:thijs.vogels@epfl.ch)
   - Nicolas El Maalouly [nicolas.elmaalouly@epfl.ch](mailto:nicolas.elmaalouly@epfl.ch)

`Contents:`

Convexity, Gradient Methods, Proximal algorithms, Subgradient Methods, Stochastic and Online Variants of mentioned methods, Coordinate Descent, Frank-Wolfe, Accelerated Methods, Primal-Dual context and certificates, Lagrange and Fenchel Duality, Second-Order Methods including Quasi-Newton Methods, Derivative-Free Optimization.

*Advanced Contents:*

Parallel and Distributed Optimization Algorithms

Computational Trade-Offs (Time vs Data vs Accuracy), Lower Bounds

Non-Convex Optimization: Convergence to Critical Points, Alternating minimization, Neural network training

### Program:
Nr | Date | Topic | Materials | Exercises
--- | --- | --- | --- | ---
#1 | 22.2. | Introduction, Convexity | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture01.pdf)| [lab01](../../tree/master/labs/ex01/)
#2 |  1.3. | Gradient Descent | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture02.pdf)| [lab02](../../tree/master/labs/ex02/)
#3 |  8.3. | Projected Gradient Descent | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture03.pdf)| [lab03](../../tree/master/labs/ex03/)
#4 | 15.3. | Projected, Proximal and Subgradient Descent | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture04.pdf)| [lab04](../../tree/master/labs/ex04/)
#5 | 22.3. | Subgradient, Stochastic Gradient Descent | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture05.pdf)| [lab05](../../tree/master/labs/ex05/)
#6 | 29.3. | SGD, Non-Convex Optimization | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture06.pdf)| [lab06](../../tree/master/labs/ex06/)
#7 |  5.4. | Non-Convex Opt., Newton's Method | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture07.pdf)| [lab07](../../tree/master/labs/ex07/)
#8 | 12.4. | Newton & Quasi-Newton | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture08.pdf)| [lab08](../../tree/master/labs/ex08/)
. | 19.4. | `easter vacation` | | -
. | 26.4. | `easter vacation` | | -
#9 |  3.5. | Frank-Wolfe | notes, [slides](../../raw/master/slides/lecture09.pdf)| [lab09](../../tree/master/labs/ex09/)
#10 | 10.5. | Coordinate Descent | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture10.pdf)| [lab10](../../tree/master/labs/ex10/)
#11 | 17.5. | Duality, Gradient-free methods, Applications | notes, [slides](../../raw/master/slides/lecture11.pdf)| [lab11](../../tree/master/labs/ex11/)
#12 | 24.5. | Opt for ML in Practice | notes, [slides](../../raw/master/slides/lecture12.pdf)
#13 | 31.5. | `Mini-Project week` | | 

### Exercises:
The [weekly exercises](../../tree/master/labs/) consist of a mix of theoretical and practical `Python` exercises for the corresponding topic each week (starting week 2). Solutions to theory exercises are available [here](../../tree/master/lecture_notes), and for practicals in the lab folder.

### Mini-project:
An optional `mini-project` will focus on the practical implementation: Here we encourage students to investigate the real-world performance of one of the studied optimization algorithms or variants, helping to provide solid empirical evidence for some behaviour aspects on a real machine-learning task. The project is optional and done in groups of 2-3 students. If students decide to do the project, and if their project grade exceeds their exam grade, it will count 20% to the final grade. Project reports (3 page PDF) are due May 31st. Here is a [detailed project description](../../raw/master/labs/mini-project/miniproject_description.pdf).

### Assessment:
Final written exam in exam session, 20.06.2019 from 08h15 to 11h15 (PO01 Polydôme). _Format: Closed book. Theoretical questions similar to exercises. You are allowed to bring one cheat sheet (A4 size paper, both sides can be used), either handwritten or 11 point minimum font size._
For practice: [exam of 2018](../../raw/master/exams/exam2018.pdf).

### Links to related courses and materials 
 - [CMU 10-725](http://www.cs.cmu.edu/~pradeepr/convexopt/)
 - [Berkeley EE-227C](https://ee227c.github.io/)
 
### Recommended Books
 - [Convex Optimization: Algorithms and Complexity](https://arxiv.org/pdf/1405.4980.pdf), by Sébastien Bubeck (free online)
 - [Convex Optimization](http://stanford.edu/~boyd/cvxbook/), Stephen Boyd and Lieven Vandenberghe (free online)
 - [Introductory Lectures on Convex Optimization](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.693.855&rep=rep1&type=pdf), Yurii Nesterov (free online)
