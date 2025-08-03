# 🚗 Vehicle Insurance ML Project (MLOps Pipeline)

This project demonstrates a complete end-to-end **Machine Learning Project** deployment pipeline using **MLOps** best practices. The pipeline covers data ingestion, validation, transformation, model training, evaluation, and deployment using **MongoDB Atlas**, **AWS (S3, EC2, ECR)**, **GitHub Actions (CI/CD)**, **Docker**, and **Flask**.

---

### ✅ **Features Implemented**
-  ☑️ MongoDB Integration
-  ☑️ Custom Logging & Exception
-  ☑️ Data Ingestion & Transformation
-  ☑️ Model Training & Evaluation
-  ☑️ S3 Model Push & Pull
-  ☑️ Dockerized App
-  ☑️ GitHub CI/CD Workflow
-  ☑️ EC2-based Hosting

## 🛠️ Project Setup

### 1. Create Project Structure
- Initialize the project using `template.py`.
- Set up `setup.py` and `pyproject.toml` to import local packages.
- Add local modules to `requirements.txt`.

### 2. Virtual Environment Setup
```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
```
---
Verify installation using pip list.

## 🗃️ MongoDB Atlas Setup
1. Sign up and create a cluster (M0 tier).
2. Create DB user with username/password.
3. Add IP Access: 0.0.0.0/0.
4. Get connection string (Python 3.6+ driver).
5. Save and update the string in environment variable:

```
$env:MONGODB_URL = "mongodb+srv://<username>:<password>@cluster.mongodb.net/"
```
## 📝 Notebook Setup
- Create notebook folder with dataset and mongoDB_demo.ipynb.
- Use vehicle virtual env as kernel.
- Push data to MongoDB from notebook and verify in Atlas.

## 🧾 Logging & Exception Handling
- Create logger.py and exception.py.
- Test them using demo.py.

## 📥 Data Ingestion Pipeline
1. Define constants in constants/__init__.py.
2. Connect MongoDB using configuration/mongo_db_connection.py.
3. Create data_access/proj1_data.py to pull and convert data to DataFrame.
4. Define configs in:
- entity/config_entity.py (till DataIngestionConfig)
- entity/artifact_entity.py (till DataIngestionArtifact)
5. Implement ingestion in components/data_ingestion.py and trigger via demo.py.

## 📥 Data Ingestion Pipeline

- Define constants in `constants/__init__.py`.
- Connect MongoDB using `configuration/mongo_db_connection.py`.
- Create `data_access/proj1_data.py` to pull and convert data to DataFrame.
- Define configs in:
  - `entity/config_entity.py` (till `DataIngestionConfig`)
  - `entity/artifact_entity.py` (till `DataIngestionArtifact`)
- Implement ingestion in `components/data_ingestion.py` and trigger via `demo.py`.

---

## ✅ Data Validation | ⚙️ Transformation | 🏋️ Model Training

### 1. Data Validation
- Define schema in `config/schema.yaml`.
- Code `DataValidation` component.

### 2. Data Transformation
- Add logic to `components/data_transformation.py`.
- Define transformations in `estimator.py`.

### 3. Model Training
- Implement training logic in `components/model_trainer.py`.

---

## ☁️ AWS Setup

### 1. IAM & S3 Configuration
- Create IAM user with `AdministratorAccess`.
- Add keys to environment variables:

```powershell
$env:AWS_ACCESS_KEY_ID = "your-access-key-id"
$env:AWS_SECRET_ACCESS_KEY = "your-secret-access-key"
```

- Create S3 bucket: `my-model-mlops-vehicleproj`

### 2. Add AWS Integration
Update `constants/__init__.py`:

```python
MODEL_BUCKET_NAME = "my-model-mlops-vehicleproj"
MODEL_PUSHER_S3_KEY = "model-registry"
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
```

- Add logic in:
  - `configuration/aws_connection.py`
  - `aws_storage.py`

---

## 📊 Model Evaluation & Pusher

- Complete model evaluation and pushing pipeline.

---

## 🧪 Prediction Pipeline

- Create `app.py` with web interface.
- Add `static` and `template` directories.

---

## 🚀 CI/CD Deployment (AWS + GitHub Actions)

### 1. Docker & EC2 Setup
Install Docker on EC2 Ubuntu instance:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

### 2. GitHub Runner on EC2
- Add self-hosted GitHub runner using EC2 instance.

### 3. GitHub Secrets
Store the following secrets in GitHub:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`
- `ECR_REPO`

### 4. ECR + EC2 Hosting
- Create ECR repo: `vehicleproj`.
- Push Docker image via GitHub Actions.
- Open EC2 port `5080` for public access.

### 5. Run the App
Paste public EC2 IP on browser with port:

```bash
http://<public-ip>:5080
```

---

## 💻 Train the Model Manually

Visit:

```bash
http://<public-ip>:5080/training
```

## 🛠️ Tech Stack

| Category         | Tools/Tech              |
| ---------------- | ----------------------- |
| Programming      | Python                  |
| ML               | Scikit-learn, Pandas    |
| DB               | MongoDB Atlas           |
| Cloud            | AWS (EC2, S3, ECR, IAM) |
| Containerization | Docker                  |
| Deployment       | GitHub Actions          |
| Web Interface    | Flask       |
