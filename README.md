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
   - Yitao Xu [yitao.xu@epfl.ch](mailto:yitao.xu@epfl.ch)
   - Gizem Yüce [gizem.yuce@epfl.ch](mailto:gizem.yuce@epfl.ch)
   - Mark Rofin [mark.rofin@epfl.ch](mailto:mark.rofin@epfl.ch)

   
`Contents:`

Convexity, Gradient Methods, Proximal algorithms, Subgradient Methods, Stochastic and Online Variants of mentioned methods, Coordinate Descent, Frank-Wolfe, Accelerated Methods, Primal-Dual context and certificates, Lagrange and Fenchel Duality, Second-Order Methods including Quasi-Newton Methods, Derivative-Free Optimization.

*Advanced Contents:*

Parallel and Distributed Optimization Algorithms, Federated Learning

Computational Trade-Offs (Time vs Data vs Accuracy), Lower Bounds

Non-Convex Optimization: Convergence to Critical Points, Alternating minimization, Neural network training

### Program:
| Nr | Date  | Topic                                                 | Materials                                                                                                  | Exercises                             |
| -- | ----- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| 1  | 20.2. | Introduction, Convexity                               |  [slides](../../raw/main/slides/lecture01.pdf)| [lab00](../../raw/main/labs/ex00/exercise00.pdf)|
| 2  | 27.2.  | Gradient Descent                                      |  [slides](../../raw/main/slides/lecture02.pdf)  | [lab01](../../raw/main/labs/ex01/exercise01.pdf)  |
| 3  | 6.3.  | Projected Gradient Descent                            |   -  | -  |
| 4  | 13.3. | Proximal and Subgradient Descent                      |  -  |  -   |
| 5  | 20.3. | Stochastic Gradient Descent, Non-Convex Optimization  |  -  | -   |
| 6  | 27.3. | Non-Convex Optimization                               | -  | -   |
| .  | 3.4. | `Easter vacation`                                     |                                                                                                            | -                                     |
| .  | 10.4.  | `Easter vacation`                                     |                                                                                                            | -                                     |
| 7  |  17.4. | Frank-Wolfe                                           |  -   | -  |
| 8  | 24.4. | Newton's Method & Quasi-Newton                        | -  | -   |
| 9  | 1.5. | Coordinate Descent                                    |  -    |
| 10 | 8.5. | Lower Bounds and Accelerated Gradient Descent |   -  | -  |
| 11 | 15.5.  | (`Ascension Day Bridge Day`)                                 |    -                                                  | Q & A Projects  | 
| 12 | 22.5.  | Gradient free and adaptive methods                           |  -                                                       | -                            |
| 13 | 29.5.  | Optimization for real-world AI model training        |  -                                                       | -                            |

### Lecture Notes:
The course is based on the following [lecture notes](../../raw/main/lecture_notes/lecture-notes.pdf).

### Videos:
The [videos](https://mediaspace.epfl.ch/channel/CS-439+Optimization+for+machine+learning/31980) of the lectures for each week will be available.

### Exercises:
The [weekly exercises](../../tree/main/labs/) consist of a mix of theoretical and practical `Python` exercises for the corresponding topic each week (starting week 2). Solutions to exercises are available in the lab folder.

### Forum:
[Discussion forum](https://edstem.org/eu/courses/2242/discussion) (EPFL internal)

### Project:
A `mini-project` will focus on the practical implementation: Here we encourage students to investigate the real-world performance of one of the studied optimization algorithms or variants, helping to provide solid empirical evidence for some behaviour aspects on a real machine-learning task. The project is mandatory and done in groups of 3 students. It will count 30% to the final grade. Project reports (3 page PDF) are due June 12th. Here is a [detailed project description](../../raw/main/labs/mini-project/miniproject_description.pdf).

### Assessment:
Session Exam. Format: Closed book. Theoretical questions similar to exercises. You are allowed to bring one cheat sheet (A4 size paper, both sides can be used).

For practice: 
- exams [2025](../../raw/main/exams/exam2025.pdf), [2024](../../raw/main/exams/exam2024.pdf), [2023](../../raw/main/exams/exam2023.pdf), [2022](../../raw/main/exams/exam2022.pdf), [2021](../../raw/main/exams/exam2021.pdf), [2020](../../raw/main/exams/exam2020.pdf), [2019](../../raw/main/exams/exam2019.pdf), [2018](../../raw/main/exams/exam2018.pdf)
- solutions [2025](../../raw/main/exams/exam2025solutions.pdf), [2024](../../raw/main/exams/exam2024solutions.pdf), [2023](../../raw/main/exams/exam2023solutions.pdf), [2022](../../raw/main/exams/exam2022solutions.pdf), [2021](../../raw/main/exams/exam2021solutions.pdf), [2020](../../raw/main/exams/exam2020solutions.pdf), [2019](../../raw/main/exams/exam2019solutions.pdf), [2018](../../raw/main/exams/exam2018solutions.pdf).

### Links to related courses and materials 
 - [CMU 10-725](https://www.stat.cmu.edu/~ryantibs/convexopt-F18/)
 - [Berkeley EE-227C](https://ee227c.github.io/)
 
### Recommended Books
 - [Convex Optimization: Algorithms and Complexity](https://arxiv.org/pdf/1405.4980.pdf), by Sébastien Bubeck (free online)
 - [Convex Optimization](http://stanford.edu/~boyd/cvxbook/), Stephen Boyd and Lieven Vandenberghe (free online)
 - [Introductory Lectures on Convex Optimization](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.693.855&rep=rep1&type=pdf), Yurii Nesterov (free online)
