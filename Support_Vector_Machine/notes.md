### Support Vector Machine

1. Imagine you're trying to separate two different groups of points (like red and blue dots) on a piece of paper. Your goal is to draw a straight line (or a curve in more complex cases) that perfectly divides them.

2. Here we've got another challenge to tackle:

   - There are many possbile lines that can separate the two groups.
   - We want to find the best one, of them.

3. This is where the **_Support Vector Machine (SVM)_** comes in the picture. Let's go step by step.

**Step-1 What is SVM?**:

- SVM is a supervised learning algorithm used for classification and regression problems.
- It finds the best boundary (decision boundary) that maximizes the margin between two classes.

**Step-2 Working of SVM**:

- Initially we find a line or plane that separates the classes perfectly, this line / plane is called as **Hyperplane**.
- The closest points to this hyperplane of any of the classes are called as _support vectors_. The distance between these support vectors and the hyperplane should be as large as possible.
- The wider the margin between the support vectors and hyperplane is, the better its generalization to newer data would be.
- These points (support vectors) which are closest to the hyperplane define the decision boundary.
- [**NOTE**] If the data is perfectly linearly separable, SVM finds the best straight-line separator. If not, it can use a trick called the **Kernel Trick** to separate data with curves.

**Step-3 Types of SVM**:

- _Linear SVM_ → Works when data can be separated with a straight line.
- _Non-Linear SVM_ → Uses kernels (like polynomial or radial basis function (RBF)) to handle complex data.
