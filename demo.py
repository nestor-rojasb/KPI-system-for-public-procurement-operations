#!/usr/bin/env python3
"""
Quick Demo Script
=================

Demonstrates the KPI system with sample data.
Run this to verify installation and see example outputs.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.kpi_calculators import WorkloadAnalyzer, InvoiceKPICalculator


def print_section(title: str):
    """Print formatted section header."""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80 + "\n")


def demo_workload_analysis():
    """Demonstrate workload KPI analysis."""
    print_section("WORKLOAD ANALYSIS DEMO")
    
    # Initialize analyzer
    analyzer = WorkloadAnalyzer()
    
    # Load sample data
    print("📊 Loading sample ticket data...")
    analyzer.load_data('data/sample/tickets_sample.csv')
    print(f"✓ Loaded {len(analyzer.tickets_df)} tickets")
    
    # Calculate KPIs
    print("\n🔢 Calculating KPIs for Week 50, 2024...")
    kpis = analyzer.calculate_kpis(period='2024-W50')
    
    # Generate report
    print("\n📋 PERFORMANCE REPORT:")
    print(analyzer.generate_report(period='2024-W50'))
    
    # Show workload balance
    print("\n⚖️  WORKLOAD BALANCE ANALYSIS:")
    balance = analyzer.get_workload_balance()
    print(balance.to_string(index=False))
    
    return kpis


def demo_invoice_analysis():
    """Demonstrate invoice KPI analysis."""
    print_section("INVOICE REGISTRATION DEMO")
    
    # Initialize calculator
    calculator = InvoiceKPICalculator()
    
    # Load sample data
    print("📊 Loading sample invoice data...")
    calculator.load_data('data/sample/invoices_sample.csv')
    print(f"✓ Loaded {len(calculator.invoices_df)} invoices")
    
    # Calculate KPIs
    print("\n🔢 Calculating KPIs for Week 50, 2024...")
    kpis = calculator.calculate_kpis(period='2024-W50')
    
    # Generate report
    print("\n📋 PERFORMANCE REPORT:")
    print(calculator.generate_report(period='2024-W50', top_n=6))
    
    # Identify training needs
    print("\n🎓 TRAINING RECOMMENDATIONS:")
    training = calculator.identify_training_needs(threshold_percentile=25)
    if len(training) > 0:
        print(training.to_string(index=False))
    else:
        print("No staff members below training threshold.")
    
    return kpis


def demo_individual_benchmark():
    """Demonstrate individual staff benchmarking."""
    print_section("INDIVIDUAL BENCHMARKING DEMO")
    
    calculator = InvoiceKPICalculator()
    calculator.load_data('data/sample/invoices_sample.csv')
    calculator.calculate_kpis(period='2024-W50')
    
    # Benchmark a specific staff member
    staff_id = 'S001'
    print(f"📊 Benchmarking {staff_id} against team averages...\n")
    
    benchmark = calculator.benchmark_against_team(staff_id)
    
    print(f"Staff Member: {benchmark['staff_id']}")
    print(f"  Invoices vs Team Avg: {benchmark['invoices_vs_avg']:+.1f}%")
    print(f"  Time vs Team Avg: {benchmark['time_vs_avg']:+.1f}%")
    print(f"  Productivity vs Baseline: {benchmark['productivity_vs_avg']:+.1f} points")
    print(f"  Team Rank: {benchmark['rank']} of {benchmark['total_staff']}")


def main():
    """Run all demos."""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                    KPI SYSTEM DEMONSTRATION                                  ║
║                Public Procurement Operations Analytics                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    try:
        # Run demos
        workload_kpis = demo_workload_analysis()
        invoice_kpis = demo_invoice_analysis()
        demo_individual_benchmark()
        
        print_section("DEMO COMPLETE")
        print("✓ All KPI calculations completed successfully!")
        print("\nNext steps:")
        print("  1. Review the generated reports above")
        print("  2. Examine the code in src/kpi_calculators/")
        print("  3. Read the documentation in docs/")
        print("  4. Try modifying the sample data or thresholds")
        print("\nFor production use:")
        print("  - Configure your database connection in config/config.yaml")
        print("  - Replace sample data paths with your data sources")
        print("  - Customize complexity thresholds for your environment")
        print("  - Build a dashboard using src/visualization/")
        
    except Exception as e:
        print(f"\n❌ Error during demo: {e}")
        print("\nTroubleshooting:")
        print("  - Ensure you're running from the project root directory")
        print("  - Verify sample data exists in data/sample/")
        print("  - Check that all dependencies are installed (pip install -r requirements.txt)")
        sys.exit(1)


if __name__ == "__main__":
    main()
