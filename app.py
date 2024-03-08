import gradio as gr
import json

def echo(text, request: gr.Request):
    output_text = json.dumps({"text": text})
    if request:
        print("Request headers dictionary:", request.headers)
        output_text = json.dumps({"headers": dict(request.headers)})
        print("IP address:", request.client.host)
        output_text = json.dumps({"headers": dict(request.headers)})
        print("Query parameters:", dict(request.query_params))
        output_text = json.dumps({"query_params": dict(request.query_params)})
    return output_text

io = gr.Interface(echo, "textbox", "textbox").launch(share=True) 

