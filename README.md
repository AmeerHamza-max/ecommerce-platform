# eCommerce Platform - Microservices Architecture

This project is a **microservices-based eCommerce platform** built with **Flask**, **Docker**, and **Docker Compose**. It includes multiple services, each handling a specific functionality.

## 🚀 Features
- **Order Service**: Manages customer orders.
- **Payment Service**: Handles payment processing.
- **User Service**: Manages user authentication and profiles.
- **Product Service**: Manages product catalog.
- **Inventory Service**: Tracks product stock.
- **Dashboard Service**: Provides a frontend for the platform.

## 💁️ Project Structure
```
ecommerce-platform/
│-- dashboard-service/
│   ├── Dockerfile
│   ├── index.html
│   ├── script.js
│   ├── styles.css
│
│-- inventory-service/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│
│-- order-service/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│
│-- payment-service/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│
│-- product-service/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│
│-- user-service/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│
│-- docker-compose.yml
│-- README.md
```

## 🛠 Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Containerization**: Docker, Docker Compose
- **Database**: (Add database if used, e.g., PostgreSQL, MongoDB)
- **API Communication**: RESTful APIs

## 🚀 Getting Started

### Prerequisites
Ensure you have **Docker** and **Docker Compose** installed.

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/ecommerce-platform.git
cd ecommerce-platform
```

### 2️⃣ Build and Run the Services
```sh
docker-compose up --build
```

### 3️⃣ Access the Services
- **Frontend (Dashboard)**: `http://localhost:80`
- **Order Service**: `http://localhost:5002`
- **Payment Service**: `http://localhost:5003`
- **User Service**: `http://localhost:5004`
- **Product Service**: `http://localhost:5005`
- **Inventory Service**: `http://localhost:5006`

## 🐝 API Endpoints

| Service         | Endpoint                  | Description |
|---------------|------------------------|-------------|
| **User**       | `/users`                | Get all users |
| **Order**      | `/orders`               | Get all orders |
| **Payment**    | `/payments`             | Process payments |
| **Product**    | `/products`             | Get product catalog |
| **Inventory**  | `/inventory`            | Check stock |

## 🛠 Stopping the Services
```sh
docker-compose down
```

## 🤝 Contributing
Feel free to submit issues or pull requests to improve the project.



