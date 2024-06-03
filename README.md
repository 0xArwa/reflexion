# Tafakkur: Improving LLM Reasoning Through Reflecting Agents

This repo is based on the original Reflexion framwork [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) by Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao. 

This project specifically targets reasoning tasks tailored for Arabic language by adapting self-reflecting agents. <br>
The code now support arabic langugae processing and can be easily adapted with an API endpoint. 

**NOTE 1**: The project is currently running on OpenAI API since the finetuned model is in a private repo. <br>
**NOTE 2**: The instruction dataset currently is not publicly available. <br>
**NOTE 3**: assign your API key in the agent_ar.py to try our project. <br>

#### Setup

To run the project:

```bash
chainlit run main.py -w
```

#### Reflexion Strategies


 - `ReflexionStrategy.NONE` - The agent is not given any information about its last attempt. 

 - `ReflexionStrategy.LAST_ATTEMPT` - The agent is given its reasoning trace from its last attempt on the question as context.

 - `ReflexionStrategy.REFLEXION` - The agent is given its self-reflection on the last attempt as context. 

 - `ReflexionStrategy.LAST_ATTEMPT_AND_REFLEXION` -  The agent is given both its reasoning trace and self-reflection on the last attempt as context.

