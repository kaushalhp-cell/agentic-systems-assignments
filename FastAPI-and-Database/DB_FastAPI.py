from sqlalchemy import (create_engine, MetaData, Table, Column, Integer, String, CheckConstraint, insert, select,
                        update, delete)
from sqlalchemy.exc import SQLAlchemyError

# STEP 1: Create Database Connection


def create_connection():
    """
    Creates and returns a database engine connection to MySQL.

    Connection string format:
    mysql+pymysql://username:password@host:port/database_name
    """
    try:
        # Replace with actual MySQL credentials
        username = "root"
        password = "password"
        host = "localhost"
        port = "3306"
        database = "student_db"

        # Create connection string
        connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

        # Create engine
        engine = create_engine(connection_string, echo=True)

        print("Database connection created successfully!")
        return engine

    except SQLAlchemyError as e:
        print(f"Error creating database connection: {e}")
        return None

# STEP 2: Create Students Table


def create_students_table(engine):
    """
    Creating the students table with specified schema.
    """
    try:
        # Create metadata object
        metadata = MetaData()

        # Define students table
        students = Table(
            'students',
            metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('name', String(100), nullable=False),
            Column('age', Integer, nullable=False),
            Column('city', String(100), nullable=True),
            CheckConstraint('age >= 18', name='check_age_18_plus')
        )

        # Creating table in database
        metadata.create_all(engine)

        print("Students table created successfully!")
        return students

    except SQLAlchemyError as e:
        print(f"Error creating students table: {e}")
        return None

# STEP 3: Insert 3 Student Records


def insert_students(engine, students_table):
    """
    Inserts 3 student records into the students table.
    """
    try:
        with engine.connect() as conn:
            # Defining student data
            student_data = [
                {'name': 'Rahul', 'age': 22, 'city': 'Mumbai'},
                {'name': 'Priya', 'age': 19, 'city': 'Delhi'},
                {'name': 'Amit', 'age': 25, 'city': 'Bangalore'}
            ]

            # Inserting records
            stmt = insert(students_table).values(student_data)
            result = conn.execute(stmt)
            conn.commit()

            print(
                f"Inserted {len(student_data)} student records successfully!")
            print(
                f"Inserted IDs: {result.inserted_primary_key if hasattr(result, 'inserted_primary_key') else 'Multiple rows'}")

    except SQLAlchemyError as e:
        print(f"Error inserting students: {e}")

# STEP 4: Fetch All Students


def fetch_all_students(engine, students_table):
    """
    Fetch and display all student records.
    """
    try:
        with engine.connect() as conn:
            # Select all students
            stmt = select(students_table)
            result = conn.execute(stmt)

            print("\n All Students:")
            print("-" * 60)
            print(f"{'ID':<5} {'Name':<15} {'Age':<5} {'City':<20}")
            print("-" * 60)

            students = result.fetchall()

            if students:
                for student in students:
                    print(
                        f"{student.id:<5} {student.name:<15} {student.age:<5} {student.city or 'N/A':<20}")
            else:
                print("No students found.")

            print("-" * 60)
            print(f"Total students: {len(students)}\n")

    except SQLAlchemyError as e:
        print(f"Error fetching students: {e}")


# STEP 5: Update City of Student Named "Rahul"

def update_rahul_city(engine, students_table, new_city="Pune"):
    """
    Updating the city of student 'Rahul'.
    """
    try:
        with engine.connect() as conn:
            # Update statement
            stmt = (
                update(students_table)
                .where(students_table.c.name == 'Rahul')
                .values(city=new_city)
            )

            result = conn.execute(stmt)
            conn.commit()

            print(f"Updated city for 'Rahul' to '{new_city}'")
            print(f"Rows affected: {result.rowcount}")

    except SQLAlchemyError as e:
        print(f"Error updating student: {e}")

# STEP 6: Delete Students with Age < 20


def delete_students_under_20(engine, students_table):
    """
    Delete all students whose age is less than 20.
    """
    try:
        with engine.connect() as conn:
            # Delete statement
            stmt = delete(students_table).where(students_table.c.age < 20)

            result = conn.execute(stmt)
            conn.commit()

            print(f"Deleted students with age < 20")
            print(f"Rows deleted: {result.rowcount}")

    except SQLAlchemyError as e:
        print(f"Error deleting students: {e}")


# MAIN EXECUTION

def main():
    """
    Main function to execute all operations in sequence.
    """
    print("="*60)
    print("STUDENT MANAGEMENT SYSTEM - SQLAlchemy Core")
    print("="*60)

    # Step 1: Create database connection
    print("\n[STEP 1] Creating database connection...")
    engine = create_connection()
    if not engine:
        print("Failed to create connection. Exiting.")
        return

    # Step 2: Create students table
    print("\n[STEP 2] Creating students table...")
    students_table = create_students_table(engine)
    if not students_table:
        print("Failed to create table. Exiting.")
        return

    # Step 3: Insert 3 student records
    print("\n[STEP 3] Inserting student records...")
    insert_students(engine, students_table)

    # Step 4: Fetch all students
    print("\n[STEP 4] Fetching all students...")
    fetch_all_students(engine, students_table)

    # Step 5: Update Rahul's city
    print("\n[STEP 5] Updating Rahul's city...")
    update_rahul_city(engine, students_table, new_city="Pune")

    # Fetch all students after update
    print("\nAfter updating Rahul's city:")
    fetch_all_students(engine, students_table)

    # Step 6: Delete students with age < 20
    print("\n[STEP 6] Deleting students with age < 20...")
    delete_students_under_20(engine, students_table)

    # Fetch all students after deletion
    print("\nAfter deleting students with age < 20:")
    fetch_all_students(engine, students_table)

    print("\n" + "="*60)
    print("OPERATIONS COMPLETED SUCCESSFULLY!")
    print("="*60)


if __name__ == "__main__":
    main()
