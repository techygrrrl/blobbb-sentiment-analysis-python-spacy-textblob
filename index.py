import spacy
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob


nlp = spacy.load("en_core_web_md")

df = pd.read_table('./sentiment-analysis-on-movie-reviews/train.tsv.zip')


nlp.add_pipe('spacytextblob')
text = "This sentiment analysis stuff is pretty cool. I'm a fan of this stuff."
doc = nlp(text)
polarity = doc._.blob.polarity
subjectivity = doc._.blob.subjectivity
assessments = doc._.blob.sentiment_assessments.assessments
ngrams = doc._.blob.ngrams() 

print(f"Polarity = {polarity} - Subjectivity = {subjectivity} - Assessments {assessments} - Ngrams = {ngrams}")