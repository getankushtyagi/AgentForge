from workflows.agent_graph import build_agent_grapgh
from tools.project_generator import ProjectGenerator
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
    generator=ProjectGenerator()
    generator.create_project(result)
    
    print("\nWorkflow finished")
    print(result)
    
    
if __name__=="__main__":
    main()