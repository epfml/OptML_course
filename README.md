# EPFL Course - Optimization for Machine Learning - CS-439

[Official coursebook information](http://edu.epfl.ch/coursebook/en/optimization-for-machine-learning-CS-439)

`Lectures:` Fri 13:15-15:00 in [CO2](https://plan.epfl.ch/?room==CO%202)

`Exercises:` Fri 15:15-17:00 in [BC01](https://plan.epfl.ch/?room==BC%2001)

This course teaches an overview of modern mathematical optimization methods, for applications in machine learning and data science. In particular, scalability of algorithms to large datasets will be discussed in theory and in implementation.

### Team
 - Instructors: 
   - Nicolas Flammarion [nicolas.flammarion@epfl.ch](mailto:nicolas.flammarion@epfl.ch)
 - Assistants:
   - Aditya Varre [aditya.varre@epfl.ch](mailto:aditya.varre@epfl.ch)
   - Oguz Kaan Yüksel [oguz.yuksel@epfl.ch](mailto:oguz.yuksel@epfl.ch)
   - Thomas Weinberger [thomas.weinberger@epfl.ch](mailto:thomas.weinberger@epfl.ch)
   - Yitao Xu [yitao.xu@epfl.ch](mailto:yitao.xu@epfl.ch)

 

   
`Contents:`

Convexity, Gradient Methods, Proximal algorithms, Subgradient Methods, Stochastic and Online Variants of mentioned methods, Coordinate Descent, Frank-Wolfe, Accelerated Methods, Primal-Dual context and certificates, Lagrange and Fenchel Duality, Second-Order Methods including Quasi-Newton Methods, Derivative-Free Optimization.

*Advanced Contents:*

Parallel and Distributed Optimization Algorithms, Federated Learning

Computational Trade-Offs (Time vs Data vs Accuracy), Lower Bounds

Non-Convex Optimization: Convergence to Critical Points, Alternating minimization, Neural network training

### Program:
| Nr | Date  | Topic                                                 | Materials                                                                                                  | Exercises                             |
| -- | ----- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| 1  | 21.2. | Introduction, Convexity                               |  [slides](../../raw/master/slides/lecture01.pdf)| [lab00](../../raw/master/labs/ex00/exercise00.pdf)|
| 2  | 28.2.  | Gradient Descent                                      |  slides| lab01 |
| 3  | 7.3.  | Projected Gradient Descent                            |  slides | lab02|
| 4  | 14.3. | Proximal and Subgradient Descent                      | slides| lab03 |
| 5  | 21.3. | Stochastic Gradient Descent, Non-Convex Optimization  |  slides | lab04 |
| 6  | 28.3. | Non-Convex Optimization                               | slides | lab05 |
| 7  | 4.4. | Newton's Method & Quasi-Newton                        | slides | lab06 |
| 8  | 11.4. | Coordinate Descent                                    |  slides | lab07 |
| .  | 18.4. | `easter vacation`                                     |                                                                                                            | -                                     |
| .  | 25.4.  | `easter vacation`                                     |                                                                                                            | -                                     |
| 9  |  2.5. | Frank-Wolfe                                           |  slides | lab08 |
| 10 | 9.5. | Accelerated Gradient, Gradient-free, adaptive methods |  slides    | lab09|
| 11 | 16.5.  | Opt for ML in Practice                                |  slides                                                    | lab10 | 
| 12 | 23.5.  | Opt for ML in Practice                                |  slides                                                     | Q&A Projects                          |
| 13 | 30.5. | `Mini-Project week`                                   |                                                                                                            | -                                     |

### Lecture Notes:
The course is based on the following [lecture notes](../../raw/master/lecture_notes/lecture-notes.pdf).

### Videos:
- [Playlist of 2024/2025 videos (EPFL internal)](https://mediaspace.epfl.ch/channel/CS-439+Optimization+for+machine+learning/31980)
- [Public playlist of 2021 videos (youtube)](https://www.youtube.com/playlist?list=PL4O4bXkI-fAeYrsBqTUYn2xMjJAqlFQzX)

### Exercises:
The [weekly exercises](../../tree/master/labs/) consist of a mix of theoretical and practical `Python` exercises for the corresponding topic each week (starting week 2). Solutions to exercises are available in the lab folder.

[Discussion forum](https://edstem.org/eu/courses/2015/discussion/) (EPFL internal)

### Project:
A `mini-project` will focus on the practical implementation: Here we encourage students to investigate the real-world performance of one of the studied optimization algorithms or variants, helping to provide solid empirical evidence for some behaviour aspects on a real machine-learning task. The project is mandatory and done in groups of 3 students. It will count 30% to the final grade. Project reports (3 page PDF) are due June 14th. Here is a [detailed project description](../../raw/master/labs/mini-project/miniproject_description.pdf).

### Assessment:
Session Exam. Format: Closed book. Theoretical questions similar to exercises. You are allowed to bring one cheat sheet (A4 size paper, both sides can be used).

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
