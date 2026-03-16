import os

class ProjectGenerator:
    def __init__(self, base_dir="generated_projects"):
        self.base_dir=base_dir
        
    def create_project(self, state):
        product_name=state["product_spec"]["product_name"]
        folder_name=product_name.lower().replace("","_")
        project_path=os.path.join(self.base_dir, folder_name)
        
        os.makedirs(project_path,exist_ok=True)
        
        self.create_prd(project_path,state["product"])
        self.create_architecture(project_path,state["architecture"])
        self.create_backend_design(project_path,state["backend_design"])
        self.create_test_plan(project_path,state["qa_plan"])
        
        print("\n Project generated at: {project_path}")
    
    def create_prd(self, path, product_spec):

        content = f"""
        # Product Requirement Document

        ## Product Name
        {product_spec['product_name']}

        ## Description
        {product_spec['description']}

        ## Target Users
        {chr(10).join(['- ' + u for u in product_spec['target_users']])}

        ## Core Features
        {chr(10).join(['- ' + f for f in product_spec['core_features']])}

        ## Success Metrics
        {chr(10).join(['- ' + m for m in product_spec['success_metrics']])}
        """

        with open(os.path.join(path, "PRD.md"), "w") as f:
            f.write(content)

    def create_architecture(self, path, architecture):

        content = f"""
        # System Architecture

        ## Services
        {chr(10).join(['- ' + s for s in architecture['services']])}

        ## Database Tables
        {chr(10).join(['- ' + d for d in architecture['database_tables']])}

        ## Tech Stack
        {chr(10).join(['- ' + t for t in architecture['tech_stack']])}
        """

        with open(os.path.join(path, "architecture.md"), "w") as f:
            f.write(content)

    def create_backend_design(self, path, backend_design):

        content = f"""
        # Backend Design

        ## API Endpoints
        {chr(10).join(['- ' + e for e in backend_design['api_endpoints']])}

        ## Database Models
        {chr(10).join(['- ' + m for m in backend_design['database_models']])}

        ## Backend Services
        {chr(10).join(['- ' + s for s in backend_design['backend_services']])}
        """

        with open(os.path.join(path, "backend_design.md"), "w") as f:
            f.write(content)

    def create_test_plan(self, path, qa_plan):

        content = f"""
        # QA Test Plan

        ## Test Cases
        {chr(10).join(['- ' + t for t in qa_plan['test_cases']])}

        ## Edge Cases
        {chr(10).join(['- ' + e for e in qa_plan['edge_cases']])}

        ## API Tests
        {chr(10).join(['- ' + a for a in qa_plan['api_tests']])}
        """

        with open(os.path.join(path, "test_plan.md"), "w") as f:
            f.write(content)
        