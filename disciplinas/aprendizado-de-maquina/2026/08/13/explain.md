An **Analytical Base Table (ABT)** is a structured dataset used in data science and machine learning projects. It’s essentially the foundation for building predictive models, where all relevant information is organized into **features** (inputs) and a **target** (output).

---

## Features vs. Target in ABT

- **Features**  
  - These are the independent variables (inputs) used to train the model.  
  - They describe the characteristics of the entities being analyzed (customers, products, transactions, etc.).  
  - Examples: age, income, purchase history, number of website visits, credit score.  
  - Features can be numerical, categorical, or derived (engineered from raw data).

- **Target**  
  - This is the dependent variable (output) the model is trying to predict.  
  - It represents the business objective or outcome of interest.  
  - Examples: whether a customer will churn (yes/no), the amount of a future purchase, probability of loan default.  
  - The target must be clearly defined and measurable.

---

## Example ABT Structure

| **Column** | **Type** | **Role** |
|------------|----------|----------|
| Customer_ID | Identifier | Not used in modeling |
| Age | Numeric | Feature |
| Income | Numeric | Feature |
| Region | Categorical | Feature |
| Past_Purchases | Numeric | Feature |
| Churn_Flag | Binary (0/1) | Target |

---

## Why ABT Matters

- Ensures **consistency** across modeling experiments.  
- Provides a **single source of truth** for features and target.  
- Simplifies collaboration between data engineers, analysts, and data scientists.  
- Makes it easier to track **data lineage** and transformations.
