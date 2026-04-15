def generate_summary(description):
    if not description:
        return "No description available"
    
    
    return description[:100] + "..."

def recommend_book(title):
    title = title.lower()

    if "science" in title:
        return "You may also like other science fiction books"
    elif "history" in title:
        return "You may enjoy historical books"
    elif "love" in title:
        return "Romantic novels might interest you"
    else:
        return "Explore more books in this category"