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
q = 'CREATE TABLE planet_osm_red_blue_intersection \
( \
  osm_id SERIAL, \
  "osmc:symbol" text, \
   way geometry(MultiLineString,3857) \
)'
cur.execute(q)
conn.commit()



q='SELECT \
ST_LineMerge(st_intersection(a.way,b.way)) \
FROM  \
(select st_union(array(select way from planet_osm_line where "osmc:symbol" like \'red%:white:%_bar\')) as way) as a, \
(select st_union(array(select way from planet_osm_line where "osmc:symbol" like \'blue%:white:%_bar\')) as way) as b \
WHERE st_intersects(a.way, b.way)'
# conn.commit();cur.execute(q);conn.commit();z = cur.fetchall();print(z)
cur.execute(q);conn.commit()
red_blue_intersection_multilinestring = cur.fetchall()


q = f'insert into public.planet_osm_red_blue_intersection (way) VALUES (\'{red_blue_intersection_multilinestring[0][0]}\');'
cur.execute(q)
conn.commit()




# create new table - for blue-red intersections
q = 'DROP TABLE planet_osm_red;'
cur.execute(q)
conn.commit()
q = 'CREATE TABLE planet_osm_red \
( \
  osm_id SERIAL, \
  "osmc:symbol" text, \
   way geometry(LineString,3857) \
)'
cur.execute(q)
conn.commit()


q = r'''
insert into public.planet_osm_red (way)

SELECT
(st_dump(ST_Difference(a.way, b.way))).geom
FROM
(select st_union(way) as way from planet_osm_line where "osmc:symbol" like 'red%:white:%_bar') as a,
(select * from planet_osm_red_blue_intersection) as b

'''
cur.execute(q)
conn.commit()





q = 'DROP TABLE planet_osm_red2;'
cur.execute(q)
conn.commit()
q = 'CREATE TABLE planet_osm_red2 \
( \
  osm_id SERIAL, \
  "osmc:symbol" text, \
   way geometry(MultiLineString,3857) \
)'
cur.execute(q)
conn.commit()

q = r'''
insert into public.planet_osm_red2 (way)

SELECT
St_LineMerge(ST_Union(b.way))
FROM
(select way from planet_osm_red) as b

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