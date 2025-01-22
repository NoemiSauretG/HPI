def most_repeated_plan(companies):
    # Extract the plan types from the list
    plans = [company[2] for company in companies]
    
    # Count occurrences of 'Basic' and 'Enterprise'
    count_basic = plans.count('Basic')
    count_enterprise = plans.count('Enterprise')
    
    if count_basic > count_enterprise:
        return "Basic", count_basic
    elif count_enterprise > count_basic:
        return "Enterprise", count_enterprise
    else:
        return "Both have the same count", count_basic

# Example usage:
companies = [
    ["Company A", "12345678A", "Basic"],
    ["Company B", "23456789B", "Enterprise"],
    ["Company C", "34567890C", "Basic"],
    ["Company D", "45678901D", "Enterprise"],
    ["Company E", "56789012E", "Basic"],
]

most_frequent_plan, count = most_repeated_plan(companies)
print(f"The most repeated plan is '{most_frequent_plan}' with {count} occurrences.")
