# Coffee Shop Management
The Coffee Shop Management program is designed to help streamline the management process for a local coffee shop owner. This program integrates various functionalities to manage employee scheduling, customer information, inventory, and customer orders efficiently. 

### Process
When the program is ran, a menu will pop up displaying a list of actions listed from 1-6. The user just type into the keyboard the operation they want to perform and another prompt will show up to guide then through that process. The user shoudldn't engage with the code at all. 

1. Employee Management: 1. Add new employees 2.remove employees 3.update employee details 4.employee schedule 
2. Customer Management: 1. Add new customer 2. Remove customer 3. Update customer details. 4. View customer information 5. Track customer loyalty status
3. Inventory Management: 1. Add new item to inventory 2.Remove item from inventory 3.Update item details 4. Search for items 5.View inventory list
4. Order Management: 1.Set up tax rates. Place new order 2.View order history
5. Settings: 1.Configure loyalty program thresholds 2.Set up tax rates 
6. Exit

#### Classes
The prograam will feature two classes:  
-  The main class will connect to the database and provide a list of menu options for the user to input. The
-  The second class will contain all the methods to perform those operation. This second class will be called by the main tasks to perform these operations based on menu selections by the user. 

#### MySQL Tables
**Customer Info**
| Customer ID | Name       | Phone Number  | Email            | Loyalty Rewards (Points) |
|-------------|------------|---------------|------------------|---------------------------|
| 1           | John Doe   | 123-456-7890  | john@example.com | 100                       |
| 2           | Jane Smith | 987-654-3210  | jane@example.com | 0                         |
| 3           | Alice Lee  | 555-555-5555  | alice@example.com| 250                       |

**Employee info**
| Employee ID | Name          | Phone Number  | Email            |
|-------------|---------------|---------------|------------------|
| 001         | John Doe      | 123-456-7890  | john@example.com |
| 002         | Jane Smith    | 987-654-3210  | jane@example.com |
| 003         | Alice Lee     | 555-555-5555  | alice@example.com|

**Inventory**
| Product Number | Brand     | Description                    | Quantity | Price  | Distributor      |
|----------------|-----------|--------------------------------|----------|--------|------------------|
| 001            | Starbucks | Colombian Medium Roast Coffee | 100      | $10.99 | ABC Distributors |
| 002            | Folgers   | Classic Roast Ground Coffee   | 50       | $8.99  | XYZ Distributors |
| 003            | Lipton    | Green Tea Bags                 | 75       | $4.49  | DEF Distributors |

**Customer Orders**
| Order ID | Customer Name | Date       | Product         | Quantity | Total Amount ($) |
|----------|---------------|------------|-----------------|----------|------------------|
| 001      | John Doe      | 2024-04-23 | Latte           | 2        | 9.98             |
| 002      | Jane Smith    | 2024-04-24 | Cappuccino      | 1        | 4.99             |
| 003      | Alice Lee     | 2024-04-25 | Espresso        | 3        | 14.97            |
| 004      | Bob Johnson   | 2024-04-26 | Americano       | 2        | 9.98             |
| 005      | John Doe      | 2024-04-27 | Iced Coffee     | 1        | 4.99             |


### Technologies Used
- [x] Java is the application that the user interacts with.
- [x] SQL is the language used to communicate and
- [x] MySQL is used as the database system that houses all the shop's information. The Java application will work in direct contact with this system using the language SQL.  


#### Note: This program is still being worked on and edited. This is just the current concepts 
