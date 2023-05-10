# Data Dictionary

This document describes the datasets used in this project.

## Users Table

| Field   | Description                   | Type   |
|---------|-------------------------------|--------|
| UserID  | Unique identifier for a user  | INT    |
| Age     | Age of the user               | INT    |
| Gender  | Gender of the user ('M' or 'F') | CHAR(1) |
| Location | Location of the user          | VARCHAR(100) |

## Products Table

| Field     | Description                       | Type          |
|-----------|-----------------------------------|---------------|
| ProductID | Unique identifier for a product   | INT           |
| Title     | Title of the product              | VARCHAR(255)  |
| Category  | Category of the product           | VARCHAR(100)  |
| Price     | Price of the product              | DECIMAL(5,2)  |

## Transactions Table

| Field         | Description                                      | Type       |
|---------------|--------------------------------------------------|------------|
| TransactionID | Unique identifier for a transaction              | INT        |
| UserID        | ID of the user who made the transaction          | INT        |
| ProductID     | ID of the product purchased                      | INT        |
| PurchaseDate  | Date of the purchase                             | DATE       |
| Quantity      | Quantity of the product purchased                | INT        |
| Price         | Price of the product at the time of transaction  | DECIMAL(5,2) |

## UserBehavior Table

| Field     | Description                      | Type        |
|-----------|----------------------------------|-------------|
| EventID   | Unique identifier for an event   | INT         |
| UserID    | ID of the user who triggered the event | INT   |
| SessionID | ID of the session during which the event occurred | VARCHAR(255) |
| EventName | Name of the event                | VARCHAR(100) |
| Timestamp | Time when the event occurred     | DATETIME    |
| ProductID | ID of the product related to the event | INT |

Please note that this is a simplified data dictionary. In a real project, you might have more fields in your datasets, more tables, and more complex relationships between them. Also, it's often a good idea to provide examples of field values, especially for fields that might not be self-explanatory.