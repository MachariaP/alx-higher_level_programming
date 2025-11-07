<div align="center">

# 🚀 ALX Higher Level Programming

### *Mastering Python, SQL, JavaScript & Full Stack Development*

![Python](https://img.shields.io/badge/Python-3.8.5-blue?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=for-the-badge&logo=mysql&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?style=for-the-badge&logo=javascript&logoColor=black)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge&logo=python&logoColor=white)

**A comprehensive educational journey through higher-level programming concepts**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
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
* [🚀 CI/CD Pipeline Overview](#7-cicd-pipeline-overview)
* [📚 Resources](#8-resources)
* [📄 License](#9-license)
* [👨‍💻 Created By](#10-created-by)

</details>

---

## 1. 📋 Project Overview

### Brief Description
The **ALX Higher Level Programming** repository is a comprehensive educational project designed to build mastery in higher-level programming languages and paradigms. This repository contains a progressive curriculum covering Python programming fundamentals, Object-Oriented Programming (OOP), SQL database management, JavaScript web development, and advanced concepts like Object-Relational Mapping (ORM). The project emphasizes practical implementation, test-driven development, and industry-standard coding practices.

The repository serves as a complete learning path for software engineers transitioning from low-level C programming to higher-level languages, with a focus on real-world application development, data structures, algorithms, web scraping, API integration, and full-stack development principles.

### Project Goals
* **Master Python Programming**: Develop proficiency in Python from basics to advanced topics including OOP, inheritance, exception handling, file I/O, and serialization/deserialization
* **Database Management**: Gain expertise in SQL for database creation, queries, joins, and advanced data manipulation techniques
* **Object-Relational Mapping**: Implement ORM using SQLAlchemy to bridge the gap between object-oriented programming and relational databases
* **Web Development Fundamentals**: Build skills in JavaScript for both client-side and server-side web development, including DOM manipulation and jQuery
* **Test-Driven Development**: Implement comprehensive unit testing using Python's unittest framework and doctest for robust code quality
* **Industry Best Practices**: Follow PEP 8 style guidelines, write maintainable documentation, and develop scalable, production-ready code
* **API Integration**: Work with network protocols, HTTP requests, and RESTful API consumption
* **Data Processing**: Master data structures, JSON/CSV serialization, and web scraping techniques

### Key Tech Stack
* **Python 3.8.5**: Core programming language for backend logic, algorithms, and automation
* **SQL (MySQL)**: Relational database management and complex query operations
* **SQLAlchemy**: Python ORM framework for database abstraction and object-relational mapping
* **JavaScript (ES6+)**: Client-side and server-side scripting for web applications
* **jQuery**: JavaScript library for simplified DOM manipulation and AJAX operations
* **C**: Low-level programming for performance-critical operations and algorithmic implementations

---

## 2. 👥 Team Roles and Responsibilities

| Role | Key Responsibility |
|------|-------------------|
| **Backend Developer** | Implement Python-based business logic, data models, OOP patterns, and server-side algorithms. Design and optimize database schemas and queries for efficient data retrieval and storage. |
| **Database Administrator** | Design relational database schemas, write complex SQL queries, optimize database performance, manage data integrity, and implement backup/recovery strategies using MySQL. |
| **ORM Specialist** | Develop and maintain SQLAlchemy models, manage database migrations, implement relationship mappings between objects and database tables, and optimize query performance. |
| **Frontend Developer** | Create interactive web interfaces using JavaScript and jQuery, implement client-side validation, handle asynchronous operations, and ensure responsive design across browsers. |
| **Quality Assurance Engineer** | Write comprehensive unit tests using unittest framework, perform integration testing, validate PEP 8 compliance with pycodestyle, and ensure code coverage meets project standards. |
| **DevOps Engineer** | Manage deployment pipelines, configure continuous integration workflows, automate testing and build processes, and maintain development/production environment consistency. |
| **Technical Documentation Specialist** | Create clear README files, write inline code documentation following docstring standards, maintain project wikis, and develop user guides for implemented features. |
| **Full Stack Developer** | Integrate frontend JavaScript with Python backend APIs, implement end-to-end features spanning database to UI, and ensure seamless data flow across application layers. |

---

## 3. ⚙️ Technology Stack Overview

| Technology | Purpose in the Project |
|-----------|----------------------|
| **Python 3.8.5** | Primary programming language used for developing backend logic, implementing OOP concepts, data structures, algorithms, file handling, serialization, and automation scripts. All Python modules follow PEP 8 standards. |
| **MySQL** | Relational database management system used for data persistence, complex queries, joins, aggregations, and transaction management. Serves as the primary data store for application data. |
| **SQLAlchemy** | Python SQL toolkit and Object-Relational Mapping (ORM) library that provides a high-level abstraction for database operations, allowing Python objects to map directly to database tables and relationships. |
| **JavaScript (ES6+)** | Client-side scripting language for creating dynamic and interactive web pages, handling DOM manipulation, event listeners, asynchronous operations, and implementing modern JavaScript patterns. |
| **jQuery** | JavaScript library that simplifies HTML document traversal, event handling, animation, and AJAX interactions, providing cross-browser compatibility and reducing boilerplate code. |
| **C (gcc)** | Low-level systems programming language used for performance-critical operations, algorithmic implementations (like linked list cycle detection), and understanding memory management concepts. |
| **Bash Shell** | Unix shell scripting for automation tasks, file operations, environment variable management, and executing Python scripts with proper configuration. |
| **unittest** | Python's built-in unit testing framework used for writing and running test cases, ensuring code reliability, validating edge cases, and maintaining high code quality standards. |
| **pycodestyle** | Python style guide checker (formerly pep8) that enforces PEP 8 coding standards, ensuring consistent code formatting, readability, and maintainability across the project. |
| **JSON** | Lightweight data interchange format used for serialization/deserialization of Python objects, API data exchange, and persistent storage of structured data. |
| **CSV** | Comma-separated values format used for data import/export operations, spreadsheet compatibility, and alternative serialization method for tabular data. |
| **Git** | Version control system for tracking code changes, collaboration, branching strategies, and maintaining project history throughout the development lifecycle. |
| **Ubuntu 20.04 LTS** | Linux operating system serving as the development and deployment environment, providing consistent execution context for all scripts and applications. |

---

## 4. 🗄️ Database Design Overview

### Key Entities

The project implements multiple database schemas across different modules, with primary entities including:

* **State**: Represents geographical states with unique identifiers and names. Used in ORM demonstrations and relationship mappings.
  - **Attributes**: `id` (Integer, Primary Key), `name` (String, max 128 chars, not null)

* **City**: Represents cities belonging to states, demonstrating foreign key relationships and one-to-many associations.
  - **Attributes**: `id` (Integer, Primary Key), `name` (String, max 128 chars, not null), `state_id` (Foreign Key to State)

* **Base**: Abstract base class providing common functionality for geometric shapes, managing ID generation and serialization.
  - **Attributes**: `id` (Integer, auto-incremented or manually set)

* **Rectangle**: Geometric entity with position and dimensions, demonstrating OOP inheritance and validation.
  - **Attributes**: `id`, `width`, `height`, `x`, `y` (all integers with validation constraints)

* **Square**: Specialized rectangle with equal dimensions, showcasing inheritance and polymorphism.
  - **Attributes**: `id`, `size`, `x`, `y` (size represents both width and height)

* **User** (inferred from typical ORM patterns): User authentication and management entity.
  - **Attributes**: `id`, `username`, `email`, `password_hash`, `created_at`

### Relationships

The database design implements several relationship patterns demonstrating relational database concepts:

* **One-to-Many Relationship**: **State** → **City**
  - A single State can contain multiple Cities, but each City belongs to exactly one State.
  - Implementation: `city.state_id` references `state.id` as a foreign key
  - SQLAlchemy relationship: `State.cities` (collection of City objects)
  - Cascade behavior: Deleting a State can optionally cascade to its Cities

* **Inheritance Hierarchy**: **Base** → **Rectangle** → **Square**
  - Implements object-oriented inheritance pattern in code (not table inheritance)
  - Base class manages common attributes and methods (ID generation, serialization)
  - Rectangle extends Base with geometric properties and validation
  - Square further specializes Rectangle with size constraints (width equals height)

* **Serialization Relationships**: All entities support conversion to dictionary and JSON formats, enabling data persistence and API communication while maintaining referential integrity across related objects.

---

## 5. ✨ Feature Breakdown

### Python Programming Fundamentals
* **Hello World Programs**: Introduction to Python syntax, print statements, string manipulation, and f-string formatting for dynamic output generation.
* **Control Flow Structures**: Implementation of conditional statements (if/elif/else), loops (for, while), and function definitions with proper parameter handling and return values.
* **Module System**: Creating importable Python modules, understanding `__name__` variable, and organizing code into reusable components with proper namespace management.

### Data Structures and Algorithms
* **List Operations**: Advanced list manipulation including slicing, indexing, list comprehensions, and lambda functions for efficient data processing and transformation.
* **Dictionary and Set Manipulation**: Working with key-value pairs, set operations (union, intersection, difference), and choosing appropriate data structures for specific use cases.
* **Algorithm Implementation**: Sorting algorithms, search patterns, and data structure traversal techniques demonstrating computational thinking and problem-solving skills.

### Object-Oriented Programming
* **Class Definitions**: Creating classes with attributes and methods, implementing constructors (`__init__`), and managing instance vs. class attributes for proper encapsulation.
* **Inheritance and Polymorphism**: Building class hierarchies, method overriding, super() usage, and demonstrating code reuse through inheritance patterns like Rectangle extending Base.
* **Encapsulation**: Implementing private attributes with getter/setter methods, property decorators, and validation logic to ensure data integrity and enforce business rules.
* **Special Methods**: Overriding `__str__`, `__repr__`, comparison operators, and other magic methods for intuitive object behavior and string representation.

### Exception Handling
* **Try-Except Blocks**: Graceful error handling, catching specific exceptions (TypeError, ValueError), and implementing appropriate error recovery strategies.
* **Custom Exceptions**: Creating user-defined exception classes for domain-specific error conditions, improving code clarity and error reporting.
* **Resource Management**: Using context managers and ensuring proper cleanup of resources like file handles and database connections.

### File Input/Output
* **File Operations**: Reading from and writing to text files, binary file handling, and managing file pointers for sequential and random access patterns.
* **JSON Serialization**: Converting Python objects to JSON format using `json.dumps()`, deserializing JSON strings to Python objects, and handling nested data structures.
* **CSV Processing**: Reading CSV files for data import, writing structured data to CSV format, and handling delimiter-separated values for spreadsheet integration.

### Test-Driven Development
* **Unit Testing**: Comprehensive test suites using Python's unittest framework, covering edge cases, boundary conditions, and expected behaviors with assertions.
* **Doctest Integration**: Embedding executable examples in docstrings that serve as both documentation and automated tests, ensuring code examples remain accurate.
* **Test Coverage**: Validating that tests exercise all code paths, including error conditions, achieving high coverage percentages for production confidence.

### SQL Database Management
* **DDL Operations**: Creating databases and tables with proper constraints (PRIMARY KEY, FOREIGN KEY, NOT NULL), defining indexes, and managing schema evolution.
* **DML Operations**: SELECT queries with WHERE clauses, INSERT statements for data creation, UPDATE for modifications, and DELETE for removal with proper transaction handling.
* **Advanced Queries**: JOINs (INNER, LEFT, RIGHT), subqueries, aggregate functions (COUNT, SUM, AVG, MAX, MIN), GROUP BY clauses, and HAVING filters for complex data analysis.
* **Data Filtering**: WHERE conditions with comparison operators, LIKE patterns for string matching, IN clauses, and combining multiple conditions with AND/OR logic.

### Object-Relational Mapping (ORM)
* **SQLAlchemy Models**: Defining declarative base classes, Column types, relationships between models, and mapping Python objects to database tables automatically.
* **Database Sessions**: Managing database connections, transactions, commits, rollbacks, and ensuring ACID properties through proper session lifecycle management.
* **Query API**: Using SQLAlchemy's query interface for database operations, filtering with Python syntax, lazy loading relationships, and optimizing query performance.
* **Relationship Mapping**: Implementing one-to-many, many-to-many, and one-to-one relationships with back_populates, cascade options, and referential integrity constraints.

### JavaScript Programming
* **ES6 Syntax**: Arrow functions, template literals, destructuring, const/let declarations, and modern JavaScript patterns for cleaner, more maintainable code.
* **DOM Manipulation**: Selecting elements with querySelector, modifying element content and attributes, creating/removing DOM nodes, and updating page structure dynamically.
* **Event Handling**: Adding event listeners for user interactions (clicks, form submissions, keyboard events), event delegation, and preventing default behaviors.
* **Asynchronous Operations**: Working with callbacks, promises, and fetch API for AJAX requests, handling asynchronous code flow, and updating UI based on server responses.

### Web Scraping
* **HTTP Requests**: Making GET/POST requests using Python's requests library, handling response status codes, and parsing HTML content for data extraction.
* **HTML Parsing**: Using libraries to navigate HTML structure, selecting elements by tag, class, or ID, and extracting text, attributes, and nested data.
* **Data Extraction**: Scraping structured data from websites, handling pagination, respecting robots.txt, and implementing rate limiting for ethical scraping.

### jQuery Integration
* **Simplified DOM Manipulation**: Using jQuery selectors ($) for element selection, chaining methods for concise code, and cross-browser compatibility for consistent behavior.
* **AJAX Operations**: Making asynchronous HTTP requests with $.ajax(), $.get(), and $.post(), handling JSON responses, and updating page content without full reload.
* **Animation and Effects**: Implementing fade, slide, and custom animations, creating interactive user experiences, and managing animation queues.

### Serialization and Data Persistence
* **Dictionary Conversion**: Converting class instances to dictionary representations with `to_dictionary()` methods for API responses and data transfer.
* **JSON Persistence**: Saving object state to JSON files using `save_to_file()`, loading objects from JSON with `load_from_file()`, enabling data persistence between sessions.
* **CSV Serialization**: Alternative serialization format for compatibility with spreadsheet applications and data analysis tools, supporting import/export workflows.

---

## 6. 🔒 API Security Overview

While this educational repository focuses primarily on foundational programming concepts, understanding and implementing API security measures is crucial for production applications. The following security practices are essential considerations:

### Input Validation and Sanitization
**Purpose**: Prevent SQL injection, XSS attacks, and data corruption by validating all user inputs before processing.
* **Implementation**: Type checking in setter methods (e.g., ensuring width is an integer), range validation (e.g., width > 0), and sanitizing string inputs to remove malicious code.
* **Critical Reason**: Unvalidated input is the #1 security vulnerability. Input validation demonstrated in Rectangle class (`TypeError` for non-integers, `ValueError` for invalid ranges) provides a foundation for secure data handling.

### Authentication and Authorization
**Purpose**: Ensure only authorized users can access protected resources and perform specific operations.
* **Implementation Approach**: Use secure password hashing (bcrypt, Argon2), implement session management with secure tokens (JWT), and enforce role-based access control (RBAC).
* **Critical Reason**: Authentication verifies user identity; authorization controls what authenticated users can do. Without these, any user could access or modify any data, leading to data breaches.

### SQL Injection Prevention
**Purpose**: Protect against malicious SQL code injection that could compromise database integrity and confidentiality.
* **Implementation**: Use parameterized queries with SQLAlchemy ORM (demonstrated in object-relational mapping modules), avoid string concatenation for SQL queries, and employ prepared statements.
* **Critical Reason**: SQL injection allows attackers to execute arbitrary database commands, potentially exposing sensitive data, deleting records, or gaining system access. ORM usage in this project inherently provides protection.

### Secure Data Transmission
**Purpose**: Protect data in transit between client and server from eavesdropping and tampering.
* **Implementation Approach**: Use HTTPS/TLS for all network communication, implement certificate pinning, and encrypt sensitive data before transmission.
* **Critical Reason**: Unencrypted HTTP traffic can be intercepted, allowing attackers to steal credentials, session tokens, or sensitive user data.

### Rate Limiting and Throttling
**Purpose**: Prevent abuse, brute force attacks, and denial of service by limiting request frequency.
* **Implementation Approach**: Implement request counters per IP/user, set time windows for allowed requests, and return 429 (Too Many Requests) status when limits exceeded.
* **Critical Reason**: Without rate limiting, attackers can brute force passwords, scrape entire databases, or overwhelm servers with requests causing service disruption.

### Error Handling and Information Disclosure
**Purpose**: Prevent leaking sensitive system information through error messages while maintaining debuggability.
* **Implementation**: Catch exceptions gracefully (as demonstrated with try-except blocks), log detailed errors server-side, and return generic error messages to clients.
* **Critical Reason**: Detailed error messages can reveal database structure, file paths, library versions, and other information attackers can exploit to craft targeted attacks.

### Session Management
**Purpose**: Securely track user state across multiple requests while preventing session hijacking.
* **Implementation Approach**: Generate cryptographically secure session IDs, set appropriate session timeouts, implement secure cookie flags (HttpOnly, Secure, SameSite).
* **Critical Reason**: Weak session management allows attackers to impersonate legitimate users, gaining unauthorized access to accounts and sensitive operations.

### Data Encryption at Rest
**Purpose**: Protect sensitive data stored in databases or files from unauthorized access if storage is compromised.
* **Implementation Approach**: Encrypt sensitive fields (passwords, personal information) using strong encryption algorithms (AES-256), manage encryption keys securely, and implement key rotation.
* **Critical Reason**: Database backups, stolen hard drives, or compromised servers expose plaintext data. Encryption ensures data remains protected even if storage media is accessed.

---

## 7. 🚀 CI/CD Pipeline Overview

**Continuous Integration/Continuous Deployment (CI/CD)** is a modern software development practice that automates the building, testing, and deployment of code changes. By implementing CI/CD, development teams can deliver features faster, with higher quality and lower risk.

### What is CI/CD?

**Continuous Integration (CI)** is the practice of automatically building and testing code every time a team member commits changes to version control. This catches integration issues early, ensures code quality standards are met, and maintains a consistently deployable codebase.

**Continuous Deployment (CD)** extends CI by automatically deploying all code changes that pass the automated test suite to production environments. This eliminates manual deployment steps, reduces human error, and enables rapid feature delivery.

### Why CI/CD for This Project?

This educational repository benefits from CI/CD practices in several ways:

1. **Automated Code Quality Checks**: Every commit automatically runs pycodestyle linting to enforce PEP 8 standards, ensuring consistent code formatting and readability across all Python modules.

2. **Automated Testing**: The comprehensive unittest suites (189+ tests in the Python Almost a Circle module) run automatically on every push, catching regressions immediately and validating that new changes don't break existing functionality.

3. **Environment Consistency**: CI/CD ensures all code is tested in a standardized Ubuntu 20.04 LTS environment with Python 3.8.5, matching the project requirements and eliminating "works on my machine" issues.

4. **Fast Feedback Loop**: Developers receive immediate feedback on test failures, style violations, or integration issues, allowing them to fix problems while the code is fresh in their minds.

5. **Deployment Automation**: Changes that pass all tests can be automatically deployed to demonstration environments, enabling stakeholders to review features quickly without manual intervention.

### Tools and Implementation

The CI/CD pipeline for this project utilizes modern cloud-based tools:

* **GitHub Actions**: Primary CI/CD platform that triggers workflows on git push/pull request events. Workflows define automated jobs for linting, testing, and deployment steps.

* **Docker**: Containerization technology that packages the application with its dependencies (Python 3.8.5, MySQL, required libraries) ensuring identical execution environments across development, testing, and production.

* **Automated Testing Pipeline**:
  1. Code pushed to GitHub triggers GitHub Actions workflow
  2. Docker container spins up with Ubuntu 20.04 LTS and Python 3.8.5
  3. Dependencies installed (SQLAlchemy, requests, jQuery if testing web components)
  4. Pycodestyle runs to verify PEP 8 compliance
  5. Full unittest suite executes (`python3 -m unittest discover tests`)
  6. MySQL container started for ORM integration tests
  7. Test coverage report generated
  8. Results reported back to pull request with pass/fail status

* **Deployment Strategy**:
  - **Staging Environment**: Successful builds deploy to staging for manual QA review
  - **Production Deployment**: After staging approval, code deploys to production
  - **Rollback Capability**: Previous versions maintained for quick rollback if issues detected

By implementing CI/CD, this project maintains high code quality, catches bugs early, and demonstrates professional software engineering practices that prepare developers for real-world production environments.

---

## 8. 📚 Resources

### Official Documentation
* [Python 3.8 Documentation](https://docs.python.org/3.8/) - Official Python language reference and library documentation
* [SQLAlchemy Documentation](https://docs.sqlalchemy.org/) - Comprehensive guide to Python SQL toolkit and ORM
* [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/) - Complete MySQL database documentation
* [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) - Mozilla's comprehensive JavaScript learning resource
* [jQuery API Documentation](https://api.jquery.com/) - Complete reference for jQuery methods and utilities

### Python Learning Resources
* [PEP 8 – Style Guide for Python Code](https://pep8.org/) - Official Python code style guidelines
* [Python unittest Documentation](https://docs.python.org/3/library/unittest.html) - Unit testing framework guide
* [Real Python Tutorials](https://realpython.com/) - High-quality Python tutorials and articles
* [Python Design Patterns](https://refactoring.guru/design-patterns/python) - Common design patterns in Python

### Database and ORM Resources
* [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/14/orm/tutorial.html) - Official ORM tutorial
* [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/) - Interactive SQL learning platform
* [Database Design Best Practices](https://www.postgresql.org/docs/current/ddl.html) - Relational database design principles

### Testing Resources
* [Test-Driven Development with Python](https://www.obeythetestinggoat.com/) - Comprehensive TDD guide
* [Python Testing Best Practices](https://docs.python-guide.org/writing/tests/) - Testing strategies and tools

### ALX Program Resources
* [ALX Africa Official Website](https://www.alxafrica.com/) - ALX Software Engineering program information
* [ALX Intranet](https://intranet.alxswe.com/) - Student portal with project requirements and resources

### Additional Tools
* [GitHub Actions Documentation](https://docs.github.com/en/actions) - CI/CD workflow automation
* [Docker Documentation](https://docs.docker.com/) - Container platform for consistent environments
* [Pycodestyle Documentation](https://pycodestyle.pycqa.org/) - Python style checker tool

---

## 9. 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

This repository is part of the **ALX Software Engineering Program** curriculum and is maintained for educational purposes. Students are expected to understand and implement solutions independently to meet learning objectives.

### Usage Terms
* The code is open source and available under the MIT License
* Feel free to use, modify, and distribute the code for learning purposes
* Students should develop original solutions to demonstrate understanding
* Code may be used for personal learning portfolios with proper attribution
* Plagiarism of solutions in academic contexts is discouraged

**Copyright © 2024 Phinehas Macharia. Licensed under the MIT License.**

---

## 10. Created By

<div align="center">

### 👨‍💻 **Phinehas Macharia**

*Software Engineering Student | ALX Africa*

---

This comprehensive repository represents the journey through higher-level programming concepts, from foundational Python syntax to advanced full-stack development techniques. Each module demonstrates progressive skill development in software engineering, database management, web development, and industry best practices.

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
**Specialization**: Full Stack Development | Backend Engineering

</div>

---

<div align="center">

### 🙏 Acknowledgments

Special thanks to the **ALX Africa** team, mentors, and fellow students for their support throughout this learning journey. This project represents countless hours of learning, debugging, and growth in software engineering.

---

### 💡 *"The only way to do great work is to love what you do."* - Steve Jobs

---

### ⭐ **Star this repository if you find it helpful!** ⭐

![Python](https://img.shields.io/badge/Python-3.8.5-blue?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=for-the-badge&logo=mysql&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?style=for-the-badge&logo=javascript&logoColor=black)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge&logo=python&logoColor=white)

---

**Built with ❤️ and ☕ by Phinehas Macharia**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

</div>
