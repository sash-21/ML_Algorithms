### Gradient Descent

1. Suppose a person is said to walk down a hill and is blindfolded. He can't see the bottom but feel the slope under the feet. The person would take steps on the slope where he feels the slops is going downwards. Eventually, the person reaches the lowest point on the hill.

2. Now lets go step by step:

**Step-1 What is a Loss Function?**:

- Imagine you are training a machine learning model. The goal is to find the best parameters (weights) for the model so that it makes accurate predictions. The way we measure how good or bad the model is doing is using a Loss Function (also called a Cost Function).
- Think of the Loss Function as the height of a hill. Our job is to find the lowest point on this hill—that’s where the loss is the smallest, meaning our model is performing well.
- There are different types of Cost Functions / Loss Functions, to name one it is, **Mean Squared Error (MSE)** which is also the most prominent one.

**Step-2 What is a Gradient?**:

- The gradient is like the slope of the hill. If you’re walking down a hill, the gradient tells you in which direction the ground is sloping downward.
  1. If the slope is steep, you take bigger steps.
  2. If the slope is less steep, you take smaller steps.
  3. When the slope is completely flat (zero gradient), you’ve reached the lowest point.

**Step-3 How does Gradient Descent Work?**:

- Gradient Descent is just a process where we:
  1. Start at a random point on the hill (random initial values for our model’s parameters).
  2. Calculate the gradient (slope) at that point.
  3. Take a small step in the opposite direction of the gradient (going downhill).
  4. Repeat until we reach the lowest point.
- Mathematically, the update rule is:

```math
    θ\=θ−α⋅dθdJ
```

- where:
  1. θ represents the parameters (weights) of the model.
  2. α (learning rate) controls how big a step we take.
  3. dθ/dJ is the gradient (the slope of the hill).

**Step-4 Learning Rate (How Big Are Our Steps?)**:

- The learning rate (α) is like deciding how big your steps should be:

  1. If you take very small steps, it will take too long to reach the bottom.
  2. If you take very big steps, you might miss the lowest point and keep overshooting.

- If I want to take an another example here, suppose you have opened a Coffee Shop and you have to find a right spot for the price of the coffee you want to sell. There can be 3 scenarios:

  1. If you make the price too high, this can lead to loss of customers (Fail Condition)
  2. If you make the price too less, this can lead to loss of money invested (Fail Condition)
  3. Price is set to a sweet spot where both the above conditions are minimized to the maximum, hence making profit.

- So you would keep an initial price of suppose `5$` for the coffee, and from there you'll increase or decrease the price where you think all the conditions are meeting making it a sweet spot.

**Step-5 Stopping Condition**:

- We stop when either:
  1. The gradient (slope) becomes very small (almost flat ground).
  2. We reach the maximum number of steps (iterations).
