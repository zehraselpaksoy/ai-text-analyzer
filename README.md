README.md# AI Text Analyzer

## Açıklama
Bu proje, **FastAPI ile geliştirilmiş asenkron bir REST API**dir ve metin analizi yapar.  
Metinlerin kelime sayısını, cümle sayısını, en sık kullanılan kelimeleri ve özetini çıkarır.  
Bu versiyonda **Noel temalı arayüz** de bulunuyor.

## Özellikler
- Asenkron endpoint’ler  
- JSON input/output  
- Form üzerinden metin analizi (Noel temalı arayüz)  
- İstek sayısı takibi (`/stats`)  
- Sistem sağlık durumu (`/health`)

## Endpoint’ler
- `GET /` → Ana sayfa (form arayüzü)  
- `GET /health` → Sistem sağlık durumu  
- `POST /analyze_form` → Form üzerinden metin analizi  
- `GET /stats` → Toplam analiz istek sayısı  

## Kullanılan Teknolojiler
- Python 3.11+  
- FastAPI  
- Jinja2 (HTML templates)  
- Uvicorn  
- NLTK  

## Lokal Çalıştırma
```powershell
# Sanal ortam oluştur
python -m venv venv

# Sanal ortamı aktif et
.\venv\Scripts\activate

# Gerekli paketleri yükle
pip install -r requirements.txt
pip install python-multipart jinja2 nltk

# NLTK veri paketini indir
python
>>> import nltk
>>> nltk.download('punkt_tab')
>>> exit()

# Sunucuyu başlat
uvicorn app.main:app --reload --port 8001
