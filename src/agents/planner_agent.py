from openai import OpenAI
from src.rag.retriever import retrieve_context
client=OpenAI()

def planner_agent(query):
    ctx=retrieve_context(query)
    prompt=f"Generate campaign plan using context:\n{ctx}\nQuery: {query}"
    out=client.chat.completions.create(model="gpt-4.1",messages=[{"role":"user","content":prompt}])
    return {"plan": out.choices[0].message.content}
