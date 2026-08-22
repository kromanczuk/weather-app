from transformers import pipeline

classifier = pipeline( "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english")

result = classifier("Streamlit makes it easy to build amazing apps!")
print(result)