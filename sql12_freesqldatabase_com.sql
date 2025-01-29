-- used www.freesqldatabase.com for creating a free sql database
show databases;

-- creating a `tenant` table under the `sql12750883` database schema
CREATE TABLE `sql12750883`.`tenant` (
    t_id INT NOT NULL,
    t_name VARCHAR(60) NULL,
    t_phno VARCHAR(60) NULL,
    t_email VARCHAR(60) NULL,
    t_apartment VARCHAR(60) NULL,
    t_room VARCHAR(60) NULL,
    t_occupancy_period VARCHAR(60) NULL,
    t_occupancy_number VARCHAR(60) NULL,
    t_photo_sample VARCHAR(60) NULL,
	PRIMARY KEY(t_id)
);

select * from sql12750883.tenant;

-- DESCRIBE sql12750883.tenant;


-- creating a `attendance` table under the `sql12750883` database schema
CREATE TABLE `sql12750883`.`attendance` (
    surv_id INT NOT NULL AUTO_INCREMENT,
    surv_name VARCHAR(60) NULL,
    surv_apartment VARCHAR(60) NULL,
    surv_room VARCHAR(60) NULL,
    surv_date DATE NULL,
    surv_time TIME NULL,
    surv_status VARCHAR(20) NULL,
    PRIMARY KEY (surv_id)
);

select * from sql12750883.attendance;

-- DESCRIBE sql12750883.attendance;

-- drop table sql12750883.tenant;

-- drop table sql12750883.attendance;

