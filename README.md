# Lex: A Legal Expert System for Business Law

Lex is a web-based legal expert system designed to assist users in understanding and applying principles of Business Law. It integrates CLIPS for rule-based reasoning and Flask for a user-friendly web interface.

---

## Features

1. **Rule-Based Inference**:
   - Powered by CLIPS, implementing rules for legal inferences.
   - Supports forward and backward chaining to derive conclusions.

2. **Web-Based Interface**:
   - Flask framework enables an interactive user experience.
   - Easy data input and visualization of results.

3. **Extensible Architecture**:
   - Modular design allows for updates and expansions.
   - Ready for integration with additional legal domains.

---

## Installation

### System Requirements

- Python 3.8+
- CLIPS (or `clipspy` for integration)
- Flask

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/HawtStrokes/Lex.git
   cd Lex
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python run.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000`.

---

## File Structure

```plaintext
lex/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── utils/
│       └── inference_engine.py
├── clips/
│   └── business_rules.clp
├── templates/
│   ├── base.html
│   └── index.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── tests/
│   └── test_app.py
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

---

## Components

### 1. Core Logic
- CLIPS rules defined in `clips/business_rules.clp`.
- Processes user input and provides legal inferences.

### 2. Web Interface
- Flask manages the routing and rendering of HTML templates.
- Data is displayed dynamically in the browser.

### 3. Inference Engine
- `app/utils/inference_engine.py` manages communication with CLIPS.
- Ensures real-time processing and rule evaluation.

---

## Example Usage

1. User inputs data (e.g., facts related to a business scenario).
2. The system runs CLIPS to evaluate rules and derive conclusions.
3. Results are displayed on the web interface.

---

## Development Workflow

1. Add or modify rules in `clips/business_rules.clp`.
2. Test changes using `tests/test_app.py`.
3. Deploy using a production-ready web server like Gunicorn.


