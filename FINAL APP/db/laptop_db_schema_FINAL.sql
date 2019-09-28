/***********************************************************/
--PREP THE TABLE CREATION: DROP JUST IN CASE THEY PRE-EXIST:
/***********************************************************/
DROP TABLE IF EXISTS frys_laptops;
DROP TABLE IF EXISTS bestbuy_laptops;

DROP TABLE IF EXISTS bestbuy_locations;
DROP TABLE IF EXISTS frys_locations;
DROP TABLE IF EXISTS both_locations;

/***********************************************************/
--CREATE TABLE FOR FRYS LAPTOPS
/***********************************************************/
CREATE Table frys_laptops (
	brand VARCHAR,
	model VARCHAR(50),
	screenSize FLOAT,
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
	screenSize FLOAT,
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
--CREATE TABLE FOR FRYS LOCATIONS:
/***********************************************************/
CREATE Table frys_locations (
	index INT PRIMARY KEY,
	store VARCHAR(10),
	address VARCHAR,
	city VARCHAR,
	region VARCHAR,
	postalcode VARCHAR,
	lat VARCHAR,
	lng VARCHAR
);


/***********************************************************/
--CREATE TABLE FOR BEST BUY LOCATIONS:
/***********************************************************/
CREATE Table bestbuy_locations (
	index INT PRIMARY KEY,
	store VARCHAR(10),
	address VARCHAR,
	city VARCHAR,
	region VARCHAR,
	postalcode VARCHAR,
	lat VARCHAR,
	lng VARCHAR
);


/***********************************************************/
--CREATE TABLE FOR BOTH LOCATIONS:
/***********************************************************/
CREATE Table both_locations (
	index INT PRIMARY KEY,
	store VARCHAR(10),
	address VARCHAR,
	city VARCHAR,
	region VARCHAR,
	postalcode VARCHAR,
	lat VARCHAR,
	lng VARCHAR
);

/***********************************************************/
-- VALIDATE TABLE REPOPULATION
/***********************************************************/
SELECT * FROM frys_laptops;
SELECT * FROM bestbuy_laptops;
SELECT * FROM frys_locations;
SELECT * FROM bestbuy_locations;
SELECT * FROM both_locations;
