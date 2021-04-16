# EPFL Course - Optimization for Machine Learning - CS-439

[Official coursebook information](http://edu.epfl.ch/coursebook/en/optimization-for-machine-learning-CS-439)

`Lectures:` Posted every monday on youtube

`Q&A:` Fri 13:15-14:00 on zoom

`Exercises:` Fri 14:15-16:00 on zoom

This course teaches an overview of modern mathematical optimization methods, for applications in machine learning and data science. In particular, scalability of algorithms to large datasets will be discussed in theory and in implementation.

### Team
 - Instructors: 
   - Martin Jaggi [martin.jaggi@epfl.ch](mailto:martin.jaggi@epfl.ch)
   - Nicolas Flammarion [nicolas.flammarion@epfl.ch](mailto:nicolas.flammarion@epfl.ch)
 - Assistants:
   - Jean-Baptiste Cordonnier [jean-baptiste.cordonnier@epfl.ch](mailto:jean-baptiste.cordonnier@epfl.ch)
   - Lie He [lie.he@epfl.ch](mailto:lie.he@epfl.ch)
   - Scott Pesme [scott.pesme@epfl.ch](mailto:scott.pesme@epfl.ch)
   - Thijs Vogels [thijs.vogels@epfl.ch](mailto:thijs.vogels@epfl.ch)

`Contents:`

Convexity, Gradient Methods, Proximal algorithms, Subgradient Methods, Stochastic and Online Variants of mentioned methods, Coordinate Descent, Frank-Wolfe, Accelerated Methods, Primal-Dual context and certificates, Lagrange and Fenchel Duality, Second-Order Methods including Quasi-Newton Methods, Derivative-Free Optimization.

*Advanced Contents:*

Parallel and Distributed Optimization Algorithms

Computational Trade-Offs (Time vs Data vs Accuracy), Lower Bounds

Non-Convex Optimization: Convergence to Critical Points, Alternating minimization, Neural network training

### Program:
| Nr  | Date  | Topic                                                 | Materials                                                                                                   | Exercises                             |
| --- | ----- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| #1  | 26.2. | Introduction, Convexity                               | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture01.pdf)  | [lab01](../../tree/master/labs/ex01/) |
| #2  | 5.3.  | Gradient Descent                                      | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture02.pdf)  | [lab02](../../tree/master/labs/ex02/) |
| #3  | 12.3. | Projected Gradient Descent                            | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides ](../../raw/master/slides/lecture03.pdf) | [lab03](../../tree/master/labs/ex03/) |
| #4  | 19.3. | Proximal and Subgradient Descent                      | [notes](../../raw/master/lecture_notes/lecture-notes.pdf),[slides ](../../raw/master/slides/lecture04.pdf)  | [lab04](../../tree/master/labs/ex04/) |
| #5  | 26.3. | Stochastic Gradient Descent, Non-Convex Optimization  |  [notes](../../raw/master/lecture_notes/lecture-notes.pdf),[slides ](../../raw/master/slides/lecture05.pdf)  | [lab05](../../tree/master/labs/ex05/) |
| .   | 2.4.  | `easter vacation`                                     |                                                                                                             | -                                     |
| .   | 9.4.  | `easter vacation`                                     |                                                                                                             | -                                     |
| #6  | 16.4. | Non-Convex Optimization, Accelerated Gradient Descent | [notes](../../raw/master/lecture_notes/lecture-notes.pdf),[slides ](../../raw/master/slides/lecture06.pdf) | lab06                                 |
| #7  | 23.4. | Newton's Method & Quasi-Newton                        | notes,slides                                                                                                | lab07                                 |
| #8  | 30.4. | Frank-Wolfe                                           | notes,slides                                                                                                | lab08                                 |
| #9  | 7.5.  | Coordinate Descent                                    | notes,slides                                                                                                | lab09                                 |
| #10 | 14.5. | Duality, Gradient-free, adaptive methods              | notes,slides                                                                                                | lab10                                 |
| #11 | 28.5. | Opt for ML in Practice                                | notes,slides                                                                                                | Q&A                                   |
| #12 | 4.6.  | Opt for ML in Practice                                | notes,slides                                                                                                | Q&A Projects                          |
| #13 | 11.4. | `Mini-Project week`                                   |                                                                                                             |

### Exercises:
The [weekly exercises](../../tree/master/labs/) consist of a mix of theoretical and practical `Python` exercises for the corresponding topic each week (starting week 2). Solutions to theory exercises are available [here](../../tree/master/lecture_notes), and for practicals in the lab folder.

### Project:
A `mini-project` will focus on the practical implementation: Here we encourage students to investigate the real-world performance of one of the studied optimization algorithms or variants, helping to provide solid empirical evidence for some behaviour aspects on a real machine-learning task. The project is mandatory and done in groups of 3 students. It will count 20% to the final grade. Project reports (3 page PDF) are due June 18th. Here is a [detailed project description](../../raw/master/labs/mini-project/miniproject_description.pdf).

### Assessment:
Final written exam in exam session on Thursday 08.07.2021 from 08h15 to 11h15 (CE1, PO01). _Format: Closed book. Theoretical questions similar to exercises. You are allowed to bring one cheat sheet (A4 size paper, both sides can be used), either handwritten or 11 point minimum font size._
For practice: [exam 2019](../../raw/master/exams/exam2019.pdf), [solutions 2019](../../raw/master/exams/exam2019solutions.pdf), [exam 2018](../../raw/master/exams/exam2018.pdf), [solutions 2018](../../raw/master/exams/exam2018solutions.pdf).

### Links to related courses and materials 
 - [CMU 10-725](https://www.stat.cmu.edu/~ryantibs/convexopt-F18/)
 - [Berkeley EE-227C](https://ee227c.github.io/)
 
### Recommended Books
 - [Convex Optimization: Algorithms and Complexity](https://arxiv.org/pdf/1405.4980.pdf), by Sébastien Bubeck (free online)
 - [Convex Optimization](http://stanford.edu/~boyd/cvxbook/), Stephen Boyd and Lieven Vandenberghe (free online)
 - [Introductory Lectures on Convex Optimization](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.693.855&rep=rep1&type=pdf), Yurii Nesterov (free online)
