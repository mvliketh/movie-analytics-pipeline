# 🎬 Movies Analytics Pipeline & Dashboard

## 📌 Project Overview
This project is an end-to-end data analytics pipeline that processes a raw dataset of movies, stores it in a relational database, and visualizes the key metrics in an interactive dashboard. 

The goal of this project was to analyze trends in the movie industry, including ratings, revenue, ROI, and genre distribution, providing a comprehensive view of cinematic success factors over the decades.

---

## 📊 Tableau Dashboard
**Interactive Version:** [View the full dashboard on Tableau Public](YOUR_TABLEAU_PUBLIC_LINK_HERE)

**Dashboard Screenshot:**
<img width="1593" height="894" alt="image" src="https://github.com/user-attachments/assets/7af1fa4a-0949-49a0-8962-660c19b75a60" />


### Key Features of the Dashboard:
*   **Custom Dark Mode UI:** A modular grid and dark theme utilizing pre-generated background assets.
*   **LOD Expressions:** Using aggregations to create "smart" coloring that maintains chart integrity when the "All" filter option is selected.
*   **Dynamic Tooltips:** Custom hover cards tailored for user experience instead of standard data logs.
*   **Interactive Dashboard Actions:** Cross-filtering setup (clicking on a chart dynamically updates the entire dashboard).
---

## ⚙️ Data Pipeline (ETL) Architecture

### 1. Extraction & Transformation (Python)
*   **Library:** `pandas`
*   Processed raw CSV files containing movie metadata.
*   Handled missing values, formatted dates, and cleaned text fields.

### 2. Loading (PostgreSQL)
*   **Libraries:** `psycopg2`, `SQLAlchemy`
*   Designed a relational database schema.
*   Wrote an automated script to establish a connection and ingest the cleaned DataFrame directly into the PostgreSQL database.

### 3. Analytics & Visualization (Tableau)
*   Aggregated metrics and built the final visual layout.

---

## 🛠️ Technologies & Tools Used
*   **Python:** pandas, psycopg2, SQLAlchemy
*   **Database:** PostgreSQL, DBeaver
*   **BI & Data Visualization:** Tableau Public
*   **Concepts applied:** ETL, Data Cleaning, Feature Engineering, Relational Databases, LOD Calculations, Dashboard Design

---

## 🚀 How to Run the ETL Script
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git)

```

2. Install the required Python packages:
```bash
pip install pandas psycopg2-binary sqlalchemy

```


3. Update the database credentials in `main.py` (or your script name) to match your local PostgreSQL setup.
4. Run the script:
```bash
python main.py

```



---

## 👨‍💻 Author

**Vladyslav Kovalenko**

* **LinkedIn:** [Vladyslav Kovalenko](https://www.linkedin.com/in/vladyslav-kovalenko-0738a33a6/)
* **GitHub:** [mvliketh](https://github.com/mvliketh)
