import pandas
import data_processing
import matplotlib.pyplot as plot
from io import BytesIO
import base64

data_dictionary = data_processing.get_data_in_frame()

student_name = data_dictionary.get("Student")
data_frame = data_dictionary.get("Data")

def check_for_data():
    return data_frame.empty

def fig_to_base64(fig):
    """Convert matplotlib figure to base64 string for embedding in HTML"""
    buffer = BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', dpi=100)
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plot.close(fig)
    return image_base64

def get_student_name():
    return student_name

def average_grade_by_semester():
    """Create a line chart visualizing average grade for each semester"""
    # Calculate average grade for each semester
    avg_grades = data_processing.filter_duplicate_grades(data_frame).groupby("Semester")["Grade"].mean().sort_index()
    
    # Create the line chart
    fig = plot.figure(figsize=(12, 6))
    plot.plot(avg_grades.index, avg_grades.values, marker='o', linewidth=2, markersize=8, color='#2E86AB')
    
    # Add labels for each point with average grade value
    for semester, grade in avg_grades.items():
        plot.text(semester, grade + 0.1, f'{grade:.2f}', ha='center', fontsize=10, fontweight='bold')
    
    # Customize the chart
    plot.title('Средноаритметичен успех по семестри', fontsize=16, fontweight='bold')
    plot.xlabel('Семестър', fontsize=12, fontweight='bold')
    plot.ylabel('Среден успех', fontsize=12, fontweight='bold')
    plot.grid(True, alpha=0.3)
    plot.xticks(avg_grades.index)
    plot.ylim(1, 6.5)
    
    # Return the chart as base64 image
    plot.tight_layout()
    return fig_to_base64(fig)


def average_grade_by_year():
    """Create a line chart visualizing average grade for each year"""
    # Calculate average grade for each year
    avg_grades = data_processing.filter_duplicate_grades(data_frame).groupby("Year")["Grade"].mean().sort_index()
    
    # Create the line chart
    fig = plot.figure(figsize=(12, 6))
    plot.plot(avg_grades.index, avg_grades.values, marker='o', linewidth=2, markersize=8, color='#2E86AB')
    
    # Add labels for each point with average grade value
    for year, grade in avg_grades.items():
        plot.text(year, grade + 0.1, f'{grade:.2f}', ha='center', fontsize=10, fontweight='bold')
    
    # Customize the chart
    plot.title('Средноаритметичен успех по години', fontsize=16, fontweight='bold')
    plot.xlabel('Година', fontsize=12, fontweight='bold')
    plot.ylabel('Среден успех', fontsize=12, fontweight='bold')
    plot.grid(True, alpha=0.3)
    plot.xticks(avg_grades.index)
    plot.ylim(1, 6.5)
    
    # Return the chart as base64 image
    plot.tight_layout()
    return fig_to_base64(fig)


def grade_distribution():
    """Create a pie chart showing the distribution of grades"""
    # Count occurrences of each grade
    grade_counts = data_frame["Grade"].value_counts().sort_index()
    
    # Create the pie chart
    fig = plot.figure(figsize=(10, 8))
    colors = ['#E8F4F8', '#B3D9E8', '#7FB3D5', '#4A90C2', '#2E5C8A', '#1A3A52']
    
    # Create custom autopct function to show both count and percentage
    def autopct_format(pct):
        total = sum(grade_counts.values)
        val = int(round(pct * total / 100.0))
        return f'{val}\n({pct:.1f}%)'
    
    plot.pie(grade_counts.values, labels=[f'{grade}' for grade in grade_counts.index], 
             autopct=autopct_format, startangle=90, colors=colors, textprops={'fontsize': 10, 'fontweight': 'bold'})
    
    # Customize the chart
    plot.title('Разпределение на оценки', fontsize=16, fontweight='bold')
    
    # Return the chart as base64 image
    plot.tight_layout()
    return fig_to_base64(fig)


def session_distribution():
    """Create a bar chart showing the distribution of session types"""
    # Define all possible session types
    all_sessions = ['редовна', 'поправителна', 'ликвидационна', 'индивидуален протокол']
    
    # Count occurrences of each session type
    session_counts = data_frame["Session"].value_counts()
    
    # Create a series with all session types, filling missing ones with 0
    session_data = pandas.Series([session_counts.get(session, 0) for session in all_sessions], index=all_sessions)
    
    # Create the bar chart
    fig = plot.figure(figsize=(12, 6))
    bars = plot.bar(range(len(session_data)), session_data.values, color='#2E86AB', edgecolor='black', linewidth=1.5)
    
    # Add value labels on top of each bar
    for i, (bar, value) in enumerate(zip(bars, session_data.values)):
        plot.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, 
                  str(value), ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Customize the chart
    plot.title('Разпределение на типовете сесии', fontsize=16, fontweight='bold')
    plot.xlabel('Сесия', fontsize=12, fontweight='bold')
    plot.ylabel('Брой', fontsize=12, fontweight='bold')
    plot.xticks(range(len(session_data)), session_data.index, rotation=45, ha='right')
    plot.grid(True, alpha=0.3, axis='y')
    plot.ylim(0, max(session_data.values) * 1.2)  # Set y-axis range with 20% padding
    
    # Return the chart as base64 image
    plot.tight_layout()
    return fig_to_base64(fig)


def examination_distribution():
    """Create a pie chart showing the distribution of examination types"""
    # Define all possible examination types
    all_examinations = ['Изпит', 'Текуща оценка', 'Курсов проект']
    
    # Count occurrences of each examination type
    examination_counts = data_frame["Examination"].value_counts()
    
    # Create a series with all examination types, filling missing ones with 0
    examination_data = pandas.Series([examination_counts.get(exam, 0) for exam in all_examinations], index=all_examinations)
    
    # Filter out zero values for the pie chart
    examination_data = examination_data[examination_data > 0]
    
    # Create the pie chart
    fig = plot.figure(figsize=(10, 8))
    colors = ['#E8F4F8', '#B3D9E8', '#7FB3D5']
    
    # Create custom autopct function to show both count and percentage
    def autopct_format(pct):
        total = sum(examination_data.values)
        val = int(round(pct * total / 100.0))
        return f'{val}\n({pct:.1f}%)'
    
    plot.pie(examination_data.values, labels=examination_data.index, 
             autopct=autopct_format, startangle=90, colors=colors[:len(examination_data)], 
             textprops={'fontsize': 10, 'fontweight': 'bold'})
    
    # Customize the chart
    plot.title('Разпределение на формите на контрол', fontsize=16, fontweight='bold')
    
    # Return the chart as base64 image
    plot.tight_layout()
    return fig_to_base64(fig)
