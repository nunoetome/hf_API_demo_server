import gradio as gr
import json

DEBUG_MODE = True

def echo(text, request: gr.Request):
    output_text = {"text": text}  # Initialize as a dictionary
    if request:
        if DEBUG_MODE:
            print("Request object:", request)
            print("Request headers dictionary:", request.headers)
            print("IP address:", request.client.host)
            print("Query parameters:", dict(request.query_params))
        # Convert headers to a dictionary and include them in the output_text
        output_text["headers"] = dict(request.headers.items())
        output_text["host"] = request.client.host
        output_text["query_params"] = dict(request.query_params)
    if DEBUG_MODE:
        print("Query parameters:", dict(request.query_params))
    
    # Convert the output_text dictionary to a JSON-formatted string
    output_text_json = json.dumps(output_text)
    return output_text_json

io = gr.Interface(echo, "textbox", "json").launch(share=True)