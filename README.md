# 🧾 Material Registry - Odoo Custom Module

Modul ini menyediakan manajemen data material dan integrasi API menggunakan Odoo JSON controller.

---

## 📦 Fitur Utama

- CRUD untuk data material (`material.registry`)
- Validasi harga beli minimum (≥ 100)
- Integrasi API (REST-like via Odoo JSON)
- Filter berdasarkan `material_type`
- Unit test untuk fungsionalitas utama
- Contoh integrasi API via `curl`

---

## ⚙️ Struktur Kode

### 🧠 Model: `material.registry`

Field utama:
- `code` (Char, required)
- `name` (Char, required)
- `material_type` (Selection: `fabric`, `jeans`, `cotton`, required)
- `buy_price` (Float, minimal 100)
- `supplier_id` (Many2one ke `res.partner`, hanya supplier)

### 🧠 ERD: `material.registry`
+-------------------------+
|     res.partner        |
|------------------------|
| id                     |
| name                   |
| supplier_rank          |
+------------------------+
          ^
          |
          | Many2one (supplier_id)
          |
+-----------------------------+
|     material.registry      |
|----------------------------|
| id                         |
| code         (Char)        |
| name         (Char)        |
| material_type (Selection)  |
| buy_price    (Float)       |
| supplier_id  (Many2one) --> res.partner
+----------------------------+

### 🌐 API Endpoint

| Endpoint | Deskripsi |
|----------|-----------|
| `POST /material_registry/materials` | List semua material |
| `POST /material_registry/create` | Buat material baru |
| `POST /material_registry/update/<id>` | Update material berdasarkan ID |
| `POST /material_registry/delete/<id>` | Hapus material |
| `POST /material_registry/materials/filter` | Filter berdasarkan `material_type` |

---

## 🔁 Contoh CURL Request

### 1. 🔐 Autentikasi

```bash
curl -X POST http://localhost:8014/web/session/authenticate \
  -H "Content-Type: application/json" \
  -c cookies.txt \
  -d '{
    "jsonrpc": "2.0",
    "params": {
      "db": "IMM",
      "login": "admin",
      "password": "admin"
    }
}'
