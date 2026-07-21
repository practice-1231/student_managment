from database import get_connection
#database
<<<<<<< HEAD
#it it
#asiodlh
=======

>>>>>>> a6da65e8c6cfbd9e642bd1b01fe03c1c83986aa2
try:
    conn = get_connection()
    print("✅ Connected to PostgreSQL successfully!")

    conn.close()

except Exception as e:
    print("❌ Connection failed")
    print(e)