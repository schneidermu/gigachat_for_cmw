import os

from langchain.chains.llm import LLMChain
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


prompt_template = """Ты - полезный ассистент, отвечающий на вопросы пользователей."""

prompt = ChatPromptTemplate.from_messages(
    [
        (
          "system",
          prompt_template,
        ),
        ("human", "{input}"),
    ]
)

ABS_PATH = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(ABS_PATH, "models/model-q4_K.gguf")

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# Define LLM chain
llm = ChatOllama(model='llama3.1', temperature=0.2, base_url="http://ollama-container:11434", keep_alive=-1, num_ctx=2048, num_thread=8, num_gpu=0)

llm_chain = LLMChain(llm=llm, prompt=prompt)


def get_answer(query):
  answer = llm_chain.run(query)
  return answer