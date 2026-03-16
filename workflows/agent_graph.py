from langgraph.graph import StateGraph , END
from schemas.agent_state import AgentState
from agents.product_manager import ProductManagerAgent
from agents.architect import ArchitectAgent
from agents.backend_engineer import BackendEngineerAgent

product_agent=ProductManagerAgent()
architect_agent=ArchitectAgent()
backend_agent=BackendEngineerAgent()

def product_manager_node(state:AgentState):
    
    idea=state["idea"]
    
    product_spec= product_agent.generate_product_spec(idea)
    
    state["product_spec"] = product_spec.model_dump()
    
    print("\nproduct specififcation generated\n")
    
    return state

def architecture_node(state:AgentState):
    product_spec=state["product_spec"]
    architecture=architect_agent.generate_architecture(product_spec)
    state["architecture"]=architecture.model_dump()
    print("\n Architecture generated\n")
    
    return state

def backend_engineer_node(state:AgentState):
    architecture=state["architecture"]
    backend_design=backend_agent.generate_backend_design(architecture)
    state["backend_design"]=backend_design.model_dump()
    print("\nBackend Design generated\n")
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
