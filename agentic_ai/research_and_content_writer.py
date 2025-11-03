import os
import warnings
from openai import OpenAI
from crewai import Agent, Task, Crew
from IPython.display import Markdown

warnings.filterwarnings("ignore")


# ============================================================
# 🛠️ Environment Setup
# ============================================================
def configure_ollama_environment():
    """
    Configure the Ollama environment to use a local LLM API endpoint.
    """
    os.environ["OPENAI_API_KEY"] = "ollama"
    os.environ["OPENAI_BASE_URL"] = "http://localhost:11434/v1"
    os.environ["OPENAI_MODEL_NAME"] = "mistral"

    base_url = os.environ["OPENAI_BASE_URL"]
    api_key = os.environ["OPENAI_API_KEY"]
    return OpenAI(base_url=base_url, api_key=api_key), os.environ["OPENAI_MODEL_NAME"]


# ============================================================
# 👥 Agent Factory
# ============================================================
def create_agents():
    """
    Define all the agents: Planner, Writer, and Editor.
    """
    planner = Agent(
        role="Content Planner",
        goal="Plan engaging and factually accurate content on {topic}",
        backstory=(
            "You're planning a blog article about the topic: {topic}. "
            "You collect relevant information and outline the structure "
            "for the content writer."
        ),
        allow_delegation=False,
        verbose=True
    )

    writer = Agent(
        role="Content Writer",
        goal="Write insightful and factually accurate opinion pieces about {topic}",
        backstory=(
            "You're writing an article based on the planner's outline, "
            "ensuring clarity, structure, and engaging flow."
        ),
        allow_delegation=False,
        verbose=True
    )

    editor = Agent(
        role="Editor",
        goal="Edit the blog post for tone, grammar, and consistency.",
        backstory=(
            "You refine the writer's post, ensuring stylistic consistency "
            "and clarity before publication."
        ),
        allow_delegation=False,
        verbose=True
    )

    return planner, writer, editor


# ============================================================
# 🧾 Task Factory
# ============================================================
def create_tasks(planner, writer, editor):
    """
    Define all tasks and assign them to the appropriate agents.
    """
    plan = Task(
        description=(
            "1. Research the latest trends, key players, and relevant facts on {topic}.\n"
            "2. Identify the target audience and pain points.\n"
            "3. Build a content outline (intro, body, conclusion).\n"
            "4. Include SEO keywords and reliable references."
        ),
        expected_output="A detailed content plan including outline, audience, and SEO keywords.",
        agent=planner
    )

    write = Task(
        description=(
            "1. Use the planner’s outline to write a complete blog post on {topic}.\n"
            "2. Ensure a captivating introduction and conclusion.\n"
            "3. Naturally integrate SEO keywords.\n"
            "4. Use 2–3 paragraphs per section."
        ),
        expected_output="A complete blog post in markdown format, ready for editing.",
        agent=writer
    )

    edit = Task(
        description="Proofread and refine the blog post for clarity, grammar, and consistency.",
        expected_output="A polished blog post in markdown format, publication-ready.",
        agent=editor
    )

    return plan, write, edit


# ============================================================
# 🚀 Crew Orchestration
# ============================================================
def create_and_run_crew(topic: str):
    """
    Orchestrates the workflow — from planning to writing to editing — for the given topic.
    """
    # 1. Configure environment
    ollama, model_name = configure_ollama_environment()

    # 2. Create agents and tasks
    planner, writer, editor = create_agents()
    plan, write, edit = create_tasks(planner, writer, editor)

    # 3. Assemble crew
    crew = Crew(
        agents=[planner, writer, editor],
        tasks=[plan, write, edit],
        verbose=2
    )

    # 4. Run workflow
    print(f"🚀 Starting content creation pipeline for topic: '{topic}'\n")
    result = crew.kickoff(inputs={"topic": topic})

    # 5. Display and save results
    Markdown(result)
    save_output(result, "research_details.md")
    return result


# ============================================================
# 💾 Utility: Save Output
# ============================================================
def save_output(content: str, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Blog post saved as {filename}")


# ============================================================
# 🧠 Main Entry Point
# ============================================================
if __name__ == "__main__":
    topic = "Serper API usage"  # You can change this or pass via CLI
    final_result = create_and_run_crew(topic)
    print("\n🎉 Content generation completed successfully!")
