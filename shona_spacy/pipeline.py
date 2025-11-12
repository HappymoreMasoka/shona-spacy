# --------------------------------------------------------------
#  pipeline.py  –  build & return a spaCy Language object
# --------------------------------------------------------------
import spacy
from spacy.lang.en import English
from .shona_component import shona_analyzer

def create_shona_pipeline() -> English:
    """
    Returns a spaCy pipeline with:
      * tokenizer (English tokenizer works fine for Shona whitespace)
      * shona_analyzer (lookup + rules)
    """
    nlp = English()
    # Replace the default tokenizer with a very simple whitespace splitter
    # (Shona is agglutinative – word boundaries are clear)
    nlp.tokenizer = nlp.tokenizer.from_bytes(
        nlp.tokenizer.to_bytes(
            exclude=["tokenizer"]
        )
    )
    nlp.tokenizer = spacy.tokenizer.Tokenizer(
        nlp.vocab,
        prefix_search=nlp.tokenizer.prefix_search,
        suffix_search=nlp.tokenizer.suffix_search,
        infix_finditer=nlp.tokenizer.infix_finditer,
        token_match=nlp.tokenizer.token_match,
        url_match=nlp.tokenizer.url_match,
    )

    # Add our component **after** the tokenizer
    nlp.add_pipe("shona_analyzer", last=True)
    return nlp