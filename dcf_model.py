# DCF (Discounted Cash Flow) & Valuation Analysis Model
# Author: Ryan Lee

def calculate_dcf(revenue, growth_rate, operating_margin, tax_rate, wacc, terminal_growth, projection_years=5):
    print("=" * 55)
    print("      DISCOUNTED CASH FLOW (DCF) VALUATION MODEL      ")
    print("=" * 55)
    
    pv_fcf_list = []
    current_rev = revenue
    last_nominal_fcf = 0
    
    # 1. Project Free Cash Flows (FCF) for 5-Year Horizon
    print("\n[1] PROJECTED FREE CASH FLOWS:")
    for year in range(1, projection_years + 1):
        current_rev *= (1 + growth_rate)
        ebit = current_rev * operating_margin
        fcf = ebit * (1 - tax_rate) # Unlevered Free Cash Flow (NOPAT)
        last_nominal_fcf = fcf
        
        # Discount FCF to Present Value (PV)
        pv_fcf = fcf / ((1 + wacc) ** year)
        pv_fcf_list.append(pv_fcf)
        
        print(f"  Year {year}: Revenue = ${current_rev:,.0f} | FCF = ${fcf:,.2f} | Discounted PV = ${pv_fcf:,.2f}")
    
    sum_pv_fcf = sum(pv_fcf_list)
    
    # 2. Terminal Value (Gordon Growth Method)
    # Terminal Value = (Year 5 FCF * (1 + g)) / (WACC - g)
    terminal_value = (last_nominal_fcf * (1 + terminal_growth)) / (wacc - terminal_growth)
    pv_terminal_value = terminal_value / ((1 + wacc) ** projection_years)
    
    # 3. Implied Enterprise Value
    enterprise_value = sum_pv_fcf + pv_terminal_value
    
    print("\n[2] VALUATION SUMMARY:")
    print(f"  Cumulative PV of 5-Year Cash Flows: ${sum_pv_fcf:,.2f}")
    print(f"  Present Value of Terminal Value:    ${pv_terminal_value:,.2f}")
    print(f"  --------------------------------------------------")
    print(f"  IMPLIED ENTERPRISE VALUE:           ${enterprise_value:,.2f}\n")

if __name__ == "__main__":
    # Model Inputs (Company Financial Assumptions)
    calculate_dcf(
        revenue=100000000,    # $100M Starting Revenue
        growth_rate=0.08,     # 8% Annual Revenue Growth
        operating_margin=0.20,# 20% EBIT Margin
        tax_rate=0.21,        # 21% Corporate Tax Rate
        wacc=0.09,            # 9% WACC
        terminal_growth=0.025 # 2.5% Long-Term Terminal Growth
    )
