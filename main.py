import chainlit as cl
import sys, os
from reasoning_runs.util import summarize_trial, log_trial, save_agents
from reasoning_runs.agents_ar import CoTAgent, ReflexionStrategy
from reasoning_runs.prompts_ar import cot_simple_reflect_agent_prompt, cot_simple_reflect_prompt, cot_simple_agent_prompt
from reasoning_runs.fewshots_ar import COTQA_SIMPLE6, COT_SIMPLE_REFLECTION
from io import StringIO
import re


def extract_thought(text):
  parts = text.split('الرد:')
  return parts[0]


def extract_ans(text):
  parts = text.split('\n')
  return parts[0]

def extract_ans_text(text):
    match = re.search(r"\[(.*?)\]", text)
    if match:
        return match.group(1)
    else:
        return None



#print(extract_thought(t.split('تفكير :')[1]))
#print(extract_ans_text(extract_ans(t.split('الرد:')[1]))) # 1 for 1st 2 for 2nd

@cl.step
async def chain_of_thought(text):
    # Simulate a running task
    
   
    return  extract_thought(text.split('تفكير :')[1])


@cl.on_message
async def main(message: cl.Message):
    # custom logic goes here...
    conversation_log = ''
    await cl.sleep(0)
    captured_output = StringIO()
    original_stdout = sys.stdout
    sys.stdout = captured_output
# ------- define the strategy ------
    strategy: ReflexionStrategy = ReflexionStrategy.REFLEXION
    
    try:
# ------- COT agent -------
        agent = CoTAgent(question=message.content,
                   context='',
                   key='', # pass no answer
                   agent_prompt=cot_simple_agent_prompt if strategy == ReflexionStrategy.NONE \
                    else cot_simple_reflect_agent_prompt,
                   cot_examples=COTQA_SIMPLE6,
                   reflect_prompt=cot_simple_reflect_prompt,
                   reflect_examples=COT_SIMPLE_REFLECTION)
    
        agent.run(reflexion_strategy = strategy)
        agent.run(reflexion_strategy = strategy)
        sys.stdout = original_stdout
        conversation_log = captured_output.getvalue().strip()
        #print(conversation_log)

        #print(conversation_log)
    except Exception:
        print('Intializing the agent failed : ', Exception)

    # Send a response back to the user
    tool_res = await chain_of_thought(conversation_log)
    #print(conversation_log)
    output = extract_ans_text(extract_ans(conversation_log.split('الرد:')[1]))
    await cl.Message(
        content=f"{output}",
    ).send()

    # await cl.Message.update()

