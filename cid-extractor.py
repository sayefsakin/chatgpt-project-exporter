from bs4 import BeautifulSoup
import re

# Load the HTML file
with open("dissproject.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# Each conversation is an <li> with class containing "group/project-item"
list_items = soup.find_all("li", class_=lambda c: c and "group/project-item" in c)

print(f"Found {len(list_items)} conversation(s):\n")

cids = []

for i, item in enumerate(list_items, 1):
    # The <a> tag href contains /shared/c/{cid}
    a_tag = item.find("a", href=re.compile(r"/shared/c/"))
    title_div = item.find("div", class_=lambda c: c and "font-medium" in c)

    title = title_div.get_text(strip=True) if title_div else "Unknown"

    if a_tag:
        href = a_tag["href"]
        # Extract the UUID after /shared/c/
        match = re.search(r"/shared/c/([0-9a-f-]+)", href)
        if match:
            cid = match.group(1)
            cids.append(cid)
            print(f'{{ id: "{cid}", title: "{title}" }},')
            # print(f"{i}. Title : {title}")
            # print(f"   CID   : {cid}")
            # print()

print("─" * 50)
print("All CIDs extracted:")
for cid in cids:
    print(f"  {cid}")
