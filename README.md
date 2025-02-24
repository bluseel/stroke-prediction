# Stroke Risk Prediction Model

This project implements a linear regression model to predict stroke risk percentages based on various features. It uses Python with NumPy, Pandas, Matplotlib, and Scikit-learn.

## Dataset

The original stroke prediction dataset can be found here: [Stroke Risk Prediction Dataset](https://www.kaggle.com/datasets/mahatiratusher/stroke-risk-prediction-dataset/suggestions?status=pending)

## Prerequisites

Ensure you have [Anaconda](https://www.anaconda.com/) installed on your system.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Create and Activate Conda Environment

```bash
conda create --name stroke_risk python=3.9 -y
conda activate stroke_risk
```

### 3. Install Dependencies

```bash
pip install numpy pandas matplotlib scikit-learn jupyter
```

### 4. Run Jupyter Notebook

```bash
jupyter notebook
```

Open the `.ipynb` file and execute the cells to train and evaluate the model.

## Usage

- Modify `stroke_risk_dataset.csv` to use your dataset.
- Adjust model parameters (learning rate, iterations, regularization) in the notebook.
- View performance metrics (MSE, predictions, graphs).

## Troubleshooting

- If `jupyter notebook` is not found, install Jupyter manually:
  ```bash
  conda install jupyter
  ```
- If environment activation fails, use:
  ```bash
  source activate stroke_risk  # For macOS/Linux
  conda activate stroke_risk   # For Windows
  ```

## License

This project is licensed under the MIT License.
