import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/
#
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is
# created in the file `pets_db.py`.
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """
SELECT name, species, age FROM animals 
    LEFT JOIN people_animals ON animals.animal_id = people_animals.pet_id 
    WHERE people_animals.owner_id IS NULL;
"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners.
# The output should be an integer.

sql_pets_older_than_owner = """
SELECT COUNT(*) FROM animals 
    INNER JOIN people_animals ON animals.animal_id = people_animals.pet_id 
    INNER JOIN people ON people_animals.owner_id = people.person_id 
    WHERE animals.age > people.age;
"""

# Part 4.C: BONUS CHALLENGE!
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)

"""
We use a sub-query to get the number of owners for each pet. We are interested in
those pets that have only one owner. We then join the people table to get the name
of the bessie. Finally, we join the animals table to get the name and species of
the pets.
"""
sql_only_owned_by_bessie = """ 
SELECT people.name, animals.name, animals.species FROM people_animals AS opa
    INNER JOIN people ON opa.owner_id = people.person_id
    INNER JOIN animals ON opa.pet_id = animals.animal_id
    INNER JOIN (
        SELECT ipa.pet_id, ipa.owner_id ,COUNT(ipa.pet_id) AS owner_count 
            FROM people_animals AS ipa GROUP BY ipa.pet_id
    ) AS animal_owner_count_tb ON opa.pet_id = animal_owner_count_tb.pet_id 
    WHERE animal_owner_count_tb.owner_count = 1 AND people.name = "bessie";
"""
