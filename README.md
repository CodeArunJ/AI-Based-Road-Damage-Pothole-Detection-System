# RoadCare - AI-Based Road Detection System

A full-stack application for reporting and managing road damage using AI-powered verification.

## Project Structure

This project consists of two main parts:

### Backend (FastAPI)
- **Location**: `backend/`
- **Technology**: Python, FastAPI, SQLAlchemy
- **Port**: 8000

### Frontend (React + Vite)
- **Location**: `frontend1/` (New React version)
- **Technology**: React 18, Vite, Tailwind CSS, Axios
- **Port**: 3000

### Legacy Frontend
- **Location**: `frontend/`
- **Technology**: Vanilla HTML/CSS/JavaScript
- **Note**: Original version, replaced by React frontend

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### 1. Start the Backend

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (if not exists)
python -m venv venv

# Activate virtual environment
# Windows:
.venv\Scripts\Activate.ps1
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python run.py
```

Backend will be available at `http://localhost:8000`

### 2. Start the React Frontend

Open a new terminal:

```bash
# Navigate to frontend directory
cd frontend1

# Install dependencies (first time only)
npm install

# Start development server
npm run dev
```

Frontend will be available at `http://localhost:3000`

## Features

### For Citizens
- 📸 Report potholes by uploading photos
- 📍 Automatic GPS location detection
- 🤖 AI-powered damage verification
- 📊 Track report status

### For Authorities
- 🔐 Secure authentication
- 📋 Dashboard for managing reports
- ✅ Verify and update report statuses
- 📈 Analytics and statistics
- 🗺️ Location-based report viewing

## API Documentation

Once the backend is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation
- **JWT** - Authentication
- **Python-multipart** - File upload handling

### Frontend
- **React 18** - UI library
- **Vite** - Build tool
- **React Router** - Client-side routing
- **Axios** - HTTP client
- **Tailwind CSS** - Styling
- **Context API** - State management

## Development

### Backend Development

```bash
cd backend

# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Format code
black .
```

### Frontend Development

```bash
cd frontend1

# Run linter
npm run lint

# Build for production
npm run build

# Preview production build
npm run preview
```

## Environment Variables

### Backend (.env)
```env
DATABASE_URL=sqlite:///./roadcare.db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend (.env)
```env
VITE_API_BASE_URL=http://localhost:8000
```

## Project Timeline

1. **Original Version**: Vanilla HTML/CSS/JavaScript frontend (`frontend/`)
2. **Current Version**: Modern React + Vite frontend (`frontend1/`)
3. **Backend**: FastAPI RESTful API (`backend/`)

## Migration Notes

The frontend has been completely migrated from vanilla JavaScript to React:

### What Changed
- ✅ Component-based architecture
- ✅ Modern React Hooks for state management
- ✅ React Router for navigation
- ✅ Context API for global state (Auth, Theme)
- ✅ Axios with interceptors for API calls
- ✅ Vite for fast development and optimized builds
- ✅ Better code organization and maintainability

### What Stayed the Same
- ✅ All existing features preserved
- ✅ Same UI/UX design
- ✅ Tailwind CSS styling
- ✅ Material Symbols icons
- ✅ Dark mode support
- ✅ Responsive design

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

© 2024 RoadCare AI Systems. All rights reserved.
