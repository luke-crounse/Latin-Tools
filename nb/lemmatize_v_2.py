# %%
from cltk import NLP
from cltk.languages.utils import get_lang

#from unidecode import unidecode

from pathlib import Path
import os

import pandas as pd

# %%
# HI LUKE I AM ADDING THESE COMMENTS
# BUTTERCUP IS A CAT
# I AM NOT A CLOWN

# %%
# Initialize the Latin pipeline
nlp = NLP(language="lat")

# %%
# Ensure the working directory is the directory that this file is in

script_dir = Path(__file__).parent
os.chdir(script_dir)
print(f"Working directory is {script_dir}")
# %%
# New version!
fn_ap = Path('..') / 'Files' / 'ap-latin-draft-course-framework-vocab-list-revised.csv'

df_ap_vocab = pd.read_csv(fn_ap)

# %%
text_input = input("Enter the Text: ")

# %%
# Process the text
doc = nlp.analyze(text=text_input)

#print(doc.words)

# Get lemmas
list_lemmas = [word.lemma for word in doc.words]
list_pos = [word.pos for word in doc.words]

list_words = [word.string for word in doc.words]

# %%
df_input = pd.DataFrame({
    "Word": list_words,
    "POS": list_pos,
    "Lemma": list_lemmas
})

# %%
print(df_ap_vocab)

# %%
df_merged = pd.merge(df_input, df_ap_vocab, how='left', left_on='Lemma', right_on = 'Base Word')

# %%
df_matches = df_merged[~df_merged["Base Word"].isna()]

# %%
df_matches

# %%
df_output = df_matches[["Word", "Vocabulary", "Definition"]]

# %%
df_output.to_csv(Path("..") / "Files" / "Vocab_list.csv")

# %%
for i, r in df_output.iterrows():
    print(r["Vocabulary"] + ": " + r["Definition"])


