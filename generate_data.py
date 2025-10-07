import pandas as pd

# Sample student data
data = {
    "Roll No": range(101, 116),
    "Student Name": [
        "Rahul Patil", "Anjali Desai", "Sameer Joshi", "Priya Kulkarni", "Amit Shinde",
        "Sneha Patil", "Vikas Jadhav", "Pooja Chavan", "Rohit More", "Neha Pawar",
        "Kiran Salunkhe", "Swati Mane", "Sagar Kadam", "Meena Bhosale", "Ajay Nikam"
    ],
    "Class": ["1st Yr"] * 15,
    "Attendance %": [85, 92, 65, 88, 75, 90, 60, 80, 70, 95, 68, 85, 77, 82, 91],
    "Math": [78, 88, 40, 67, 59, 92, 35, 72, 60, 85, 55, 80, 69, 73, 90],
    "Science": [67, 74, 30, 70, 55, 85, 40, 65, 50, 90, 52, 77, 60, 68, 88],
    "English": [80, 69, 55, 75, 62, 88, 45, 70, 58, 84, 50, 79, 64, 72, 86]
}

# Create DataFrame
df = pd.DataFrame(data)

# Add Total, Percentage and Result columns
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Percentage"] = (df["Total"] / 3).round(2)
df["Result"] = df["Percentage"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# Save Excel file inside data folder
df.to_excel("../data/StudentData.xlsx", index=False)

print("✅ StudentData.xlsx generated successfully!")
