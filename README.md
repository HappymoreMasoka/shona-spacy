Shona spaCy — Rule-Based NLP Pipeline for the Shona Language
🧩 Overview

Shona spaCy is a lightweight, rule-based Natural Language Processing (NLP) pipeline for the Shona language built using the spaCy
 framework.
It provides morphological analysis, noun class detection, and verb tense recognition by combining:

a verified JSON lexicon (hand-annotated tokens), and

a set of linguistic rules derived from Shona grammar.

The system lets researchers and developers perform tokenization, POS tagging, and basic morphology analysis on Shona text — similar to what spaCy provides for English, French, or German.

⚙️ Features

✅ Token-level morphological analysis
✅ Automatic detection of noun classes (Mupanda)
✅ Verb tense and subject concord identification
✅ Closed-class recognition for pronouns, conjunctions, adverbs, etc.
✅ Extensible via JSON lexicon for domain-specific Shona terms
✅ Compatible with spaCy ≥ 3.7

🧠 Example Output

Input:

Mbudzi iri kumhanya mumunda.


Output:

Mbudzi    | NOUN | Mupanda 9  | NounClass=9|Rule=True
iri       | VERB |            | Rule=True|SC=i|Tense=None
kumhanya  | VERB |            | Rule=True|SC=ku|Tense=None
mumunda   | NOUN | Mupanda 18 | NounClass=18|Prefix=mu-|Locative=True|Internal=True|Agricultural=True
.         | X    |            | Unknown

🧩 How It Works

The pipeline analyzes each token in three stages:

Lexicon Lookup (JSON-based)

If the token exists in shona_lexicon.json, the analysis uses its manually verified fields:
pos, lemma, category_detail, morph_features, gloss, comments.

Closed-Class Matching

Common function words (e.g., ini, iwe, kana, uye, mangwana) are classified directly from rule tables.

Rule-Based Morphological Parsing

For unknown words, the analyzer applies Shona morphological rules:

Noun Class (Mupanda): Prefix-based detection (e.g., mu-, va-, chi-, zvi-).

Verb Analysis: Detects subject concords (ndi-, u-, a-, ti-, mu-, va-), tense markers (no-, ka-, cha-, a-, na-), and derivational suffixes (-a, -e, -w).

Locatives: Handles classes 16–18 (pa-, ku-, mu-).

📦 Installation

You can install it directly from PyPI:

pip install shona-spacy


Requires: Python ≥ 3.8, spaCy ≥ 3.7

🚀 Quick Start
import shona_spacy
from shona_spacy.pipeline import create_shona_pipeline

# Create a Shona NLP pipeline
nlp = create_shona_pipeline()

# Analyze text
doc = nlp("Mbudzi iri kumhanya mumunda.")

# Display morphological information
for token in doc:
    print(f"{token.text:<10} | {token.pos_:<6} | {token._.category_detail or ''} | {token._.morph_features or ''}")


Expected output:

Mbudzi     | NOUN  | Mupanda 9  | NounClass=9|Rule=True
iri        | VERB  |            | Rule=True|SC=i|Tense=None
kumhanya   | VERB  |            | Rule=True|SC=ku|Tense=None
mumunda    | NOUN  | Mupanda 18 | NounClass=18|Locative=True
.          | X     |            | Unknown
