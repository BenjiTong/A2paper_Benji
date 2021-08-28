CREATE TABLE `main` (
	`id` INT(10) unsigned NOT NULL AUTO_INCREMENT,
	`datetime` timestamp DEFAULT CURRENT_TIMESTAMP,
	`radiance` INT(10) unsigned DEFAULT '0',
	`pixels` INT(10) unsigned DEFAULT '10',
	`city_id` TINYINT(4) unsigned DEFAULT '0',
	`window` VARCHAR(150) DEFAULT '',
	`file` VARCHAR(250) DEFAULT '',
	UNIQUE KEY `file` (`file`) USING BTREE,
	KEY `city_by_time` (`datetime`,`city_id`) USING BTREE,
	PRIMARY KEY (`id`)
);