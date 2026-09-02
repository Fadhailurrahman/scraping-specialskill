# Scraping SpecialSkill.id

Web scraper sederhana menggunakan Python untuk mengumpulkan daftar artikel dari beberapa kategori di [SpecialSkill.id](https://specialskill.id/).

## Features

- Scraping artikel berdasarkan kategori.
- Mendukung pagination pada halaman kategori.
- Menghindari artikel duplikat berdasarkan URL.
- Mengambil kategori, judul, dan URL artikel.
- Mengekspor hasil scraping ke file CSV.
- Menggunakan `Requests` dan `BeautifulSoup`.

## Categories

Scraper mengambil artikel dari beberapa kategori:

- Programming
- Machine Learning
- Mobile Development
- Website Development
- Data Analyst
- UI/UX Design
- Graphic Design
- Digital Marketing

## Requirements

- Python 3.9+
- `requests`
- `beautifulsoup4`

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/Fadhailurrahman/scraping-specialskill.git
cd scraping-specialskill
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

Jalankan scraper dengan perintah:

```bash
python scraper.py
```

Setelah proses selesai, hasil scraping akan disimpan secara otomatis sebagai:

```text
artikel_special_skill.csv
```

## Output

File CSV memiliki struktur sebagai berikut:

| Kolom | Deskripsi |
|---|---|
| `No` | Nomor urut artikel |
| `Kategori` | Kategori artikel |
| `Judul Artikel` | Judul artikel |
| `URL` | URL artikel |

Contoh:

| No | Kategori | Judul Artikel | URL |
|---:|---|---|---|
| 1 | Programming | Contoh Judul Artikel | https://specialskill.id/article/... |
| 2 | Data Analyst | Contoh Judul Artikel | https://specialskill.id/article/... |

## Data

File [`artikel_special_skill.csv`](./artikel_special_skill.csv) berisi hasil scraping pada saat repository dibuat.

Karena konten pada website sumber dapat berubah dari waktu ke waktu, jumlah dan daftar artikel yang dihasilkan dapat berbeda ketika scraper dijalankan kembali.

## Project Structure

```text
scraping-specialskill/
│
├── artikel_special_skill.csv
├── README.md
├── requirements.txt
└── scraper.py
```

## How It Works

Secara sederhana, proses scraping berjalan dengan alur berikut:

```text
Category URLs
      ↓
Request Web Page
      ↓
Parse HTML with BeautifulSoup
      ↓
Extract Article Data
      ↓
Check Duplicate URL
      ↓
Handle Pagination
      ↓
Collect All Articles
      ↓
Export to CSV
```

Scraper menggunakan URL artikel sebagai identifier untuk mencegah data artikel yang sama tersimpan lebih dari satu kali.

## Limitations

- Struktur HTML website sumber dapat berubah sehingga selector pada scraper mungkin perlu diperbarui.
- Data disimpan dalam format CSV sehingga belum menggunakan database persistence.
- Scraper bergantung pada ketersediaan website sumber.
- Jumlah artikel dapat berubah ketika scraper dijalankan kembali.
- Belum menggunakan asynchronous requests.

## Disclaimer

Project ini dibuat untuk tujuan pembelajaran dan pengembangan kemampuan web scraping menggunakan Python.

Penggunaan scraper harus tetap memperhatikan `robots.txt`, Terms of Service, rate limits, hak cipta, serta kebijakan website yang menjadi sumber data.

Gunakan scraper secara bertanggung jawab dan hindari memberikan beban berlebihan terhadap server website sumber.

## Author

**Moh. Fadhailurrahman**

GitHub: [@Fadhailurrahman](https://github.com/Fadhailurrahman)
