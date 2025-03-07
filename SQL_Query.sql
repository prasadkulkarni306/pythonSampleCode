desc customer;

alter table customer add column city varchar(20);

alter table customer modify column city varchar(40);

alter table customer rename column city to country;

alter table customer drop column country;


truncate table customer;

create table employee(
emp_id integer,
emp_name varchar(20),
emp_addr varchar(50),
mobile_no integer,
DOB date,
age int,
country varchar(20) not null default ('INDIA'),
dept_id integer,
constraint pk_emp_id_mob_no primary key(emp_id,mobile_no),
constraint chk_age check(age>=18),
constraint nn_dob unique(DOB),
constraint cust_dept foreign key(dept_id) references dept(dept_id)
);


create table dept(
dept_id integer primary key,
dept_name varchar(20)
);

desc customer;
desc employee;

desc dept;
insert into dept_id value (1,'Maths');

create table multi(img blob);

desc multi;

desc customer;
desc employee;
desc dept;

drop table customer;
create table customer(cust_id integer primary key,
first_name varchar(20),
last_name varchar(20),
mobile_no varchar(10),
gender char(1),
sal float(8,2));

desc customer;
alter table customer modify column gender char(5);
alter table customer add constraint unique(mobile_no);

alter table customer add primary key (cust_id);
select * from customer;
delete from customer where cust_id=1;
insert into customer values(1,'Prasad','KulkarniA','123453781','M',1000);
insert into customer values(2,'PrasadA','KulkarniB','133456781','M',2000);
insert into customer values(3,'PrasadB','KulkarniC','223466781','M',3000);
insert into customer values(4,'PrasadC','KulkarniD','323458781','M',4000);
insert into customer values(5,'PrasadD','KulkarniE','423459781','M',5000);
insert into customer values(6,'PrasadE','KulkarniF','53451781','M',6000);
insert into customer values(7,'PrasadF','KulkarniG','623452781','M',7000);
insert into customer values(8,'PrasadG','Kulkar5niH','723453781','M',8000);
insert into customer values(9,'PrasadH','KulkarniI','813454781','M',9000);
insert into customer values(10,'PrasadI','KulkarniJ','923466781','M',10000);
insert into customer values(11,'PrasadJ','KulkarniK','133476781','M',11111);
insert into customer values(12,'PrasadK','KulkarniL','143486781','M',12111);
insert into customer values(13,'PrasadL','KulkarniM','153496781','M',12222.45);
insert into customer values(14,'PrasadM','KulkarniN','163436381','M',2333,566);
insert into customer values(15,'PrasadN','KulkarniO','172426781','M',566666.67);



select * from customer;

select * from customer where sal between 10000 and 20000;

select * from customer where mobile_no='163436381' OR mobile_no='143486781';

select * from customer where sal  < 30000;

desc customer;

select * from customer where first_name in('PrasadK','PrasadL');

select * from customer where first_name not in ('PrasadK','PrasadL');

select * from customer where first_name like 'P%';

select * from customer where first_name like '%C';

select * from customer where last_name like '%a%';

select * from customer where last_name like '__l%';


select * from customer;

select * from customer where first_name like '_r%' and sal <= 3000;

select * from customer where first_name like '_r%' or sal <= 3000;

select * from customer where first_name  not like '_r%' or sal <= 3000;

desc customer;
select * from customer where mobile_no is null;

select * from customer where mobile_no is not null;

select * from customer order by sal;

select * from customer order by sal desc;

select * from customer order by cust_id desc,sal asc ;


create table category(cid integer primary key,pcat varchar(20));

insert into category values(1,'Fridge');
insert into category values(2,'Mobile');
insert into category value(3,'TV');

drop table category;
create table product(pid integer primary key, name varchar(20),price float(6,2),id integer,constraint fkey foreign key(id) references category(cid));

insert into product values(1,'F01',3000.11,1);
insert into product values(2,'F02',4000.12,1);
insert into product values(3,'F03',5000.13,1);
insert into product values(4,'M01',6000.14,2);
insert into product values(5,'M01',7000.15,2);
insert into product values(6,'M01',8000.16,2);
insert into product values(7,'T01',9000.17,3);
insert into product values(8,'T01',1000.18,3);
insert into product values(9,'T01',2000.19,3);
insert into product values(10,'T01',2000.19,NULL);

select * from product;
select * from category;

desc category;


select p.pid,p.name,p.price,c.cid,c.pcat
from product p inner join category c on p.id=c.cid;

select p.pid,p.name,p.price,c.cid,c.pcat
from product p left join category c on p.id=c.cid;

select c.cid,c.pcat,p.pid,p.name,p.price
from product p right join category c on p.id=c.cid;

desc category;

insert into category values(4,'Accessories');




select * from product;
select count(pid) "Total products" from product;
select sum(price) "Total price" from product;
select round(avg(price),2) "Average Price" from product;
select min(price) "Minimum Price" from product;
select max(price) "Maximum Price" from product;


select * from employee;
select * from dept;


select * from customer;
select * from category;

select c.cust_id,g.pcat
from customer c,category g;


select c.cust_id,g.pcat
from customer c cross join category g;

update customer set gender='F' where cust_id between 7 and 13;

select * from customer;

select gender,count(cust_id)
from customer
group by gender having count(cust_id)>1
order by gender desc ;


select * from customer;
update customer c JOIN (select avg(sal) as avg_sal from customer where gender='M') as temp on c.sal> temp.avg_sal set c.sal=c.sal*0.2;
select rowid from customer;
desc customer;

DELIMITER // ;
create procedure prasad4 (in cust_id integer,in first_name varchar(20),in last_name varchar(20),in mob_no varchar(20),gen varchar(3),in sal float(5,2))
begin
insert into sample.customer values (cust_id,first_name,last_name,mob_no,gen,sal);
END ;

call prasad4(501,'Rajesh','kumar','211122','M',30.11);



DELIMITER // ;
create procedure info (in c_id integer)
begin 
select * from sample.customer where cust_id=c_id;
end;

call info(501);


select * from customer;

DELIMITER //
create procedure display()
begin
select * from sample.customer;
end //

call display();

DELIMITER !!
create procedure update_data(in mob_no varchar(20))
begin
update customer set molbile_no=mob_no;
end !!

update_data();

DELIMITER !
create procedure delete_date(in c_id integer)
begin
delete from customer where cust_id=c_id;
end !



DELIMITER ;



create table employee1 (id integer primary key auto_increment,
name varchar(20),
salary int,
city varchar(30)
);
