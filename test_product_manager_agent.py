from agents.product_manager import ProductManagerAgent


def main():

    agent = ProductManagerAgent()

    idea = "Build a SaaS platform for fitness trainers to manage clients"

    result = agent.generate_product_spec(idea)

    print("\nGenerated Product Specification:\n")
    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()