# 📊 KPI System for Public Procurement Operations

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive KPI (Key Performance Indicator) system designed for operations teams in public procurement environments, specifically tailored for Chilean government suppliers working through ChileCompra.

## 🎯 Project Overview

This project implements two distinct KPI systems developed to measure and optimize team performance in a high-volume procurement operation:

1. **Workload Analysis System** - Measures operational analyst performance based on ticket complexity
2. **Invoice Registration System** - Tracks efficiency and accuracy of invoice processing staff

### Key Features

- ✅ Automated ticket complexity classification based on SKU counts
- ✅ Real-time performance tracking with 100% reliable metrics
- ✅ Analyst specialization detection and workload balancing
- ✅ Weekly performance dashboards with actionable insights
- ✅ Scalable architecture for multi-entity operations

## 📈 Business Context

The system was designed for organizations operating as suppliers to the Chilean government through:
- **Convenios Marco** (Framework Agreements)
- **Public Tenders** (Licitaciones)
- Multiple operational entities with diverse product categories

### Operational Scope
- 🏢 12+ legal entities
- 📦 3 main business areas: Food, Cleaning Supplies, Large Tenders
- 📊 High-volume ticket processing (100+ weekly per analyst)
- 🔄 Complex SKU management (tickets ranging from 1 to 500+ SKUs)

## 🏗️ System Architecture

### Workload KPI System

**Purpose**: Measure analyst productivity while accounting for ticket complexity

**Key Innovation**: Complexity-weighted performance metrics

```
Ticket Complexity Categories:
├── Simple: 1-10 SKUs (Weight: 1.0)
├── Medium: 11-50 SKUs (Weight: 2.5)
├── Complex: 51-150 SKUs (Weight: 5.0)
└── Very Complex: 151+ SKUs (Weight: 10.0)
```

**Core Metrics**:
- Weighted tickets processed
- Average complexity handled
- Specialization index
- Efficiency ratio

### Invoice Registration KPI System

**Purpose**: Track invoice processing efficiency with maximum reliability

**Design Philosophy**: 3 completely reliable KPIs over 5 potentially questionable metrics

**Core Metrics**:
1. **Total Invoices Registered** - Raw volume processed
2. **Average Registration Time** - Efficiency per invoice
3. **Weekly Productivity Index** - Combined performance score

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8+
pandas >= 1.3.0
numpy >= 1.21.0
plotly >= 5.0.0
streamlit >= 1.10.0 (optional, for dashboard)
```

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/kpi-system-chilecompra.git
cd kpi-system-chilecompra

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from src.kpi_calculators.workload_kpi import WorkloadAnalyzer
from src.kpi_calculators.invoice_kpi import InvoiceKPICalculator

# Initialize workload analyzer
workload = WorkloadAnalyzer()
workload.load_data('data/sample/tickets_sample.csv')

# Calculate KPIs
kpis = workload.calculate_kpis(analyst_id='A001', period='2024-W50')
print(kpis)

# Generate report
report = workload.generate_report(period='2024-W50')
```

## 📊 Example Outputs

### Workload Analysis Dashboard

The system identifies analyst specializations and performance patterns:

```
Analyst Performance Summary (Week 50, 2024)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Analyst A    │ 45 tickets │ Avg Complexity: 2.8 │ Specialist: Medium-Complex
Analyst B    │ 38 tickets │ Avg Complexity: 5.2 │ Specialist: Complex
Analyst C    │ 52 tickets │ Avg Complexity: 1.4 │ Specialist: High-Volume
```

### Invoice KPI Report

```
Weekly Invoice Processing Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Staff Member    │ Invoices │ Avg Time │ Productivity Index
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Staff A         │   127    │  4.2 min │     95.3
Staff B         │   134    │  3.9 min │    102.1
Staff C         │   118    │  4.5 min │     88.7
```

## 🧪 Methodology

### Design Principles

1. **Reliability First**: Only include metrics that are 100% trustworthy
2. **Actionable Insights**: Every KPI must drive specific decisions
3. **Context-Aware**: Account for inherent complexity variations
4. **Fair Evaluation**: Weight tasks appropriately, not just count them

### Key Learnings

- **Complexity Matters**: A 200-SKU ticket isn't comparable to a 5-SKU ticket
- **Specialization Exists**: Different analysts naturally excel at different complexity levels
- **Less is More**: 3 reliable KPIs > 5 questionable ones
- **Recent Data Wins**: Current performance is the best predictor

## 📁 Project Structure

```
kpi-system-chilecompra/
├── src/
│   ├── data_processing/      # ETL and data cleaning modules
│   ├── kpi_calculators/      # Core KPI calculation engines
│   └── visualization/        # Dashboard and reporting tools
├── data/
│   └── sample/              # Anonymized sample datasets
├── notebooks/               # Jupyter notebooks for analysis
├── docs/                    # Detailed documentation
└── tests/                   # Unit and integration tests
```

## 🔍 Use Cases

This KPI system is ideal for:

- **Performance-based compensation decisions** - Objective, fair metrics
- **Resource allocation** - Identify who handles which complexity best
- **Process optimization** - Spot bottlenecks and inefficiencies
- **Team management** - Data-driven workload balancing
- **Continuous improvement** - Track progress over time

## 🛠️ Technical Stack

- **Python 3.8+** - Core programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Plotly** - Interactive visualizations
- **Streamlit** - Dashboard interface (optional)
- **PostgreSQL/MySQL** - Database backend (production)

## 📚 Documentation

- [KPI Definitions](docs/kpi_definitions.md) - Detailed explanation of each metric
- [Methodology](docs/methodology.md) - Statistical approach and validation
- [API Reference](docs/api_reference.md) - Code documentation
- [User Guide](docs/user_guide.md) - Step-by-step usage instructions

## 🤝 Contributing

This is a professional portfolio project. While it's not open for direct contributions, feedback and suggestions are welcome through issues.


## 🎓 Key Achievements

- ✅ Implemented KPI system across 12 operational entities
- ✅ Enabled data-driven performance compensation decisions
- ✅ Reduced subjective evaluation bias by 100%
- ✅ Improved resource allocation efficiency
- ✅ Foundation for ML-driven demand forecasting (Phase 2)

## 📧 Contact

For questions, opportunities, or collaboration:
- GitHub: [@nestor-rojas](https://github.com/nestor-rojas)
- LinkedIn: www.linkedin.com/in/néstor-rojas-bravo-249053327

---

**Note**: All data in this repository has been anonymized and synthesized to protect business confidentiality while demonstrating technical capabilities.
