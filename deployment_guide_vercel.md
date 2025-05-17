# Panduan Deploy Project Flask ke Vercel

Berikut adalah langkah-langkah untuk melakukan deployment project Flask Anda ke platform Vercel menggunakan konfigurasi yang sudah ada.

## Persiapan

1. Pastikan Anda sudah memiliki akun Vercel. Jika belum, daftar di https://vercel.com/signup
2. Install Vercel CLI secara global di komputer Anda:
   ```bash
   npm i -g vercel
   ```
3. Pastikan project Anda sudah memiliki file berikut:
   - `vercel.json` (konfigurasi Vercel)
   - `requirements-vercel.txt` (daftar dependencies Python)
   - `runtime.txt` (versi Python, misal python-3.9.13)
   - `app.py` (file utama Flask app)
   - Folder `model/` berisi model TensorFlow dan file pendukung lainnya

## Langkah Deploy

1. Buka terminal dan arahkan ke direktori project Anda:
   ```bash
   cd path/to/your/project
   ```
2. Login ke Vercel menggunakan CLI:
   ```bash
   vercel login
   ```
   Ikuti instruksi untuk login dengan akun Vercel Anda.

3. Jalankan perintah deploy pertama kali:
   ```bash
   vercel
   ```
   - Vercel akan membaca konfigurasi di `vercel.json`.
   - Pilih scope (akun atau tim) jika diminta.
   - Pilih project name atau gunakan default.
   - Pilih direktori root (gunakan default jika project root).
   - Tunggu proses build dan deploy selesai.

4. Setelah deploy selesai, Vercel akan memberikan URL untuk mengakses aplikasi Flask Anda.

## Mengelola File .env yang Tidak Ada di Repository

Jika Anda memiliki file `.env` yang berisi variabel environment dan tidak ingin menyimpannya di GitHub repository, Anda dapat mengatur variabel tersebut langsung di dashboard Vercel:

1. Buka https://vercel.com dan login ke akun Anda.
2. Pilih project yang sudah Anda deploy.
3. Masuk ke menu **Settings** > **Environment Variables**.
4. Tambahkan variabel environment yang ada di file `.env` Anda satu per satu dengan nama dan nilainya.
5. Setelah disimpan, variabel ini akan tersedia di environment aplikasi Anda saat dijalankan di Vercel.

Dengan cara ini, Anda tidak perlu menyimpan file `.env` di repository, sehingga rahasia seperti API keys atau konfigurasi sensitif tetap aman.

## Catatan Penting

- Pastikan semua file model (`model/resep_model.h5`, `model/vectorizer.pkl`, dll) sudah termasuk dalam direktori project dan tidak di-ignore oleh `.gitignore`.
- Jika Anda menggunakan environment variables lain, Anda bisa menambahkannya di dashboard Vercel pada bagian Settings > Environment Variables.
- Karena aplikasi menggunakan TensorFlow, ukuran deployment bisa cukup besar dan cold start mungkin agak lama.
- Port sudah di-set ke 3000 di `vercel.json` dan `app.py`, jadi tidak perlu diubah.

## Update dan Redeploy

Jika Anda melakukan perubahan pada kode atau model, cukup jalankan kembali:

```bash
vercel --prod
```

untuk melakukan deploy ke environment production.

---

Dengan mengikuti langkah-langkah di atas, project Flask Anda akan berjalan di Vercel dengan baik.
