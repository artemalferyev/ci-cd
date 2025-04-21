# Python CI/CD Project

This project demonstrates a basic **CI/CD pipeline** setup for a Python application using **GitHub Actions**. It includes automated testing with `pytest` and a deployment script to simulate a production release.

---

## Features

- GitHub Actions for continuous integration
- Automated testing with `pytest`
- Simple shell-based deployment script
- Clean project structure with `src/` and `tests/`

---
## Project Structure
ci-cd/
├── .github/workflows/ci-cd.yml     # GitHub Actions workflow
├── src/
│   └── app.py                      # Main application logic
├── tests/
│   └── test_app.py                 # Unit tests
├── requirements.txt                # Python dependencies
├── deploy.sh                       # Simple deployment script
└── README.md

---

## ⚙️ Setup
```bash
1. Clone the repo:

git clone https://github.com/artemalferyev/ci-cd.git
cd ci-cd

2.	Create a virtual environment and install dependencies:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3.	Run tests locally:
pytest

CI/CD Workflow

The GitHub Actions workflow is triggered on every push to main:
	•	Runs pytest to validate code
	•	Executes deploy.sh script (can be replaced with real deployment logic)
