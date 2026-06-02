from database.sql_analysis import run_sql_query

def studytime_vs_performance():
    query = """
    SELECT studytime,
           AVG(G3) AS avg_final_grade,
           COUNT(*) AS student_count
    FROM students
    GROUP BY studytime
    ORDER BY studytime;
    """
    return run_sql_query(query)

def gender_vs_performance():
    query = """
    SELECT sex,
           AVG(G3) AS avg_final_grade
    FROM students
    GROUP BY sex;
    """
    return run_sql_query(query)

def absences_vs_performance():
    query = """
    SELECT
        CASE
            WHEN absences < 5 THEN 'Low Absences'
            WHEN absences BETWEEN 5 AND 15 THEN 'Medium Absences'
            ELSE 'High Absences'
        END AS absence_group,
        AVG(G3) AS avg_grade
    FROM students
    GROUP BY absence_group;
    """
    return run_sql_query(query)
