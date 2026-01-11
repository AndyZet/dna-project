"""
Database migrations
"""
from .models import create_database


def run_migrations():
    """Run database migrations"""
    print("Creating database...")
    engine = create_database()
    print("Database created successfully!")
    return engine


if __name__ == "__main__":
    run_migrations()
