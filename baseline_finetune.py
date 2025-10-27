from datasets import load_dataset

ds = load_dataset("dair-ai/emotion", "split")

print(ds['train'][:5])