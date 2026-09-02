import requests
from bs4 import BeautifulSoup
import html
import csv

# Daftar URL kategori artikel di specialskill.id
category_urls = [
    "https://specialskill.id/article/programming/",
    "https://specialskill.id/article/machine-learning/",
    "https://specialskill.id/article/mobile-development/",
    "https://specialskill.id/article/website-development/",
    "https://specialskill.id/article/data-analyst/",
    "https://specialskill.id/article/ui-ux-design/",
    "https://specialskill.id/article/graphic-design/",
    "https://specialskill.id/article/digital-marketing/"
]

seen_urls = set()  # Set untuk melacak URL agar tidak ada data yang duplikat
all_articles = []

print("Memulai proses scraping artikel berdasarkan kategori...\n")

for cat_url in category_urls:
    print(f"Mengakses kategori: {cat_url}")
    
    page = 1
    while True:
        if page == 1:
            target_url = cat_url
        else:
            target_url = f"{cat_url}page/{page}/"
            
        response = requests.get(target_url)
        
        # Jika halaman tidak ditemukan (404) atau habis, keluar dari loop kategori ini
        if response.status_code != 200:
            break
            
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("div", class_="e-loop-item")
        
        # Jika tidak ada artikel di halaman ini, hentikan pagination kategori ini
        if not articles:
            break
            
        # Cek duplikasi halaman (mencegah loop jika WordPress meredirect balik ke halaman 1)
        first_link = articles[0].select_one("h3.elementor-heading-title a")
        if first_link and page > 1 and first_link.get("href") in seen_urls:
            break
            
        found_new = False
        for item in articles:
            title_tag = item.select_one("h3.elementor-heading-title a")
            category_tag = item.select_one(".elementor-widget-heading span")
            
            if title_tag:
                title = html.unescape(title_tag.get_text(strip=True))
                article_url = title_tag.get("href")
                category = category_tag.get_text(strip=True) if category_tag else "Kategori Lain"
                
                # Simpan hanya jika URL belum pernah terekam sebelumnya
                if article_url not in seen_urls:
                    seen_urls.add(article_url)
                    all_articles.append({
                        "category": category,
                        "title": title,
                        "url": article_url
                    })
                    found_new = True
                    
        # Jika di halaman ini tidak ada artikel baru yang unik, hentikan pagination
        if not found_new and page > 1:
            break
            
        page += 1

print("\n" + "="*60)
print(f"KESIMPULAN: Berhasil mengumpulkan total {len(all_articles)} artikel unik!")
print("="*60 + "\n")

# Menampilkan hasil ke terminal
for i, art in enumerate(all_articles, start=1):
    print(f"[{i}] {art['category']} | {art['title']}")
    print(f"    URL: {art['url']}")
    print("-" * 50)

# Menyimpan hasil ke file CSV agar otomatis tersimpan dan bisa dibuka di Excel
file_name = "artikel_special_skill.csv"

with open(file_name, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    # Menulis header kolom
    writer.writerow(["No", "Kategori", "Judul Artikel", "URL"])
    
    # Menulis baris data artikel
    for i, art in enumerate(all_articles, start=1):
        writer.writerow([i, art['category'], art['title'], art['url']])

print(f"\n[SUKSES] Data berhasil dieksport dan disimpan ke file: '{file_name}' 🎉")