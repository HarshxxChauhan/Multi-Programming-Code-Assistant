import requests
import json
import gradio as gr

url="http://localhost:11434/api/generate"

headers={

    'Content-Type':'application/json'
}

history=[]

def generate_response(prompt):
    history.append(prompt)
    final_prompt="\n".join(history)

    data={
        "model":"Helper",
        "prompt":final_prompt,
        "stream":False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            data = response.json()
            return data.get("response", "No response from model.")
        else:
            return f"API Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"


interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4,placeholder="Enter your Prompt"),
    outputs="text"
)
interface.launch(share=True)
