from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization")
    print("######################################")
    print("my text: ", text)
    print("######################################")
    summary = summarizer(text, max_length=500, min_length=300, do_sample=False)
    print("######################################")
    print("my summary: ", summary[0]['summary_text'])
    print("######################################")
    return summary[0]['summary_text']
