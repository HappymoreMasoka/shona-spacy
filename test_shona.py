from shona_spacy.pipeline import create_shona_pipeline

nlp = create_shona_pipeline()

texts = [
    "Vakomana vanofamba kuchikoro mangwanani.",
    "Ndine chikafu chikuru.",
    "Mukomana anotamba bhora.",
    "Uyu ndiye mutungamiri wedu.",
]

for txt in texts:
    print(f"\n=== {txt} ===")
    doc = nlp(txt)
    for t in doc:
        print(f"{t.text:<12} {t.pos_:>6}  {t.lemma_:<12}  {t._.shona_features}")