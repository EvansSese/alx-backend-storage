-- Calculate the rank of country origins based on the number of fans
WITH CountryFansRank AS (
    SELECT
        origin,
        COUNT(*) AS nb_fans
    FROM
        bands
    GROUP BY
        origin
)
SELECT
    origin,
    nb_fans,
    RANK() OVER (ORDER BY nb_fans DESC) AS country_rank
FROM
    CountryFansRank
ORDER BY
    nb_fans DESC;
