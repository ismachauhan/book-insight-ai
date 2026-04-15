def generate_summary(description):
    if not description:
        return "No description available"
    
    
    return description[:100] + "..."