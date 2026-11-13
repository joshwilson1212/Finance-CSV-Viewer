# Python Finance CSV Interpreter

A Python desktop application that reads financial transaction data from a CSV file, organizes transactions by month, and visualizes monthly financial activity using Matplotlib.

The application provides a graphical interface where users can view monthly income and expenses alongside their account balance and inspect individual transactions for each month.

## Features

- **CSV Import:** Reads financial transaction data from CSV files.
- **Monthly Transaction Grouping:** Organizes individual transactions by month and year.
- **Monthly Financial Summary:** Calculates the net total of transactions for each month.
- **Account Balance Tracking:** Extracts account balances from transaction records.
- **Financial Visualization:** Displays monthly transaction totals and account balances on a combined bar and line graph.
- **Transaction Explorer:** Uses a dropdown menu to select a month and view its individual transactions.
- **Color-Coded Transactions:** Displays positive transactions in green and negative transactions in red.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Tkinter
- CSV Module

## How It Works

1. Reads transaction records from a CSV file.
2. Extracts transaction dates, amounts, and account balances.
3. Groups transactions by month and year.
4. Calculates the net transaction total for each month.
5. Generates a visualization comparing monthly transaction totals against account balances.
6. Displays the graph and transaction explorer in a Tkinter GUI.

## Visualization

The application generates a combined chart containing:

- **Bar Chart:** Displays the net total of transactions for each month.
- **Line Graph:** Tracks the account balance over time.
- **Zero Reference Line:** Helps distinguish positive and negative monthly totals.

## Requirements

Install the required Python packages:

```bash
pip install pandas numpy matplotlib
```

Tkinter is included with most standard Python installations. On some Linux distributions, it may need to be installed separately.

## Running the Application

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd <project-directory>
```

3. Update the CSV file path in `Main()` to point to your transaction data:

```python
file = "path/to/info.csv"
```

4. Run the application:

```bash
python main.py
```

## CSV Format

The application expects a CSV file containing transaction records with the following information:

| Column | Description |
|---|---|
| Date | Transaction date (MM/DD/YYYY) |
| Transaction Information | Additional transaction details |
| Amount | Transaction amount |
| Balance | Account balance |

The application uses the first, third, and fourth columns to perform its calculations.

## Purpose

This project was developed to explore Python file processing, financial data organization, data visualization, and GUI development. It combines CSV parsing and data manipulation with graphical representations to make financial transaction history easier to understand.
