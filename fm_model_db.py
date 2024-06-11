import psycopg2


#import fm_core as core

def testcon():
    cur.execute("""SELECT m.fmid, m.marketname, m.state, m.zip, m.x, m.y FROM markets m""")
    res = cur.fetchone()
    print(res)


def show_all():
    cur.execute("""SELECT m.fmid, m.marketname, m.state, m.zip, m.x, m.y  FROM markets m
""")
    res = cur.fetchall()
    return res


def show_all_reviews():
    cur.execute("""SELECT m.fmid, m.marketname, m.state, m.zip, m.x, m.y, r.review_text, r.score FROM markets m
INNER JOIN reviews r ON r.review_market_id = m.fmid""")
    res = cur.fetchall()
    return res


def show_rev_by_id(id):
    try:
        cur.execute(
            """SELECT r.review_text, r.score FROM reviews r WHERE review_market_id = (%s)""",
            (id,))
    except psycopg2.Error:
        print(psycopg2.Error)
    finally:
        res = cur.fetchall()
        return res


def market_by_state(state):
    cur.execute(
        """SELECT m.fmid, m.marketname, m.state, m.zip, m.x, m.y FROM markets m WHERE lower(m.state) = lower(%s)""",
        (state,))
    res = cur.fetchall()
    return res

def market_by_zip(zip):
    cur.execute(
        """SELECT m.fmid, m.marketname, m.state, m.zip, m.x, m.y FROM markets m WHERE lower(m.zip) = lower(%s)""",
        (zip,))
    res = cur.fetchall()
    return res


def market_by_name(name):
    cur.execute(
        """SELECT m.fmid, m.marketname, m.state, m.zip, m.x, m.y FROM markets m WHERE lower(m.marketname) 
        LIKE lower(%s)""",
        (name,))
    res = cur.fetchone()
    return res


def market_by_id(id):
    cur.execute(
        """SELECT m.fmid, m.marketname, m.state, m.zip, m.x, m.y FROM markets m WHERE m.fmid = (%s)""",
        (id,))
    res = cur.fetchone()
    return res


def market_full_info(id):
    cur.execute("""SELECT * FROM markets m WHERE m.fmid = (%s)""", (id,))
    res = cur.fetchone()
    return res


def get_marketid_name(name):
    cur.execute("""SELECT fmid FROM markets m WHERE lower(m.marketname) LIKE lower(%s)""", (name,))


def add_review(id, id_text, score):
    market_check = market_by_id(id)
    if len(market_check) > 0:
        cur.execute("""INSERT INTO reviews VALUES (DEFAULT, (%s),(%s),(%s))""", (id, id_text, score,))
    conn.commit()

def delete_by_id(id):
    cur.execute(
        """DELETE FROM markets WHERE m.fmid = (%s)""", (id,))
    conn.commit()


conn = psycopg2.connect(dbname="farmers_markets",
                        host="localhost",
                        port="5432",
                        user="Biker",
                        password="password")
cur = conn.cursor()
data = show_all()
