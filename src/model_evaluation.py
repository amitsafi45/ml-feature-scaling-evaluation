from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred)

def plot_scaling_effects(X_train, X_train_scaled):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))
    ax1.scatter(X_train['Age'], X_train['EstimatedSalary'])
    ax1.set_title("Before Scaling")
    ax2.scatter(X_train_scaled['Age'], X_train_scaled['EstimatedSalary'], color='red')
    ax2.set_title("After Scaling")
    plt.show()

def plot_distributions(X_train, X_train_scaled):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))
    ax1.set_title('Before Scaling')
    sns.kdeplot(X_train['Age'], ax=ax1)
    sns.kdeplot(X_train['EstimatedSalary'], ax=ax1)

    ax2.set_title('After Standard Scaling')
    sns.kdeplot(X_train_scaled['Age'], ax=ax2)
    sns.kdeplot(X_train_scaled['EstimatedSalary'], ax=ax2)
    plt.show()
