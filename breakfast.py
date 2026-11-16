
from langchain_openai import ChatOpenAI

# Initialize LangChain model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# Request exactly five healthy breakfast ideas
prompt = """
Suggest exactly 5 healthy breakfast ideas.

Requirements:
- Number them from 1 to 5.
- Write each idea on a separate line.
- Include nutritious, balanced breakfast options.
- Prefer simple Indian breakfast dishes.
- Do not include explanations or a preamble.
"""

# Call OpenAI through LangChain
reply = llm.invoke(prompt)

# Print only the answer text
print(reply.content)
