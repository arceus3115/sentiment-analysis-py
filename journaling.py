import os
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime
from questions import QUESTIONS

analyzer = SentimentIntensityAnalyzer()
responses = []

def proccessResponses():
    for category, question in QUESTIONS.items():
        print(f"Category: {category}")
        for q in question:
            print(f"\n{q}")
            
            userInputResponse = input("> ")

            sentimentScores = analyzer.polarity_scores(userInputResponse)

            responses.append({
                "Question": q,
                "Category": category,
                "Response": userInputResponse,
                "Compound Score": sentimentScores["compound"],
                "Positive Score": sentimentScores["pos"],
                "Neutral Score": sentimentScores["neu"],
                "Negative Score": sentimentScores["neg"]
            })

def saveResponsesToFile(directory="sentiment_data", filename=None):
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Format the filename with the current date and time
    if filename is None:
        # Replace spaces with underscores and remove colons for a valid filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"sentiment_data_{timestamp}.json"
    
    # Complete path to save the file
    file_path = os.path.join(directory, filename)

    # Write responses to JSON file
    with open(file_path, 'w') as f:
        json.dump(responses, f, indent=4)

    print(f"Responses saved to {file_path}")
