"""[summary]
"""
#! still better than nothing

SQLITE = {
    "average number of items per player": """
        SELECT AVG(Item_Count) AS Avg_Items_Per_Char
        FROM (SELECT DISTINCT character_id as Character_ID,
        COUNT(character_id) as Item_Count
        FROM Charactercreator_character_inventory
        GROUP BY Character_ID)
        """,
    "griffins average weapon count query": """
        select avg(item_count) as avg_items_per_char 
        from (
        select
        c.character_id,
        COUNT(distinct i.item_id) as item_count
        from charactercreator_character c
        join charactercreator_character_inventory i on c.character_id = i.character_id 
        group by c.character_id)
        """,
    "average weapon alternate": """
        SELECT AVG(Weapon_Count) AS Avg_Weapons_Per_Char
        FROM (SELECT DISTINCT character_id AS Character_ID,
        COUNT(character_id) AS Weapon_Count
        FROM charactercreator_character_inventory
        WHERE item_id IN
        (SELECT item_ptr_id FROM armory_weapon)
        GROUP BY Character_ID)
        LIMIT 20
        """,
}
