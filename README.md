# sql-insert-opmizer
An utility which optimizer insert script


## How to use it?

```bash
python main.py -sql location_of_the_sql_file -batch batch_size
```


For example your `sql_file.sql` contains following

```sql
insert into post(it, title) values(1, 'Isaac Newton');
insert into post(it, title) values(2, 'Richard Feynman');
insert into post(it, title) values(3, 'Albert Einstein');
insert into post(it, title) values(4, 'Nicolaus Copernicus');
insert into post(it, title) values(5, 'Giordano Bruno');
```

The result of the script looks shown below.

```sql
insert into post(id, title) values(1, 'Isaac Newton'),
(2, 'Richard Feynman'),
(3, 'Albert Einstein');
insert into post(id, title) values(4, 'Nicolaus Copernicus'),
(5, 'Giordano Bruno');
```
