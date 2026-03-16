from workflows.agent_graph import build_agent_grapgh

def main():
    graph=build_agent_grapgh()
    
    state={
        "idea":"Build a Saas platform for fitness trainers",
        "product_spec":None,
        "architecture":None,
        "backend_design":None,
        "qa_plan":None
    }
    
    result = graph.invoke(state)
    
    print("\nWorkflow finished")
    print(result)
    
    
if __name__=="__main__":
    main()