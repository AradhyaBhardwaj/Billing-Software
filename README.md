
<div align="center">

# 🧾 Billing Software

### A Retail Billing & Inventory Management System

A desktop solution for streamlined retail billing, inventory control, and sales analytics.

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-2E8B57?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

<br>

[![Features](https://img.shields.io/badge/Explore-Features-2563EB?style=for-the-badge)](#-features)
[![Installation](https://img.shields.io/badge/Get-Started-16A34A?style=for-the-badge)](#-installation)
[![GitHub](https://img.shields.io/badge/View-Repository-181717?style=for-the-badge&logo=github)](https://github.com/AradhyaBhardwaj/Billing-Software)

</div>

---


✨ Overview
Billing Software is a Python desktop application built to simplify day-to-day retail operations. It brings product management, customer billing, inventory updates, bill records, QR-code workflows, and sales analytics into one interface.

Built with Tkinter and SQLite, the application stores its operational data locally and does not require a separate database server.
🚀 Features
<table>
<tr>
<td width="50%" valign="top">

🧾 Billing Workflow
- Create customer bills
- Calculate bill totals
- Save bill records
- Update stock after billing
</td>
<td width="50%" valign="top">

📦 Inventory Management
- Add, update, and remove products
- Manage categories, prices, and quantities
- Review product-management activity
- Search saved bill records
</td>
</tr>
<tr>
<td width="50%" valign="top">

📊 Sales Analytics
- Daily and monthly sales charts
- Category-level sales visualizations
- Date-based filtering
- Matplotlib-powered dashboard
</td>
<td width="50%" valign="top">

🔎 QR & PDF Tools
- QR-code generation and scanning workflows
- PDF exports for supported reports
- Bill and activity record review
- Calendar-based date selection
</td>
</tr>
</table>

🧰 Tech Stack
Technology	Purpose
Python	Application logic
Tkinter / ttk	Desktop GUI
SQLite	Local data storage
Pillow	Image handling
Pandas	Data preparation for analytics
Matplotlib	Sales charts
tkcalendar	Date selection
FPDF	PDF report exports
qrcode	QR-code generation
OpenCV	QR-code scanning


🖥️ Application Modules
File	Responsibility
app.py	Application entry point
Homepage.py	Home screen and navigation
Login.py	Admin login interface
Admin_Billing.py	Product management, bill/activity history, exports, QR utilities, and dashboard access
Billing_Software.py	Customer billing and product selection
DataAnalysis.py	Sales analytics and charts
aboutUs.py	About screen and animated UI elements
Requirement.txt	Dependency list


⚡ Installation
Prerequisites
- Python 3.9 or newer recommended
- pip
- A graphical desktop environment
1. Clone the repository
git clone https://github.com/AradhyaBhardwaj/Billing-Software.git
cd Billing-Software
2. Install dependencies
python -m pip install -r Requirement.txt
If Pandas or OpenCV are not installed by the dependency file, install them with:
python -m pip install pandas opencv-python
3. Launch the application
python app.py
Tip: Run the command from the project directory so relative database paths work as expected. On some Linux distributions, Tkinter may need to be installed separately.

🔐 Default Admin Login
The application code initializes this default admin account if it does not already exist:
Field	Value

Username:	admin

Password:	admin123


Security warning: These are development/demo credentials. Change them before using the application with real data. The current password comparison is not production-grade authentication.

🔄 Typical Workflow
1. Launch the application.
2. Open the Admin Panel and sign in.
3. Add products with their category, price, and available quantity.
4. Open the Customer Panel and enter customer details.
5. Select products and verify the bill total.
6. Save the bill and confirm the inventory update.
7. Review bill history, activity records, PDF exports, or sales charts from the admin tools.
   
🗄️ Database
The application uses a local SQLite database named Billing_Software.db. The code works with tables for:
- Admin — admin credentials
- Products — product details, category, price, quantity, and QR data
- Bills — bill identifiers, customer details, totals, dates, and QR data
- Activities — product-management activity records
Back up the database regularly if it contains records you need to preserve.

🗂️ Project Structure
Billing-Software/

├── app.py

├── Homepage.py

├── Login.py

├── Admin_Billing.py

├── Billing_Software.py

├── DataAnalysis.py

├── aboutUs.py

├── Requirement.txt

└── Billing_Software.db   # Local database, if present/generated

🛣️ Roadmap
- [ ] Secure authentication with password hashing and credential updates
- [ ] Automated tests for billing, stock updates, and database operations
- [ ] Transaction rollback for consistent bill and inventory updates
- [ ] Low-stock alerts and inventory movement reports
- [ ] Configurable tax, discounts, and invoice settings
- [ ] Database backup and restore
- [ ] Dependency pinning and packaged desktop installer

🤝 Contributing
Contributions and suggestions are welcome.
1. Fork the repository.
2. Create a feature branch: git checkout -b feature/your-feature
3. Commit your changes.
4. Push your branch and open a pull request with a clear description.
   
👨‍💻 Author

Aradhya Bhardwaj


📄 License

No license file was present in the supplied source archive. Until a license is added, reuse and redistribution permissions are not explicitly granted.
<div align="center">

Built with Python for practical retail workflows.

<a href="#-billing-software">⬆ Back to top</a>
</div>
