## Integration of a Mathematical Calulations with a Chat Completion System using LLM Function-Calling

### AIM:
To design and implement a Python function for calculating the volume of a cylinder, integrate it with a chat completion system utilizing the function-calling feature of a large language model (LLM).

### PROBLEM STATEMENT:
To calculate Volume of Cylinder by using LLM Function-Calling by passing arguments through function call and display volume in JSON format.

### DESIGN STEPS:
#### STEP 1:
Import required libraries: os, openai, json, math. Load the API key securely using dotenv to access OpenAI.

#### STEP 2:
Create the volume_of_cylinder(radius, height, unit="meter") function.Calculate volume using the formula: 𝑉=𝜋×radius^2×height. Store the result in a dictionary with radius, height, volume, and unit. Return the data in JSON format.

#### STEP 3:
Create a user message to request cylinder volume calculation and show the calculated volume in JSON format. Send a request to openai.ChatCompletion.create(), including:
1. Model: "gpt-3.5-turbo"
2. Messages: User input
3. Functions: Defined function metadata
4. Function Call: Explicitly request "volume_of_cylinder"

### PROGRAM:
~~~
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
~~~

### OUTPUT:
![alt text](<Screenshot 2025-04-12 083700.png>)
### RESULT:
Thus, The integration of a Mathematical Calulations with a Chat Completion System using LLM Function-Calling is executed successfully.