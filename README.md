# Sleep Quality Analyzer

Sleep Quality Analyzer is a lightweight Flask web application that turns a few everyday sleep habits into a simple sleep quality score, a category label, practical insights, and visual summaries.

It is designed to be beginner-friendly, fast to run locally, and easy to extend without adding machine learning complexity.

## Key Features

- Sleep Quality Score from 0 to 100
- Automatic sleep category classification
- Insights based on screen time, caffeine, stress, and sleep duration
- Practical suggestions for improving sleep habits
- Responsive Bootstrap dashboard
- Bar chart and pie chart visualizations with Chart.js

## Inputs

The app analyzes four user inputs:

- Sleep duration in hours
- Screen time before bed in hours
- Caffeine intake in cups per day
- Stress level on a 1 to 10 scale

## How the Score Works

The score is calculated with a transparent rule-based formula:

- Sleep duration contributes up to 40 points, with 7 to 8 hours treated as ideal
- Screen time contributes up to 20 points, with lower screen time scoring better
- Caffeine intake contributes up to 20 points, with lower intake scoring better
- Stress contributes up to 20 points, with lower stress scoring better

The final total is normalized to a 0 to 100 score.

### Sleep Categories

- 0 to 40: Poor Sleep
- 41 to 70: Average Sleep
- 71 to 100: Good Sleep

## Tech Stack

- Python
- Flask
- pandas
- HTML
- Bootstrap 5
- Chart.js
- CSS

## Project Structure

```text
sleep-health-insight-tool/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── utils/
    └── analyzer.py
```

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/mandeep6207/Sleep-Health-Insight-Tool.git
cd Sleep-Health-Insight-Tool
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the app

```bash
python app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## Usage

1. Enter your sleep duration, screen time, caffeine intake, and stress level.
2. Submit the form.
3. Review the score, sleep category, insights, and suggestions.
4. Use the charts to understand which factors are affecting sleep quality most.

## Customization

If you want to tune the scoring behavior, edit [utils/analyzer.py](utils/analyzer.py).

If you want to adjust the dashboard layout, styling, or chart presentation, edit [templates/index.html](templates/index.html) and [static/style.css](static/style.css).

## Development Notes

- The app uses deterministic scoring logic instead of machine learning.
- `pandas` is used to keep the analysis pipeline easy to extend.
- Chart data is prepared on the backend and rendered on the frontend with Chart.js.

## License

No license has been added yet. Add one before publishing or distributing the project publicly.
