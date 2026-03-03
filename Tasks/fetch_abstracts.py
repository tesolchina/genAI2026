import requests
import time
import urllib.parse

def reconstruct_abstract(inverted_index):
    if not inverted_index:
        return "Abstract not available via OpenAlex API."
    
    # Create a list of (position, word) tuples
    word_positions = []
    for word, positions in inverted_index.items():
        for pos in positions:
            word_positions.append((pos, word))
    
    # Sort by position
    word_positions.sort()
    
    # Join words
    return " ".join([word for _, word in word_positions])

def fetch_paper_data(paper):
    base_url = "https://api.openalex.org/works"
    data = None
    
    # Try DOI first if available
    if paper.get("doi") and paper["doi"] != "Unknown":
        doi_url = f"{base_url}/https://doi.org/{paper['doi']}"
        try:
            response = requests.get(doi_url)
            if response.status_code == 200:
                data = response.json()
        except Exception as e:
            # print(f"Error fetching DOI {paper['doi']}: {e}")
            pass

    # Fallback to Title search if no data yet
    if not data:
        encoded_title = urllib.parse.quote(paper["title"])
        search_url = f"{base_url}?search={encoded_title}"
        try:
            response = requests.get(search_url)
            if response.status_code == 200:
                results = response.json().get('results', [])
                if results:
                    # Simple heuristic: pick the first one. 
                    # In a production app we might check title similarity.
                    data = results[0]
        except Exception as e:
            pass

    if data:
        abstract_index = data.get("abstract_inverted_index")
        abstract = reconstruct_abstract(abstract_index)
        
        # We can also update metadata from the API if we wanted, 
        # but the prompt asks to use provided list, just fetching abstract.
        # However, getting the canonical DOI if we searched by title is good practice.
        found_doi = data.get("doi")
        if found_doi: 
             # OpenAlex returns full URL (https://doi.org/...), we might want just the ID or the URL.
             # User prompt asked for DOI link or "Not found". 
             # The provided list has short DOIs or Unknown. 
             # We'll use the found DOI URL.
             pass
        else:
             found_doi = "Not found"
             
        return abstract, found_doi
    else:
        return "Abstract not available via OpenAlex API.", "Not found"

