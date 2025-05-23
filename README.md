# UN Intercambio Project

## Overview

This project is a web application for managing and visualizing international agreements ("convenios") data. It consists of a backend server that serves data and APIs, and a frontend web interface that displays dashboards and information about the agreements.

## Project Structure

- **Back/**: Backend server and data files
  - `server.py`: Flask backend server providing API endpoints and serving the frontend.
  - `ConveniosData/`: Contains the main JSON data file `DataConvenios.json` with agreements data.
  - `HeatMapData/`: Contains additional data and packages related to heatmap visualizations.

- **Front/**: Frontend web application
  - `src/`: Source files for the frontend
    - `pages/`: HTML pages including `Analytics.html` (dashboard) and `Convenios.html`.
    - `atoms/`, `molecules/`, `organisms/`: CSS and component files for styling and UI.
    - `assets/`: Images and flags used in the UI.
    - `scripts/`: JavaScript files (if any).
    - `templates/`: HTML templates (if any).

## Backend

- Built with Flask.
- Provides API endpoints:
  - `/api/convenios`: Returns the full agreements data from `DataConvenios.json`.
  - `/api/analytics`: Returns aggregated data for dashboards, including:
    - Total agreements per year.
    - Agreements per year by state.
    - Agreements by country.
    - Distribution of agreement types.
    - Key performance indicators (KPIs) such as total and active agreements.

## Frontend

- Uses HTML, CSS, and JavaScript.
- Dashboard page (`Analytics.html`) uses Chart.js to render various charts:
  - Area chart for total agreements per year.
  - Stacked area chart for agreements per year by state.
  - Bar chart for agreements by country.
  - Donut chart for agreement types distribution.
  - Displays KPIs for total and active agreements.
- Fetches data from the backend `/api/analytics` endpoint.

## Running the Project

1. Ensure Python and Flask are installed.
2. Navigate to the `Back` directory.
3. Run the backend server:
   ```
   python server.py
   ```
4. Open the frontend pages in a browser by navigating to:
   ```
   http://localhost:5000/index.html
   ```
## Notes

- The backend server enables CORS to allow frontend requests.
- The frontend uses Chart.js from CDN for chart rendering.
- The project includes many country flag images used in the UI.
- The data file `DataConvenios.json` contains detailed information about agreements, institutions, countries, years, and states.

## Future Improvements

- Add more chart types such as funnel, gauge, combined charts, and maps.
- Enhance UI/UX with better styling and interactivity.
- Implement authentication and user management.
- Optimize data loading and caching for performance.
# Uxchange
