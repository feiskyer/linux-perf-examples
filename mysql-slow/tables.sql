CREATE DATABASE IF NOT EXISTS `test`;
USE `test`;

DROP TABLE IF EXISTS `products`;
CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `productCode` text NOT NULL DEFAULT '' COMMENT '产品代码',
  `productName` text NOT NULL COMMENT '产品名称',
  `productLine` text NOT NULL COMMENT '产品线',
  `productScale` text NOT NULL,
  `productVendor` text NOT NULL,
  `productDescription` text NOT NULL,
  `quantityInStock` smallint(6) NOT NULL COMMENT '库存',
  `buyPrice` decimal(10,2) NOT NULL COMMENT '价格',
  `MSRP` decimal(10,2) NOT NULL COMMENT '建议零售价',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;