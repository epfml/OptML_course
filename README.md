# EPFL Course - Optimization for Machine Learning - CS-439

[Official coursebook information](http://edu.epfl.ch/coursebook/en/optimization-for-machine-learning-CS-439)

`Lectures:` Fri 13:15-15:00 in [CO2](https://plan.epfl.ch/?room==CO%202)

`Exercises:` Fri 15:15-17:00 in [BC01](https://plan.epfl.ch/?room==BC%2001)

This course teaches an overview of modern mathematical optimization methods, for applications in machine learning and data science. In particular, scalability of algorithms to large datasets will be discussed in theory and in implementation.

### Team
 - Instructors: 
   - Martin Jaggi [martin.jaggi@epfl.ch](mailto:martin.jaggi@epfl.ch)
   - Nicolas Flammarion [nicolas.flammarion@epfl.ch](mailto:nicolas.flammarion@epfl.ch)
 - Assistants:
   - Aditya Varre [aditya.varre@epfl.ch](mailto:aditya.varre@epfl.ch)
   - Amirkeivan Mohtashami [amirkeivan.mohtashami@epfl.ch](mailto:amirkeivan.mohtashami@epfl.ch)
   - Matteo Pagliardini [matteo.pagliardini@epfl.ch](mailto:matteo.pagliardini@epfl.ch)
   - Scott Pesme [scott.pesme@epfl.ch](mailto:scott.pesme@epfl.ch)

`Contents:`

Convexity, Gradient Methods, Proximal algorithms, Subgradient Methods, Stochastic and Online Variants of mentioned methods, Coordinate Descent, Frank-Wolfe, Accelerated Methods, Primal-Dual context and certificates, Lagrange and Fenchel Duality, Second-Order Methods including Quasi-Newton Methods, Derivative-Free Optimization.

*Advanced Contents:*

Parallel and Distributed Optimization Algorithms

Computational Trade-Offs (Time vs Data vs Accuracy), Lower Bounds

Non-Convex Optimization: Convergence to Critical Points, Alternating minimization, Neural network training

### Program:
| Nr  | Date  | Topic                                                 | Materials                                                                                                  | Exercises                             |
| --- | ----- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| 1  | 25.2. | Introduction, Convexity                               | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture01.pdf) | [lab01](../../tree/master/labs/ex01/) |
| 2  | 4.3.  | Gradient Descent                                      | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture02.pdf) | [lab02](../../tree/master/labs/ex02/) |
| 3  | 11.3. | Projected Gradient Descent                            | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture03.pdf) | [lab03](../../tree/master/labs/ex03/) |
| 4  | 18.3. | Proximal and Subgradient Descent                      | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture04.pdf) | [lab04](../../tree/master/labs/ex04/) |
| 5  | 25.3. | Stochastic Gradient Descent, Non-Convex Optimization  | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture05.pdf) | [lab05](../../tree/master/labs/ex05/) |
| 6  | 1.4.  | Non-Convex Optimization, Accelerated Gradient Descent | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture06.pdf) | [lab06](../../tree/master/labs/ex06/) |
| 7  | 8.4.  | Newton's Method & Quasi-Newton                        | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture07.pdf) | [lab07](../../tree/master/labs/ex07/) |
| .  | 15.4. | `easter vacation`                                     |                                                                                                            | -                                     |
| .  | 22.4. | `easter vacation`                                     |                                                                                                            | -                                     |
| 8  | 29.4. | Coordinate Descent                                    | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture08.pdf) | [lab08](../../tree/master/labs/ex08/) |
| 9  | 6.5.  | Frank-Wolfe                                           | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture09.pdf) | [lab09](../../tree/master/labs/ex09/) |
| 10 | 13.5. | Accelerated Gradient, Gradient-free, adaptive methods              | notes,  [slides](../../raw/master/slides/lecture10.pdf)                                                         | [lab10](../../tree/master/labs/ex10/) |
| 11 | 20.5. | Opt for ML in Practice                                | notes,  [slides](../../raw/master/slides/lecture11.pdf)                                                                     | Q&A                                   |
| 12 | 27.5. | `Mini-Project week`                                   |                                                                                                            | -
| 13 | 3.6.  | Opt for ML in Practice                                | notes,  [slides](../../raw/master/slides/lecture12.pdf)                                                                                                             | Q&A Projects                          |

### Videos:
- [Public playlist of 2021 videos (youtube)](https://www.youtube.com/playlist?list=PL4O4bXkI-fAeYrsBqTUYn2xMjJAqlFQzX)
- [Playlist of current 2022 videos (EPFL internal)](https://tube.switch.ch/switchcast/epfl.ch/series/4fab28ac-1c8f-4632-8d01-e128746b7a1d)

### Exercises:
The [weekly exercises](../../tree/master/labs/) consist of a mix of theoretical and practical `Python` exercises for the corresponding topic each week (starting week 2). Solutions to theory exercises are available [here](../../tree/master/lecture_notes), and for practicals in the lab folder.

### Project:
A `mini-project` will focus on the practical implementation: Here we encourage students to investigate the real-world performance of one of the studied optimization algorithms or variants, helping to provide solid empirical evidence for some behaviour aspects on a real machine-learning task. The project is mandatory and done in groups of 3 students. It will count 25% to the final grade. Project reports (3 page PDF) are due June 17th. Here is a [detailed project description](../../raw/master/labs/mini-project/miniproject_description.pdf).

### Assessment:
Final written exam in exam session on Thursday 07.07.2022 from 09h15 to 12h15 (in CE1, CE1106, CE3) _Format: Closed book. Theoretical questions similar to exercises. You are allowed to bring one cheat sheet (A4 size paper, both sides can be used)._
For practice: [exam 2020](../../raw/master/exams/exam2020.pdf), [solutions 2020](../../raw/master/exams/exam2020solutions.pdf), [exam 2019](../../raw/master/exams/exam2019.pdf), [solutions 2019](../../raw/master/exams/exam2019solutions.pdf), [exam 2018](../../raw/master/exams/exam2018.pdf), [solutions 2018](../../raw/master/exams/exam2018solutions.pdf).

### Links to related courses and materials 
 - [CMU 10-725](https://www.stat.cmu.edu/~ryantibs/convexopt-F18/)
 - [Berkeley EE-227C](https://ee227c.github.io/)
 
### Recommended Books
 - [Convex Optimization: Algorithms and Complexity](https://arxiv.org/pdf/1405.4980.pdf), by Sébastien Bubeck (free online)
 - [Convex Optimization](http://stanford.edu/~boyd/cvxbook/), Stephen Boyd and Lieven Vandenberghe (free online)
 - [Introductory Lectures on Convex Optimization](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.693.855&rep=rep1&type=pdf), Yurii Nesterov (free online)
