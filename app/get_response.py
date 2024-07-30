import os

from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_community.llms import LlamaCpp


prompt_template = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Ты - полезный ассистент, отвечающий на вопросы пользователей.<|eot_id|><|start_header_id|>user<|end_header_id|>

{input}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

"""
prompt = PromptTemplate.from_template(prompt_template)

ABS_PATH = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(ABS_PATH, "models/model-q4_K.gguf")

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# Define LLM chain
llm = LlamaCpp(
  model_path=model_path,
  f16_kv=True,
  verbose=True,
  callback_manager=callback_manager
)

llm_chain = LLMChain(llm=llm, prompt=prompt)


def get_answer(query):
  answer = llm_chain.run(query)
  return answer