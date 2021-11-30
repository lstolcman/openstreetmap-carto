'''
script creates a new table called planet_osm_bars with a multilinestrings of intersections between
red_bar, green_bar, blue_bar, yellow_bar, black_bar
'''


import itertools
import psycopg2
conn = psycopg2.connect("dbname=gis user=postgres password='postgres'")

cur = conn.cursor()


q = 'DROP TABLE planet_osm_bars;'
cur.execute(q)
conn.commit()
q = r'''
CREATE TABLE planet_osm_bars
(
  osm_id SERIAL,
  red_bar BOOLEAN,
  green_bar BOOLEAN,
  blue_bar BOOLEAN,
  yellow_bar BOOLEAN,
  black_bar BOOLEAN,
   way geometry(MultiLineString,3857)
)
'''
cur.execute(q)
conn.commit()


colors = ['red','green','blue', 'yellow', 'black']

bars_colors = [f'{color}:white:{color}_bar' for color in colors]

for bar_color in bars_colors:
    print(f'{bar_color=}')
    q = f'''
    INSERT INTO
        public.planet_osm_bars (red_bar, green_bar, blue_bar, yellow_bar, black_bar, way)
    VALUES (
        {bar_color==bars_colors[0]}, -- if it is red bar, returns True
        {bar_color==bars_colors[1]}, -- if it is green bar, returns True
        {bar_color==bars_colors[2]}, -- ...
        {bar_color==bars_colors[3]},
        {bar_color==bars_colors[4]},
        (
            SELECT
                ST_Multi(ST_LineMerge(ST_Difference(a.way,b.way)))
            FROM 
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bar_color}')) AS way) AS a,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" != '{bar_color}')) AS way) AS b
        )
    )
    '''
    cur.execute(q);conn.commit()

## working routes rendering for intersection of 2 routes
bars_comb2 = list(itertools.combinations(bars_colors,2))

for bar_color1, bar_color2 in bars_comb2:
    bar_color_combined = f'{bar_color1};{bar_color2}'
    print(f'{bar_color_combined=}')
    bars_want = set({bar_color1, bar_color2})
    bars_dont_want = set(bars_colors) - bars_want
    bars_want = list(bars_want)
    bars_dont_want = list(bars_dont_want)
    q = f'''
    INSERT INTO
        public.planet_osm_bars (red_bar, green_bar, blue_bar, yellow_bar, black_bar, way)
    VALUES (
        {bars_colors[0] in bar_color_combined},
        {bars_colors[1] in bar_color_combined},
        {bars_colors[2] in bar_color_combined},
        {bars_colors[3] in bar_color_combined},
        {bars_colors[4] in bar_color_combined},
        (
            SELECT
                -- ST_Difference(ST_Intersection(a.way,b.way), ST_Union(array[c.way, d.way, e.way])) -- (A n B) - (C u D u E) = 3,3s
                ST_Multi(ST_LineMerge(ST_Difference(ST_Difference(ST_Difference(ST_Intersection(a.way,b.way), c.way), d.way), e.way))) -- (A n B) - C - D - E = 1,6s
                
            FROM 
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_want[0]}')) AS way) AS a,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_want[1]}')) AS way) AS b,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_dont_want[0]}')) AS way) AS c,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_dont_want[1]}')) AS way) AS d,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_dont_want[2]}')) AS way) AS e
        )
    )
    '''
    cur.execute(q);conn.commit()


## working routes rendering for intersection of 3 routes
bars_comb3 = list(itertools.combinations(bars_colors, 3))

