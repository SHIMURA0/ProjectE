import gradio as gr
import os
from datetime import datetime

# 定义保存数据的函数
def greet(name):
    # 获取当前时间
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 将数据写入本地文件
    with open("user_data.txt", "a", encoding="utf-8") as f:
        f.write(f"{timestamp}: {name}\n")
    return "Hello " + name + "!"

# 创建 Gradio 接口
demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="请输入您的名字"),
    outputs=gr.Textbox(label="问候"),
    title="问候应用",
    description="请输入您的名字，我们将向您打招呼并保存您的数据。"
)

# 启动应用，并生成公开分享链接
demo.launch(share=True)

