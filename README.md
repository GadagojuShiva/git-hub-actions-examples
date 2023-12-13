# My First GitHub Actions

This repository contains a simple Python script for addition (`addition.py`) along with a GitHub Actions workflow (`first-action.yml`) that automates the testing process using pytest.

## Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Workflow Overview](#workflow-overview)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The `addition.py` script defines an `add` function for basic addition and includes a test function (`test_add`) using the `pytest` testing framework.

## Usage

To use the addition script, you can import the `add` function into your own Python code or run the tests using the provided GitHub Actions workflow.

## Workflow Overview

The GitHub Actions workflow (`first-action.yml`) is triggered on each push to the repository. Here's a summary of the workflow:

1. **Checkout**: Checks out the repository.
2. **Set up Python**: Sets up a Python environment with specified versions (3.8 and 3.9).
3. **Install dependencies**: Upgrades pip and installs the `pytest` library.
4. **Run tests**: Changes to the `src` directory and runs the tests using the `pytest` command on the `addition.py` file.

## Testing

The `test_add` function in `addition.py` has two simple test cases. The GitHub Actions workflow automatically runs these tests on each push, providing feedback on the success or failure of the tests.

## Contributing

Feel free to contribute by opening issues or pull requests. Follow the standard GitHub flow for contributing.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Open a pull request.

