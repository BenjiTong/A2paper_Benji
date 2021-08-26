CREATE TABLE `A2_main` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`datetime` DATE NOT NULL DEFAULT '',
	`radiance` INT(10) NOT NULL DEFAULT '0',
	`pixels` INT(10) NOT NULL DEFAULT '0',
	`city_id` INT NOT NULL DEFAULT '0',
	`window` VARCHAR(200) NOT NULL DEFAULT '',
	KEY `city_id` (`city_id`) USING BTREE,
	PRIMARY KEY (`id`)
);