papers = [
    {"title": "More than just a chat: A taxonomy of consumers’ relationships with conversational AI agents and their well-being implications", "authors": "A. Alabed, A. Javornik, D. Gregory-Smith, R. Casey", "year": "2024", "doi": "10.1108/EJM-01-2023-0037"},
    {"title": "Empowering AI companions for enhanced relationship marketing", "authors": "R. Chaturvedi, S. Verma, V. Srivastava", "year": "2024", "doi": "10.1177/00081256231215838"},
    {"title": "Ethical tensions in human-ai companionship: A dialectical inquiry into replika", "authors": "R.F. Ciriello, O. Hannon, A.Y. Chen, E. Vaast", "year": "2024", "doi": "Unknown"},
    {"title": "Ideal technologies, ideal women: AI and gender imaginaries in Redditors’ discussions on the Replika bot girlfriend", "authors": "I. Depounti, P. Saukko, S. Natale", "year": "2023", "doi": "10.1177/01634437221119021"},
    {"title": "Better alone than in bad company: Addressing the risks of companion chatbots through data protection by design", "authors": "P. Dewitte", "year": "2024", "doi": "10.1016/j.clsr.2024.106019"},
    {"title": "Alexa, My Love: Analyzing reviews of amazon echo", "authors": "Y. Gao, Z. Pan, H. Wang, G. Chen", "year": "2018", "doi": "Unknown"},
    {"title": "How smart experiences build service loyalty: The importance of consumer love for smart voice assistants", "authors": "B. Hernandez-Ortega, I. Ferreira", "year": "2021", "doi": "10.1002/mar.21497"},
    {"title": "Digital humans to combat loneliness and social isolation: Ethics concerns and policy recommendations", "authors": "N.S. Jecker, R. Sparrow, Z. Lederman, A. Ho", "year": "2024", "doi": "10.1002/hast.1562"},
    {"title": "Too human and not human enough: A grounded theory analysis of mental health harms from emotional dependence on the social chatbot Replika", "authors": "L. Laestadius, A. Bishop, M. Gonzalez, D. Illencik, C. Campos-Castillo", "year": "2022", "doi": "10.1177/14614448221142007"},
    {"title": "Finding love in algorithms: Deciphering the emotional contexts of close encounters with AI chatbots", "authors": "H. Li, R. Zhang", "year": "2024", "doi": "10.1093/jcmc/zmae015"},
    {"title": "What affects the usage of artificial conversational agents? An agent personality and love theory perspective", "authors": "D. Pal, V. Vanijja, H. Thapliyal, X. Zhang", "year": "2023", "doi": "10.1016/j.chb.2023.107788"},
    {"title": "Desirable or distasteful? Exploring uncertainty in human-chatbot relationships", "authors": "S. Pan, J. Cui, Y. Mou", "year": "2023", "doi": "10.1080/10447318.2023.2256554"},
    {"title": "Digital lovers and jealousy: Anticipated emotional responses to emotionally and physically sophisticated sexual technologies", "authors": "A. Prochazka, R.C. Brooks", "year": "2024", "doi": "10.1155/2024/1413351"},
    {"title": "‘Trust me over my privacy policy’: Privacy discrepancies in romantic ai chatbot apps", "authors": "A. Ragab, M. Mannan, A. Youssef", "year": "2024", "doi": "10.1109/EuroSPW61312.2024.00060"},
    {"title": "Reconfiguring the alterity relation: The role of communication in interactions with social robots and chatbots", "authors": "D. Root", "year": "2024", "doi": "10.1007/s00146-024-01953-9"},
    {"title": "Why do we turn to virtual companions? A text mining analysis of Replika reviews", "authors": "D. Siemon, T. Strohmann, B. Khosrawi-Rad, T. de Vreede, E. Elshan, M. Meyer", "year": "2022", "doi": "Unknown"},
    {"title": "A longitudinal study of self-disclosure in human–chatbot relationships", "authors": "M. Skjuve, A. Følstad, P.B. Brandtzæg", "year": "2023", "doi": "10.1093/iwc/iwad022"},
    {"title": "My chatbot companion—A study of human-chatbot relationships", "authors": "M. Skjuve, A. Følstad, K.I. Fostervold, P.B. Brandtzaeg", "year": "2021", "doi": "10.1016/j.ijhcs.2021.102601"},
    {"title": "The experience of conversation and relation with a well-being chatbot: Between proximity and remoteness", "authors": "J. Wygnańska", "year": "2023", "doi": "10.18778/1733-8077.19.4.05"},
    {"title": "Attachment theory as a framework to understand relationships with social chatbots: A case study of Replika", "authors": "T. Xie, I. Pentina", "year": "2022", "doi": "Unknown"},
    {"title": "Friend, mentor, lover: Does chatbot engagement lead to psychological dependence?", "authors": "T. Xie, I. Pentina, T. Hancock", "year": "2023", "doi": "10.1108/JOSM-02-2022-0072"}
]

print("# Reviewed Papers in Ho et al.\n")

for paper in papers:
    abstract, api_doi = fetch_paper_data(paper)
    
    # Use the DOI found by API if the input was Unknown, otherwise use the input (formatted as link)
    display_doi = paper['doi']
    if display_doi == "Unknown":
        if api_doi != "Not found":
            display_doi = api_doi # This is usually full URL from openalex
        else:
            display_doi = "Not found"
    else:
        # Format known DOI as link if it isn't one
        if not display_doi.startswith("http"):
            display_doi = f"https://doi.org/{display_doi}"

    print(f"## {paper['title']}")
    print(f"**Authors**: {paper['authors']}")
    print(f"**Year**: {paper['year']}")
    print(f"**DOI**: {display_doi}")
    print(f"**Abstract**:")
    print(f"{abstract}")
    print("\n---\n")
    
    # Be polite to the API
    time.sleep(0.2)
