--first task :
-- a. Find all allstar MVP players. 
-- b. Find all players born in New York.
-- c. Which players born in New York hold a MVP title?
select *  from allstar_mvps;

SELECT d.player_id, e.id, e.full_name
FROM allstar_mvps d
JOIN players e ON d.player_id = e.id
GROUP BY d.player_id, e.id, e.full_name;


select id, full_name, birth_place from players 
where birth_place = 'New York'


SELECT d.player_id, e.id, e.full_name, e.birth_place 
FROM allstar_mvps d
JOIN players e ON d.player_id = e.id
where e.birth_place like  '%New York'
GROUP BY d.player_id, e.id, e.full_name, e.birth_place;



-- second task:
-- Define which players have the same height

SELECT height, array_agg(full_name ) AS players_with_same_height
FROM players
GROUP BY height
HAVING count(*) > 1;

-- third task:
-- List the top 10 of the players having the most Player of the Month Awards.

SELECT d.player_id, e.id, e.full_name
FROM monthly_player_awards d
JOIN players e ON d.player_id = e.id
GROUP BY d.player_id, e.id, e.full_name;

SELECT d.player_id, e.id, e.full_name, COUNT(d.*) AS award_count
FROM monthly_player_awards d
JOIN players e ON d.player_id = e.id
GROUP BY d.player_id, e.id, e.full_name
ORDER BY award_count DESC
LIMIT 10;

-- fourth task:
-- Using table teams, create a new column that writes the messages 
-- "More than 2000 wins", "2000 wins" or "Less than 2000 wins" 
-- depending the number of wins it has, and also print the name and the number 
-- of wins for each team.
  SELECT
    team_id,
    team_name,
    total_wins,
    CASE
      WHEN total_wins <= 2000 THEN 'Less than 2000'
      WHEN total_wins = 2000 THEN '2000 wins'
      WHEN total_wins >= 2000 THEN 'More than 2000 wins'
    END AS total_wins_perteam
  FROM teams
  

-- fifth task:
-- Find all players that have both awards and other awards 
-- and print the name of the award as well.

SELECT d.payer_id, d.award as other_award, e.id, e.full_name, f.player_id, f.award as award
FROM other_player_awards d
JOIN players e ON d.payer_id = e.id
JOIN player_awards f ON d.payer_id = f.player_id
GROUP BY d.payer_id, e.id, f.player_id, d.award, e.full_name , f.award ;

