import sys, os
from util import summarize_trial, log_trial, save_agents
from agents_ar import CoTAgent, ReflexionStrategy
from datasets import load_dataset # temp data
from prompts_ar import cot_simple_reflect_agent_prompt, cot_simple_reflect_prompt, cot_simple_agent_prompt
from fewshots_ar import COTQA_SIMPLE6, COT_SIMPLE_REFLECTION


sys.path.append('..')
root = '../root/'

train_dataset = load_dataset('json', data_files='D:/files_new/10-samples.json', split='train') 

row = train_dataset[9] # take one example


#print(ReflexionStrategy.__doc__)

# ------- define the strategy ------
strategy: ReflexionStrategy = ReflexionStrategy.REFLEXION


try:
# ------- COT agent -------
    agent = CoTAgent(question=row['question'],
                   context='',
                   key=row['answer'], # pass no answer (later)
                   agent_prompt=cot_simple_agent_prompt if strategy == ReflexionStrategy.NONE \
                    else cot_simple_reflect_agent_prompt,
                   cot_examples=COTQA_SIMPLE6,
                   reflect_prompt=cot_simple_reflect_prompt,
                   reflect_examples=COT_SIMPLE_REFLECTION)
    
    agent.run(reflexion_strategy = strategy)
    print(f'Answer: {agent.key}')

except Exception:
    print('Intializing the agent failed : ', Exception)



# ------- saving logs --------
#with open(os.path.join(root, 'CoT', 'no_context', strategy.value, f'{len(agents)}_questions_{trial}_trials.txt'), 'w') as f:
#    f.write(log)
#save_agents(agents, os.path.join(root, 'CoT', 'no_context', strategy.value, 'agents'))