# Perkenalan REST API menggunakan framework FastAPI

## Persiapan

Buat dan aktifkan virtualenv. Sebagai contoh saya menggunakan conda env.

```bash
conda create -n docker-workshop python=3.7
conda activate docker-workshop
```

Di workshop ini, kami menggunakan framework [FastAPI](https://fastapi.tiangolo.com).
Sekarang install library `FastAPI` dan juga `uvicorn`, yang digunakan sebagai web server.

```bash
pip install fastapi uvicorn
```

## Endpoint Pertama: Health Check

Saatnya membuat endpoint pertama, `/health`.
Endpoint health check bertujuan untuk mengecek apakah api server anda berjalan sebagaimana mestinya.

Pertama, kita buat file `simple/main.py` dengan

```python
from fastapi import FastAPI

app = FastAPI()


@app.get('/health')
def health_check():
    return {'status': 'ok'}

```

Disini kita menyatakan bahwa setiap request `GET` ke endpoint `/health` akan ditangani oleh method `health_check`.

Untuk mengetes API yang sudah kita buat, kita jalankan uvicorn

```bash
cd simple
uvicorn main:app --reload
```

Lalu buka browser anda ke [http://localhost:8000/health](http://localhost:8000/health).

Salah satu manfaat menggunakan FastAPI adalah adanya dokumentasi yang secara otomatis dihasilkan oleh framework ini.

Buka URL [http://localhost:8000/docs](http://localhost:8000/docs), anda akan disajikan halaman dokumentasi Swagger secara otomatis!

## Endpoint Kedua: NER

```bash
pip install polyglot pycld2 morfessor pyicu
```

```bash
sudo apt install libicu-dev
conda install numpy nomkl
```

```bash
polyglot download embeddings2.id ner2.id
```
