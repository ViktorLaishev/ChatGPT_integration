# import openai
# import gradio

# openai.api_key = "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"

# def CustomChatGPT(user_input, messages=[]):
#     try:
#         messages.append({"role": "user", "content": user_input})
#         response = openai.Completion.create(
#             model="gpt-3.5-turbo",
#             messages=messages
#         )
#         ChatGPT_reply = response.choices[0].message.content
#         messages.append({"role": "assistant", "content": ChatGPT_reply})
#         return ChatGPT_reply, messages
#     except Exception as e:
#         return "An error occurred: {}".format(str(e)), messages

# demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="ChatGPT Demo", description="Enter your message.")
# demo.launch()
import openai
import gradio

openai.api_key = "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"

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
