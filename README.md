Scraping SpecialSkill.id

Web scraper sederhana menggunakan Python untuk mengumpulkan daftar artikel dari beberapa kategori di SpecialSkill.id
.

Features
Scraping artikel berdasarkan kategori.
Mendukung pagination pada halaman kategori.
Menghindari artikel duplikat berdasarkan URL.
Mengambil kategori, judul, dan URL artikel.
Mengekspor hasil scraping ke file CSV.
Menggunakan requests dan BeautifulSoup.
Categories

Scraper mengambil artikel dari beberapa kategori:

Programming
Machine Learning
Mobile Development
Website Development
Data Analyst
UI/UX Design
Graphic Design
Digital Marketing
Requirements
Python 3.9+
requests
beautifulsoup4
Installation

Clone repository:

git clone https://github.com/USERNAME/SCRAPING-SPECIALSKILL.git
cd SCRAPING-SPECIALSKILL


Buat virtual environment:

python -m venv .venv


Aktifkan virtual environment.

Windows:

.venv\Scripts\activate


macOS/Linux:

source .venv/bin/activate


Install dependencies:

pip install -r requirements.txt

Usage

Jalankan scraper:

python scraper.py


Setelah proses selesai, hasil scraping akan disimpan sebagai:

artikel_special_skill.csv


CSV memiliki kolom:

Kolom	Deskripsi
No	Nomor urut artikel
Kategori	Kategori artikel
Judul Artikel	Judul artikel
URL	URL artikel
Data

File artikel_special_skill.csv berisi hasil scraping pada saat repository dibuat.

Karena website sumber dapat berubah, jumlah dan daftar artikel dapat berbeda ketika scraper dijalankan kembali.

Disclaimer

Project ini dibuat untuk tujuan pembelajaran dan pengembangan kemampuan web scraping menggunakan Python.

Pastikan penggunaan scraper tetap memperhatikan robots.txt, terms of service, rate limits, dan kebijakan website yang menjadi sumber data.