import os
import sqlite3

DB_FILEPATH = "rpg_db.sqlite3"

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

#how many characters are there?
query0 = ''' 
    SELECT
	count(distinct character_id) as CharacterCount
    FROM charactercreator_character
    '''

result0 = cursor.execute(query0).fetchall()
print("How many characters?", result0)

#how many of each subclass?
query1 = '''
SELECT
	count(DISTINCT charactercreator_fighter.character_ptr_id) as Fighters,
	count(DISTINCT charactercreator_cleric.character_ptr_id) as Clerics,
	count(DISTINCT charactercreator_mage.character_ptr_id) as Mages,
	count(DISTINCT charactercreator_necromancer.mage_ptr_id) as Necromancers,
	count(DISTINCT charactercreator_thief.character_ptr_id) as Thiefs
FROM charactercreator_fighter, charactercreator_cleric, charactercreator_mage, charactercreator_necromancer, charactercreator_thief
'''
result1 = cursor.execute(query1).fetchall()
print('how many of each subclass?', result1)


#I get the idea for how to do run from python so i'll just paste the rest of the queries here 
'''
-- how many total items? -- 174
/*
SELECT 
	count(DISTINCT item_id) as NumberofItems
FROM armory_item
*/
 -- how many are weapons? -- 37. How many are not? -- 137 
/*
Select
	count(DISTINCT item_ptr_id) as Num_weapons
FROM armory_weapon
*/
-- How many items does each character have? (first 20 rows)
/*
SELECT
	character_id,
	count(Distinct item_id) as ItemsOnCharacter
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
*/

-- How many weapons does each character have?
/*
SELECT 
	charactercreator_character_inventory.character_id,
	count(DISTINCT armory_weapon.item_ptr_id)
FROM charactercreator_character_inventory
JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character_inventory.character_id
LIMIT 20
*/

-- Average items per character
/*
SELECT
	AVG(mycount) as Avg_items_per_char
FROM (
	SELECT 
		COUNT(DISTINCT item_id) as mycount
		FROM charactercreator_character_inventory
		GROUP BY character_id)
*/	
-- average weapons per character -- .67
SELECT AVG(weapon_count) as avg_wep_per_char
FROM (
	SELECT
		c.character_id,
		c.name,
		--i.id,
		--i.item_id,
		count(DISTINCT w.item_ptr_id) as weapon_count
	FROM charactercreator_character c
	JOIN charactercreator_character_inventory i ON c.character_id = i.character_id
	LEFT JOIN armory_weapon w ON i.item_id = w.item_ptr_id
	GROUP BY c.character_id
) subq
'''