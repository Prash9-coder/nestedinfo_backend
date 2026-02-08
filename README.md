# NexaTech Contact Backend

Django REST API with PostgreSQL for handling contact form submissions.

## Setup Instructions

### 1. Install PostgreSQL
Make sure PostgreSQL is installed and running on your system.

### 2. Create Database
```sql
CREATE DATABASE nexatech_db;
CREATE USER postgres WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE nexatech_db TO postgres;
```

### 3. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 4. Configure Environment
Copy `.env.example` to `.env` and update with your credentials:
```bash
copy .env.example .env
```

Edit `.env` with your database credentials.

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `POST /api/contact/` - Submit contact form
- `GET /api/contact/messages/` - List all messages (admin)
- `GET /admin/` - Django admin panel

## Frontend Integration

Update your React Contact component to use this endpoint:

```javascript
const handleSubmit = async (e) => {
  e.preventDefault();
  setIsSubmitting(true);
  
  try {
    const response = await fetch('http://localhost:8000/api/contact/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    });
    
    if (response.ok) {
      setSubmitStatus('success');
      setFormData({ name: '', email: '', subject: '', message: '' });
    }
  } catch (error) {
    console.error('Error:', error);
  } finally {
    setIsSubmitting(false);
  }
};
```
