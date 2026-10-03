# DCF (Discounted Cash Flow) & Valuation Analysis Model
# Author: Ryan Lee

def calculate_dcf(revenue, growth_rate, operating_margin, tax_rate, wacc, terminal_growth, projection_years=5):
    print("=" * 50)
    print("      DISCOUNTED CASH FLOW (DCF) VALUATION MODEL      ")
    print("=" * 50)
    
    projected_fcf = []
    current_rev = revenue
    
    # 1. Project Free Cash Flows (FCF) for 5 Years
    print("\n[1] PROJECTED FREE CASH FLOWS (5-Year Horizon):")
    for year in range(1, projection_years + 1):
        current_rev *= (1 + growth_rate)
        ebit = current_rev * operating_margin
        fcf = ebit * (1 - tax_rate)
        
        # Discount FCF to Present Value (PV)
        pv_fcf = fcf / ((1 + wacc) ** year)
        projected_fcf.append(pv_fcf)
        
        print(f"  Year {year}: Projected FCF = ${fcf:,.2f} | Discounted PV = ${pv_fcf:,.2f}")
    
    sum_pv_fcf = sum(projected_fcf)
    
    # 2. Calculate Terminal Value (Gordon Growth Method)
    last_year_fcf = projected_fcf[-1] * ((1 + wacc) ** projection_years)
    terminal_value = (last_year_fcf * (1 + terminal_growth)) / (wacc - terminal_growth)
    pv_terminal_value = terminal_value / ((1 + wacc) ** projection_years)
    
    # 3. Calculate Intrinsic Enterprise Value
    enterprise_value = sum_pv_fcf + pv_terminal_value
    
    print("\n[2] VALUATION SUMMARY:")
    print(f"  Cumulative PV of 5-Year Cash Flows: ${sum_pv_fcf:,.2f}")
    print(f"  Present Value of Terminal Value:    ${pv_terminal_value:,.2f}")
    print(f"  --------------------------------------------------")
    print(f"  IMPLIED ENTERPRISE VALUE:           ${enterprise_value:,.2f}\n")

# Model Inputs (Company Financial Assumptions)
if __name__ == "__main__":
    calculate_dcf(
        revenue=100000000,    # $100M Starting Revenue
        growth_rate=0.08,     # 8% Annual Revenue Growth
        operating_margin=0.20,# 20% EBIT Margin
        tax_rate=0.21,        # 21% Corporate Tax Rate
        wacc=0.09,            # 9% Weighted Average Cost of Capital
        terminal_growth=0.025 # 2.5% Terminal Growth Rate
    )
