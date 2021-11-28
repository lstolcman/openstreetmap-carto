'''
script creates a new table called planet_osm_red_blue_intersection with a multilinestrings of intersectiojns between red and blue bar
'''



import psycopg2
conn = psycopg2.connect("dbname=gis user=postgres password='postgres'")

cur = conn.cursor()



# create new table - for blue-red intersections
q = 'DROP TABLE planet_osm_red_blue_intersection;'
cur.execute(q)
conn.commit()
q = r'''
CREATE TABLE planet_osm_red_blue_intersection
(
  osm_id SERIAL,
  "osmc:symbol" text,
   way geometry(MultiLineString,3857)
)
'''
cur.execute(q)
conn.commit()



q = r'''
INSERT INTO
    public.planet_osm_red_blue_intersection ("osmc:symbol", way)
VALUES (
    'red:white:red_bar;blue:white:blue_bar',(
    SELECT
        ST_LineMerge(ST_Intersection(a.way,b.way))
    FROM 
        (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = 'red:white:red_bar')) AS way) AS a,
        (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = 'blue:white:blue_bar')) AS way) AS b
    WHERE
        ST_Intersects(a.way, b.way)
    )
)
'''
# conn.commit();cur.execute(q);conn.commit();z = cur.fetchall();print(z)
cur.execute(q);conn.commit()
# red_blue_intersection_multilinestring = cur.fetchall()

# create new table - for blue-red intersections
q = 'DROP TABLE planet_osm_red;'
cur.execute(q)
conn.commit()

q = r'''
CREATE TABLE planet_osm_red
(
  osm_id SERIAL,
  "osmc:symbol" text,
   way geometry(MultiLineString,3857)
)
'''
cur.execute(q)
conn.commit()

q = r'''
INSERT INTO
    public.planet_osm_red (way)
SELECT
    St_LineMerge(ST_Difference(a.way, b.way))
FROM
    (SELECT ST_Union(way) as way FROM planet_osm_line WHERE "osmc:symbol" = 'red:white:red_bar') AS a,
    (SELECT * FROM planet_osm_red_blue_intersection) AS b
'''
cur.execute(q)
conn.commit()






'''
all combinations of lines are:

In [934]: list(itertools.combinations(['red','green','blue', 'yellow', 'black'],2))
Out[934]:
[('red', 'green'),
 ('red', 'blue'),
 ('red', 'yellow'),
 ('red', 'black'),
 ('green', 'blue'),
 ('green', 'yellow'),
 ('green', 'black'),
 ('blue', 'yellow'),
 ('blue', 'black'),
 ('yellow', 'black')]

In [935]: list(itertools.combinations(['red','green','blue', 'yellow', 'black'],3))
Out[935]:
[('red', 'green', 'blue'),
 ('red', 'green', 'yellow'),
 ('red', 'green', 'black'),
 ('red', 'blue', 'yellow'),
 ('red', 'blue', 'black'),
 ('red', 'yellow', 'black'),
 ('green', 'blue', 'yellow'),
 ('green', 'blue', 'black'),
 ('green', 'yellow', 'black'),
 ('blue', 'yellow', 'black')]

In [936]: list(itertools.combinations(['red','green','blue', 'yellow', 'black'],4))
Out[936]:
[('red', 'green', 'blue', 'yellow'),
 ('red', 'green', 'blue', 'black'),
 ('red', 'green', 'yellow', 'black'),
 ('red', 'blue', 'yellow', 'black'),
 ('green', 'blue', 'yellow', 'black')]

In [937]: list(itertools.combinations(['red','green','blue', 'yellow', 'black'],5))
Out[937]: [('red', 'green', 'blue', 'yellow', 'black')]

In [938]:

'''