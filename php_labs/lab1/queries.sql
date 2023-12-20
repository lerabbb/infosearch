select * from cust where snum=1001;
select city, sname, snum, comm from sal;
select rating, cname from cust where cname="San Jose";
select distinct snum from ord;
select sname, city from sal where city = "London" and comm>0.11;
select * from cust where rating<=200 and city!="Rome";
select * from ord where odate = '03-OCT-90' or odate = '05-OCT-90';
select * from ord where odate in ('03-OCT-90', '05-OCT-90');
select * from cust where cname regexp '^[A-G]';
select * from sal where sname LIKE '%e%';
select count(amt) from ord where odate='03-OCT-90';
select count(amt) from ord where snum=1001;
select snum, max(amt) from ord group by snum;
select * from cust where cname like '%s' order by cname limit 0, 1;
select city, avg(comm) from sal group by city;

select ord.onum, ord.amt * 0.8 as euro_amt, sal.sname, sal.comm
    from ord join sal using(snum) where odate = '03-OCT-90';

select onum, sname, cname
    from ord join sal using(snum) join cust using (cnum)
    where sal.city in ('London', 'Rome')
    order by onum asc;

select sname, SUM(ord.amt), comm
    from sal join ord using(snum) 
    where odate < '05-Oct-90'
    group by sname, comm
    order by sname asc;

select onum, amt, sname, cname
    from ord join sal using(snum) join cust using (cnum)
    where sal.city regexp '^[L-R]' and cust.city regexp '^[L-R]';

select snum, cust1.cname, cust2.cname 
    from cust as cust1 join cust as cust2 using(snum) 
    where cust1.cnum < cust2.cnum;

select cname from cust
    where snum in (select snum from sal where comm < 0.13);

create table sal_copy as select * from sal;
desc sal;
desc sal_copy;

insert into sal (snum, sname, city, comm)
values
    (1005, "Anna", "Novosibirsk", 0.14),
    (1008, "Ivan",  "Moscow", 0.13);
select * from sal;
delete from sal where snum = 1005;
delete from sal where snum = 1008;
select * from sal;

insert into sal (snum, sname, city, comm)
values
    (1010, "Mark", "Paris", 0.15),
    (1011, "Beth",  "Tokyo", 0.12);
update sal set comm = comm * 2;
select * from sal;
update sal set comm = comm / 2;
delete from sal where snum = 1010;
delete from sal where snum = 1011;
select * from sal;
