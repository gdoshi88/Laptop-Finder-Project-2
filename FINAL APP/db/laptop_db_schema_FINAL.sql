/***********************************************************/
--PREP THE TABLE CREATION: DROP JUST IN CASE THEY PRE-EXIST:
/***********************************************************/
DROP TABLE IF EXISTS frys_laptops;
DROP TABLE IF EXISTS bestbuy_laptops;


/***********************************************************/
--CREATE TABLE FOR FRYS LAPTOPS
/***********************************************************/
CREATE Table frys_laptops (
	brand VARCHAR,
	model VARCHAR(50),
	screensize FLOAT,
	cpu VARCHAR,
	ram INT,
	hd VARCHAR,
	upc INT PRIMARY KEY, 
	price FLOAT,
	link VARCHAR,
	title VARCHAR,
	lastUpdated DATE
);

/***********************************************************/
--CREATE TABLE FOR BESTBUY LAPTOPS
/***********************************************************/
CREATE Table bestbuy_laptops (
	brand VARCHAR,
	model VARCHAR(50),
	screensize FLOAT,
	cpu VARCHAR,
	ram INT,
	hd VARCHAR,
	graphics VARCHAR,
	upc INT PRIMARY KEY, 
	price FLOAT,
	link VARCHAR,
	title VARCHAR,
	lastUpdated DATE
);


/***********************************************************/
-- VALIDATE TABLE REPOPULATION
/***********************************************************/
SELECT * FROM frys_laptops;
SELECT * FROM bestbuy_laptops;
