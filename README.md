# Sentiment Analysis

Sentiment analysis with:

- [spacy](https://github.com/explosion/spacy-models)
- [spacytextblob](https://spacy.io/universe/project/spacy-textblob)
- [Kaggle dataset](https://www.kaggle.com/competitions/sentiment-analysis-on-movie-reviews/data?select=train.tsv.zip): Sentiment Analysis on Movie Reviews


## Usage

    source venv/bin/activate
    pip install -r requirements.txt

### Examples

Example input:

    This sentiment analysis stuff is pretty cool. I'm a fan of this stuff.

Example output:

    Polarity = 0.3 - Subjectivity = 0.825 - Assessments [(['pretty'], 0.25, 1.0, None), (['cool'], 0.35, 0.65, None)] - Ngrams = [WordList(['This', 'sentiment', 'analysis']), WordList(['sentiment', 'analysis', 'stuff']), WordList(['analysis', 'stuff', 'is']), WordList(['stuff', 'is', 'pretty']), WordList(['is', 'pretty', 'cool']), WordList(['pretty', 'cool', 'I']), WordList(['cool', 'I', "'m"]), WordList(['I', "'m", 'a']), WordList(["'m", 'a', 'fan']), WordList(['a', 'fan', 'of']), WordList(['fan', 'of', 'this']), WordList(['of', 'this', 'stuff'])]

## More Reading

- https://pythonwife.com/sentimental-analysis-with-spacy


## Troubleshooting

If it says something is missing you may need to run this:

    python -m spacy download en_core_web_md
