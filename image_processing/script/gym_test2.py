import gym
env = gym.make('CartPole-v0')

for i_episode in range(20):
    observation = env.reset()
    done = False
    while not done:
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)

def test_funfun_defence(self):
    env = Environment(env_name="Pong-v0")
    agent = CycleAgent((2,3),keep_length=20)

    for episode, step, reward in env.play(agent, episode=1):
        pass
