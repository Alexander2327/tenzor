create_table_query = """ CREATE TABLE IF NOT EXISTS test (
                             id INT PRIMARY KEY,
                             ParentId INT,
                             Name VARCHAR(255),
                             Type INT ) """

insert_data = """ INSERT INTO test (id, ParentId, Name, Type)
                      VALUES (%s, %s, %s, %s)
                      ON CONFLICT (id) DO NOTHING """

main_query = """ WITH r AS (
                     SELECT id, ParentId, Name
                     FROM test
                     WHERE ParentId IN (SELECT ParentId FROM test
                                            WHERE id IN (SELECT ParentId FROM test
                                                             WHERE id = %s)
                                        )
                )
                SELECT test.Name FROM test
                    JOIN r ON test.ParentId = r.id """
