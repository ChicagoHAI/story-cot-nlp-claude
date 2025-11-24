# Downloaded Papers

This directory contains research papers relevant to the "Story CoT" hypothesis investigating whether story-based chain-of-thought reasoning can improve language model performance.

## Papers

### 1. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- **File**: [2201.11903_chain_of_thought_prompting.pdf](2201.11903_chain_of_thought_prompting.pdf)
- **Authors**: Jason Wei, Xuezhi Wang, Dale Schuurmans, et al.
- **Year**: 2022 (updated 2023)
- **arXiv**: 2201.11903
- **Why relevant**: Foundational paper on CoT prompting. Shows how generating intermediate reasoning steps significantly improves LLM performance on complex reasoning tasks. Establishes baseline methods for our comparison.

### 2. Can Stories Help LLMs Reason? Curating Information Space Through Narrative
- **File**: [2410.19221_stories_help_llms_reason.pdf](2410.19221_stories_help_llms_reason.pdf)
- **Authors**: [Authors from arXiv]
- **Year**: 2024
- **arXiv**: 2410.19221
- **Why relevant**: HIGHLY RELEVANT - Directly addresses our hypothesis! Introduces "Story of Thought" (SoT) method that uses narrative structures in prompting. Tests on GPQA and JEEBench datasets. Shows superior performance to existing prompting techniques.

### 3. Self-Consistency Improves Chain of Thought Reasoning in Language Models
- **File**: [2203.11171_self_consistency_cot.pdf](2203.11171_self_consistency_cot.pdf)
- **Authors**: Xuezhi Wang, Jason Wei, Dale Schuurmans, et al.
- **Year**: 2022
- **arXiv**: 2203.11171
- **Why relevant**: Proposes self-consistency decoding strategy for CoT - samples diverse reasoning paths and selects most consistent answer. Important baseline method and evaluation approach.

### 4. Multimodal Chain-of-Thought Reasoning in Language Models
- **File**: [2302.00923_multimodal_cot.pdf](2302.00923_multimodal_cot.pdf)
- **Authors**: [Authors from arXiv]
- **Year**: 2023
- **arXiv**: 2302.00923
- **Why relevant**: Shows how CoT can be extended to multimodal settings (text + images). Demonstrates two-stage framework separating rationale generation and answer inference - relevant for understanding CoT mechanisms.

### 5. Physics Reasoner: Knowledge-Augmented Reasoning for Solving Physics Problems
- **File**: [2412.13791_physics_reasoner.pdf](2412.13791_physics_reasoner.pdf)
- **Authors**: [Authors from arXiv]
- **Year**: 2024
- **arXiv**: 2412.13791
- **Why relevant**: Directly relevant to physics problem-solving use case mentioned in hypothesis. Shows LLMs struggle with physics problems even with CoT (6.8% accuracy on SciBench). Provides benchmark for evaluation.

### 6. Automatic Chain of Thought Prompting in Large Language Models
- **File**: [2210.03493_auto_cot.pdf](2210.03493_auto_cot.pdf)
- **Authors**: [Authors from arXiv]
- **Year**: 2022
- **arXiv**: 2210.03493
- **Why relevant**: Auto-CoT automatically generates demonstrations with diversity. Matches or exceeds manual CoT on 10 benchmarks. Provides automated baseline approach and methodology.

## Summary Statistics

- Total papers: 6
- Date range: 2022-2024
- Key domains: Chain-of-thought reasoning, narrative reasoning, physics problem solving
- Papers with code available: 2-3 (Auto-CoT confirmed)

## Key Themes

1. **Foundational CoT Methods**: Original CoT prompting and variations (self-consistency, auto-CoT)
2. **Narrative/Story-based Reasoning**: Story of Thought (SoT) - most directly relevant to hypothesis
3. **Domain-Specific Applications**: Physics reasoning as test domain
4. **Multimodal Extensions**: CoT in vision+language settings

## Next Steps

Based on these papers:
- Use SoT paper as primary reference for story-based CoT methodology
- Consider physics reasoning benchmarks (SciBench, GPQA, JEEBench) for evaluation
- Implement Auto-CoT as automated baseline
- Compare story-based CoT against standard CoT and self-consistency
