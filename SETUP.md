# Setup and Installation Guide

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/kpi-system-chilecompra.git
cd kpi-system-chilecompra
```

### 2. Create Virtual Environment

**On Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Demo

```bash
python demo.py
```

You should see output showing workload analysis, invoice KPIs, and benchmarking results.

---

## Development Setup

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=src --cov-report=html

# View coverage report
open htmlcov/index.html
```

### Code Quality

```bash
# Format code
black src/ tests/ demo.py

# Check style
flake8 src/ tests/

# Type checking (if mypy is installed)
mypy src/
```

---

## Configuration

### Basic Configuration

1. Copy the example config:
```bash
cp config/config.example.yaml config/config.yaml
```

2. Edit `config/config.yaml` with your settings

### Database Configuration (Optional)

For production use with a database:

**PostgreSQL:**
```yaml
database:
  type: postgresql
  host: localhost
  port: 5432
  database: kpi_system
```

Set environment variables:
```bash
export DB_USER=your_username
export DB_PASSWORD=your_password
```

**MySQL:**
```yaml
database:
  type: mysql
  host: localhost
  port: 3306
  database: kpi_system
```

---

## Using Your Own Data

### Data Format Requirements

#### Tickets CSV
```csv
ticket_id,analyst_id,sku_count,processed_date,entity
TKT-1001,A001,15,2024-12-09,Your Entity
TKT-1002,A002,75,2024-12-09,Your Entity
```

Required columns:
- `ticket_id`: Unique identifier
- `analyst_id`: Analyst code
- `sku_count`: Number of SKUs (integer)
- `processed_date`: ISO date format (YYYY-MM-DD)
- `entity`: Business unit (optional)

#### Invoices CSV
```csv
invoice_id,staff_id,registration_time_minutes,registration_date,entity
INV-5001,S001,4.2,2024-12-09,Your Entity
INV-5002,S002,3.8,2024-12-09,Your Entity
```

Required columns:
- `invoice_id`: Unique identifier
- `staff_id`: Staff member code
- `registration_time_minutes`: Time in minutes (float)
- `registration_date`: ISO date format (YYYY-MM-DD)
- `entity`: Business unit (optional)

### Loading Your Data

```python
from src.kpi_calculators import WorkloadAnalyzer

analyzer = WorkloadAnalyzer()
analyzer.load_data('path/to/your/tickets.csv')
kpis = analyzer.calculate_kpis(period='2024-W50')
print(analyzer.generate_report(period='2024-W50'))
```

---

## Customization

### Adjusting Complexity Thresholds

Edit `src/kpi_calculators/workload_kpi.py`:

```python
COMPLEXITY_THRESHOLDS = {
    'simple': (1, 10, 1.0),      # (min_sku, max_sku, weight)
    'medium': (11, 50, 2.5),
    'complex': (51, 150, 5.0),
    'very_complex': (151, float('inf'), 10.0)
}
```

Adjust ranges and weights based on your operational reality.

### Modifying KPI Calculations

The calculation logic is in:
- `src/kpi_calculators/workload_kpi.py` - Workload KPIs
- `src/kpi_calculators/invoice_kpi.py` - Invoice KPIs

Each calculator has clear methods for:
- Data loading
- KPI calculation
- Report generation

---

## Deployment Options

### Option 1: Local Dashboard

Create a Streamlit dashboard:

```python
# src/visualization/dashboard.py
import streamlit as st
from src.kpi_calculators import WorkloadAnalyzer

st.title("KPI Dashboard")
analyzer = WorkloadAnalyzer()
# ... add your dashboard code
```

Run with:
```bash
streamlit run src/visualization/dashboard.py
```

### Option 2: Scheduled Reports

Use cron (Linux/Mac) or Task Scheduler (Windows):

```bash
# Run weekly report every Monday at 9 AM
0 9 * * 1 cd /path/to/kpi-system && /path/to/venv/bin/python weekly_report.py
```

### Option 3: API Service

Create a Flask/FastAPI service:

```python
from flask import Flask, jsonify
from src.kpi_calculators import WorkloadAnalyzer

app = Flask(__name__)

@app.route('/kpis/<period>')
def get_kpis(period):
    analyzer = WorkloadAnalyzer()
    analyzer.load_data('data/tickets.csv')
    kpis = analyzer.calculate_kpis(period=period)
    return jsonify(kpis.to_dict())
```

### Option 4: Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "demo.py"]
```

Build and run:
```bash
docker build -t kpi-system .
docker run kpi-system
```

---

## Troubleshooting

### Common Issues

**Issue: "Module not found" error**
```bash
# Make sure you're in the project root
cd kpi-system-chilecompra

# Verify Python can find src/
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

**Issue: Date parsing errors**
```python
# Ensure dates are in correct format
df['processed_date'] = pd.to_datetime(df['processed_date'], format='%Y-%m-%d')
```

**Issue: "No module named 'src'"**
```bash
# Run from project root directory
cd /path/to/kpi-system-chilecompra
python demo.py
```

### Getting Help

1. Check the [documentation](docs/)
2. Review [example data](data/sample/)
3. Open an issue on GitHub
4. Verify your data format matches requirements

---

## Next Steps

After setup:

1. ✅ Run the demo to verify installation
2. ✅ Review sample data structure
3. ✅ Read KPI definitions in docs/
4. ✅ Try with your own data
5. ✅ Customize thresholds for your needs
6. ✅ Build visualizations or reports
7. ✅ Integrate with your systems

---

## Production Checklist

Before deploying to production:

- [ ] Configure database connection
- [ ] Set up environment variables
- [ ] Adjust complexity thresholds
- [ ] Test with representative data
- [ ] Create backup procedures
- [ ] Set up monitoring/alerting
- [ ] Document your customizations
- [ ] Train team on system usage
- [ ] Establish review schedule
- [ ] Plan for system evolution

---

## Support

For questions or issues:
- Check existing documentation
- Review code comments and docstrings
- Open a GitHub issue
- Refer to demo.py for examples
