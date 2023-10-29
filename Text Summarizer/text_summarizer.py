import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config

def initialize_model():
    """
    Initialize and return the T5 model, tokenizer, and device.
    """
    model = T5ForConditionalGeneration.from_pretrained('t5-small')
    tokenizer = T5Tokenizer.from_pretrained('t5-small')
    device = torch.device('cpu')
    return model, tokenizer, device

def preprocess_text(text):
    """
    Preprocess the input text for summarization.
    """
    preprocessed_text = text.strip().replace('\n','')
    t5_input_text = 'summarize: ' + preprocessed_text
    return t5_input_text

def summarize_text(text, model, tokenizer, device, min_length=30, max_length=120):
    """
    Summarize the input text using the T5 model.
    """
    t5_input_text = preprocess_text(text)
    tokenized_text = tokenizer.encode(t5_input_text, return_tensors='pt', max_length=512).to(device)
    summary_ids = model.generate(tokenized_text, min_length=min_length, max_length=max_length)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

if __name__ == "__main__":
    # Initialize the model, tokenizer, and device
    model, tokenizer, device = initialize_model()

    # Get user input for text and desired summary lengths
    text = input("Please enter the text you want to summarize: ")
    min_length = int(input("Enter minimum summary length (default is 30): ") or 30)
    max_length = int(input("Enter maximum summary length (default is 120): ") or 120)

    # Generate and print the summary
    summary = summarize_text(text, model, tokenizer, device, min_length, max_length)
    print("\nSummary:\n", summary)
