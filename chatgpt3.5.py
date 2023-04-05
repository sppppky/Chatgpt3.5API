import os
import openai
proxy_url = " "
#这里要换成你自己的代理和端口，格式，IP:端口，比如'128.0.0.1:23221'，一定要用代理！！！
#不用代理IP是国内，也有可能被封。
os.environ["HTTP_PROXY"] = proxy_url
os.environ["HTTPS_PROXY"] = proxy_url
#if you live outside of china, there is no need to care about this code


openai.api_key = " "
#这里要换成你自己的API key（去openai)的官网申请
# please take place these as your own api key(get it in openai.com)
#%%申请获取API访问
def obtain_chatanswer(ask1,content1):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages = [{"role": "system", "content" : "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.\nKnowledge cutoff: 2021-09-01\nCurrent date: 2023-03-28"},
                    {"role": "user", "content" : "How are you?"},
                    {"role": "assistant", "content" : "I am doing well"},
                    {"role": "user", "content" : ask1+content1}])
    a=completion.choices[0]['message']['content'].lower()
    return a
#ask是你询问的问题，比如请帮我回答一个问题，content1可以接你想要它帮你回答的内容，可以用循环
