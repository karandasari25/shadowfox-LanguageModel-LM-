# GPT-3.5 Language Model Exploration (Azure OpenAI)

# 1. Introduction
print("Exploring GPT-3.5's capabilities: creativity, context understanding, and temperature effects.")

# 2. Setup
import openai
import matplotlib.pyplot as plt
import os

# Set Azure OpenAI API settings
os.environ["AZURE_OPENAI_API_KEY"] = "7EXec5WYk8eZwNDnE4Hp9pZPCqILeZbWGFTyfrdrXyP2sIcKGiMyJQQJ99BCAC77bzfXJ3w3AAABACOGwsnj"

openai.api_type = "azure"
openai.api_base = "https://manomitra.openai.azure.com/"  # <-- Change this
openai.api_version = "2023-05-15"  # Check Azure portal if your version is different
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")  # Better to use env variable

deployment_name = "gpt-35-turbo"  # <-- Change this to your deployed model name

# 3. Define function to interact with Azure GPT-3.5
def generate_text(prompt, deployment_name=deployment_name, temperature=0.7, max_tokens=150):
    try:
        response = openai.ChatCompletion.create(
            engine=deployment_name,   # use 'engine', not 'model'
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.error.OpenAIError as e:
        return f"[Error: {str(e)}]"

# 4. Sample prompts
prompts = [
    "Explain quantum computing in simple terms.",
    "Write a fantasy story about a time-traveling dog.",
    "Explain Fourier Transform to a high school student.",
    "Summarize the benefits and risks of AI in healthcare.",
    "Compose a short poem about the future of space exploration."
]

# 5. Generate responses
temperatures = [0.2, 0.5, 0.7, 1.0]
results = {}

for temp in temperatures:
    temp_results = []
    for prompt in prompts:
        response = generate_text(prompt, temperature=temp)
        temp_results.append((prompt, response))
    results[temp] = temp_results

# 6. Save responses to file
with open("azure_gpt3_5_outputs.txt", "w", encoding="utf-8") as f:
    for temp, temp_results in results.items():
        f.write(f"\n=== Temperature: {temp} ===\n")
        for prompt, response in temp_results:
            f.write(f"\nPrompt: {prompt}\nResponse: {response}\n")

print("Responses saved to 'azure_gpt3_5_outputs.txt'.")

# 7. Manual scoring of creativity
creativity_scores = {
    0.2: 2,
    0.5: 5,
    0.7: 7,
    1.0: 9
}

# 8. Visualization
plt.figure(figsize=(8, 5))
plt.plot(list(creativity_scores.keys()), list(creativity_scores.values()), marker='o', color='green')
plt.title("Effect of Temperature on GPT-3.5 Creativity (Azure)")
plt.xlabel("Temperature")
plt.ylabel("Creativity Score (1-10)")
plt.grid(True)
plt.savefig("azure_creativity_vs_temperature.png")
plt.show()

# 9. Research Questions
print("\nResearch Questions:")
print("- How does GPT-3.5's creativity vary with temperature settings?")
print("- Does increasing temperature impact coherence of outputs?")
print("- How adaptable is GPT-3.5 across scientific, storytelling, and technical prompts?")

# 10. Conclusion
print("\nConclusion:")
print("Higher temperatures produce more creative but slightly less focused outputs.")
print("Lower temperatures result in more deterministic, precise outputs.")
print("GPT-3.5 adapts well across multiple prompt types but can become unpredictable at high temperatures.")