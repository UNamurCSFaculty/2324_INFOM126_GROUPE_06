# Contributor Guidelines

Thank you for your interest in contributing to our Django project! We welcome contributions from everyone. To ensure a smooth collaboration, please follow these guidelines:

## Getting Started

1. Fork the repository and clone it to your local machine.
3. Create a new branch for your changes: `git checkout -b feature/your-feature-name`.
4. Make your changes and ensure that the tests pass. You can launch the project with `docker-compose -f docker-compose.dev.yml up --build` and then run the tests with `docker exec -it django python manage.py test`.
5. Commit your changes: `git commit -m "Add your commit message"`.
6. Push your changes to your forked repository: `git push origin feature/your-feature-name`.
7. Open a pull request to the main repository.

## Code Style

- Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code.
- Use meaningful variable and function names.
- Variable Naming Scheme:
    - Use lowercase with words separated by underscores as necessary to improve readability (snake_case).
    - Avoid using single-character variables except for counters or iterators.
    - Use descriptive names for boolean variables (e.g., `is_authenticated` instead of `auth`).
    - Avoid using names that are built-in or reserved keywords in Python.
- Write clear and concise comments to explain your code.
- Use docstrings to document classes, functions, and methods.
- Use type hints to indicate the expected data type of function parameters and return values.
- `__init__.py` files:
    - Use `__init__.py` files to make Python treat the directories as containing packages.
    - Keep `__init__.py` files as empty as possible. They should only contain absolute necessary imports and initialization code.
    - Avoid importing classes, functions, or variables into `__init__.py` from other modules within the package. This can lead to circular dependencies.


## Paradigm

- This project follows the Object-Oriented Programming (OOP) paradigm.
- Ensure that your code encapsulates data and operations on that data within objects.
- Use classes to define new types of objects.
- Use inheritance to create hierarchies of classes and reuse code.
- Use polymorphism to process objects differently depending on their data type or class.
- Use abstraction to hide implementation details from the user.

## Testing

- Write unit tests to cover your code changes.
- Ensure that all existing tests pass before submitting your changes.
- Include any necessary documentation updates.

## Documentation

- Update the project documentation if necessary.
- Provide clear and concise explanations for new features or changes.

## Communication

For any communication, please refer to [this section](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_06/blob/main/README.md#contacting-us)

## Issue template

```text
Issue Title:
[Concise and descriptive title of the issue]

Description:
[Provide a clear and detailed description of the issue. Include information such as what you were trying to achieve, what happened, and any error messages or unexpected behavior you encountered. If applicable, provide steps to reproduce the issue.]

Expected Behavior:
[Describe what you expected to happen when encountering this issue.]

Actual Behavior:
[Describe what actually happened when encountering this issue.]

Environment:
Operating System: [e.g., Windows 10, macOS, Linux]
Browser (if applicable): [e.g., Chrome, Firefox, Safari]
Version/Commit: [Specify the version or commit of the software or project you are using]

Additional relevant environment details:
Steps to Reproduce:
[Step 1]
[Step 2]
[Step 3]
...

Screenshots (if applicable):
[Include screenshots that help visualize the issue. This can be especially helpful for UI-related problems.]

Additional Information:
[Provide any additional information that might be relevant, such as workarounds you've attempted, logs, or related issues.]

Related Issues:
[If there are any related issues, mention them here.]

```

## Join the Community
- Want to find others to discuss/promote our django project? Add yourself to the project discord server [here](https://discord.gg/).

We appreciate your contributions and look forward to working with you!
