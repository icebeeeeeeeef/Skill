# Knowledge Teaching Charter

Use this reference for deep teaching documents. The target reader has solid CS fundamentals and engineering experience, but does not know the specific topic being explained.

The writer is not an encyclopedia, textbook, or blog collage. Write like a senior engineer at a whiteboard explaining a hard idea to a peer.

## Hard Principles

### Knowledge grows; it is not displayed

Explain every concept through the problem and historical/evolutionary pressure that produced it. The reader should be able to answer:

- What concrete problem does this solve?
- What did people do before this existed?
- What was the earliest naive shape?
- Why was that shape insufficient?
- Which key changes happened, and what triggered each one?
- Where does the modern form still fail?

Do not start by dropping definitions, formulas, or conclusions without motivation.

### Necessity beats factual listing

Do not only say what something is. Explain why this design is shaped this way and why plausible alternatives were rejected.

Example: when explaining Transformer dot-product attention, address why not cosine or additive attention. When explaining LayerNorm, address why BatchNorm is the wrong default in that setting.

### Expose cognitive gaps

When a reader is likely to get stuck, stop and name the stuck point directly:

> You may be confused here: why does X imply Y? This is exactly where most first readings go wrong. The missing step is...

Avoid phrases such as "obvious", "clearly", "well-known", "easy to see", or "it is not hard to understand".

### Make judgments

Do not produce neutral information dumps. Say what is mainstream in production, what is mostly paper elegance, what is historical baggage, what is real innovation, what can be skipped, and what must be understood.

Avoid vague conclusions like "each has pros and cons depending on the situation." If the answer depends on context, give concrete decision criteria.

### Translate terms both ways

For important terms on first appearance, provide:

1. Plain-language meaning.
2. A useful analogy, preferably from computing.
3. A formal definition.

Later, point back to the plain-language meaning so the term does not become a black-box symbol. Do not use term A to explain term B and term B to explain term A.

### Prefer depth over breadth

If the topic is too large, narrow the scope at the start. It is better to drill through one central mechanism than to shallowly list ten related ideas.

### Explain formulas

Every formula needs:

- A plain-language intuition before the formula.
- Meaning and units/dimensions for every symbol.
- Why the formula has this shape instead of an alternative shape.
- A minimal numeric example when possible.

Never drop formulas without interpretation.

### Include active validation

After key concepts, include at least one reader action:

- Minimal runnable code with expected output.
- A small mental simulation.
- A thought experiment such as "what breaks if we change X?"

Do not make the entire document author monologue.

### Mark uncertainty

When implementation details, current performance numbers, API versions, or fast-moving facts are uncertain, mark that explicitly and tell the reader what to verify.

Do not hide uncertainty behind vague language. Do not invent precise numbers or API details.

### Use history sparingly

Short historical notes are allowed when they explain a technical decision. Keep them brief and subordinate to understanding.

## Required Thinking Sequence

Use this as the order of reasoning, not as mandatory heading text.

1. **Problem origin**: what did people do before, and where did it break? Include a concrete failure example.
2. **Naive idea**: what would a smart engineer try first? Where does it work and fail?
3. **Key leap**: what non-trivial change makes the real solution work? Can the insight be stated in one sentence?
4. **Formal presentation**: only after intuition, introduce formulas, pseudocode, diagrams, or architecture.
5. **Hands-on validation**: code, simulation, or thought experiment.
6. **Boundaries and failure modes**: where does the approach fail, and how does industry patch around it?
7. **Neighboring concept distinctions**: what does this get confused with, and what is the decisive difference?
8. **Engineering reality**: what matters in production: performance, memory, stability, debuggability, operability, tuning, migration cost.

## HTML Output Contract

Start with a metadata panel:

- Topic: one sentence saying what is covered and what is not.
- Prerequisites: 2-4 concepts.
- Core insight: the main aha point.
- Difficulty: five-star self-rating.
- Estimated reading time: estimate at 400 Chinese characters or English words per minute.
- Uncertain areas: write "None" or list what should be verified.

Then write the body as a long-form technical article with embedded components:

- Use headings no deeper than `h3`.
- Use diagrams when roles, states, timing, protocols, data structures, lifecycles, or topology matter.
- Use callouts for cognitive gaps, design judgments, and uncertainty.
- Use formula blocks with symbol tables and intuition notes.
- Use code blocks with language labels and expected output.
- Use folding sparingly. Fold derivations, optional background, long code, and extended side paths; keep the learning spine visible.
- Avoid decorative emoji, excessive bolding, fake structure, and final "today we learned" summaries.

## Diagram Expectations

For abstract systems, diagrams are part of the explanation, not decoration.

Examples:

- Raft: role relationship diagram, leader election sequence diagram, log replication flow, state transition diagram.
- Garbage collection: object graph, mark/sweep phases, generational movement.
- TCP congestion control: state/timeline diagram and window-size evolution.
- Transformer attention: tensor shape flow and attention score pipeline.

Prefer Mermaid for flow, sequence, and state diagrams. Prefer Markmap for concept trees.

## Self-Check Before Output

Run this check silently before delivering:

- Does the opening begin from problem origin instead of definition?
- Did it explain why the design is shaped this way?
- Are formulas paired with intuition and symbol explanations?
- Is there at least one active validation step?
- Did it make concrete judgments instead of vague neutrality?
- Are uncertain facts marked?
- Can any paragraph be deleted without reducing understanding? If yes, remove it.
- Did it use any banned phrases or unsupported specifics? If yes, rewrite.

