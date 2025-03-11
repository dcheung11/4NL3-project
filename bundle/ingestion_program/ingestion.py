import json
import os
import sys
import time
import numpy as np
import pandas as pd

# Paths
input_dir = '/app/input_data/'  # Data
output_dir = '/app/output/'     # For the predictions
program_dir = '/app/program'
submission_dir = '/app/ingested_program'  # The code submitted
sys.path.append(output_dir)
sys.path.append(program_dir)
sys.path.append(submission_dir)

def get_data():
    """Get X_train, y_train, and X_test from your dataset."""
    # Read training data
    train_data = pd.read_csv(os.path.join(input_dir, 'train.csv'))
    X_train = train_data['Tweets To Be Annotated']  # Extract tweet text
    y_train = train_data.drop(columns=['Tweets To Be Annotated'])  # Extract all labels

    # Read test data
    test_data = pd.read_csv(os.path.join(input_dir, 'test.csv'))
    X_test = test_data['Tweets To Be Annotated']  # Extract tweet text

    # Convert to numpy arrays
    X_train, X_test = np.array(X_train), np.array(X_test)
    y_train = np.array(y_train)
    return X_train, y_train, X_test

def print_bar():
    """Display a bar ('----------')."""
    print('-' * 10)

def main():
    """The ingestion program."""
    print_bar()
    print('Ingestion program.')
    from model import Model  # The model submitted by the participant
    start = time.time()
    print_bar()
    print('Reading data')
    X_train, y_train, X_test = get_data()
    # Initialize model
    print('Initializing the model')
    m = Model()
    # Train model
    print('Training the model')
    m.fit(X_train, y_train)
    # Make predictions
    print('Making predictions')
    y_pred = m.predict(X_test)
    # Save predictions
    np.savetxt(os.path.join(output_dir, 'predictions.csv'), y_pred)
    duration = time.time() - start
    print(f'Completed. Total duration: {duration}')
    with open(os.path.join(output_dir, 'metadata.json'), 'w+') as f:
        json.dump({'duration': duration}, f)
    print('Ingestion program finished. Moving on to scoring')
    print_bar()

if __name__ == '__main__':
    main()