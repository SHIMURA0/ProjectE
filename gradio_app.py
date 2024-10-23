import gradio as gr
from langchain.llms import OpenAI

# 使用 OpenAI 的 GPT 作为语言模型，确保替换为你自己的API密钥
llm = OpenAI(temperature=0.7, openai_api_key="your-openai-api-key")

# 定义处理用户输入并通过Langchain生成响应的函数
def chatbot_response(input_text):
    try:
        # 获取Langchain模型的响应
        response = llm(input_text)
        return response
    except Exception as e:
        return str(e)

# 创建一个 Gradio 接口，并将其绑定到上面定义的函数
iface = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs="text",
    title="Langchain Chatbot Demo",
    description="Ask anything and get a response!",
)

# 启动 Gradio 接口
iface.launch()
