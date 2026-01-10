import charts

#Check if there is data to visualize
if charts.check_for_data():
    print(f"No data available to represent for {charts.get_student_name()}!")
    exit()

# Get student name
student_name = charts.get_student_name()

# Generate all charts
semester_chart = charts.average_grade_by_semester()
year_chart = charts.average_grade_by_year()
grade_chart = charts.grade_distribution()
session_chart = charts.session_distribution()
examination_chart = charts.examination_distribution()

# Create HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Grades Statistics - {student_name}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2E86AB;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5em;
        }}
        .student-info {{
            text-align: center;
            margin-bottom: 30px;
            font-size: 1.1em;
            color: #555;
        }}
        .charts-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 40px;
            margin-top: 30px;
        }}
        .chart {{
            text-align: center;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 8px;
            border: 1px solid #eee;
        }}
        .chart img {{
            max-width: 80%;
            height: auto;
            border-radius: 4px;
        }}
        footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            color: #999;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Статистика на следването</h1>
        <div class="student-info">
            <strong>Студент:</strong> {student_name}
        </div>
        
        <div class="charts-grid">
            <div class="chart">
                <img src="data:image/png;base64,{semester_chart}" alt="Average Grade by Semester">
            </div>
            <div class="chart">
                <img src="data:image/png;base64,{year_chart}" alt="Average Grade by Year">
            </div>
            <div class="chart">
                <img src="data:image/png;base64,{grade_chart}" alt="Grade Distribution">
            </div>
            <div class="chart">
                <img src="data:image/png;base64,{session_chart}" alt="Session Type Distribution">
            </div>
            <div class="chart">
                <img src="data:image/png;base64,{examination_chart}" alt="Examination Type Distribution">
            </div>
        </div>
        
        <footer>
            <p>Generated automatically | University Grades Statistics Application</p>
        </footer>
    </div>
</body>
</html>
"""

# Save HTML file
output_filename = f"student_grades_{student_name.replace(' ', '_')}.html"
with open(output_filename, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML file created successfully: {output_filename}")