-- Active: 1667120187038@@127.0.0.1@3306@togle
create Table customers(    
                        cust_name VARCHAR(30),
                        cust_id  INT PRIMARY KEY AUTO_INCREMENT,
                        cust_pass CHAR(8),
                        cust_gender CHAR(1),
                        cust_birth_date INT,
                        cust_Weight DECIMAL,
                        cust_email varchar(320),
                        cust_height DECIMAL,
                        cust_age INT 

                       
);




drop TABLE customers;
SELECT * from customers;


Insert into customers(cust_name,cust_pass,cust_gender,cust_birth_date,cust_Weight,cust_email,cust_height,cust_age) values(tehmina,!tehmina,F,2013,24.0,abc@gmail.com,138.0,9);
alter TABLE ADD COLUMN cust_Weight INT ;


insert into customers(cust_name,cust_id,cust_pass,cust_gender,cust_birth_date,cust_Weight,cust_email,cust_height,cust_age) values("Adnan",1,'98!adnan',"M",2005,50,'syedadnanali0106@gmail.com',168,17);
insert into customers(cust_name,cust_pass,cust_gender,cust_birth_date,cust_Weight,cust_email,cust_height,cust_age) values("Ali",'786adnan',"M",2005,50,'syedadnanali0106@gmail.com',168,17);
insert into customers(cust_name,cust_pass,cust_gender) values("Rayhan",'9!rayhan',"M");
insert into customers(cust_name,cust_pass,cust_gender) values("Tehmina",'!tehmina',"M");

SELECT * from customers;

DELETE FROM customers WHERE cust_id = 2;