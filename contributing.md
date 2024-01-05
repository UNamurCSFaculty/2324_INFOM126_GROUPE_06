# Contributor Guidelines

Following these guidelines helps to communicate that you respect the time of the developers managing and developing this open source project. In return, they should reciprocate that respect in addressing your issue, assessing changes, and helping you finalize your pull requests.

## Getting Started

1. Fork the repository and clone it to your local machine.
3. Create a new branch for your changes: `git checkout -b feature/your-feature-name`.
4. Make your changes and ensure that the tests pass. You can launch the project with `docker-compose -f docker-compose.dev.yml up --build` and then run the tests with `docker exec -it django python manage.py test`.
5. Commit your changes: `git commit -m "Add your commit message"`.
6. Push your changes to your forked repository: `git push origin feature/your-feature-name`.
7. Open a pull request to the main repository.### Issue Template

### Issue Template

**Description:**
Briefly describe the issue or feature request.

**Steps to Reproduce (if applicable):**
1. Step one
2. Step two
3. ...

**Expected Behavior:**
Explain what you expected to happen.

**Actual Behavior:**
Explain what actually happened.

**Additional Information:**
Any additional context, environment details, or screenshots.


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

## Continuous Integration (CI)
We use Continuous Integration to automate the process of checking new contributions for errors and ensuring they adhere to our project's standards. Our CI pipeline is configured using [Tool Name], and it includes the following checks:

### Linting
Ensure your code adheres to our coding standards by running the linting tools (SonarLint in our case). 

### Build:
Ensure your changes do not introduce build errors. You can check the build locally using:

```bash
docker-compose -f docker-compose.dev.yml up --build
```

### Unit Tests
Ensure your changes do not break existing functionality by running the unit tests. You can run the tests locally using the following command:

```bash
docker-compose -f docker-compose.dev.yml up --build
docker exec -it django python guestbook/manage.py test
```

### Code Coverage
Aim for good code coverage to ensure comprehensive testing. Check the coverage locally using:

```bash
docker-compose -f docker-compose.dev.yml up --build
docker exec -it django coverage guestbook/manage.py test
```

To make sure your changes pass these checks, it's recommended to run them locally before submitting a pull request. The CI pipeline will automatically run these checks again when you open a pull request.

## Code Review Process
We follow a collaborative code review process to maintain code quality. Here's how it works:

### Submit a Pull Request (PR)
Once you have completed your changes and the local tests pass, submit a pull request to the main repository.
Please, do only focus on your own features. Don't try to change minimal styling issue to minimize the changes by pr.

### Reviewers
Your PR will be assigned to one or more reviewers. They will carefully examine your code for adherence to coding standards, correctness, and other best practices.

### Feedback and Iteration
Expect feedback on your PR. Address the comments and make necessary changes. This may involve several iterations until your contribution is ready for merging.

### Approval
Once the reviewers are satisfied, your PR will be approved, and your changes will be merged into the main branch.

Remember to be patient and open to feedback during the code review process. It's a crucial step in maintaining the quality and stability of our project.
Feel free to adapt and customize these sections based on the specific tools and processes used in your project.

## Testing
- Write unit tests to cover your code changes.
- Ensure that all existing tests pass before submitting your changes.
- Include any necessary documentation updates.

## Documentation
- Update the project documentation if necessary.
- Provide clear and concise explanations for new features or changes.

## Communication

### Reporting a bug
Please follow the provided template to report a bug.

Please, don't use the issue tracker for support questions.

### Naming a PR
Please follow the provided template to name your pull requests (PRs).

### Naming a branch
Please be concise and clear when naming a branch.

### Other
For any other communication, please refer to [this section](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_06/blob/main/README.md#contacting-us)

## License Agreement
By contributing to this project, you agree that your contributions will be licensed under the [project's license](). Please review and confirm your acceptance before submitting your contribution.

## Join the Community
- Want to find others to discuss/promote our django project? Add yourself to the project discord server [here](https://discord.gg/).

We appreciate your contributions and look forward to working with you!
