# LLM Finetuning and Quantization

This repository focuses on **optimizing large language models (LLMs)** for efficient training and deployment. It includes implementations of key techniques to reduce model size and inference cost while maintaining performance.

---

## Overview

The project covers multiple optimization strategies for LLMs:
- **Baseline Fine-tuning:** Standard supervised fine-tuning on downstream tasks.  
- **Post-Training Quantization (PTQ):** Reducing model precision after training to improve efficiency.  
- **Quantization-Aware Training (QAT):** Training models with simulated quantization to preserve accuracy.  
- **Quantized Low-Rank Adaptation (QLoRA):** Fine-tuning LLMs using low-rank adapters with 4-bit quantization to minimize memory and compute requirements.

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/<your-username>/llm-finetuning-and-quantization.git
cd llm-finetuning-and-quantization

# Install dependencies
pip install -r requirements.txt
