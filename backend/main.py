from fastapi import FastAPI, UploadFile, File, Form
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sales Insight Automator API"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...), email: str = Form(...)):

    df = pd.read_csv(file.file)

    total_revenue = df["Revenue"].sum()
    total_units = df["Units_Sold"].sum()

    summary = f"""
Sales Summary

Total Revenue: {total_revenue}
Total Units Sold: {total_units}
"""

    return {
        "email": email,
        "summary": summary
    }