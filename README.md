
GPT-3.5 Language Model Exploration (Azure OpenAI) Project Overview

This project explores the capabilities of the GPT-3.5 model deployed on Azure OpenAI. It focuses on evaluating how the model's creativity and coherence vary with temperature settings across various prompt types, including scientific explanations, storytelling, technical summaries, and poetry.

Objectives

- Examine the impact of different `temperature` values (0.2, 0.5, 0.7, 1.0) on the creativity of model responses.
- Assess GPT-3.5’s adaptability across various domains:
  - Science 
  - Fantasy storytelling
  - Technical summaries 
  - Poetry and imaginative writing
- Visualize how creativity changes with temperature.

 Setup

 Prerequisites

- Python 3.7+
- An Azure OpenAI resource with GPT-3.5-turbo deployed
- Required Python libraries:
  ```bash
  pip install openai matplotlib
  ```

Environment Variables

Ensure the following environment variable is set:

```bash
export AZURE_OPENAI_API_KEY="your_azure_api_key"
```

 Configuration

Edit your Python file with your actual Azure values:

```python
openai.api_base = "https://<your-resource-name>.openai.azure.com/"
deployment_name = "<your-deployment-name>"
openai.api_version = "2023-05-15"
```

 How It Works

1. Prompts a set of five distinct queries to GPT-3.5.
2. Generates responses at four temperature levels: `0.2`, `0.5`, `0.7`, and `1.0`.
3. Saves all model outputs to `azure_gpt3_5_outputs.txt`.
4. Assigns **manual creativity scores** based on response richness.
5. Plots a graph of **Temperature vs. Creativity** (`azure_creativity_vs_temperature.png`).

 Prompts Used

- Explain quantum computing in simple terms.
- Write a fantasy story about a time-traveling dog.
- Explain Fourier Transform to a high school student.
- Summarize the benefits and risks of AI in healthcare.
- Compose a short poem about the future of space exploration.

 Output

- **Text File**: `azure_gpt3_5_outputs.txt` (All model responses)
- **Visualization**: `azure_creativity_vs_temperature.png` (Line plot showing how creativity varies)

 Key Insights

- **Lower temperatures** (0.2) yield deterministic and focused results.
- **Higher temperatures** (1.0) encourage imaginative, creative, and less predictable responses.
- GPT-3.5 adapts **effectively across multiple domains**, showcasing context-awareness and tone matching.
  
 Research Questions

- How does GPT-3.5's creativity vary with temperature settings?
- Does increasing temperature affect the coherence of outputs?
- How adaptable is GPT-3.5 across scientific, storytelling, and technical prompts?


 Conclusion

 "Higher temperatures produce more creative but slightly less focused outputs. Lower temperatures result in more deterministic, precise outputs. GPT-3.5 adapts well across multiple prompt types but can become unpredictable at high temperatures."
 File Structure

├── gpt3_5_azure_experiment.py
├── azure_gpt3_5_outputs.txt
├── azure_creativity_vs_temperature.png
└── README.md

Contact

If you'd like to collaborate or share feedback, feel free to connect!

 License

This project is licensed under the MIT License.
