import openai
import gradio

openai.api_key = "API_KEY"

def CustomChatGPT(user_input, messages=[]):
    try:

        messages.append({"role": "user", "content": user_input})
        

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages  
        )
        

        assistant_response = completion.choices[0].message.content
        

        messages.append({"role": "assistant", "content": assistant_response})
        
        return assistant_response, messages
    except Exception as e:
        return "An error occurred: {}".format(str(e)), messages

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="ChatGPT Demo", description="Enter your message.")
demo.launch(share=True)
