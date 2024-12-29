import asyncio
import asyncpg
import os
import time

from app.config import settings


def delete_and_new_initiate_migration():
    """Считает кол-во файлов с миграциями, и все их откатывает"""
    mig_files = [file for file in os.listdir(f'{os.getcwd()}/app/migrations/versions') if file.endswith('.py')]
    os.system(f'alembic downgrade -{len(mig_files)}')
    print(f'all migrations downgraded')

    for file_name in mig_files:
        os.remove(f'{os.getcwd()}/app/migrations/versions/{file_name}')
        print(f'file {file_name} deleted')

    os.system(f'alembic revision --autogenerate -m "Initial tables"')
    print(f'migration created')

    time.sleep(1)

    os.system(f'alembic upgrade head')
    print(f'migration applied')


async def add_initial_info():
    # conn = await asyncpg.connect(f'postgresql://admin:admin@localhost:5432/{settings.DB_NAME}') TODO Сделать ссылку через env
    conn = await asyncpg.connect(user=settings.DB_USER, password=settings.DB_PASS,
                                 database=settings.DB_NAME, host=settings.DB_HOST, port=5432)
    print("Connect to database")
    try:
        # Insert into artists table
        await conn.executemany(
            "INSERT INTO artists (nick, slug) VALUES ($1, $2)",
            [
                ('21 Savage', '21-savage'),
                ('NLE Choppa', 'nle-choppa'),
                ('Drake', 'drake'),
                ('Gunna', 'gunna')
            ]
        )
        print('artists successfully inserted')

        # Insert into genre table
        await conn.executemany(
            "INSERT INTO genre (title, slug) VALUES ($1, $2)",
            [
                ('Jazz', 'jazz'),
                ('Rap', 'rap'),
                ('Rock', 'rock'),
                ('Hip hop', 'hip-hop')
            ]
        )
        print('genre successfully inserted')

        # Insert into songs table
        await conn.executemany(
            """
            INSERT INTO songs (title, slug, slang, ambiguity, flow, words_slurring, description, published, accent, genre_id)
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
            """,
            [
                ('a lot', 'a-lot', 3, 4, 3, 5, 'test', False, 'american', 4),
                ('Shotta Flow 5', 'shotta-flow-5', 5, 8, 1, 10, 'test', False, 'american', 4),
                ('One Dance', 'one-dance', 3, 2, 2, 3, 'test', False, 'american', 4),
                ('I’M ON SOME', 'i-am-on-some', 7, 2, 9, 10, 'test', False, 'american', 4)
            ]
        )
        print('songs successfully inserted')

        # Insert into song_artist table
        await conn.executemany(
            "INSERT INTO song_artist (song_id, artist_id) VALUES ($1, $2)",
            [
                (1, 1),
                (1, 3),
                (2, 2),
                (3, 1),
                (3, 3),
                (3, 4),
                (4, 4)
            ]
        )
        print('song_artist successfully inserted')

        # Insert into users table
        await conn.executemany(
            """
            INSERT INTO users (user_name, user_password, email, email_confirmed, eng_lvl, is_admin, is_superuser)
            VALUES ($1, $2, $3, $4, $5, $6, $7)
            """,
            [
                ('ivan', '123', 'test@gmail.com', True, 'B1', True, True),
                ('user', 'test', 'user@user.ru', False, 'A1', False, False),
                ('admin', 'qerty123', 'admin@admin.com', False, 'IDK', True, False)
            ]
        )
        print('users successfully inserted')

        # Insert into song_likes table
        await conn.executemany(
            "INSERT INTO song_likes (song_id, user_id) VALUES ($1, $2)",
            [
                (1, 1),
                (1, 3),
                (2, 2),
                (3, 1),
                (3, 3),
                (3, 2),
                (4, 2)
            ]
        )
        print('song_likes successfully inserted')

        # Insert into song_comments table
        await conn.executemany(
            """
            INSERT INTO song_comments (user_id, song_id, comm_text)
            VALUES ($1, $2, $3)
            """,
            [
                (1, 1, 'Я в шоке'),
                (1, 3, 'РЕКОММЕНДУЮ'),
                (2, 2, 'НУ ТАКОЕ'),
                (3, 4, 'Я БЫ ЛУЧЫЧШЕ ИСПОЛНИЛ'),
                (2, 3, 'оценка конечно оставляет желать лучшего'),
                (2, 2, 'Вау какой он красивый'),
                (3, 4, 'Рэп это жизнь')
            ]
        )
        print('song_comments successfully inserted')


    finally:
        # Close the connection
        await conn.close()
        print("Database closed")


# if __name__ == '__main__':
delete_and_new_initiate_migration()
time.sleep(1)
asyncio.run(add_initial_info())
