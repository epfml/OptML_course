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
   - Atli Kosson [atli.kosson@epfl.ch](mailto:atli.kosson@epfl.ch) 
   - Dongyang Fan [dongyang.fan@epfl.ch](mailto:dongyang.fan@epfl.ch)
   - Oguz Kaan Yüksel [oguz.yuksel@epfl.ch](mailto:oguz.yuksel@epfl.ch)
   
`Contents:`

Convexity, Gradient Methods, Proximal algorithms, Subgradient Methods, Stochastic and Online Variants of mentioned methods, Coordinate Descent, Frank-Wolfe, Accelerated Methods, Primal-Dual context and certificates, Lagrange and Fenchel Duality, Second-Order Methods including Quasi-Newton Methods, Derivative-Free Optimization.

*Advanced Contents:*

Parallel and Distributed Optimization Algorithms, Federated Learning

Computational Trade-Offs (Time vs Data vs Accuracy), Lower Bounds

Non-Convex Optimization: Convergence to Critical Points, Alternating minimization, Neural network training

### Program:
| Nr | Date  | Topic                                                 | Materials                                                                                                  | Exercises                             |
| -- | ----- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| 1  | 23.2. | Introduction, Convexity                               | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture01.pdf) | [lab00](../../raw/master/labs/ex00/exercise00.pdf) |
| 2  | 1.3.  | Gradient Descent                                      | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture02.pdf)  | [lab01](../../raw/master/labs/ex01/exercise01.pdf) |
| 3  | 8.3.  | Projected Gradient Descent                            | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture03.pdf) | [lab02](../../raw/master/labs/ex02/exercise02.pdf) |
| 4  | 15.3. | Proximal and Subgradient Descent                      | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), [slides](../../raw/master/slides/lecture04.pdf) | [lab03](../../raw/master/labs/ex03/exercise03.pdf) |
| 5  | 22.3. | Stochastic Gradient Descent, Non-Convex Optimization  | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), slides | lab04 |
| .  | 29.3. | `easter vacation`                                     |                                                                                                            | -                                     |
| .  | 5.4.  | `easter vacation`                                     |                                                                                                            | -                                     |
| 6  | 12.4. | Non-Convex Optimization                               | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), slides | lab05 |
| 7  | 19.4. | Newton's Method & Quasi-Newton                        | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), slides | lab06 |
| 8  | 26.4. | Coordinate Descent                                    | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), slides | lab07 |
| 9  |  3.5. | Frank-Wolfe                                           | [notes](../../raw/master/lecture_notes/lecture-notes.pdf), slides | lab08 |
| 10 | 10.5. | `Mini-Project week`                                   |                                                                                                            | -
| 11 | 17.5. | Accelerated Gradient, Gradient-free, adaptive methods | notes,  slides                                                    | lab09 |
| 12 | 24.5. | Opt for ML in Practice                                | notes,  slides                                                    | lab10                                  |
| 13 | 31.5. | Opt for ML in Practice                                | notes, slides                                                     | Q&A Projects                          |


### Videos:
- [Public playlist of 2021 videos (youtube)](https://www.youtube.com/playlist?list=PL4O4bXkI-fAeYrsBqTUYn2xMjJAqlFQzX)
- [Playlist of 2022 videos (EPFL internal)](https://tube.switch.ch/switchcast/epfl.ch/series/4fab28ac-1c8f-4632-8d01-e128746b7a1d)
- [Playlist of 2024 videos (EPFL internal)](https://mediaspace.epfl.ch/channel/CS-439+Optimization+for+machine+learning/31980)

### Exercises:
The [weekly exercises](../../tree/master/labs/) consist of a mix of theoretical and practical `Python` exercises for the corresponding topic each week (starting week 2). Solutions to exercises are available in the lab folder.

### Project:
A `mini-project` will focus on the practical implementation: Here we encourage students to investigate the real-world performance of one of the studied optimization algorithms or variants, helping to provide solid empirical evidence for some behaviour aspects on a real machine-learning task. The project is mandatory and done in groups of 3 students. It will count 30% to the final grade. Project reports (3 page PDF) are due June 14th. Here is a [detailed project description](../../raw/master/labs/mini-project/miniproject_description.pdf).

### Assessment:
Session Exam on Monday 01.07.2024 from 15h15 to 18h15 (INM200, INM202). Format: Closed book. Theoretical questions similar to exercises. You are allowed to bring one cheat sheet (A4 size paper, both sides can be used).

For practice: 
- exams [2023](../../raw/master/exams/exam2023.pdf), [2022](../../raw/master/exams/exam2022.pdf), [2021](../../raw/master/exams/exam2021.pdf), [2020](../../raw/master/exams/exam2020.pdf), [2019](../../raw/master/exams/exam2019.pdf), [2018](../../raw/master/exams/exam2018.pdf)
- solutions [2023](../../raw/master/exams/exam2023solutions.pdf), [2022](../../raw/master/exams/exam2022solutions.pdf), [2021](../../raw/master/exams/exam2021solutions.pdf), [2020](../../raw/master/exams/exam2020solutions.pdf), [2019](../../raw/master/exams/exam2019solutions.pdf), [2018](../../raw/master/exams/exam2018solutions.pdf).

### Links to related courses and materials 
 - [CMU 10-725](https://www.stat.cmu.edu/~ryantibs/convexopt-F18/)
 - [Berkeley EE-227C](https://ee227c.github.io/)
 
### Recommended Books
 - [Convex Optimization: Algorithms and Complexity](https://arxiv.org/pdf/1405.4980.pdf), by Sébastien Bubeck (free online)
 - [Convex Optimization](http://stanford.edu/~boyd/cvxbook/), Stephen Boyd and Lieven Vandenberghe (free online)
 - [Introductory Lectures on Convex Optimization](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.693.855&rep=rep1&type=pdf), Yurii Nesterov (free online)
