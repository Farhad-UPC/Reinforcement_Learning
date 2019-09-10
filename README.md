# Reinforcement_Learning
Reinforcement learning is an area of machine learning concerned with how software agents ought to take actions in an environment so as to maximize some notion of cumulative reward


# Epsilon-Greedy algorithm
To get you started thinking algorithmically about the Explore-Exploit dilemma, you should leran how to code up one of the simplest possible algorithms for trading off exploration and exploitation. This algorithm is called the epsilon-Greedy algorithm. In computer science, a greedy algorithm is an algorithm that always takes whatever action seems best at the present moment, even when that decision might lead to bad long term consequences. The epsilon-Greedy algorithm is almost a greedy algorithm because it generally exploits the best available option, but every once in a while the epsilon-Greedy algorithm explores the other available options. As we’ll see, the term epsilon in the algorithm’s name refers to the odds that the algorithm explores instead of exploiting [Bandit Algorithms for Website Optimization by John Myles White].


# Optimistic Initial Values
Another way to solve the Explore exploit dilemma called the optimistic initial values method [http://www.incompleteideas.net/book/first/ebook/node21.html].



# Upper Confidence Bound Algorithm (UCB)
The algorithm is based on the principle of optimism in the face of uncertainty, which is to choose your actions as if the environment (in this case bandit) is as nice as is plausibly possible. By this we mean that the unknown mean payoffs of each arm is as large as plausibly possible based on the data that has been observed (unfounded optimism will not work — see the illustration on the right!). The intuitive reason that this works is that when acting optimistically one of two things happens. Either the optimism was justified, in which case the learner is acting optimally, or the optimism was not justified. In the latter case the agent takes some action that they believed might give a large reward when in fact it does not. If this happens sufficiently often, then the learner will learn what is the true payoff of this action and not choose it in the future. It overcomes all of the limitations of strategies based on exploration followed by commitment, including the need to know the horizon and sub-optimality gaps. The algorithm has many different forms, depending on the distributional assumptions on the noise[https://banditalgs.com/2016/09/18/the-upper-confidence-bound-algorithm/].


# Bayesian / Thompson Sampling
Thompson sampling takes a different approach to selecting the next arm to be pulled than ε-greedy. A downside of ε-greedy is that it potentially gets stuck on local maximums — sub-par distributions that perform well through statistical chance. The eta parameter is designed to counteract this by forcing the algorithm to take what appears in current view to be a sub-optimal choice (i.e. not the current maximum predicted probability), but which may in fact be the optimal choice given enough information. To do this, Thompson sampling draws from the posterior predictive distributions of each choice using a random uniform variable. This allows a non-optimal distribution to be sampled with varying frequency — as the posterior distribution becomes more certain, the probability of the choice being made decreases dynamically, thus Thompson sampling dynamically balances the desire for more information with making the currently optimal choice [Tony Pistilli, Using Bayesian Updating For Online Decision Making, 2019].
