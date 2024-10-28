import os
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def load_responses_from_files(directory="sentiment_data"):
    all_responses = []
    
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return pd.DataFrame()  # Return an empty DataFrame
    
    # Load all JSON files from the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            
            # Extract the date from the filename
            try:
                # Assuming the filename format: sentiment_data_2024-10-24_16-23-02.json
                timestamp_str = filename.split('_')[2] + "_" + filename.split('_')[3].replace('.json', '')
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d_%H-%M-%S")
            except (IndexError, ValueError) as e:
                print(f"Error parsing date from filename '{filename}': {e}")
                continue  # Skip this file if there's an issue

            with open(file_path, 'r') as f:
                data = json.load(f)

                # Append the date from the filename to each record
                for record in data:
                    record['Date'] = timestamp
                
                all_responses.extend(data)  # Append each response to the list

    if all_responses:
        return pd.DataFrame(all_responses)  # Return as DataFrame
    else:
        print("No data found in the directory.")
        return pd.DataFrame()  # Return empty DataFrame if no responses

def plot_summary(df, plot_type="bar"):
    # Ensure the DataFrame only contains numeric columns for sentiment scores
    numeric_cols = ['Compound Score', 'Positive Score', 'Neutral Score', 'Negative Score']

    # Check for missing numeric columns and filter out any non-numeric or missing columns
    numeric_cols_present = [col for col in numeric_cols if col in df.columns]
    
    if not numeric_cols_present:
        print(f"Error: None of the expected numeric columns ({numeric_cols}) are present in the DataFrame.")
        return

    if plot_type == "bar":
        try:
            # Group by category and calculate the mean sentiment scores
            summary = df.groupby('Category')[numeric_cols_present].mean()

            # Plotting the average sentiment scores by category
            summary.plot(kind='bar', figsize=(10, 6))
            plt.title("Average Sentiment Scores by Category")
            plt.ylabel("Average Sentiment Score")
            plt.xlabel("Category")
            plt.xticks(rotation=45)
            plt.tight_layout()  # Adjust layout to fit labels
            plt.show()
        except Exception as e:
            print(f"Error while plotting bar chart: {e}")

    elif plot_type == "line":
        # Ensure the Date column exists before proceeding
        if 'Date' not in df.columns:
            print("Error: 'Date' column is missing from the DataFrame.")
            return
        
            # Plot average compound score over time
            # plt.figure(figsize=(10, 6))
            # plt.plot(df_grouped.index, df_grouped['Compound Score'], label='Compound Score', color='blue')
            # plt.title("Average Compound Score Over Time")
            # plt.xlabel("Date")
            # plt.ylabel("Average Compound Score")
            # plt.xticks(rotation=45)
            # plt.legend()
            # plt.tight_layout()
            # plt.show()
    #     except Exception as e:
    #         print(f"Error while plotting line chart: {e}")

    # else:
    #     print(f"Invalid plot type: {plot_type}. Please choose 'bar' or 'line'.")
