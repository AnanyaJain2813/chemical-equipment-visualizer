📄 README.md (paste in GitHub)
# Chemical Equipment Parameter Visualizer  
Hybrid Web + Desktop Application

This project is a hybrid data analytics application for chemical equipment.  
It uses a single Django REST backend consumed by a React web app and a PyQt5 desktop app.

---

##  Features
- Upload CSV file of chemical equipment
- Automatic data analytics using Pandas
- Summary API (total, averages, type distribution)
- Interactive charts (Web: Chart.js, Desktop: Matplotlib)
- Dataset history (last 5 uploads)
- PDF report generation
- Shared backend for both clients

---

##  Tech Stack
Backend: Django, Django REST Framework, Pandas, SQLite  
Web: React.js, Chart.js  
Desktop: PyQt5, Matplotlib  

---

##  Sample Data
Use:
sample_equipment_data.csv

---

##  Setup

### Backend
```bash
cd backend
python -m venv venv
source backend/venv/bin/activate
pip install django djangorestframework pandas django-cors-headers reportlab
python manage.py migrate
python manage.py runserver
Web
cd web
npm install
npm start
Desktop
cd desktop-app
pip install pyqt5 matplotlib requests
python main.py
🎥Demo
Refer to Google Drive demo video.
