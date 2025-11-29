from openai import OpenAI
client=OpenAI()

def builder_agent(state):
    prompt=f"Convert plan to platform-ready adsets:\n{state['plan']}"
    out=client.chat.completions.create(model='gpt-4.1',messages=[{"role":"user","content":prompt}])
    return {"adsets": out.choices[0].message.content}
