from env import CartPole

cartpole = CartPole.env(gui=True)

counter = 0
while counter < 1000:
    counter = counter+1
    cartpole.step(0)
    cartpole.render()
