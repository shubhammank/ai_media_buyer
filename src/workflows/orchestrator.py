from langgraph import StateGraph
from src.agents.planner_agent import planner_agent
from src.agents.builder_agent import builder_agent

def run_workflow(query):
    graph=StateGraph()
    graph.add_node("planner", planner_agent)
    graph.add_node("builder", builder_agent)
    graph.set_entry_point("planner")
    graph.add_edge("planner","builder")
    wf=graph.compile()
    return wf.run({"query":query})
