#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']


# In[2]:


import json
import math

def get_cylinder_volume(radius, height):
    """Calculate the volume of a cylinder given its radius and height"""
    volume = math.pi * (radius ** 2) * height
    cylinder_info = {
        "radius": radius,
        "height": height,
        "volume": round(volume, 2),
        "unit": "cubic units"
    }
    return json.dumps(cylinder_info)



# In[3]:


functions = [
    {
        "name": "get_cylinder_volume",
        "description": "Calculate the volume of a cylinder given its radius and height",
        "parameters": {
            "type": "object",
            "properties": {
                "radius": {
                    "type": "number",
                    "description": "The radius of the cylinder base in units",
                },
                "height": {
                    "type": "number",
                    "description": "The height of the cylinder in units",
                }
            },
            "required": ["radius", "height"],
        },
    }
]


# In[4]:


messages = [
    {
        "role": "user",
        "content": "What is the volume of a cylinder with radius 5 and height 10?"
    }
]


# In[5]:


import openai


# In[6]:


# Call the ChatCompletion endpoint
response = openai.ChatCompletion.create(
    # OpenAI Updates: As of June 2024, we are now using the GPT-3.5-Turbo model
    model="gpt-4-turbo",
    messages=messages,
    functions=functions
)


# In[7]:


print(response)


# In[8]:


response_message = response["choices"][0]["message"]


# In[9]:


response_message


# In[10]:


response_message["content"]


# In[11]:


response_message["function_call"]


# In[12]:


json.loads(response_message["function_call"]["arguments"])


# In[13]:


json.loads(response_message["function_call"]["arguments"])


# In[14]:


args = json.loads(response_message["function_call"]["arguments"])


# In[15]:


get_cylinder_volume(**args)


# In[ ]:




