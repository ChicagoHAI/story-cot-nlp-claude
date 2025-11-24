#!/usr/bin/env python3
"""
Script to download datasets for Story CoT research project.
Downloads: GPQA, JEEBench, GSM8K, and SciBench datasets from HuggingFace.
"""

from datasets import load_dataset
import os

def download_datasets():
    """Download all required datasets from HuggingFace"""

    # Create datasets directory if it doesn't exist
    os.makedirs("datasets", exist_ok=True)

    print("=" * 80)
    print("Downloading datasets for Story CoT research")
    print("=" * 80)

    # 1. GPQA Dataset (Graduate-level Problem-solving QA)
    print("\n[1/4] Downloading GPQA dataset...")
    try:
        gpqa = load_dataset("Idavidrein/gpqa", "gpqa_diamond")
        gpqa.save_to_disk("datasets/gpqa_diamond")
        print(f"✓ GPQA dataset downloaded: {len(gpqa['train'])} examples")
    except Exception as e:
        print(f"✗ Error downloading GPQA: {e}")

    # 2. JEEBench Dataset (Physics, Math, Chemistry)
    print("\n[2/4] Downloading JEEBench dataset...")
    try:
        jeebench = load_dataset("daman1209arora/jeebench")
        jeebench.save_to_disk("datasets/jeebench")
        print(f"✓ JEEBench dataset downloaded: {len(jeebench['train'])} examples")
    except Exception as e:
        print(f"✗ Error downloading JEEBench: {e}")

    # 3. GSM8K Dataset (Math word problems)
    print("\n[3/4] Downloading GSM8K dataset...")
    try:
        gsm8k = load_dataset("openai/gsm8k", "main")
        gsm8k.save_to_disk("datasets/gsm8k")
        train_size = len(gsm8k['train']) if 'train' in gsm8k else 0
        test_size = len(gsm8k['test']) if 'test' in gsm8k else 0
        print(f"✓ GSM8K dataset downloaded: {train_size} train, {test_size} test examples")
    except Exception as e:
        print(f"✗ Error downloading GSM8K: {e}")

    # 4. SciBench Dataset (College-level science problems)
    print("\n[4/4] Downloading SciBench dataset...")
    try:
        scibench = load_dataset("xw27/scibench")
        scibench.save_to_disk("datasets/scibench")
        print(f"✓ SciBench dataset downloaded")
    except Exception as e:
        print(f"✗ Error downloading SciBench: {e}")

    print("\n" + "=" * 80)
    print("Dataset download complete!")
    print("=" * 80)

if __name__ == "__main__":
    download_datasets()
