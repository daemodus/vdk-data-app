CREATE VIEW usa_cities
AS
    SELECT *
    FROM cities
    WHERE country = 'United States';
    