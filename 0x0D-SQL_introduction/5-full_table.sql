-- describe table without describe statement
SELECT * 
  FROM information_schema.columns 
 WHERE table_name = 'first_table';