for bar_color1, bar_color2, bar_color3 in bars_comb3:
    bar_color_combined = f'{bar_color1};{bar_color2};{bar_color3}'
    print(f'{bar_color_combined=}')
    bars_want = set({bar_color1, bar_color2, bar_color3})
    bars_dont_want = set(bars_colors) - bars_want
    bars_want = list(bars_want)
    bars_dont_want = list(bars_dont_want)
    q = f'''
    INSERT INTO
        public.planet_osm_bars (red_bar, green_bar, blue_bar, yellow_bar, black_bar, way)
    VALUES (
        {bars_colors[0] in bar_color_combined},
        {bars_colors[1] in bar_color_combined},
        {bars_colors[2] in bar_color_combined},
        {bars_colors[3] in bar_color_combined},
        {bars_colors[4] in bar_color_combined},
        (
            SELECT
                ST_Multi(ST_LineMerge(ST_Difference(ST_Difference(ST_Intersection(ST_Intersection(a.way,b.way), c.way), d.way), e.way))) -- (A n B n C) - D - E
                
            FROM 
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_want[0]}')) AS way) AS a,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_want[1]}')) AS way) AS b,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_want[2]}')) AS way) AS c,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_dont_want[0]}')) AS way) AS d,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_dont_want[1]}')) AS way) AS e
        )
    )
    '''
    cur.execute(q);conn.commit()


## working routes rendering for intersection of 4 routes
bars_comb4 = list(itertools.combinations(bars_colors, 4))

for bar_color1, bar_color2, bar_color3, bar_color4 in bars_comb4:
    bar_color_combined = f'{bar_color1};{bar_color2};{bar_color3};{bar_color4}'
    print(f'{bar_color_combined=}')
    bars_want = set({bar_color1, bar_color2, bar_color3, bar_color4})
    bars_dont_want = set(bars_colors) - bars_want
    bars_want = list(bars_want)
    bars_dont_want = list(bars_dont_want)
    q = f'''
    INSERT INTO
        public.planet_osm_bars (red_bar, green_bar, blue_bar, yellow_bar, black_bar, way)
    VALUES (
        {bars_colors[0] in bar_color_combined},
        {bars_colors[1] in bar_color_combined},
        {bars_colors[2] in bar_color_combined},
        {bars_colors[3] in bar_color_combined},
        {bars_colors[4] in bar_color_combined},
        (
            SELECT
                ST_Multi(ST_LineMerge(ST_Difference(ST_Intersection(ST_Intersection(ST_Intersection(a.way,b.way), c.way), d.way), e.way))) -- (A n B n C n D) - E
                
            FROM 
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_want[0]}')) AS way) AS a,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_want[1]}')) AS way) AS b,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_want[2]}')) AS way) AS c,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_want[3]}')) AS way) AS d,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_dont_want[0]}')) AS way) AS e
        )
    )
    '''
    cur.execute(q);conn.commit()



## working routes rendering for intersection of 5 routes
bars_comb5 = list(itertools.combinations(bars_colors, 5))

for bar_color1, bar_color2, bar_color3, bar_color4, bar_color5 in bars_comb5:
    bar_color_combined = f'{bar_color1};{bar_color2};{bar_color3};{bar_color4};{bar_color5}'
    print(f'{bar_color_combined=}')
    bars_want = set({bar_color1, bar_color2, bar_color3, bar_color4, bar_color5})
    bars_dont_want = set(bars_colors) - bars_want
    bars_want = list(bars_want)
    bars_dont_want = list(bars_dont_want)
    q = f'''
    INSERT INTO
        public.planet_osm_bars (red_bar, green_bar, blue_bar, yellow_bar, black_bar, way)
    VALUES (
        {bars_colors[0] in bar_color_combined},
        {bars_colors[1] in bar_color_combined},
        {bars_colors[2] in bar_color_combined},
        {bars_colors[3] in bar_color_combined},
        {bars_colors[4] in bar_color_combined},
        (
            SELECT
                ST_Multi(ST_LineMerge(ST_Intersection(ST_Intersection(ST_Intersection(ST_Intersection(a.way,b.way), c.way), d.way), e.way))) -- (A n B n C n D n E)
                
            FROM 
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_want[0]}')) AS way) AS a,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_want[1]}')) AS way) AS b,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_want[2]}')) AS way) AS c,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_want[3]}')) AS way) AS d,
                (SELECT ST_Union(array(SELECT way FROM planet_osm_line WHERE "osmc:symbol" IS NOT null AND "osmc:symbol" = '{bars_want[4]}')) AS way) AS e
        )
    )
    '''
    cur.execute(q);conn.commit()



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