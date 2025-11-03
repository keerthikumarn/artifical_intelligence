import streamlit as st
import warnings
import os
from openai import OpenAI
from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool

warnings.filterwarnings('ignore')

# -----------------------------
# 🧠 Streamlit Page Setup
# -----------------------------
st.set_page_config(page_title="CrewAI Multi-Agent Support", layout="wide")
st.title("🤖 CrewAI Multi-Agent Support System")

st.markdown(
    """
    Welcome to the **CrewAI Multi-Agent Support Assistant**.  
    This app uses two AI agents:
    1. 🧑‍💼 **Senior Support Representative** – provides an initial, detailed response.  
    2. 🕵️ **Quality Assurance Specialist** – reviews and improves the response for accuracy and completeness.
    """
)

# -----------------------------
# 🔧 Input Fields
# -----------------------------
customer = st.text_input("Customer / Organization Name", "Block Chain Technology")
person = st.text_input("Person Contacting", "Keerthi Kumar N")
inquiry = st.text_area(
    "Customer Inquiry",
    "I need some introduction about block chain technology and how the same can be leveraged in telecom industry."
)

run_button = st.button("🚀 Run Multi-Agent Workflow")

# -----------------------------
# ⚙️ When user clicks Run
# -----------------------------
if run_button:
    st.info("⚙️ Initializing CrewAI Agents...")
    with st.spinner("Starting Ollama + CrewAI pipeline... please wait ⏳"):

        # Configure Ollama locally
        os.environ["OPENAI_API_KEY"] = "ollama"
        #os.environ["OPENAI_API_KEY"] = "gemma"
        os.environ["OPENAI_BASE_URL"] = "http://localhost:11434/v1"
        os.environ["OPENAI_MODEL_NAME"] = "gemma:2b"
        #os.environ["OPENAI_MODEL_NAME"] = "mistral"

        # Initialize Ollama client
        ollama = OpenAI(base_url=os.environ["OPENAI_BASE_URL"], api_key="ollama")
        model_name = "mistral"

        # -----------------------------
        # 🧩 Define CrewAI Agents
        # -----------------------------
        support_agent = Agent(
            role="Senior Support Representative",
            goal="Provide the most helpful and friendly support in your team.",
            backstory=(
                "You work at CrewAI and are supporting {customer}, "
                "a highly valuable client. Your job is to give full, clear, "
                "and friendly answers without assumptions."
            ),
            allow_delegation=False,
            verbose=True
        )

        qa_agent = Agent(
            role="Support Quality Assurance Specialist",
            goal="Ensure that all responses meet high-quality, accurate, and friendly standards.",
            backstory=(
                "You review responses from the support representative to ensure "
                "they are complete, clear, accurate, and friendly."
            ),
            verbose=True
        )

        # -----------------------------
        # 🧰 Tools
        # -----------------------------
        docs_scrape_tool = ScrapeWebsiteTool(
            website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
        )

        # -----------------------------
        # 📝 Tasks
        # -----------------------------
        inquiry_resolution = Task(
            description=(
                f"{customer} just reached out with a question:\n"
                f"{inquiry}\n\n"
                f"{person} from {customer} is the one that reached out. "
                "Provide a complete and friendly answer with all required context."
            ),
            expected_output="A detailed and informative response addressing all aspects of the inquiry.",
            tools=[docs_scrape_tool],
            agent=support_agent,
        )

        qa_review = Task(
            description=(
                f"Review the answer provided by the Senior Support Representative for {customer}. "
                "Ensure completeness, accuracy, references, and friendly tone."
            ),
            expected_output=(
                "A polished, final response ready to send to the customer, "
                "friendly yet professional."
            ),
            agent=qa_agent,
        )

        # -----------------------------
        # 🧠 Crew Orchestration
        # -----------------------------
        crew = Crew(
            agents=[support_agent, qa_agent],
            tasks=[inquiry_resolution, qa_review],
            verbose=2,
            memory=False
        )

        # -----------------------------
        # 🚀 Execute Workflow
        # -----------------------------
        progress_placeholder = st.empty()
        progress_bar = st.progress(0)

        try:
            progress_placeholder.markdown("🧩 **Stage 1:** Running Senior Support Representative...")
            progress_bar.progress(40)

            inputs = {"customer": customer, "person": person, "inquiry": inquiry}
            result = crew.kickoff(inputs=inputs)

            progress_placeholder.markdown("✅ **Stage 2:** QA Review Complete. Final response generated.")
            progress_bar.progress(100)

            # Display results
            st.success("🎉 Workflow completed successfully!")
            st.markdown("### 💬 Final Response:")
            st.markdown(result)

            # Save to file
            with open("multi_agent_support.md", "w", encoding="utf-8") as f:
                f.write(result)

            st.download_button(
                label="📥 Download Response as Markdown",
                data=result,
                file_name="multi_agent_support.md",
                mime="text/markdown"
            )

        except Exception as e:
            st.error(f"⚠️ Error occurred: {e}")

