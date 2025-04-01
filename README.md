# 🌟 Job Tracker — Django Web App

A fully responsive, dark-mode enabled job application tracker built with Django, HTMX, and TailwindCSS.  
Designed to help job seekers organize their application process using a clean, Kanban-style interface.

> ⚡️ Built in under 48 hours to explore Django + HTMX after receiving an interview invite from Carbon Equity.

---

## 🔧 Tech Stack

- **Django** — full server-side rendered backend (views, forms, models)
- **Tailwind CSS** — utility-first styling, dark mode, responsive layout
- **HTMX + Alpine.js** — dynamic UI without a frontend framework or JS build step
- **PostgreSQL** — production-grade relational database
- **Render.com** — live deployment with CI/CD integration
- **Whitenoise** — static file handling for production

---

## 💡 Features

✅ Kanban-style board (Applied, Interview, Offer, Rejected)  
✅ Full CRUD functionality for job entries  
✅ Dark mode toggle (saved via `localStorage`)  
✅ Responsive mobile-first layout  
✅ Modular Django template structure  
✅ Friendly empty state UX  
✅ Deployed live (Render) with PostgreSQL + static hosting

---

<img width="1440" alt="Screenshot 2025-04-01 at 23 46 03" src="https://github.com/user-attachments/assets/a168663f-c53b-4101-8b44-d644b5869fff" />

---

## 🚀 Live Demo & Repository

**Live App:** 
[[job-tracker-demo.render.com]([https://job-tracker-demo.render.com](https://jobtracker-1v1e.onrender.com/))](https://jobtracker-1v1e.onrender.com/)
---

## 📦 Setup (Local Development)

git clone https://github.com/yussypu/job-tracker.git

cd job-tracker

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

# Set up DB
python manage.py makemigrations

python manage.py migrate

# Run dev server
python manage.py runserver


## 🛠 Future Features / Roadmap

These are features I’m actively planning or considering for future updates:

- [ ] **User Authentication** — allow users to register and securely manage their own job boards  
- [ ] **Drag & Drop Kanban** — enable intuitive reordering and column shifting with JS or HTMX extensions  
- [ ] **Job Notes & Logs** — add notes or timeline updates (e.g. sent follow-up, received feedback)  
- [ ] **Deadline Reminders** — notify users of upcoming deadlines for applications or interviews  
- [ ] **Custom Columns** — allow users to define their own application stages (e.g. Coding Challenge, Final Round)  
- [ ] **CSV Export** — export job data for backup or analysis  
- [ ] **Search & Filters** — search by title, company, or status  
- [ ] **Tagging System** — label jobs by industry, location, or job type  
- [ ] **Multi-user Collaboration** — share job boards with mentors or accountability partners  

> If you'd like to contribute or collaborate on any of these, feel free to open an issue or reach out!


