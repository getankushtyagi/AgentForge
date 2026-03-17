import os


class CodeGeneratorAgent:

    def generate_backend_code(self, state, project_path):

        backend_path = os.path.join(project_path, "backend")

        os.makedirs(backend_path, exist_ok=True)

        self.create_main_file(backend_path)
        self.create_models_file(backend_path, state)
        self.create_routes_file(backend_path, state)
        self.create_requirements_file(backend_path)
        self.create_backend_readme(backend_path, state)

        print("\nBackend project generated\n")


    def create_main_file(self, path):

        content = """from fastapi import FastAPI
from routes import router

app = FastAPI(title="Generated API")

# Include routes
app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "API is running", "docs": "/docs"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
"""

        with open(os.path.join(path, "main.py"), "w") as f:
            f.write(content)


    def create_models_file(self, path, state):

        models = state["backend_design"]["database_models"]

        content = """from pydantic import BaseModel
from typing import Optional
from datetime import datetime


"""

        for model in models:
            # Clean model name - extract the main entity name
            model_name = model.strip()
            
            # Handle plural to singular if needed (basic conversion)
            # Remove common prefixes/suffixes
            if model_name.lower().endswith(" model"):
                model_name = model_name[:-6].strip()
            if model_name.lower().endswith(" table"):
                model_name = model_name[:-6].strip()
            
            # Convert to PascalCase if not already
            model_name = "".join(word.capitalize() for word in model_name.replace("_", " ").replace("-", " ").split())
            
            if not model_name:
                continue

            content += f"""class {model_name}(BaseModel):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    # Add your fields here

"""

        with open(os.path.join(path, "models.py"), "w") as f:
            f.write(content)


    def create_routes_file(self, path, state):

        endpoints = state["backend_design"]["api_endpoints"]

        content = """from fastapi import APIRouter

router = APIRouter()
"""

        for ep in endpoints:
            # Handle different endpoint formats
            if " " in ep:
                # Format: "METHOD /path"
                method, route = ep.split(" ", 1)
                method = method.lower()
            else:
                # Format: just "/path", default to GET
                method = "get"
                route = ep if ep.startswith("/") else f"/{ep}"
            
            # Sanitize method name (only common HTTP methods)
            if method not in ["get", "post", "put", "delete", "patch"]:
                method = "get"
            
            # Create a unique function name from the route
            func_name = route.replace("/", "_").replace("{", "").replace("}", "").replace("-", "_").strip("_") or "root"

            content += f"""
@router.{method}("{route}")
def {func_name}_{method}_handler():
    return {{"message": "Endpoint {method.upper()} {route}"}}

"""

        with open(os.path.join(path, "routes.py"), "w") as f:
            f.write(content)


    def create_requirements_file(self, path):
        """Generate requirements.txt for the backend project"""
        
        content = """fastapi==0.112.0
uvicorn==0.30.6
pydantic==2.8.2
python-dotenv==1.0.1
sqlalchemy==2.0.31
"""

        with open(os.path.join(path, "requirements.txt"), "w") as f:
            f.write(content)


    def create_backend_readme(self, path, state):
        """Generate README.md for the backend project"""
        
        product_name = state.get("product_spec", {}).get("product_name", "API")
        
        content = f"""# {product_name} - Backend API

## Overview
This is the auto-generated backend API for {product_name}.

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python main.py
```

The API will be available at:
- API: http://localhost:8000
- Interactive Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

All endpoints are prefixed with `/api`

### Available Routes
Check the interactive documentation at `/docs` for complete API documentation.

## Project Structure

```
backend/
├── main.py          # FastAPI application entry point
├── models.py        # Pydantic models for data validation
├── routes.py        # API route definitions
└── requirements.txt # Python dependencies
```

## Development

To add new endpoints:
1. Define your route in `routes.py`
2. Add corresponding models in `models.py`
3. The routes are automatically included via the router

## Generated with AgentForge
This backend was automatically generated using AgentForge multi-agent system.
"""

        with open(os.path.join(path, "README.md"), "w") as f:
            f.write(content)