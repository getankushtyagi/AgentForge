from langgraph.graph import StateGraph , END
from schemas.agent_state import AgentState

def product_manager_node(state:AgentState):
    print("product manager agent running")
    return state

def architecture_node(state:AgentState):
    print("Architect agent running")
    return state

def backend_engineer_node(state:AgentState):
    print("Backend Engineer agent running")
    return state

def qa_engineer_node(state:AgentState):
    print("QA Engineer agent running")
    return state



def build_agent_grapgh():
    builder=StateGraph(AgentState)
    
    builder.add_node("product_manager",product_manager_node)
    builder.add_node("architect",architecture_node)
    builder.add_node("backend_engineer",backend_engineer_node)
    builder.add_node("qa_engineer",qa_engineer_node)
    
    builder.set_entry_point("product_manager")
    
    builder.add_edge("product_manager", "architect")
    builder.add_edge("architect", "backend_engineer")
    builder.add_edge("backend_engineer", "qa_engineer")
    builder.add_edge("qa_engineer", END)
    
    return builder.compile()
