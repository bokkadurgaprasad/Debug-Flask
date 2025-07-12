# Flask Debugging Tutorial

This project is designed to help you learn debugging techniques in Flask by intentionally including various types of errors. It's particularly useful for understanding how to troubleshoot issues in Python 3.13.0 environments.

## Features

- Multiple intentional errors covering different scenarios
- Version conflicts to demonstrate dependency issues
- Template rendering problems
- Runtime exceptions
- Configuration mistakes

## Errors Included

1. **Import Error**: Non-existent module import
2. **Configuration Error**: Accessing config before setting
3. **Runtime Error**: Division by zero
4. **Key Error**: Accessing non-existent dictionary key
5. **Template Error**: Undefined variable in template
6. **Version Conflict**: Incompatible package versions

## Setup Instructions

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the problematic dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask application:
    ```bash
    python app.py


## Debugging Tasks
1. Fix the import error in app.py
2. Resolve the configuration access issue
3. Handle the division by zero error properly
4. Fix the KeyError for invalid user IDs
5. Correct the template rendering issue
6. Update the package versions to resolve conflicts

