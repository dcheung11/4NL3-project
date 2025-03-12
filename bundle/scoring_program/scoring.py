import json
import os
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score

# Paths
input_dir = '/app/input'  # Input from ingestion program
output_dir = '/app/output/'  # To write the scores
reference_dir = os.path.join(input_dir, 'ref')  # Ground truth data
prediction_dir = os.path.join(input_dir, 'res')  # Predictions made by the model
score_file = os.path.join(output_dir, 'scores.json')  # Scores
html_file = os.path.join(output_dir, 'detailed_results.html')  # Detailed feedback

def write_file(file, content):
    """Write content in file."""
    with open(file, 'a', encoding="utf-8") as f:
        f.write(content)

def get_data():
    """Get ground truth (y_test) and predictions (y_pred) from your dataset."""
    # Load ground truth
    y_test = pd.read_csv(os.path.join(reference_dir, 'test_ground_truth.csv'))
    y_test = y_test.drop(columns=['Tweets To Be Annotated'])  # Extract all labels
    y_test = np.array(y_test)

    # Load predictions
    y_pred = np.genfromtxt(os.path.join(prediction_dir, 'predictions.csv'), delimiter=',')
    return y_test, y_pred

def print_bar():
    """Display a bar ('----------')."""
    print('-' * 10)

def make_figure(accuracy, f1):
    fig, ax = plt.subplots()
    ax.bar(['Accuracy', 'F1 Score'], [accuracy, f1])
    ax.set_ylabel('Score')
    ax.set_title('Submission Results')
    return fig

def fig_to_b64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    fig_b64 = base64.b64encode(buf.getvalue()).decode('ascii')
    return fig_b64

def main():
    """The scoring program."""
    print_bar()
    print('Scoring program.')
    # Initialize detailed results
    write_file(html_file, '<h1>Detailed results</h1>')  # Create the file to give real-time feedback
    # Read data
    print_bar()
    print('Reading prediction')
    y_test, y_pred = get_data()
    # Compute scores
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')  # Use weighted F1 for multi-label
    print(f'Accuracy: {accuracy}')
    print(f'F1 Score: {f1}')
    # Write scores
    print_bar()
    print('Scoring program finished. Writing scores.')
    scores = {'accuracy': accuracy, 'f1_score': f1}
    print(scores)
    write_file(score_file, json.dumps(scores))
    # Create a figure for detailed results
    figure = fig_to_b64(make_figure(accuracy, f1))
    write_file(html_file, f'<img src="data:image/png;base64,{figure}">')

if __name__ == '__main__':
    main()