# Tafakkur: Improving LLM Reasoning Through Reflecting Agents

This repo is based on the original Reflexion framwork [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) by Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao. 

This project specifically targets reasoning tasks tailored for Arabic language by adapting self-reflecting agents.

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


### Cite

```bibtex
@misc{shinn2023reflexion,
      title={Reflexion: Language Agents with Verbal Reinforcement Learning}, 
      author={Noah Shinn and Federico Cassano and Edward Berman and Ashwin Gopinath and Karthik Narasimhan and Shunyu Yao},
      year={2023},
      eprint={2303.11366},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```
