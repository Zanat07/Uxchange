from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from collections import defaultdict, Counter

app = Flask(__name__)
CORS(app)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'ConveniosData', 'DataConvenios.json')

FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Front', 'src')

@app.route('/api/convenios', methods=['GET'])
def get_convenios():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/analytics', methods=['GET'])
def get_analytics():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Aggregate total agreements per year
    agreements_per_year = defaultdict(int)
    # Aggregate agreements per year by state
    agreements_per_year_state = defaultdict(lambda: defaultdict(int))
    # Agreements by country
    agreements_by_country = defaultdict(int)
    # Agreement types distribution
    agreement_types = defaultdict(int)
    # KPIs
    total_agreements = 0
    active_agreements = 0

    for item in data:
        year = item.get('year', 'Unknown')
        state = item.get('state', 'Unknown')
        country = item.get('country', 'Unknown')
        agreement_type = item.get('type', 'Unknown')
        total_agreements += 1
        if state.lower() == 'active':
            active_agreements += 1

        agreements_per_year[year] += 1
        agreements_per_year_state[year][state] += 1
        agreements_by_country[country] += 1
        agreement_types[agreement_type] += 1

    # Prepare data for charts
    years_sorted = sorted(agreements_per_year.keys())
    states = set()
    for year in years_sorted:
        states.update(agreements_per_year_state[year].keys())
    states = sorted(states)

    # Stacked area chart data
    stacked_area_data = {state: [] for state in states}
    for year in years_sorted:
        for state in states:
            stacked_area_data[state].append(agreements_per_year_state[year].get(state, 0))

    analytics_data = {
        'areaChart': {
            'labels': years_sorted,
            'values': [agreements_per_year[year] for year in years_sorted],
            'label': 'Total Agreements per Year'
        },
        'stackedAreaChart': {
            'labels': years_sorted,
            'datasets': [
                {
                    'label': state,
                    'data': stacked_area_data[state]
                } for state in states
            ]
        },
        'barChart': {
            'labels': list(agreements_by_country.keys()),
            'values': list(agreements_by_country.values()),
            'label': 'Agreements by Country'
        },
        'donutChart': {
            'labels': list(agreement_types.keys()),
            'values': list(agreement_types.values()),
            'label': 'Agreement Types Distribution'
        },
        'kpis': {
            'totalAgreements': total_agreements,
            'activeAgreements': active_agreements
        }
    }

    return jsonify(analytics_data)

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def serve_frontend(path):
    return send_from_directory(FRONTEND_DIR, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
