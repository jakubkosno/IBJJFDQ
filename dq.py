from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse


url = input("Enter full URL: ").strip()

parsed = urlparse(url)

base_url = f"{parsed.scheme}://{parsed.netloc}"
tournament_url = parsed.path
response = requests.get(base_url+tournament_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    print("Looking for disqualified athletes. It may take a while.")
    category_urls = [
        a["href"]
        for a in soup.find_all("a", href=True)
        if tournament_url in a["href"] and "?" not in a["href"]
    ]
    results = []
    skip_reasons = ["Disqualified by no show", "Disqualified by overweight"]
    for category_url in category_urls:
        response = requests.get(base_url+category_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            category = " / ".join(
                span.get_text(strip=True)
                for span in soup.select(".category-title__divisions .category-title__label")
                )
            for icon in soup.select("i.match-card__disqualification"):
                reason = icon.get("title", "").strip()
                if reason in skip_reasons:
                    continue
                competitor = icon.find_parent("div", class_="match-card__competitor")
                name = competitor.select_one(".match-card__competitor-name").get_text(strip=True)
                match = competitor.find_parent("div", class_="match-card")
                competitors = match.select("div.match-card__competitor")
                opponent = next(c for c in competitors if c != competitor)
                opponent_name = opponent.select_one(".match-card__competitor-name").get_text(strip=True)
                results.append({"category":category, "disqualified" : name, "opponent": opponent_name, "reason": reason})
else:
    print("No response with this url.")

with open("dq_results.txt", "w", encoding="utf-8") as f:
    for entry in results:
        f.write(
            f"{entry['category']} | "
            f"Disqualified: {entry['disqualified']} ({entry['reason']}) | "
            f"Opponent: {entry['opponent']}\n"
        )
print("List of disqualified athletes has been saved to dq_results.txt")
