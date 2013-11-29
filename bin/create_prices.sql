CREATE TABLE `items_history` (
  `type_id` int(11) NOT NULL COMMENT 'eve_inv_types.type_id',
    `region_id` int(11) NOT NULL COMMENT 'eve_map_regions.region_id',
    `date_str` varchar(100) NOT NULL COMMENT 'date for the entry',
    `price_low` double NOT NULL DEFAULT '0' COMMENT 'low price',
    `price_high` double NOT NULL DEFAULT '0' COMMENT 'high price',
    `price_average` double NOT NULL DEFAULT '0' COMMENT 'average price',
    `quantity` bigint(20) NOT NULL DEFAULT '0' COMMENT 'quantity moved',
    `num_orders` bigint(20) NOT NULL DEFAULT '0' COMMENT 'number of orders',
    `created` datetime NOT NULL COMMENT 'date we received the first data',
    `date` date DEFAULT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8
