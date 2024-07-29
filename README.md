
---

# ML Feature Scaling Evaluation

## Overview

This repository is a machine learning project focused on understanding the impact of feature scaling on model performance. The project explores how scaling affects two common models: Logistic Regression and Decision Tree.

## Project Structure

- **`data/`**: Contains the dataset and its processed versions. Raw data is in the `raw/` directory, and processed data (including scaled versions) is stored in the `processed/` directory.
- **`src/`**: Includes Python scripts for data preprocessing, model training, and evaluation.
- **`notebooks/`**: Features a Jupyter Notebook for detailed analysis and visualization of results.
- **`models/`**: Stores the trained models for both Logistic Regression and Decision Tree, both with and without scaling.
- **`README.md`**: Provides an overview and instructions for using the project.
- **`requirements.txt`**: Lists the necessary Python packages for running the project.

## Features

- **Data Preprocessing**: Scripts for loading, cleaning, and scaling the dataset.
- **Model Training**: Code to train Logistic Regression and Decision Tree models, with and without scaling.
- **Model Evaluation**: Tools to assess model performance using accuracy metrics and to visualize the effects of scaling on data and model performance.
- **Data Storage**: Procedures for saving raw, processed, and scaled datasets to ensure reproducibility.

## Getting Started

1. **Clone the Repository**: Download the repository to your local machine.
2. **Install Dependencies**: Ensure all required libraries are installed by using the `requirements.txt` file.
3. **Preprocess Data**: Use the provided scripts to load and preprocess the dataset, including scaling features.
4. **Train Models**: Execute the training scripts to build models with both raw and scaled data.
5. **Evaluate Models**: Use the evaluation scripts to measure and compare model performance. Visualizations will help illustrate the effects of scaling.
6. **Analyze Results**: Open the Jupyter Notebook to review detailed analysis and visualizations of the results.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- Data Source: Social Network Ads dataset
- Libraries: Utilizes `pandas`, `scikit-learn`, `matplotlib`, and `seaborn` for data processing, model training, and visualization.

---

Feel free to adapt or expand this description to better fit the specifics of your project or any additional details you'd like to include.