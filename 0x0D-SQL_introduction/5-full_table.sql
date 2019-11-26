-- describe table without describe statement
select * 
  from information_schema.columns 
 where table_name = 'first_table';
