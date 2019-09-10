# Reinforcement_Learning
Reinforcement learning is an area of machine learning concerned with how software agents ought to take actions in an environment so as to maximize some notion of cumulative reward


# Epsilon-Greedy algorithm
To get you started thinking algorithmically about the Explore-Exploit dilemma, you should leran how to code up one of the simplest possible algorithms for trading off exploration and exploitation. This algorithm is called the epsilon-Greedy algorithm. In computer science, a greedy algorithm is an algorithm that always takes whatever action seems best at the present moment, even when that decision might lead to bad long term consequences. The epsilon-Greedy algorithm is almost a greedy algorithm because it generally exploits the best available option, but every once in a while the epsilon-Greedy algorithm explores the other available options. As we’ll see, the term epsilon in the algorithm’s name refers to the odds that the algorithm explores instead of exploiting [Bandit Algorithms for Website Optimization by John Myles White].


# Optimistic Initial Values
Another way to solve the Explore exploit dilemma called the optimistic initial values method.


# Upper Confidence Bound Algorithm (UCB)
The algorithm is based on the principle of optimism in the face of uncertainty, which is to choose your actions as if the environment (in this case bandit) is as nice as is plausibly possible. By this we mean that the unknown mean payoffs of each arm is as large as plausibly possible based on the data that has been observed (unfounded optimism will not work — see the illustration on the right!). The intuitive reason that this works is that when acting optimistically one of two things happens. Either the optimism was justified, in which case the learner is acting optimally, or the optimism was not justified. In the latter case the agent takes some action that they believed might give a large reward when in fact it does not. If this happens sufficiently often, then the learner will learn what is the true payoff of this action and not choose it in the future. 
