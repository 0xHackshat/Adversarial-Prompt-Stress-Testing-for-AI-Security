import os
from vulnerable_ai import vulnerable_respond

# File paths
prompts_file = "prompts/attack_prompts.txt"
results_file = "prompts/ai_responses.txt"

# Load attack prompts
with open(prompts_file, "r", encoding="utf-8") as f:
    attack_prompts = [line.strip() for line in f if line.strip()]

# Test each prompt on the vulnerable AI
responses = []
for prompt in attack_prompts:
    response = vulnerable_respond(prompt)
    responses.append((prompt, response))
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")
    print("-" * 50)

# Save responses to a file
os.makedirs("prompts", exist_ok=True)
with open(results_file, "w", encoding="utf-8") as f:
    for prompt, response in responses:
        f.write(f"Prompt: {prompt}\nResponse: {response}\n{'-'*40}\n")

print(f"All responses saved to {results_file}")
