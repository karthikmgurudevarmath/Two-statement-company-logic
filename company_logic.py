def run_company_logic(facts):
    print(f"Initial facts: {facts}")
    
    # Statement 1: Profitability Logic
    if "revenue > expenses" in facts and "company_profitable" not in facts:
        print("Statement 1 triggered: Company is profitable!")
        facts.add("company_profitable")
        
    # Statement 2: Bonus Logic
    if "company_profitable" in facts and "give_bonuses" not in facts:
        print("Statement 2 triggered: Giving bonuses to employees!")
        facts.add("give_bonuses")
        
    print(f"Final derived facts: {facts}")
    return facts

if __name__ == "__main__":
    print("--- Running Two Statement Company Logic ---")
    current_facts = {"revenue > expenses"}
    run_company_logic(current_facts)
