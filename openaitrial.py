import os
import openai


response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write an email to my boss for increment in salary.\n",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)