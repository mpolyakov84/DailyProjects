# App is a Calculator Chatbot with Gemini and LangChain
from dotenv import load_dotenv, find_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
def get_api_keys():
    """
    Func load and return api keys
    :return: tuple of  (google_api_key, langsmith_api_key)
    """
    load_dotenv(find_dotenv())
    google_api_key = os.getenv('GOOGLE_API_KEY')
    langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
    return google_api_key, langsmith_api_key


get_api_keys()

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "you have to act as a calculator. Answer all questions to the best of your ability."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)


# define new Graph
workflow = StateGraph(state_schema=MessagesState)

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
# define the function that calls the model
def call_model(state: MessagesState):
    prompt = prompt_template.invoke(state)
    response = model.invoke(prompt)
    return {"messages": response}

# Define the (single) mode in the Graph
workflow.add_edge(START, "model")
workflow.add_node("model",call_model)

#add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "abc123"}}

print("Calculator started:")
exit_list = ['exit', 'quit', 'q']
while True:
    query = input('You: ')
    if query.lower() in exit_list:
        break

    input_messages = [HumanMessage(query)]
    output = app.invoke({"messages": input_messages}, config)
    print('Calculator:',output["messages"][-1].content)# output contains all messages in state
