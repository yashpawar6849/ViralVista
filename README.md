# 🚀 Project for Supermind Hackathon

**ViralVista** is a cutting-edge application designed for social media performance analysis. It leverages the power of LangFlow for workflow orchestration and DataStax Astra DB for scalable and efficient data storage. ViralVista provides actionable insights into the performance of social media posts, including metrics like likes, shares, and comments.

---

## 🛠️ How It Works

### 1. Data Ingestion:
- Social media performance data (e.g., likes, comments, shares) is fetched and stored in DataStax Astra DB.
- Data is processed and analyzed using a LangFlow-based workflow.

### 2. LangFlow Workflow:
ViralVista integrates LangFlow to orchestrate the data processing pipeline. Below is a snapshot of the workflow:
![Workflow Diagram](https://github.com/yashpawar6849/ViralVista/blob/main/Snapshot%20of%20flow.png)



#### Workflow Steps:
- **Take Input:** Accept input from the user.
- **Retrieve Data:** Fetch data from Astra DB.
- **Extract UserId:** Parse the UserId from the input text.
- **Filter Data:** Filter the retrieved data using the UserId.
- **Calculate Averages:** Compute averages by post types.
- **Input to Model:** Feed the processed data into the ML model.
- **Retrieve Output:** Return actionable insights from the model.

### 3. Data Storage with Astra DB:
DataStax Astra DB is used for storing social media data in a scalable, cloud-native database. The table schema includes:
- `user_id`: Unique identifier for the user.
- `post_type`: Type of post (reel, carousel, static image).
- `likes`, `comments`, `shares`: Metrics tracked for performance analysis.

---

## 🌟 Features

- **Real-Time Data Analysis:** Analyze social media metrics instantly.
- **Customizable Insights:** Generate insights tailored to user needs.
- **Scalable Storage:** Handle millions of records with DataStax Astra DB.
- **Workflow Automation:** Orchestrate data analysis with LangFlow.

---

## 💻 Run Locally

### Prerequisites:
- Python installed.
- Access to DataStax Astra DB.
- Streamlit for frontend deployment.

### Steps:
1. Clone this repository:
   ```bash
   git clone https://github.com/yashpawar6849/ViralVista.git
   cd ViralVista
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables:
   - `LANGFLOW_APPLICATION_TOKEN`
   - `ASTRA_TOKEN`
   - `ASTRA_URL`

4. Start the application:
   ```bash
   streamlit run app.py
   ```
5. Access the app at `http://localhost:8501`.

---

## 🎥 Demo Video

Watch the complete demo of **ViralVista** on YouTube: [Walkthrough Video](#).

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python, LangFlow
- **Database:** DataStax Astra DB
- **Orchestration:** LangFlow

---

*Thank you for visiting ❤️*
