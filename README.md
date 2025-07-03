# Flask Authenticator API

A self-contained REST API built with Flask, JWT, and bcrypt for secure user authentication. This project handles user registration, login, and protected access to user-specific resources without heavily relying on external services.

---

## 🔐 Features

- Register users with hashed passwords
- Login returns JWT token (1-hour expiration)
- Access protected `/profile` route with Bearer token
- All logic and data are handled locally (no external APIs)

---

## ⚙️ Tech Stack

- **Python**
- **Flask**
- **bcrypt** (password hashing)
- **PyJWT** (JWT token handling)
- **python-dotenv** (environment variable loading)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/av-toledo/flask-auth-api.git
cd flask-auth-api
```

---

### 2. Create `.env` file

Create a file named `.env` in the root directory and add your secret key:

```env
SECRET_KEY=LALALA
```

(You can also copy and rename `.env.example`)

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, you can install dependencies manually:

```bash
pip install flask bcrypt pyjwt python-dotenv
```

---

### 4. Run the app

```bash
python app.py
```

You should see the app running on `http://127.0.0.1:5000/`

---

## 🔄 API Endpoints

### `POST /register`
Registers a new user

**Request Body:**
```json
{
  "username": "userr",
  "password": "securepassword"
}
```

---

### `POST /login`
Logs in a user and returns a JWT token

**Request Body:**
```json
{
  "username": "userr",
  "password": "securepassword"
}
```

---

### `GET /profile`
Returns a protected resource if the request includes a valid JWT token.

**Request Header:**
```http
Authorization: Bearer (auth token)
```

---

## ✅ Status

✔️ Fully functional MVP  
🔒 Future improvements:
- SQLite or some sort of permanent data storage 
- Token refresh & blacklist (logout)  
- Frontend for sure

---

## 📄 License

MIT — free to use, modify, and share.
