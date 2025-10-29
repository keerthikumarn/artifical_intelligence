import warnings
from IPython.display import Markdown
import os
from openai import OpenAI
from crewai import Agent, Task, Crew

warnings.filterwarnings('ignore')

# Configure Ollama environment
os.environ["OPENAI_API_KEY"] = "ollama"
os.environ["OPENAI_BASE_URL"] = "http://localhost:11434/v1"
os.environ["OPENAI_MODEL_NAME"] = "mistral"

ollama = OpenAI(base_url=os.environ["OPENAI_BASE_URL"], api_key="ollama")
model_name = "mistral"

# === Agents ===
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

# === Tasks ===
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

# === Crew ===
crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)

result = crew.kickoff(inputs={"topic": "Serper API usage"})
Markdown(result)
with open("final_blog_post.md", "w", encoding="utf-8") as f:
    f.write(result)

print("✅ Saved as final_blog_post.md")
