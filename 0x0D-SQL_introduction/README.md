<div align="center">

# 🗄️ SQL Introduction

### *Mastering MySQL Fundamentals & Database Management*

![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=for-the-badge&logo=mysql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Database-blue?style=for-the-badge&logo=postgresql&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

**A comprehensive introduction to SQL and relational database management with MySQL**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](../LICENSE)
[![ALX](https://img.shields.io/badge/ALX-Software_Engineering-blueviolet?style=for-the-badge)](https://www.alxafrica.com/)

</div>

---

## 📜 Table of Contents

<details>
<summary><b>Click to expand</b></summary>

* [📋 Project Overview](#1-project-overview)
* [👥 Team Roles and Responsibilities](#2-team-roles-and-responsibilities)
* [⚙️ Technology Stack Overview](#3-technology-stack-overview)
* [🗄️ Database Design Overview](#4-database-design-overview)
* [✨ Feature Breakdown](#5-feature-breakdown)
* [🔒 API Security Overview](#6-api-security-overview)
* [📚 Resources](#7-resources)
* [📄 License](#8-license)
* [👨‍💻 Created By](#9-created-by)

</details>

---

## 1. 📋 Project Overview

### Brief Description
The **SQL Introduction** module is a foundational project designed to build comprehensive expertise in Structured Query Language (SQL) and relational database management using MySQL. This module covers essential database operations from basic database creation and table manipulation to advanced query techniques including aggregations, grouping, and data transformations. Through 21 progressive SQL scripts, learners develop practical skills in Data Definition Language (DDL), Data Manipulation Language (DML), and complex query optimization techniques that form the backbone of modern data-driven applications.

This project emphasizes hands-on learning with real-world database scenarios, including student score management, temperature data analysis, and character encoding conversions. Each exercise builds upon previous concepts, creating a comprehensive learning path from fundamental SHOW and CREATE statements to sophisticated aggregate functions and multi-table operations.

### Project Goals
* **Master SQL Fundamentals**: Develop proficiency in core SQL syntax including SELECT, INSERT, UPDATE, DELETE, and database/table creation statements
* **Database Design**: Understand relational database concepts, table structures, data types, constraints (PRIMARY KEY, NOT NULL), and schema design principles
* **Query Optimization**: Learn to write efficient queries using proper indexing strategies, WHERE clause optimization, and understanding query execution plans
* **Data Manipulation**: Gain expertise in filtering, sorting, grouping, and aggregating data using ORDER BY, GROUP BY, HAVING, and aggregate functions (COUNT, AVG, MAX, MIN, SUM)
* **Advanced Operations**: Implement complex queries with JOINs, subqueries, and multi-condition filtering for sophisticated data analysis
* **Character Encoding**: Understand and manage database character sets (UTF-8, utf8mb4) and collations for international text support
* **Best Practices**: Follow SQL coding standards, write readable queries, use proper naming conventions, and implement data integrity through constraints
* **Real-World Applications**: Work with practical datasets (student scores, temperature readings) to solve authentic database challenges

### Key Tech Stack
* **MySQL 8.0**: Industry-standard relational database management system for data storage and retrieval
* **SQL (Structured Query Language)**: Declarative language for database definition, manipulation, and querying
* **Ubuntu 20.04 LTS**: Linux environment for MySQL server deployment and command-line operations

---

## 2. 👥 Team Roles and Responsibilities

| Role | Key Responsibility |
|------|-------------------|
| **Database Administrator (DBA)** | Design and implement database schemas, manage MySQL server configuration, optimize query performance, handle backup/recovery procedures, and ensure database security and integrity. Monitor server health and resource utilization. |
| **SQL Developer** | Write efficient SQL queries, develop stored procedures and functions, create complex queries with JOINs and subqueries, optimize query execution plans, and implement data validation logic through constraints and triggers. |
| **Data Engineer** | Design data pipelines for ETL (Extract, Transform, Load) operations, implement data transformation logic, manage data quality and consistency, automate database maintenance tasks, and ensure scalable data architecture. |
| **Backend Developer** | Integrate database operations with application code, implement ORM patterns, design API endpoints that interact with databases, handle database connection pooling, and ensure secure data access from application layer. |
| **Data Analyst** | Create analytical queries for business intelligence, generate reports using aggregate functions and grouping operations, design data visualizations from query results, and provide insights from database metrics. |
| **Quality Assurance Engineer** | Validate data integrity through SQL queries, test database constraints and triggers, verify query results against expected outcomes, perform load testing on database operations, and ensure data consistency across environments. |
| **DevOps Engineer** | Automate database deployment scripts, manage database version control, configure CI/CD pipelines for database migrations, monitor database performance metrics, and maintain development/staging/production database parity. |

---

## 3. ⚙️ Technology Stack Overview

| Technology | Purpose in the Project |
|-----------|----------------------|
| **MySQL 8.0** | Primary relational database management system (RDBMS) used for storing structured data in tables with defined relationships. Provides ACID (Atomicity, Consistency, Isolation, Durability) compliance for reliable transactions and supports advanced features like JSON data types, window functions, and common table expressions. |
| **SQL** | Standardized declarative language for database interaction. Used for creating databases and tables (DDL - Data Definition Language), inserting/updating/deleting data (DML - Data Manipulation Language), and querying data with SELECT statements. Enables powerful data operations through JOINs, subqueries, and aggregate functions. |
| **MySQL Command-Line Client** | Interactive terminal interface for executing SQL commands directly against MySQL server. Allows for script execution (`mysql < script.sql`), interactive query testing, and database administration tasks. Essential for running the SQL scripts in this project. |
| **Bash Shell** | Unix shell used for automating SQL script execution, piping results to files, and managing MySQL server operations through command-line tools like `mysql`, `mysqldump`, and `mysqladmin`. |
| **Ubuntu 20.04 LTS** | Linux operating system providing the stable server environment for MySQL installation and execution. Ensures consistent behavior across development, testing, and production environments. |
| **UTF-8 / utf8mb4** | Character encoding standard for international text support. utf8mb4 is MySQL's full UTF-8 implementation supporting all Unicode characters including emojis and special symbols. Critical for modern applications serving global audiences. |
| **Git** | Version control system for tracking SQL script changes, collaborating with team members, and maintaining a history of database schema evolution through migration scripts. |

---

## 4. 🗄️ Database Design Overview

### Key Entities

This module works with several practice databases and tables to demonstrate SQL concepts:

* **hbtn_0c_0 (Database)**: Primary practice database for basic SQL operations
  - **Purpose**: Learning environment for database creation, table management, and basic CRUD operations

* **first_table**: Initial table for demonstrating table creation and basic operations
  - **Attributes**: 
    - `id` (INT) - Unique identifier for records
    - `name` (VARCHAR(256)) - Text field for storing names
  - **Purpose**: Introduction to CREATE TABLE, INSERT, and SELECT operations

* **second_table**: Enhanced table demonstrating score management and advanced queries
  - **Attributes**:
    - `id` (INT) - Unique identifier for student records
    - `name` (VARCHAR(256)) - Student name
    - `score` (INT) - Student score for ranking and aggregation
  - **Purpose**: Practice with WHERE clauses, ORDER BY, GROUP BY, and aggregate functions (AVG, COUNT, MAX)
  - **Sample Data**: Contains student records (John, Alex, Bob, George) with various scores for realistic query practice

* **temperatures (Database)**: Practice database for weather data analysis
  - **city** (VARCHAR) - City name for geographical grouping
  - **value** (INT/DECIMAL) - Temperature readings in Fahrenheit
  - **Purpose**: Demonstrate GROUP BY aggregations, calculating averages by category, and sorting complex results

### Relationships

As an introductory module, the focus is on single-table operations rather than complex relationships. However, the concepts learned here form the foundation for multi-table relationships:

* **Data Integrity**: Tables use constraints like NOT NULL to ensure data quality at the database level
* **Primary Keys**: Understanding unique identifiers (id fields) prepares for foreign key relationships in advanced modules
* **Normalization Concepts**: Practice with separate tables (first_table, second_table) introduces the principle of organizing data into logical structures
* **Future Relationships**: The skills learned here enable one-to-many (e.g., State → Cities) and many-to-many relationships covered in subsequent SQL modules

### Database Schema Evolution

The project demonstrates database lifecycle management:
1. **Creation**: Starting with empty databases using `CREATE DATABASE IF NOT EXISTS`
2. **Table Definition**: Adding tables with appropriate data types and constraints
3. **Data Population**: Inserting initial records with INSERT statements
4. **Modification**: Updating existing records and table structures
5. **Cleanup**: Removing databases and tables when no longer needed
6. **Character Set Migration**: Converting tables to UTF-8 for improved character support

---

## 5. ✨ Feature Breakdown

### Database Management Operations
* **Database Creation (0-list_databases.sql, 1-create_database_if_missing.sql)**: List all databases on MySQL server using `SHOW DATABASES` and create new databases with conditional creation using `CREATE DATABASE IF NOT EXISTS` to prevent errors when database already exists.
* **Database Deletion (2-remove_database.sql)**: Safely remove databases using `DROP DATABASE IF EXISTS` with existence checking to avoid errors, understanding the permanent nature of database deletion.
* **Table Listing (3-list_tables.sql)**: Display all tables within a database using `SHOW TABLES FROM database_name`, essential for understanding database structure and available data entities.

### Table Creation and Schema Design
* **Basic Table Creation (4-first_table.sql)**: Create tables with `CREATE TABLE IF NOT EXISTS` specifying column names, data types (INT, VARCHAR), and proper syntax for table definition. Demonstrates foundational table structure design.
* **Table Structure Inspection (5-full_table.sql)**: View complete table schema including column definitions, data types, constraints, and character sets using `SHOW CREATE TABLE`, providing insight into table DDL statements.
* **Advanced Table Creation (9-full_creation.sql)**: Create tables with multiple columns, define appropriate data types for different data (INT for numeric, VARCHAR for text), and populate tables with initial data using multiple INSERT statements in a single script.

### Data Retrieval and Querying
* **Basic SELECT Operations (6-list_values.sql)**: Retrieve all records from a table using `SELECT * FROM table_name`, understanding result set formatting and how data is displayed in tabular format.
* **Conditional Filtering (8-count_89.sql, 13-change_class.sql)**: Use WHERE clause to filter records based on specific conditions (`WHERE score = 89`, `WHERE score <= 5`), demonstrating precise data filtering and boolean logic.
* **Sorting Results (10-top_score.sql)**: Order query results using `ORDER BY column_name DESC/ASC`, essential for ranking data, finding top performers, and organizing output logically.
* **Column Selection (10-top_score.sql)**: Select specific columns (`SELECT score, name`) rather than all columns, improving query performance and focusing on relevant data fields.

### Data Modification Operations
* **Inserting Records (7-insert_value.sql)**: Add new records to tables using `INSERT INTO table_name (columns) VALUES (values)` syntax, understanding data insertion and primary key management.
* **Updating Records (12-no_cheating.sql)**: Modify existing records using `UPDATE table_name SET column = value WHERE condition`, demonstrating how to change specific records while preserving others.
* **Deleting Records (13-change_class.sql)**: Remove records based on conditions using `DELETE FROM table_name WHERE condition`, understanding data removal and its permanent nature.

### Aggregate Functions and Analysis
* **Counting Records (8-count_89.sql)**: Use `COUNT(*)` to determine the number of records matching specific criteria, fundamental for data analysis and reporting metrics.
* **Calculating Averages (14-average.sql)**: Compute average values using `AVG(column_name)` aggregate function with aliases (`AS average`), essential for statistical analysis and summary reports.
* **Grouping Data (15-groups.sql)**: Combine `GROUP BY` with aggregate functions to group records by category and count occurrences per group (`GROUP BY score`), enabling category-based analysis.
* **Finding Maximum Values (103-max_state.sql)**: Use `MAX()` function to identify highest values within groups, useful for finding top performers or peak measurements.

### Advanced Query Techniques
* **Filtering Groups (16-no_link.sql)**: Exclude records with NULL values using `WHERE column IS NOT NULL`, ensuring data quality in query results and avoiding incomplete records.
* **Multi-Level Sorting (10-top_score.sql)**: Order results by multiple columns for complex ranking scenarios, providing detailed result organization.
* **Temperature Analysis (101-avg_temperatures.sql, 102-top_city.sql)**: Real-world data analysis computing average temperatures by city, demonstrating practical applications of GROUP BY, AVG(), and ORDER BY for geographical data analysis.
* **State-Based Filtering (103-max_state.sql)**: Find maximum values per state/category using GROUP BY with MAX(), showcasing how to perform aggregate operations within logical groups.

### Character Encoding and Internationalization
* **UTF-8 Conversion (100-move_to_utf8.sql)**: Convert database, tables, and columns to UTF-8 character set (utf8mb4_unicode_ci collation) using `ALTER TABLE CONVERT TO CHARACTER SET`, essential for supporting international characters, emojis, and special symbols in modern applications.

### Naming Conventions
* **Column Aliases (14-average.sql, 15-groups.sql)**: Use `AS` keyword to provide meaningful names for calculated columns in result sets, improving query readability and API response clarity.

---

## 6. 🔒 API Security Overview

While this module focuses on foundational SQL syntax, understanding security implications is critical for building production databases:

### SQL Injection Prevention
**Purpose**: Protect against malicious SQL code injection that could compromise database security.
* **Implementation**: These practice scripts demonstrate direct SQL execution. In production applications, ALWAYS use parameterized queries/prepared statements rather than string concatenation. For example, instead of `"SELECT * FROM users WHERE id = " + user_input`, use parameterized queries where the database driver automatically escapes special characters.
* **Critical Reason**: SQL injection is consistently ranked in OWASP Top 10 vulnerabilities. An attacker could inject malicious SQL (`' OR '1'='1'; DROP TABLE users; --`) to bypass authentication, extract sensitive data, or destroy databases. Parameterized queries ensure user input is treated as data, not executable code.

### Principle of Least Privilege
**Purpose**: Limit database user permissions to only what is necessary for their role.
* **Implementation**: Create separate MySQL users for different application components. A web application should connect with a user that has only SELECT, INSERT, UPDATE, DELETE privileges on specific tables, not DROP DATABASE or CREATE USER permissions. Database administrators have elevated privileges used only for maintenance tasks.
* **Critical Reason**: If an application is compromised, attackers gain the same database privileges as the application's database user. Restricting privileges limits damage potential—a user without DROP privilege cannot delete entire tables even if SQL injection occurs.

### Data Encryption
**Purpose**: Protect sensitive data from unauthorized access.
* **Implementation**: Encrypt sensitive columns (passwords, personal information, financial data) at the application level before storing in database. Use MySQL's built-in encryption functions (AES_ENCRYPT/AES_DECRYPT) or application-level encryption libraries. Never store passwords in plaintext—use bcrypt or Argon2 hashing.
* **Critical Reason**: Database backups, compromised servers, or malicious insiders could expose plaintext data. Encrypted data remains protected even if storage media is accessed. Proper password hashing ensures stolen password hashes cannot be reversed to expose original passwords.

### Secure Connection Management
**Purpose**: Protect data in transit between application and database server.
* **Implementation**: Use SSL/TLS for MySQL connections, especially when database server is remote. Configure MySQL with `require_secure_transport=ON`. Applications should connect via `mysql://user:pass@host:3306/db?ssl=true` ensuring encrypted communication channels.
* **Critical Reason**: Unencrypted database connections transmit credentials and data in plaintext over networks. Network sniffing tools can capture authentication credentials, query contents, and result sets, exposing sensitive information.

### Input Validation
**Purpose**: Ensure data meets expected formats before reaching the database.
* **Implementation**: Validate data types, ranges, and formats at application level. If expecting an integer ID, verify input is numeric before using in queries. Use regular expressions to validate email formats, phone numbers, and other structured data. Set appropriate VARCHAR lengths to prevent oversized inputs.
* **Critical Reason**: Invalid input can cause application errors, bypass business logic, or enable injection attacks. Validating input type (the score field should be INT, name should be reasonable length) prevents malformed data from corrupting database integrity.

### Audit Logging
**Purpose**: Track database access and modifications for security monitoring and compliance.
* **Implementation**: Enable MySQL general query log and slow query log for monitoring. Create trigger-based audit tables that log INSERT, UPDATE, DELETE operations with timestamps and user information. Regularly review logs for suspicious patterns (mass deletions, unusual query times, failed login attempts).
* **Critical Reason**: Audit logs enable detection of security breaches, provide accountability for data changes, support compliance requirements (GDPR, HIPAA), and help diagnose performance issues. Without logging, unauthorized data access or modification goes undetected.

### Backup and Recovery
**Purpose**: Protect against data loss from hardware failure, corruption, or malicious deletion.
* **Implementation**: Schedule regular automated backups using `mysqldump` or MySQL Enterprise Backup. Store backups in geographically separate locations. Test backup restoration procedures regularly. Implement point-in-time recovery capability using binary logs.
* **Critical Reason**: Databases are mission-critical. Hardware failures, ransomware attacks, accidental deletions (`DROP DATABASE`), or natural disasters can cause catastrophic data loss. Regular tested backups ensure business continuity and data recovery capability.

---

## 7. 📚 Resources

### Official Documentation
* [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/) - Comprehensive MySQL documentation covering all SQL statements, functions, and server configuration
* [MySQL Tutorial](https://dev.mysql.com/doc/mysql-tutorial-excerpt/8.0/en/) - Official beginner-friendly tutorial with practical examples
* [SQL Standard Documentation](https://www.iso.org/standard/63555.html) - ISO/IEC 9075 SQL standard specification

### Learning Resources
* [W3Schools SQL Tutorial](https://www.w3schools.com/sql/) - Interactive SQL learning platform with try-it-yourself examples
* [SQLZoo](https://sqlzoo.net/) - Interactive SQL tutorials with progressive difficulty levels and practice exercises
* [Mode SQL Tutorial](https://mode.com/sql-tutorial/) - Comprehensive SQL tutorial focused on data analysis use cases
* [LeetCode SQL Problems](https://leetcode.com/problemset/database/) - Practice SQL through coding challenges of varying difficulty

### MySQL Tools
* [MySQL Workbench](https://www.mysql.com/products/workbench/) - Visual database design and administration tool with query builder and schema visualization
* [phpMyAdmin](https://www.phpmyadmin.net/) - Web-based MySQL administration interface for database management
* [DBeaver](https://dbeaver.io/) - Universal database tool supporting MySQL and multiple database platforms

### Character Encoding Resources
* [UTF-8 and Unicode FAQ](https://www.unicode.org/faq/utf_bom.html) - Understanding Unicode and UTF-8 encoding
* [MySQL Character Sets](https://dev.mysql.com/doc/refman/8.0/en/charset.html) - MySQL character set and collation documentation
* [utf8mb4 in MySQL](https://mathiasbynens.be/notes/mysql-utf8mb4) - Why utf8mb4 matters for proper UTF-8 support

### Best Practices
* [SQL Style Guide](https://www.sqlstyle.guide/) - Community-driven SQL coding conventions and formatting standards
* [Database Design Best Practices](https://www.sisense.com/blog/better-sql-schema/) - Principles for effective database schema design
* [SQL Naming Conventions](https://www.c-sharpcorner.com/article/sql-server-naming-conventions/) - Standards for naming databases, tables, and columns

### Performance Optimization
* [MySQL Query Optimization](https://dev.mysql.com/doc/refman/8.0/en/optimization.html) - Official guide to optimizing SQL queries and indexes
* [Use The Index, Luke!](https://use-the-index-luke.com/) - Guide to database performance for developers explaining indexing strategies
* [EXPLAIN Statement](https://dev.mysql.com/doc/refman/8.0/en/explain.html) - Understanding query execution plans for optimization

### ALX Resources
* [ALX Africa Official Website](https://www.alxafrica.com/) - Software Engineering program information and curriculum overview
* [ALX Intranet](https://intranet.alxswe.com/) - Student portal with project requirements, deadlines, and learning resources

---

## 8. 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](../LICENSE) file for details.

The SQL scripts in this repository are part of the **ALX Software Engineering Program** curriculum and are intended for educational purposes. Students should develop their own solutions to demonstrate understanding of SQL concepts and database management principles.

### Usage Terms
* Open source under MIT License - free to use, modify, and distribute
* Educational resource for learning SQL and MySQL fundamentals
* Students should implement original solutions to meet learning objectives
* Code may be referenced for understanding but should not be copied for academic submissions
* Appropriate for personal portfolios with proper attribution to ALX program

**Copyright © 2024 Phinehas Macharia. Licensed under the MIT License.**

---

## 9. 👨‍💻 Created By

<div align="center">

### **Phinehas Macharia**

*Software Engineering Student | Database Enthusiast | ALX Africa*

---

This SQL introduction module represents the foundational journey into relational database management and structured query language. Each script demonstrates progressive skill development from basic database operations to complex data analysis techniques, preparing for advanced database concepts and real-world application development.

**Connect with the Creator:**

<p align="center">
  <a href="https://github.com/MachariaP">
    <img src="https://img.shields.io/badge/GitHub-MachariaP-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
  <a href="https://www.linkedin.com/in/phinehas-macharia">
    <img src="https://img.shields.io/badge/LinkedIn-Phinehas_Macharia-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <a href="mailto:walburphinehas78@gmail.com">
    <img src="https://img.shields.io/badge/Email-walburphinehas78@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>
</p>

**Project Timeline**: 2024  
**ALX Program**: Software Engineering Cohort  
**Module Focus**: SQL Introduction & MySQL Fundamentals

</div>

---

<div align="center">

### 🙏 Acknowledgments

Special thanks to **ALX Africa** for providing a comprehensive software engineering curriculum, the mentors who guide this learning journey, and fellow students collaborating on database challenges. This module represents the essential first steps in database management that power modern web applications.

---

### 💡 *"Data is the new oil, and SQL is the refinery."* - Inspired by Data Science Community

---

### ⭐ **Star this repository if you find it helpful!** ⭐

![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=for-the-badge&logo=mysql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Structured_Query_Language-blue?style=for-the-badge&logo=postgresql&logoColor=white)
![Learning](https://img.shields.io/badge/Status-Learning-brightgreen?style=for-the-badge)

---

**Built with ❤️ and ☕ by Phinehas Macharia | ALX Software Engineering Program**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](../LICENSE)

</div>

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| **Total SQL Scripts** | 21 |
| **Core Concepts Covered** | DDL, DML, Aggregation, Grouping, Sorting |
| **Database Operations** | CREATE, DROP, INSERT, UPDATE, DELETE, SELECT |
| **Advanced Features** | GROUP BY, ORDER BY, AVG(), COUNT(), MAX() |
| **Character Encoding** | UTF-8 (utf8mb4) Support |
| **Difficulty Level** | Beginner to Intermediate |

---

<div align="center">

### 🚀 Ready to master SQL? Start with script 0 and progress through each numbered file!

**Each script builds upon previous concepts - follow the numerical order for optimal learning.**

</div>
