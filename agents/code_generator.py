import os


class CodeGeneratorAgent:

    def generate_backend_code(self, state, project_path):

        backend_path = os.path.join(project_path, "backend")

        os.makedirs(backend_path, exist_ok=True)

        self.create_main_file(backend_path)
        self.create_models_file(backend_path, state)
        self.create_routes_file(backend_path, state)

        print("\nBackend project generated\n")


    def create_main_file(self, path):

        content = """
        from fastapi import FastAPI

        app = FastAPI()

        @app.get("/")
        def root():
            return {"message": "API is running"}
        """

        with open(os.path.join(path, "main.py"), "w") as f:
            f.write(content)


    def create_models_file(self, path, state):

        models = state["backend_design"]["database_models"]

        content = "from pydantic import BaseModel\n\n"

        for model in models:

            content += f"class {model}(BaseModel):\n"
            content += "    id: int\n\n"

        with open(os.path.join(path, "models.py"), "w") as f:
            f.write(content)


    def create_routes_file(self, path, state):

        endpoints = state["backend_design"]["api_endpoints"]

        content = """
        from fastapi import APIRouter

        router = APIRouter()
        """

        for ep in endpoints:

            method, route = ep.split(" ", 1)

            method = method.lower()

            content += f"""
            @router.{method}("{route}")
            def handler():
                return {{"message": "Endpoint {route}"}}
            """

        with open(os.path.join(path, "routes.py"), "w") as f:
            f.write(content)