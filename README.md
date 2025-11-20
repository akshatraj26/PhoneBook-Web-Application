# 📘 **PhoneBook Web Application**

A simple and functional **PhoneBook web application** built with **Django**, styled with **TailwindCSS + Bootstrap**, and Dockerized with **MySQL** as the database.
This project also uses **Crispy Forms** for better UI and provides CRUD operations for managing phone contacts.

---

## 🚀 **Features**

* Create, read, update, delete phonebook entries
* MySQL database integration
* Django ORM + Class-Based Views
* TailwindCSS + Bootstrap UI
* Crispy Forms for UI enhancements
* Fully Dockerized (Django + MySQL)
* Environment variables for security
* REST API support using Django REST Framework (optional)

---

## 🛠️ **Tech Stack**

* **Backend:** Django
* **Database:** MySQL
* **Frontend:** TailwindCSS, Bootstrap, Crispy Forms
* **API (Optional):** Django REST Framework
* **Containerization:** Docker & Docker Compose
* **Environment Management:** `.env` file

---

# 📂 **Project Structure**

```
PhoneBook/
├── config/
├── phonebook/
├── phonebook_api/
├── users/
├── static/
├── templates/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── .env
```

---

# 🔧 **Installation (Without Docker)**

### **1. Clone the repository**

```bash
git clone <your-repo-url>
cd PhoneBook
```

### **2. Create & activate virtual environment**

```bash
python3 -m venv env
source env/bin/activate
```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

### **4. Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Run the server**

```bash
python manage.py runserver
```

---

# 🔐 **Environment Variables**

Create a `.env` file in the project root:

```
DB_NAME=your_db_name
DB_USER=your_user
DB_PWD=your_password
DB_HOST=db
DB_PORT=3306
SECRET_KEY=your_secret_key
DEBUG=True
```

---

# 🐳 **Docker Setup (Using docker-compose)**

### **1. Build and start containers**

```bash
docker compose up -d --build
```

### **2. View running containers**

```bash
docker ps
```

### **3. Stop containers**

```bash
docker compose down
```

---

## 🛠️ **Running Django Migrations in Docker**

Start containers:

```bash
docker compose up -d
```

Run migrations inside the running container:

```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

---

# 🐳 **Building Docker Image (Manual Method — WITHOUT docker-compose)**

*(You asked for a separate section — this is completely independent.)*

### **1. Build the Django image**

```bash
docker build -t phonebook_app .
```

### **2. Run the Django container**

```bash
docker run -d -p 8000:8000 --env-file .env phonebook_app
```

### **3. Build and run MySQL container separately**

```bash
docker run -d \
  --name phonebook_db \
  -e MYSQL_DATABASE=your_db_name \
  -e MYSQL_USER=your_user \
  -e MYSQL_PASSWORD=your_password \
  -e MYSQL_ROOT_PASSWORD=root \
  -p 3306:3306 \
  mysql:8.0
```

### **4. Run Django migrations manually (single container)**

```bash
docker exec -it <container_name_or_id> python manage.py makemigrations
docker exec -it <container_name_or_id> python manage.py migrate
```

### **5. View logs**

```bash
docker logs -f phonebook_app
```

---

# 📡 **API Endpoints (If REST API is used)**

| Method | Endpoint              | Description      |
| ------ | --------------------- | ---------------- |
| GET    | `/api/contacts/`      | List contacts    |
| POST   | `/api/contacts/`      | Create contact   |
| GET    | `/api/contacts/<id>/` | Retrieve contact |
| PUT    | `/api/contacts/<id>/` | Update contact   |
| DELETE | `/api/contacts/<id>/` | Delete contact   |

---

# 🧪 **Running Tests**

```bash
python manage.py test
```

---

# 🔧 **Common Docker Commands**

| Command                        | Description                 |
| ------------------------------ | --------------------------- |
| `docker compose up -d --build` | Build + run containers      |
| `docker compose exec web bash` | Shell inside web container  |
| `docker compose logs -f web`   | View Django logs            |
| `docker compose down -v`       | Remove containers + volumes |

---

# 🤝 **Contributing**

Pull requests are welcome. For major changes, please open an issue first.

---

# 📜 **License**

MIT License.