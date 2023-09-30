from sqlalchemy import create_engine,text


engine = create_engine('sqlite:///IRSv2.db')

with engine.connect() as connection:
    result = connection.execute(text('SELECT * from ''User'' '))

    print(result.all())